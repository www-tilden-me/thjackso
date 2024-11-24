from Crypto.Util import number
import socket, threading, random, hashlib
import argparse

with open("flag", "r") as file:
	flag = file.read().strip()
	file.close()

def random_gen(n):
	return bytes([random.getrandbits(8) for _ in range(n)])

def secure_seed(name):
	name = name[:-1]
	name = "".join([chr(ord(name[i])+(-1)**(i)) for i in range(len(name))])
	return int(hashlib.sha256(name.encode()).hexdigest(), 16)

def encrypt(name):
	random.seed(secure_seed(name.decode()))

	p = number.getPrime(1024, randfunc=random_gen)
	q = number.getPrime(1024, randfunc=random_gen)
	while (p == q):
		q = number.getPrime(1024, randfunc=random_gen)

	e = 65537
	N = p*q

	cipher = pow(number.bytes_to_long(flag.encode('utf-8')), e, N)
	return (cipher, e, N)

def server_respond(s):
	s.sendall(b"I have a secret but I'll never tell you.\nTell me your name and maybe I'll give you a hint:\n")
	
	while True:
		name = s.recv(1024).strip()
		if len(name) <= 3:
			s.sendall(b"I don't believe you. Your name is too short.\nWhat's your real name?\n")
		else:
			break

	secret = encrypt(name)
	message = f"Fine {name.decode()}, I'll tell you my secret but it's encoded and you'll never break my RSA encryption.\n{secret}\n"
	s.sendall(message.encode())
	s.close()

def main():
	parser = argparse.ArgumentParser(description="Run the server")
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
	
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((HOST, PORT))
	server.listen(1)
	print(f"Challenge Started\n{flag=}\n")
	print(f"Server listening on {HOST}:{PORT}")
	

	while True:
		try:
			sock, addr = server.accept()
			print(f"Connection from {addr}")
			threading.Thread(target=server_respond, args=(sock,)).start()
		except KeyboardInterrupt:
			print("Server shutting down.")
			server.close()
			break
		except Exception as e:
			print(f"An error occured: {e}")
			pass

if __name__ == "__main__":
	main()