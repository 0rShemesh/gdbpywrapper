import pexpect
import gdb_constants

DEBUG_CURRENT_SELECTED_GDB = "gdb"


class GdbClientBasicProccessWrapper:
    """
    this is the basic gdb executable wrapper
    its read and can write also know to quit
    """
    def __init__(self, gdb_path, *args):
        self.process = pexpect.spawn(gdb_path, list(args))

    def write(self, commmand_to_send):
        return self.process.sendline(commmand_to_send)

    def read(self,timeout=5):
        self.process.expect(gdb_constants.GDB_START_LINE,timeout=timeout)
        return self.process.before
    
    def go_interactive_session(self):
        self.process.interact()

    def quit(self):
        self.write("quit")
    