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

class RecipeGeneration(recipe_generation_pb2_grpc.RecipeGenerationServicer):
    def __init__(self):
        client = instructor.patch(OpenAI(api_key= os.environ['OPENAI_API_KEY']))
        self.generate_recipe_service = GenerateRecipe(client)
        self.logger = logging.getLogger(__name__)

    def getRecipeBreakDown(self, request, context):
        recipe = self.generate_recipe_service.generate_recipe(request.description)

        reply = recipe_generation_pb2.RecipeBreakdownReply()

        for task in recipe.tasks:
            protoTask = recipe_generation_pb2.Task()
            newUUID = uuid.uuid4()
            self.logger.info(f"newUUID {newUUID}")
            protoTask.uuid = newUUID.bytes_le
            protoTask.title       = task.title
            protoTask.description = task.description
            protoTask.difficulty  = task.difficulty

            for ingredient in task.ingredients:
                protoIngredient = recipe_generation_pb2.Ingredient()
                protoIngredient.name     = ingredient.name
                protoIngredient.quantity = ingredient.quantity
                protoIngredient.unit     = ingredient.unit

                protoTask.ingredients.extend([protoIngredient])

            for kitchenware in task.kitchenware:
                protoKitchenware = recipe_generation_pb2.Kitchenware()
                protoKitchenware.name     = kitchenware.name
                protoKitchenware.quantity = kitchenware.quantity

                protoTask.kitchenware.extend([protoKitchenware])

            # for dependency in task.dependencies:
            #     protoTask.dependencies.extend([dependency])

            reply.tasks.extend([protoTask])
        
        # reply = self.assignUUID(reply)
        reply = self.convertDepTitleToUUID(recipe, reply)

        return reply
    
    # def assignUUID(self, reply : recipe_generation_pb2.RecipeBreakdownReply):
    #     for task in reply.tasks:
    #         task.uuid = uuid.uuid4().bytes_le
    #     return reply
    
    def convertDepTitleToUUID(self, recipe : Recipe, reply : recipe_generation_pb2.RecipeBreakdownReply):
        for task in recipe.tasks:
            for dep in task.dependencies:
                replyTaskToUpdate = next((t for t in reply.tasks if t.title == task.title), None)
                if(replyTaskToUpdate != None):
                    for replyTask in reply.tasks:
                        if(dep == replyTask.title):
                            self.logger.info(f"ADDING UUID FOR DEP")
                            replyTaskToUpdate.dependencies.extend([replyTask.uuid])

        return reply

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
