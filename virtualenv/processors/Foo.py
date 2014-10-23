from pyasm.processor import processor

class Foo(processor):
    """This is a generic, arbitrary processor architecture. It has no basis in reality.
    These classes allow different architectures to function exactly as they should.
    """
    def mov(dst, val):
        # get dst register, put val in it
        pass

    def add(dst, val):
        # but for real..
        dst += val
        return dst

    def jnz(location):
        ## This might be tricky.
        pass

    def cmp(val1, val2):
        # Set flags
        pass

    
