from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecipeBreakdownRequest(_message.Message):
    __slots__ = ["description"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    description: str
    def __init__(self, description: _Optional[str] = ...) -> None: ...

class RetryTaskRequest(_message.Message):
    __slots__ = ["task", "prompt"]
    TASK_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    task: Task
    prompt: str
    def __init__(self, task: _Optional[_Union[Task, _Mapping]] = ..., prompt: _Optional[str] = ...) -> None: ...

class Fraction(_message.Message):
    __slots__ = ["whole", "numerator", "denominator"]
    WHOLE_FIELD_NUMBER: _ClassVar[int]
    NUMERATOR_FIELD_NUMBER: _ClassVar[int]
    DENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    whole: int
    numerator: int
    denominator: int
    def __init__(self, whole: _Optional[int] = ..., numerator: _Optional[int] = ..., denominator: _Optional[int] = ...) -> None: ...

class Ingredient(_message.Message):
    __slots__ = ["name", "quantity", "unit"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    name: str
    quantity: Fraction
    unit: str
    def __init__(self, name: _Optional[str] = ..., quantity: _Optional[_Union[Fraction, _Mapping]] = ..., unit: _Optional[str] = ...) -> None: ...

class Kitchenware(_message.Message):
    __slots__ = ["name", "quantity"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    name: str
    quantity: int
    def __init__(self, name: _Optional[str] = ..., quantity: _Optional[int] = ...) -> None: ...

class Dependency(_message.Message):
    __slots__ = ["UUID", "name"]
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID: bytes
    name: str
    def __init__(self, UUID: _Optional[bytes] = ..., name: _Optional[str] = ...) -> None: ...

class Task(_message.Message):
    __slots__ = ["uuid", "title", "description", "difficulty", "duration", "ingredients", "kitchenware", "dependencies"]
    UUID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    INGREDIENTS_FIELD_NUMBER: _ClassVar[int]
    KITCHENWARE_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    uuid: bytes
    title: str
    description: str
    difficulty: int
    duration: int
    ingredients: _containers.RepeatedCompositeFieldContainer[Ingredient]
    kitchenware: _containers.RepeatedCompositeFieldContainer[Kitchenware]
    dependencies: _containers.RepeatedCompositeFieldContainer[Dependency]
    def __init__(self, uuid: _Optional[bytes] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., difficulty: _Optional[int] = ..., duration: _Optional[int] = ..., ingredients: _Optional[_Iterable[_Union[Ingredient, _Mapping]]] = ..., kitchenware: _Optional[_Iterable[_Union[Kitchenware, _Mapping]]] = ..., dependencies: _Optional[_Iterable[_Union[Dependency, _Mapping]]] = ...) -> None: ...

class RecipeBreakdownReply(_message.Message):
    __slots__ = ["tasks"]
    TASKS_FIELD_NUMBER: _ClassVar[int]
    tasks: _containers.RepeatedCompositeFieldContainer[Task]
    def __init__(self, tasks: _Optional[_Iterable[_Union[Task, _Mapping]]] = ...) -> None: ...

class RetryTaskRequestReply(_message.Message):
    __slots__ = ["task"]
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: Task
    def __init__(self, task: _Optional[_Union[Task, _Mapping]] = ...) -> None: ...
