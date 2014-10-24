class memory:
    pass

class virtualmemory(memory):
    
    def __init__(self, mb=1, stack_size=1):
        """This creates virtual memory
        that is 8,000,000 bits. Each bit can
        be manipulated by its index (memory address)
        
        addr = 123456
        rax = self.blocks[addr:addr+64]

        This is big-endian, but should be written to 
        support both, if that's possible.

        I've been testing with 1-2mb only.
        """
        # Store used bits here, for gc/defrag ops
        self.chunks = []

        # This is going to be problematic...
        bits = 8000000
        self.blocks = [0] * (mb * bits)
        self.stack = [0] * (stack_size * bits)
        

    def sizeOf(self, units='b'):
        """Returns size of virtual memory in bytes
        @param units (optional, default 'b') One of b, k, m, or g
        """
        bits = len(self.blocks)
        _bytes = bits / 8

        if units == 'k':
            return _bytes / 1000
        elif units == 'm':
            return _bytes / 1000000
        elif units == 'g':
            return _bytes / 1000000000
        
        return _bytes
        

    def _initPointers(self):
        """Determines where *BP and *SP are pointed
        """
        self._basePointer = 0
        # Red Zone allocation..128 bytes = 128 bits * 8
        self._stackPointer = len(self.stack) - 128 * 8
        self._framePointer = 0 

    def getSP(self):
        """Returns _stackPointer
        """
        return self._stackPointer

    def getBP(self):
        """Returns _basePointer
        """
        return self._basePointer

    def debugUsage(self):
        import resource
        vals = resource.getrusage(resource.RUSAGE_SELF)
        
        print "\n".join([
                "Unshared data size: %d kb" % (vals.ru_idrss),
                "Shared memory size: %d kb" % (vals.ru_ixrss),
                ])
        
        
class Register:
    def __init__(self, size=64):
        """Registers reference a block of memory.
        """
        self.start = 0
        self.size = size * 8
        
        
    def __str(self):
        print 
        
        
