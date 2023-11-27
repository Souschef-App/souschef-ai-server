from pydantic import BaseModel, Field
from enum     import Enum, auto
from typing   import List, Literal

# class Unit(Enum):
#     NONE        = auto()
#     Ounces      = auto()  #Start of weight units
#     Pounds      = auto()
#     Grams       = auto()
#     Kilograms   = auto()  #End of weight units
#     teaspoon    = auto()  #Start of volume units
#     teaspoons   = auto()
#     tablespoon  = auto()
#     tablespoons = auto()
#     Cups        = auto()
#     Pints       = auto()
#     Quarts      = auto()
#     Gallons     = auto()
#     Liters      = auto()  #End of volume units

# class Fraction(BaseModel):
#     whole: int = Field(..., description="whole component of the number", examples=[1, 2])
#     numerator: int   = Field(..., description="numerator of fraction; if no fraction put 1", examples=[0, 1, 2])
#     denominator: int  = Field(..., description="denominator of fraction; if no fraction put 1", examples=[0, 1, 2])

class Ingredient(BaseModel):
    name : str = Field(...,description="Name of ingredient", examples=["beets", "carrot", "steak", "flour", "water"])
    quantity : str = Field(...,description="amount of this ingredient as written string", examples=["1 2/3"])
    # unit : Unit = Field(description="Correctly assign one of the predefined units to the ingredient. If no match use NONE")
    unit : Literal["none", "ounces", "pounds", "grams", "kilograms", "teaspoon", "tablespoon", "cup", "cups","pints", "quarts", "gallons", "liters", "milliliters", "pieces"] = Field(
        ...,
        description="Correctly assign one of the predefined units to the ingredient. If no match use none"
    )

class Kitchenware(BaseModel):
    name : str = Field(...,description="Name of kitchenware", examples=["knife", "blender", "stove", "measuring cup"])
    quantity: int = Field(...,description="Amount of this kitchenware needed")

class Task(BaseModel):
    id: int = Field(
        ...,
        description="Unique identifier for the entity, used for deduplication, design a scheme allows multiple entities",
    )
    title: str = Field(...,description="Name of task")
    description: str = Field(...,description="Instructions needed to complete this task")
    ingredients: List[Ingredient] = Field(..., default_factory=list)
    kitchenware: List[Kitchenware] = Field(..., default_factory=list)
    difficulty: int = Field(...,description="Difficutly of this task 0 being the easiest, up to 2 being the hardest")
    duration: int = Field(...,description="Estimate the time for this task in mins")
    dependencies: List[int] = Field(..., default_factory=list, description="List of task ids that this task depends or relies on to resolve it",)

class Recipe(BaseModel):
    tasks: List[Task] = Field(..., default_factory=list, description="List of all tasks needed to complete this")
