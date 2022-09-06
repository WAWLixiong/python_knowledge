from typing import TypeVar, Generic, Iterator, _T_co

T = TypeVar('T')


# ----------------------------
# 泛型函数中用到的类型变量可以被推断出来，以便在同一代码块中表示不同的类型

def fun_1(x: T) -> T: ...


def fun_2(x: T) -> T: ...


fun_1(1)
fun_2('a')

# ----------------------------
# 当泛型类的方法中用到类型变量时，若该变量正好用作参数化类，那么此类型变量一定是绑定不变的

M = TypeVar('M')


class MyClass(Generic[M]):
    def fun_1(self, x: M) -> M: ...

    def fun_2(self, x: M) -> M: ...


a = MyClass()  # type: MyClass[int]
a.fun_1(1)
a.fun_2('a')  # error

# ----------------------------
# 如果某个方法中用到的类型变量与所有用于参数化类的变量都不相符，则会使得该方法成为返回类型为该类型变量的泛型函数

K = TypeVar('K')
V = TypeVar('V')


class Foo(Generic[K]):
    def fun(self, x: K, y: V) -> V:
        ...


foo = Foo()  # type: Foo[int]
ret = foo.fun(0, 'abc')
# ----------------------------
# 在泛型函数体内不应出现未绑定的类型变量，在类中除方法定义以外的地方也不应出现

O = TypeVar('O')
P = TypeVar('P')


def a_fun(x: O) -> None:
    y = []  # type: List[O]  # Ok
    y = []  # type: List[P]  # Error


class Bar(Generic[O]):
    an_attr = []  # type: List[P]  # Error

    def do_something(self, x: P) -> P:  # Ok
        ...


# ----------------------------
# 如果泛型类的定义位于某泛型函数内部，则其不允许使用参数化该泛型函数的类型变量
from typing import List


def b_fun(x: T) -> None:
    a_list = []  # type: List[T]  # Ok

    class MyGeneric(Generic[T]):  # Error
        ...


# ----------------------------
# 嵌套的泛型类不能使用相同的类型变量。外部类的类型变量，作用域不会覆盖内部类
from typing import Iterable

X = TypeVar('X')
Y = TypeVar('Y')


class Outer(Generic[X]):
    class Bad(Iterable[X]):  # Error todo: 这里使用 mypy 没有检测到错误
        ...

    class AlsoBad:
        x = None  # type: List[X]  # Also an Error

    class Inner(Iterable[Y]):  # Ok
        ...

    attr = None  # type: Inner[X]
