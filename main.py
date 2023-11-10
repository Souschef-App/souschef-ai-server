import os
import logging

logging.basicConfig(level=logging.INFO)

import instructor
from openai import OpenAI
from app.generate_recipe_service import GenerateRecipe

def main():
    logger = logging.getLogger()
    logger.info("Running AI...")

    client = instructor.patch(OpenAI(api_key= os.environ['OPENAI_API_KEY']))
    generate_recipe_service = GenerateRecipe(client)
    generate_recipe_service.generate_recipe("chicken")

if __name__ == "__main__":
    main()
