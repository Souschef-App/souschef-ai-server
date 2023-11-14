
import os
import logging

from openai import OpenAI
from .entities import Ingredient, Recipe, Task

ingredent = Ingredient(name="chicken", quantity=2, unit="teaspoon")
task = Task(id=1, title="Hi", description="yo yo yoi", difficulty=1, ingredients=[ingredent], kitchenware=[], dependencies=[])
task2 = Task(id=2, title="BYE", description="yo yo yoi", difficulty=3, ingredients=[ingredent], kitchenware=[], dependencies=[1])
Dummy : Recipe = Recipe(tasks=[task, task2])

class GenerateRecipe:
    def __init__(self, client):
        self.client = client
        self.logger = logging.getLogger(__name__)

    def generate_recipe(self, input) -> Recipe:
        if os.environ["DUMMY_MODE"] == "TRUE":
            return Dummy
        else:
            return self.client.chat.completions.create(
                model="gpt-4-0613",
                messages=[
                    {
                        "role": "system",
                        "content": "your role is to process a user prompt recipe into a list of atomic tasks: ",
                    },
                    {
                        "role": "user",
                        "content": f"can you break down the following tasks into the list of sub tasks more broken down further than the original: \n {input}",
                    }
                ],
                response_model=Recipe,
            )   
        