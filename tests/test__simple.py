

from fallback_toolkit.simple import (
    FallbacksFailed,
    fallback_registry,
    fallback,
)



def test__basic():
    @fallback(id='one')
    def foo():
        pass

    foo()

    del fallback_registry['one']



def test__fallback_1():
    call_order = []
    value = 0

    @fallback(id='one')
    def foo():
        call_order.append('foo')
        raise ValueError()

    @fallback(id='one')
    def baa():
        call_order.append('baa')
        raise ValueError()

    @fallback(id='one')
    def bar():
        nonlocal value
        call_order.append('bar')
        value = 1

    foo()

    assert call_order == ['foo', 'baa', 'bar']
    assert value == 1

    del fallback_registry['one']


def test__fallback_2():
    call_order = []
    value = 0

    @fallback(id='one')
    def foo():
        call_order.append('foo')
        raise ValueError()

    @fallback(id='one')
    def baa():
        call_order.append('baa')
        raise ValueError()

    @fallback(id='one')
    def bar():
        nonlocal value
        call_order.append('bar')
        value = 1

    # even if we call the 3rd wrapped function, the order of call
    # is the same as if we called the first one
    bar()

    assert call_order == ['foo', 'baa', 'bar']
    assert value == 1

    del fallback_registry['one']
