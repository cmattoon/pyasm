from pyasm.processor import processor

class Foo(processor):
    """This is a generic, arbitrary processor architecture. 
    It has no basis in reality.

    These classes should allow simulation of different architectures
    and for them to produce expected output.

    The virtualenvironment directs the proecssor to do things
    to assigned memory locations or values.

    p.mov(rax, rbx)
    
    """
    def __init__(self):
        pass

    def __getattr__(self, name):
        pass

    def initEnv(self):
        pass

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

    
