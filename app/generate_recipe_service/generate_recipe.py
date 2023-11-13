

from .entities import Recipe

# ingredent = Ingredient(name="chicken", quantity=2, unit="teaspoon")
# task = Task(title="Hi", description="yo yo yoi", difficulty=1, ingredients=[ingredent])
# Dummy : Recipe = Recipe(tasks=[task])

class GenerateRecipe:
    def __init__(self, client):
        self.client = client

    def generate_recipe(self, input) -> Recipe:
        return self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "your role is a bot that processes a recipe into a set of smaller individualized tasks: ",
                },
                                {
                    "role": "system",
                    "content": f"you'll return a list of tasks that each have the following header: Title, Description, Ingredients, Kitchenware, Duration, Difficulty, Dependencies",
                },
                                {
                    "role": "system",
                    "content": f"Title will be the name of task, Description will be the instructions, Ingredients will be a list if the ingredients just for that step, Kitchenware will be a list of all the utensils and other tools, Duration will be an estimate in minutes for the task, Difficulty will be an estimate from 0-3 on how hard the task is, Dependencies is a list of any other tasks that need to be completed before this task indicated as an index number",
                },
                {
                    "role": "system",
                    "content": f"can you break down the following recipe into the list as described",
                },
                {
                    "role": "user",
                    "content": f"each of the provided steps should be broken down even further into smaller steps: {input}",
                }
            ],
            response_model=Recipe,
        )   