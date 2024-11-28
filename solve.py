from Crypto.Util import number
from sympy import mod_inverse
import socket, random, hashlib
import argparse

def netcat_read(s):
	response = s.recv(2048).decode()
	for line in response.splitlines():
		print("<< "+line)

	return response

def netcat_write(s, message):
	for line in message.splitlines():
		print(">> "+line)

	s.sendall((message+"\n").encode())

def random_gen(n):
	return bytes([random.getrandbits(8) for _ in range(n)])

def secure_seed(name):
	name = name[:-1]
	name = "".join([chr(ord(name[i])+(-1)**(i)) for i in range(len(name))])
	return int(hashlib.sha256(name.encode()).hexdigest(), 16)

def main():
	parser = argparse.ArgumentParser(description="Run the solve")
	parser.add_argument(
		"--port", 
		"-p", 
		action="store", 
		type=int,
		default=8888, 
		help="Port to connect on", 
		required=False
	)
	parser.add_argument(
		"--host",
		action="store",
		default="127.0.0.1",
		help="Host for server",
		required=False,
	)

	args = parser.parse_args()
	HOST, PORT = args.host, args.port
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST,PORT))

	netcat_read(s)

	name = "Tilden"
	netcat_write(s, name)

	result = netcat_read(s)
	result = result.splitlines()[-1][1:-1].split(",")
	c, e, N = result
	c, e, N = int(c), int(e), int(N)

	random.seed(secure_seed(name))

	p = number.getPrime(1024, randfunc=random_gen)
	q = number.getPrime(1024, randfunc=random_gen)
	while (p*q != N):
		q = number.getPrime(1024, randfunc=random_gen)

	phi = (p-1)*(q-1)
	d = mod_inverse(e, phi)

	flag = number.long_to_bytes(pow(c, d, N)).decode()
	print(f"\n{flag=}")

if __name__ == "__main__":
	main()