from typing import TypeVar, Generic, Iterable, Iterator, _T_co
from logging import Logger

T = TypeVar('T')


class LoggerVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log(f'Set{repr(self.value)}')
        self.value = new

    def get(self) -> T:
        self.log(f'Get{repr(self.value)}')
        return self.value

    def log(self, message: str) -> None:
        self.logger.info(f'{self.name}: {message}')


def zero_all_vars(vars: Iterable[LoggerVar[int]]) -> None:
    for var in vars:
        var.set(0)


# -------------------------------------


M = TypeVar('M')
N = TypeVar('N')


class Pair(Generic[M, N]):  # 不能 Generic[T, T] 重复的泛型参数
    ...


# -------------------------------------

class MyIterator(Iterator[T]):
    """
    简单场合直接继承泛型类并指定类型变量参数
    等价于 MyIter(Iterator[T], Generic[T]):
    """

    def __next__(self) -> _T_co:
        pass


# -------------------------------------
from typing import Sized, Tuple, Container


class LinkedList(Sized, Generic[T]):
    """多重继承"""

    def __len__(self) -> int:
        pass


K = TypeVar('K')
V = TypeVar('V')


class MyMapping(Iterable[Tuple[K, V]], Container[Tuple[K, V]], Generic[K, V]):
    """多重继承"""

    def __contains__(self, __x: object) -> bool:
        pass

    def __iter__(self) -> Iterator[_T_co]:
        pass


# -------------------------------------
class MyIterable(Iterable):
    """
    MyIterable 不是泛型，而是隐士的继承 Iterable[Any]
    """

    def __iter__(self) -> Iterator[_T_co]:
        pass
