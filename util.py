#Helper functions
def str_to_int(message: str):

    return int.from_bytes(message.encode(), byteorder='big')

def int_to_str(number: int):

    byte_length = (number.bit_length() + 7) // 8
    return number.to_bytes(byte_length, byteorder='big').decode()

