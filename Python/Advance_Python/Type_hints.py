from typing import Annotated, TypeAlias, NewType


def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"




Vector: TypeAlias = list[float]

UserId = NewType('UserId', int)
some_id = UserId(524313)

def get_user_name(user_id: UserId) -> str:
    return str(user_id)


print(get_user_name(some_id))

print(get_user_name(-1))

abcd: Vector = [12.12, 23.34, 56.76]

# type Vector = list[float] # Python-3.12 and above