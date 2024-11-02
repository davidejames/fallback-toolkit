

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



