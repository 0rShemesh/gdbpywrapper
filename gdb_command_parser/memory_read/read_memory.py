"""
this file supposed for parse read memory features of gdb
"""

import re
from typing import Generator, Optional
HEX_REGEX_MATCH = r"0x(?P<hex>[\da-fA-F]+)"

def eval_hex_string_to_number(string_number :str) -> Optional[int]:
    """
    get number as string and eval it to hex
    string_number - the number in hex we want to convert to int
    TODO: maybe an better solution is to raise exception insted of return None
    """
    is_hex = re.compile(HEX_REGEX_MATCH)
    is_there_match = is_hex.search(string_number)
    if is_there_match:
        return int(is_there_match.group("hex"),16)
    return None



def parse_examining_memory(*string_to_parse) -> Generator[int]:
    """
    this method get unpacking argument lists of string and convert it to generator contains numbers right now
    TODO: need to think if that the best design
    """
    for line in string_to_parse:
        splitted_text = line.split(":",1)[-1]
        for number in (not_empty for not_empty in splitted_text.split("\t") if not_empty):
            yield eval_hex_string_to_number(number)

        
    

