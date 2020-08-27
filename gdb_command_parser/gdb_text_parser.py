


def get_command_text(returned_text : bytes) -> list:
    decdoded_string = returned_text.decode().split("\r\n")
    return decdoded_string[1::]