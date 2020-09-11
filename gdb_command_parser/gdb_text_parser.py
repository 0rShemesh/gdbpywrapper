"""
gdb text parser
will have functions that parse the gdb cli
"""
from typing import Tuple

def get_command_text(returned_text : bytes) -> Tuple[str,str]:
    """
    split the lines to tuple the first value in the tuple that string with the sent command
    the seccond argument is the answer
    """
    decdoded_string = returned_text.decode().split("\r\n")
    return (decdoded_string[0], decdoded_string[1::])