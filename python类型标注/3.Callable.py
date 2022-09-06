from typing import Callable


def feeder(get_next_item: Callable[[], str]) -> None:
    ...


def async_query(on_success: Callable[[int], None], on_error: Callable[[int, Exception], None]) -> None:
    ...


def partial(func: Callable[..., str], *args) -> Callable[..., str]:
    """isinstance(x, typing.Callable) 与 isinstance(x, collections.abc.Callable)兼容"""
    ...
