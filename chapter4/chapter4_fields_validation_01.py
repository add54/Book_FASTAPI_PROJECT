from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class Person(BaseModel):
    first_name: str = Field(..., min_length=3)
    last_name: str = Field(..., min_length=3)
    age: Optional[int] = Field(None, ge=0, le=120)


# Invalid first name
try:
    Person(first_name="J", last_name="Doe", age=30)
except ValidationError as e:
    print(str(e))
    assert len(e.errors()) == 1


# Invalid age
try:
    Person(first_name="John", last_name="Doe", age=2000)
except ValidationError as e:
    print(str(e))
    assert len(e.errors()) == 1


# Valid
person = Person(first_name="John", last_name="Doe", age=30)
assert person.first_name == "John"
assert person.last_name == "Doe"
assert person.age == 30