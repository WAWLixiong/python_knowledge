from typing import Mapping, Set


class Employee:
    ...


def notify_by_email(employees: Set[Employee], overrides: Mapping[str, str]) -> None: ...


# -------------------------


from typing import Sequence, TypeVar

T = TypeVar('T')  # 不能 redefine T, 参数 'T' 与 变量名 T 要相同


def first(l: Sequence[T]) -> T:  # Generic function
    """TypeVar()只能赋值给某个变量，不能用其组成其他表达式"""
    return l[0]


# -------------------------

from typing import TypeVar, Text

AnyStr = TypeVar('AnyStr', Text, bytes)


def concat(x: AnyStr, y: AnyStr) -> AnyStr:
    """x, y 类型需要相同，不能混用"""
    return x + y


concat('1', '2')
concat(b'1', b'2')
concat('1', b'h')


class MyStr(str):
    ...


concat(MyStr('1'), MyStr('2'))
concat(MyStr(b'1'), MyStr(b'2'))
concat(MyStr('1'), MyStr(b'2'))  # str(b'2') -> "b'2'"

# -------------------------
from typing import List, Any


def count_truthy(elements: List[Any]) -> int:
    """elements: List[Any] 等价于 elements: List"""
    return sum(1 for i in elements if i)
