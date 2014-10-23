
class register:
    """This class represents a register in memory.
    It has a name (rax, eax, etc), a size (8, 16, 32, 64, 128),
    a fake memory address and a value
    
    It handles operations like:
    mov rax, [rbx]
    rax.val(rbx.address())

    It is used by instructions (eg):
    add rax, rbx
    def add(reg1, reg2):
        reg1.val(reg1.val() + reg2.val())
        return reg1
    """
    def __init__(self, name, bits=64):
        self._name = name
        self._address = ''
        self._bits = bits
        self._value = []

        self._initValue()

    def _initValue(self):
        """Creates an empty list of self._bits bits
        """
        if self._bits not in [pow(2, x) for x in range(3,8)]:
            raise InvalidArgumentError("Invalid bit value in register")
        self._value = [0] * self._bits

    
