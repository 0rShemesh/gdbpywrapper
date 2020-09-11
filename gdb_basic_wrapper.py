import pexpect
import gdb_constants

class GdbClientBasicProccessWrapper:
    """
    this is the basic gdb executable wrapper
    its read and can write also know to quit
    """
    def __init__(self, gdb_path, *args):
        self.process = pexpect.spawn(gdb_path, list(args))

    def write(self, commmand_to_send: str) -> int:
        """
        send command
        return the number of bytes written
        """
        return self.process.sendline(commmand_to_send)

    def read(self,timeout=5) -> str:
        """
        read data from the gdb
        return the output of the cli
        may raise pexpect.TIMEOUT
        """
        self.process.expect(gdb_constants.GDB_START_LINE,timeout=timeout)
        return self.process.before
    
    def raw_read(self,timeout=5):
        buffer = b""
        counter = 0
        while timeout  > counter:
            try:
                buffer = buffer + self.process.read_nonblocking(1,0.001)
                counter = 0
            except pexpect.exceptions.TIMEOUT:
                counter += 0.001
        return buffer
            
    def go_interactive_session(self):
        self.process.interact()

    def quit(self):
        self.write("quit")
    