import random
import os

#end = bytes([random.getrandbits(8) for _ in range(8)]).hex()
#flag = "flag{s33d1ng_f(_)n(t10n_"+end+"}"

#print(f"Generated {flag=}")
flag = os.environ.get("FLAG")

if not flag:
    print("Flag was not found in FLAG environment variable. Aborting.")
    exit(-1)

with open("flag", "w") as file:
    file.write(flag)
    file.close()

