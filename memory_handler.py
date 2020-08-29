
from gdb_basic_wrapper import GdbClientBasicProccessWrapper
from gdb_command_parser.gdb_text_parser import get_command_text
from gdb_command_parser.memory_read.read_memory import parse_examining_memory


class MemoryHandler:
    def __init__(self, process: GdbClientBasicProccessWrapper):
        self._process = process

    def do_examining_memory_raw(self,FMT:str,ADDRESS:str):
        """"
        examining memory 
        write on gdb: help x for more
        """
        string_to_send = "x"
        if FMT:
            string_to_send +"/" + format(FMT)
        string_to_send += " " + ADDRESS
        self._process.write(string_to_send)
        return get_command_text(self._process.read())

    def do_examining_memory(self, repeat_count=1, display_format="x", unit_size="b", address=0x7ffffff00000):

        examining_format = "{repeat_count}{unit_size}{display_format}".format(repeat_count=repeat_count, display_format=display_format, unit_size=unit_size)

        return self.do_examining_memory_raw(examining_format,address if isinstance(address,str) else str(address))

    def read_bytes(self, address: int, amount: int = 1):
        returned_data = self.do_examining_memory(
            repeat_count=amount, unit_size="b", address=address)
        return parse_examining_memory(*returned_data)

    def read_words(self, address: int, amount: int = 1):
        returned_data = self.do_examining_memory(
            repeat_count=amount, unit_size="w", address=address)
        return parse_examining_memory(*returned_data)
