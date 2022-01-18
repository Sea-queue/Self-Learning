
# Echo Client

import socket

HOST = '127.0.0.1' # The server's hostname or IP address
PORT = 65432       # The port used by the server

"""
It creates a socket object, connects to the server and calls s.sendall() to
send its message.
it calls s.recv() to read the server's reply and then prints it.

Running th EchoClient and Server:

$ ./echo-server.py
The terminal will appear to hang because the server is blocked(suspended)
in a call: "conn, addr = s.accept()"

It's waiting for a client connection. Now open another terminal window or
command prompt and run the client:
$ ./echo-client.py
Received b'Hello, world'

In the server window, you should see:
Connected by ('127.0.0.1', 64623)

In the output above, the server printed the addr tuple returned from s.accept().
This is the client's IP address and TCP port number. The port number, 64623, will
most likely different when you run it each time.
"""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))
