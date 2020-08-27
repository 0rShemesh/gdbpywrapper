

def eval_string_to_number(string_number :str) -> int:
    return eval(string_number) # need to replace

def parse_examining_memory(*string_to_parse):
    for line in string_to_parse:
        splitted_text = line.split(":",1)[-1]
        for number in (not_empty for not_empty in splitted_text.split("\t") if not_empty):
            yield eval_string_to_number(number)

        
    

