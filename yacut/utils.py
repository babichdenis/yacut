import random
from .const import (
    ID_ERROR_MESSAGE, ITERATIONS,
    PATTERN_FOR_SHORT, LEN_OF_SHORT
)


def get_unique_short(get_function) -> str:
    for _ in range(ITERATIONS):
        short = ''.join(random.choices(PATTERN_FOR_SHORT, k=LEN_OF_SHORT))
        if get_function(short) is None:
            return short
    raise RuntimeError(ID_ERROR_MESSAGE)
