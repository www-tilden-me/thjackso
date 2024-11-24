import random

end = bytes([random.getrandbits(8) for _ in range(8)]).hex()
flag = "flag{s33d1ng_f(_)n(t10n_"+end+"}"

print(f"Generated {flag=}")
with open("flag", "w") as file:
    file.write(flag)
    file.close()

