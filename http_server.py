import socket
import http.server
import socketserver
import os
import time
import sys

host = socket.gethostname()
host = socket.gethostbyname(host)
#host = "127.0.0.1"
print(host)
port=80

print("*"*30)
print("Welcome to http file sharing service!!!!!!")
print("*"*30)



while True:
	try:
		print("Press cntl+c to closing the server!!!!!")
		print("*"*30)
		dirs = input("Enter the directory you want to share!!!!!\n")
		print()
		os.chdir(dirs)

	except KeyboardInterrupt as e:
		print("*"*30)
		print("closing the connection!!!!!!")
		sys.exit(0)
		break

	except FileNotFoundError as e:
		print("*"*30)
		print("Invalid directory!!!!!")
		print("*"*30)
		print("Try again!!!!")
		continue

	except:
		print("closing The connection!!!!")
		break
	try:
		handlr = http.server.SimpleHTTPRequestHandler
		with socketserver.TCPServer((host,port),handlr) as httpd:
			print("*"*30)
			print("serving at port",port)
			print("*"*30)
			print("Enter cntl+c to change the directory!!!!")
			print("*"*30)
			httpd.serve_forever()

	except ConnectionResetError as e:
		print("Request closed by the remote host")

	except KeyboardInterrupt as e:
		print("Processing your Request!!!!")
		time.sleep(0.5)
		continue

	except Exception as e:
		print(str(e))

print()
print("*"*30)
print("Bye bye see you again!!!!!")


