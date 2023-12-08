import os
import logging
from concurrent import futures
import uuid

import grpc

import instructor
from openai import OpenAI
from app.generate_recipe_service.entities import Recipe
from app.generate_recipe_service import GenerateRecipe
from .generated import recipe_generation_pb2
from .generated  import recipe_generation_pb2_grpc

from dataclasses import dataclass

@dataclass
class Fraction:
    whole: int
    numerator: int
    denominator: int

class RecipeGeneration(recipe_generation_pb2_grpc.RecipeGenerationServicer):
    def __init__(self):
        client = instructor.patch(OpenAI(api_key= os.environ['OPENAI_API_KEY']))
        self.generate_recipe_service = GenerateRecipe(client)
        self.logger = logging.getLogger(__name__)

    def getRecipeBreakDown(self, request, context):

        self.logger.info(f"consulting the chat gippity")
        recipe = self.generate_recipe_service.generate_recipe(request.description)

        self.logger.info(f"recipe {recipe}")

        reply = recipe_generation_pb2.RecipeBreakdownReply()

        idProtoTask_dict = dict()

        for task in recipe.tasks:
            protoTask = recipe_generation_pb2.Task()
            protoTask.uuid = uuid.uuid4().bytes_le
            protoTask.title       = task.title
            protoTask.description = task.description
            protoTask.difficulty  = max(0, min(task.difficulty, 2))
            protoTask.duration    = task.duration

            for ingredient in task.ingredients:

                protoIngredient = recipe_generation_pb2.Ingredient()
                if not ingredient.error:
                    protoIngredient.name     = ingredient.name

                    frac = self.parse_mixed_number(ingredient.quantity)

                    protoIngredient.quantity.whole = frac.whole
                    protoIngredient.quantity.numerator = frac.numerator
                    protoIngredient.quantity.denominator = frac.denominator

                    protoIngredient.unit     = ingredient.unit

                else:
                    self.logger.info(f"ingredient error {ingredient.message}")
                    protoIngredient.name     = ""
                    protoIngredient.quantity.whole = 0
                    protoIngredient.quantity.numerator = 0
                    protoIngredient.quantity.denominator = 0

                    protoIngredient.unit     = "none"

                protoTask.ingredients.extend([protoIngredient])

            for kitchenware in task.kitchenware:
                protoKitchenware = recipe_generation_pb2.Kitchenware()
                protoKitchenware.name     = kitchenware.name
                protoKitchenware.quantity = kitchenware.quantity

                protoTask.kitchenware.extend([protoKitchenware])

            # for dependency in task.dependencies:
            #     protoTask.dependencies.extend([dependency])

            # reply.tasks.extend([protoTask])
            idProtoTask_dict[task.id] = protoTask
        
        # reply = self.assignUUID(reply)
        reply = self.convertDepIDToUUID(recipe, idProtoTask_dict, reply)

        self.logger.info(f"reply {reply}")  

        return reply
    
    
    def retryTask(self, request, context):
        self.logger.info(f"retryTask {request.task}")  

        taskString = f"Task Title: {request.task.title} Duration: {request.task.description} Ingredients "

        for ingredient in request.task.ingredients:
            ingredientsSubString = f"Name: {ingredient.name} Quantity: {ingredient.quantity} Unit: {ingredient.unit}"
            taskString + ingredientsSubString
   
        self.logger.info(f"taskString {taskString}")      

        task = self.generate_recipe_service.retry_task(taskString)

        reply = recipe_generation_pb2.RetryTaskRequestReply()

        reply.task.uuid = uuid.uuid4().bytes_le
        reply.task.title       = task.title
        reply.task.description = task.description
        reply.task.difficulty  = max(0, min(task.difficulty, 2))
        reply.task.duration  = task.duration

        for ingredient in task.ingredients:
            protoIngredient = recipe_generation_pb2.Ingredient()
            protoIngredient.name     = ingredient.name

            frac = self.parse_mixed_number(ingredient.quantity)

            protoIngredient.quantity.whole = frac.whole
            protoIngredient.quantity.numerator = frac.numerator
            protoIngredient.quantity.denominator = frac.denominator

            protoIngredient.unit     = ingredient.unit

            reply.task.ingredients.extend([protoIngredient])

        for kitchenware in task.kitchenware:
            protoKitchenware = recipe_generation_pb2.Kitchenware()
            protoKitchenware.name = kitchenware.name
            protoKitchenware.quantity = kitchenware.quantity
            reply.task.protoKitchenware.extend([protoKitchenware])

        return reply

    def convertDepIDToUUID(self, recipe : Recipe, idProtoTask_dict : dict, reply : recipe_generation_pb2.RecipeBreakdownReply):
        for task in recipe.tasks:
            protoTask = idProtoTask_dict[task.id]
            for dep in task.dependencies:
                protoDep = recipe_generation_pb2.Dependency()
                protoDep.UUID = idProtoTask_dict[dep].uuid
                protoDep.name = idProtoTask_dict[dep].title
                protoTask.dependencies.extend([protoDep])

            reply.tasks.extend([protoTask])

        return reply
    
    def parse_mixed_number(self, mixed_number : str):
        
        if mixed_number.find(' ') != -1:
            whole = 0, 
            fraction = 0
            try:
                whole, fraction = map(str.strip, mixed_number.split())

            except Exception as ex:
                self.logger.info(ex)

            whole = int(whole) if whole else 0
            
            numerator = 0
            denominator = 0

            if fraction.find('/') != -1:
                numerator, denominator = map(int, fraction.split('/'))
        
                return Fraction(whole=whole, numerator=numerator, denominator=denominator)
        else:
            if mixed_number.find('/') != -1:
                numerator, denominator = map(int, mixed_number.split('/'))
        
                return Fraction(whole=0, numerator=numerator, denominator=denominator)
            else:
                whole = int(mixed_number)
                return Fraction(whole=whole, numerator=0, denominator=0)

class Server:
    def __init__(self):
        self.port = "50051"
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        recipe_generation_pb2_grpc.add_RecipeGenerationServicer_to_server(RecipeGeneration(), self.server)
        self.server.add_insecure_port("[::]:" + self.port)
        self.logger = logging.getLogger(__name__)

    def listen(self):   
        self.server.start()
        self.logger.info("Server started, listening on " + self.port)
        self.server.wait_for_termination()
