
class env:
    """This class the user interacts with. It takes arguments like env.mov(rax, rbx) or env.call() and 
    directs their execution.
    """
    def __init__(self, arch=None):
        self.memory = virtualmemory(1)
        # Points to the top of the stack.
        self.RSP = self.memory.getSP()
        # Points to base of stack.
        self.RBP = self.memory.getBP()

        # Points to the top of the frame.
        # Normally, no IO allowed.
        self.FP = self.memory.getFP()
        
        # Import the processor.
        # Processor should have say in environment.
        if arch is None:
            import processors.Foo
            arch = processors.Foo.Foo()

        self.proc = arch
        self.proc.initEnv(self)
