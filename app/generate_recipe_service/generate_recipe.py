

from .entities import Recipe


class GenerateRecipe:
    def __init__(self, client):
        self.client = client

    def generate_recipe(self, input) -> Recipe:
        return self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": f"Help me understand the following by describing it as a detailed knowledge graph: {input}",
                }
            ],
            response_model=Recipe,
        )