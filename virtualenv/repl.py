
class REPL:
    """ Why not?
    """
    def __init__(self):
        self.env = None
        self.proc = None
        self.commands = []

        self._initCommands()

    def _initCommands(self):
        self.commands = ['mov', 'add', 'mul', 'jnz', 'jne', 'call', 'dec', 'inc'] # etc...

    def getCmd(self):
        command = raw_input(">>> ") # mov eax bax
        cmd, arg1, arg2 = split(" ")
        if cmd.lower() not in self.commands:
            print "Invalid Command"
            return None
        
        print "Calling %s(%s, %s)" % (cmd, arg1, arg2)
        return True  # return cmd(arg1,arg2)

    
