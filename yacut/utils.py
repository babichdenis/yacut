import random
from .const import ID_ERROR_MESSAGE


def get_unique_short(
        iterations: int,
        pattern_for_short: str,
        len_of_short: int,
        get_function) -> str:
    for _ in range(iterations):
        short = ''.join(random.choices(pattern_for_short, k=len_of_short))
        if get_function(short) is None:
            return short
    raise RuntimeError(ID_ERROR_MESSAGE)
