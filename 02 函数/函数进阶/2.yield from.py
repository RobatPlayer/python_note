def foo():
    yield 1
    yield 2


def fun():
    yield 3
    yield 1
    yield from foo()  # 可以跳到另外一个函数生成
    yield 2
