from typing import Union
import core
import util

# Encrypts an integer/string message using the public key (n, e)
def encrypt(message: Union[str, int], public_key: tuple[int, int]):

    if type(message) == str:

        m = util.str_to_int(message)

    elif type(message) == int:

        m = message

    else:

        raise TypeError("Only strings or integer values allowed")
    
    return core.encryption(m, public_key)


# Decrypts an encrypted integer/string message using the private key (n, d)
def decrypt(encrypted_message: int, private_key: tuple[int, int], return_as_string: bool):

    message = core.decryption(encrypted_message, private_key)

    if return_as_string:

        return util.int_to_str(message)
    else:

        return message


