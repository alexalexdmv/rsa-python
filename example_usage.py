import key_generation
import crypto


public_key, private_key = key_generation.generate_key_pair(512)

message = "I like cryptography"

cipher = crypto.encrypt(message, public_key)

print("Encrypted: ", cipher)

decrypted_cipher = crypto.decrypt(cipher, private_key, True)

print("Decrypted: ", decrypted_cipher)