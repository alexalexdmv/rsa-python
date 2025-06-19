import math
import secrets
import miller_rabin_test


# Perform a primality check efficiently with the Miller-Rabin test
def is_prime(num, num_of_test):
    return miller_rabin_test.miller_rabin(num, num_of_test)

# Generate a random prime number in a large range
def generate_prime_random(minimum, maximum, num_of_test = 10):
    candidate = secrets.randbelow(maximum-minimum) + minimum

    while not is_prime(candidate, num_of_test):
        candidate = secrets.randbelow(maximum-minimum) + minimum

    return candidate

# Compute modular inverse of e modulo z (d such that e*d ≡ 1 mod z)
def inverse_mod(e, z):
        return pow(e, -1, z)

# Generate RSA key pair of a given bit length
def generate_key_pair(bit_length):

    # Enforce a large minimum bit length
    if bit_length < 512:
        bit_length = 512

    min_val = 1 << (bit_length - 1)
    max_val = (1<< bit_length) - 1


    p = generate_prime_random(min_val, max_val)
    q = generate_prime_random(min_val, max_val)

    #Enforce using two distinct prime numbers
    while p == q:
        q = generate_prime_random(min_val, max_val)

    n = p * q

    z = (p-1) * (q-1)

    e = secrets.randbelow(z - 3) + 3

    while math.gcd(e, z) != 1:
        e = secrets.randbelow(z - 3) + 3

    d = inverse_mod(e, z)

    # Return public and private RSA key pairs:
    # Public key:  (n, e)
    # Private key: (n, d)
    return (n,e), (n,d)
