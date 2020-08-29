import re

HEX_REGEX_MATCH = r"0x(?P<hex>[\da-fA-F]+)"

def eval_hex_string_to_number(string_number :str) -> int:
    is_hex = re.compile(HEX_REGEX_MATCH)
    is_there_match = is_hex.search(string_number)
    if is_there_match:
        return int(is_there_match.group("hex"),16)
    return None

def parse_examining_memory(*string_to_parse):
    for line in string_to_parse:
        splitted_text = line.split(":",1)[-1]
        for number in (not_empty for not_empty in splitted_text.split("\t") if not_empty):
            yield eval_hex_string_to_number(number)

        
    

