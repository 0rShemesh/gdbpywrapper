


def get_command_text(returned_text : bytes) -> tuple:
    decdoded_string = returned_text.decode().split("\r\n")
    return (decdoded_string[0], decdoded_string[1::])