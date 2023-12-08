
import os
import logging

from openai import OpenAI
from .entities import Ingredient, Recipe, Task
# fraction = Fraction(whole="2", numerator="1", denominator="3")
ingredent = Ingredient(name="chicken", quantity="1 1/2", unit="teaspoon")
task = Task(id=1, title="H HFIE GJIEGJ GJGGGgi", description="yo yo yoi efef ef ef ef fe eaaaaa efe ", difficulty=1, duration=3, ingredients=[ingredent], kitchenware=[], dependencies=[])
task2 = Task(id=2, title="H HFIE GJIEGJ GJGGGgi a ef ef", description="yo yo yoi afea sefefefefef efefe ef ef efefe fef " , difficulty=2, duration=2, ingredients=[ingredent], kitchenware=[], dependencies=[1])
task3 = Task(id=3, title="BYE ef ef ef ef eddddd", description="yo yo yoi asdfes aefesa fef aef WEf", difficulty=0, duration=10, ingredients=[ingredent], kitchenware=[], dependencies=[1,2])
Dummy : Recipe = Recipe(tasks=[task, task2, task3])

task4 = Task(id=4, title="Bacon", description="Fry Bacon", difficulty=2, duration=11, ingredients=[ingredent], kitchenware=[], dependencies=[1,2])

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
        
    def retry_task(self, input) -> Recipe:
        if os.environ["DUMMY_MODE"] == "TRUE":
            return task4
        else:
            return self.client.chat.completions.create(
                model="gpt-4-0613",
                messages=[
                    {
                        "role": "system",
                        "content": "your role is to improve this tasks clarity: ",
                    },
                    {
                        "role": "user",
                        "content": f"can you re phrase this task in a slightly different way: \n {input}",
                    }
                ],
                response_model=Task,
            )   
        