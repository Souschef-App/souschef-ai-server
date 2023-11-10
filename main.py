import os
import logging
logging.basicConfig(level=logging.INFO)

import instructor
from openai import OpenAI
from entities import Recipe

client = instructor.patch(OpenAI(api_key= os.environ['OPENAI_API_KEY']))

def generate_recipe(input) -> Recipe:
    return client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"Help me understand the following by describing it as a detailed knowledge graph: {input}",
            }
        ],
        response_model=Recipe,
    )

def main():
    logger = logging.getLogger()
    logger.info("Running AI...")

    generate_recipe("chicken")

if __name__ == "__main__":
    main()
    