# RSA Cryptography in Python

This project implements RSA cryptography in Python.

---

## Files Overview

- `core.py`  
  Contains the core RSA encryption and decryption functions working on integers.

- `crypto.py`  
  Higher-level implementation to encrypt/decrypt strings or integers using keys.

- `key_generation.py`  
  RSA key pair generation including prime generation using the Miller-Rabin test.

- `miller_rabin_test.py`  
  Probabilistic primality testing with Miller-Rabin algorithm.

- `util.py`  
  Helper functions for conversions between strings and integers.

- `example_usage.py`  
  Simple usage example demonstrating key generation, encryption, and decryption.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/alexalexdmv/rsa-python.git
cd rsa-python

---

## Notes

- Primality testing uses the Miller-Rabin algorithm for efficiency and reliability.
- Recommended minimum bit length for secure keys is 512 bits; prefer 1024 or higher for better security.
- This implementation is for educational purposes, **not** for production security.

---

## Usage

You can generate keys, encrypt, and decrypt messages by importing the modules in your Python code. See example_usage.py for a simple demonstration.



