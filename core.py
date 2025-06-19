# Encrypts an integer message using the public key (n, e)
def encryption(message: int, public_key: tuple[int, int]):

    n, e = public_key

    encrypted_message = pow(message, e, n)
    
    return encrypted_message

# Decrypts an encrypted integer message using the private key (n, d)
def decryption(encrypted_message, private_key:tuple[int, int]):
    
    n, d = private_key

    decrypted_message = pow(encrypted_message, d, n)
   
    return decrypted_message

