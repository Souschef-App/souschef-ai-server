import os
import logging
from concurrent import futures

import grpc

import instructor
from openai import OpenAI
from app.generate_recipe_service import GenerateRecipe
from .generated import recipe_generation_pb2
from .generated  import recipe_generation_pb2_grpc

class RecipeGeneration(recipe_generation_pb2_grpc.RecipeGenerationServicer):
    def __init__(self):
        client = instructor.patch(OpenAI(api_key= os.environ['OPENAI_API_KEY']))
        self.generate_recipe_service = GenerateRecipe(client)

    def getRecipeBreakDown(self, request, context):
        # self.generate_recipe_service.generate_recipe("chicken")
        return recipe_generation_pb2.RecipeBreakdownReply(message="Hello BreakDown, %s!" % request.description)

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
