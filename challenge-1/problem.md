# Secure Seed?

- Namespace: picoctf/18739f24
- ID: tilden-challenge-1
- Type: custom
- Category: Cryptography
- Points: 10
- Templatable: yes
- MaxUsers: 1

## Description

My data is encrypted securely... from the roots to the seed.

## Details

Connect to {{server}}:{{port}} and decrypt the RSA encrypted ciphertext for the flag.. {{url_for("challenge.py", "source")}}

## Hints

- Have you heard of random function seeding?
- Did you know you can specify random functions in RSA crypto primitives?

## Solution Overview
* Control the seed
* Simulate the encryption/decryption key generation
* Check it matches

Check solve.py.

## Attributes
- author: Tilden Jackson
- organization: 18739
