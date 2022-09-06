Url = str


def retry(url: Url, retry_count: int) -> None: ...


# -----------------------------------

from typing import TypeVar, Iterable, Tuple

T = TypeVar('T', int, float, complex)
Vector = Iterable[Tuple[T, T]]


def inproduct(v: Vector[T]) -> T:
    """等价于 def inproduct(v: Iterable[Tuple[T, T]]) -> T: """
    return sum(x * y for x, y in v)


def dilate(v: Vector[T], scale: T) -> Vector[T]:
    """等价于 def dilate(v: Iterable[Tuple[T, T]], scale: T) -> Iterable[Tuple[T, T]]: """
    return ((x * scale, y * scale) for x, y in v)


vec = []
