from environment import environment as env

class syscalls:
    """This class holds a framework for system calls and should ultimately depend on an
    architecture template I think. For now, it's basically a function map to allow
    programming system calls like you really would.
    """
    
    def __init__(self):
        pass

    def call(self):
        """ Represents the 0x80 instruction.
        """
        syscall_number = env.rax.val()
        # args = [env.ebx.val(), env.ecx.val(), env.edx.val(), env.esi.val(), env.edi.val(), env.ebp.val()] 
        # handle stack args
        
        # Look up syscall_number in the function map,
        pass

    def getIdByName(self, name):
        """ Return a system call number based on the name of the syscall.
        env.mov(rax, sys.getIdByName('foo_bar'))
        """
        try:
            value = self._map[name]
        except KeyError:
            raise KeyError("Invalid syscall name")

        return value
