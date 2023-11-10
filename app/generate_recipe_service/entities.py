from pydantic import BaseModel, Field
from enum     import Enum, auto
from typing   import List

class Unit(Enum):
    NONE        = auto()
    Ounces      = auto()  #Start of weight units
    Pounds      = auto()
    Grams       = auto()
    Kilograms   = auto()  #End of weight units
    teaspoon    = auto()  #Start of volume units
    teaspoons   = auto()
    tablespoon  = auto()
    tablespoons = auto()
    Cups        = auto()
    Pints       = auto()
    Quarts      = auto()
    Gallons     = auto()
    Liters      = auto()  #End of volume units

class Ingredient(BaseModel):
    name : str
    quantity : float
    unit: str
    # unit : Unit = Field(description="Correctly assign one of the predefined units to the ingredient.")

class Kitchenware(BaseModel):
    name : str
    quantity: int

class Task(BaseModel):
    title: str
    description: str
    ingredients: List[Ingredient] = Field(..., default_factory=list)
    kitchenware: List[Kitchenware] = Field(..., default_factory=list)
    difficulty: int 
    dependencies: List[str] = Field(..., default_factory=list)

class Recipe(BaseModel):
    tasks: List[Task] = Field(..., default_factory=list)
    