from gdb_basic_wrapper import GdbClientBasicProccessWrapper
from memory_handler import MemoryHandler




class GDBClient(GdbClientBasicProccessWrapper):
    
    def __init__(self,gdb_path, *args):
        super().__init__(gdb_path,*args)
        self.data = MemoryHandler(self)

    def run(self):
        super().write("run")
        return super().read(15)
    
    def send_raw_command(self,command_of_gdb : str):
        super().write(commmand_to_send=command_of_gdb)

        
    

    
