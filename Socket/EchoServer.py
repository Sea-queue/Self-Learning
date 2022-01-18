
# Echo Server

#!/usr/bin/env python3
import socket

"""
socket.socket():
creates a socket object that supports the "context manager" type, so you can
use it in a "with statement". There is no need to call s.close()

The arguments passed to socket() specify the address family and socket type.
AF_INET is the internet address family for IPv4.
SOCK_STREAM is the socket type for TCP, the protocol that will be used to
transport our messages in the network.

bind():
Associate the socket with a specific network interface and port number.
The values passed to bind() depend on the address family of the socket.
socket.AF_INET(IPv4)  : (host, port)
socket.AF_INET6(IPv6) : (host, port, flowinfo, scopeid)

host:
can be a hostname, IP address, or empty string.
• hostname
note: the program may show a non-deterministic behavior, as Python uses the
first address returned from the DNS resolution. The socket address will be
resolved differently into an actual IPv6/v6 address, depending on the results
from DNS resolution and/or the host configuration. For deterministic behavior
use a numeric address in host portion.
• 127.0.0.1
the standard IPv4 address for the loopback interface, only processess on the
host will be able to connect to the server.
• Empty string
the server will accept connections on all available IPv4 interfaces.

port:
An integer from 1-6553 (0 is reserved) is the TCP port number to accept
connections from clients.

listen():
enables a server to accept() connections. It makes it a "listening" socket.

accept():
blocks and waits for an incoming connection.
When a client connects to it, it returns a new socket object representing the
connection and a tuple holding the address of the client.The tuple will contain
(host, port) for IPv4 connections
(host, port, flowinfo, scopeid) for IPv6 connections

After getting the client socket object "conn" from accept(), an infinite
while loop is used to loop over blocking calls to conn.recv(). This reads
whatever data the client sends and echoes it back using conn.sendall().

If conn.recv() returns an empty bytes object then the client close the connection
and the loop is terminated. The "with statement" is used with conn to automatically
close the socket at the end of the block.
"""

HOST = '127.0.0.1' # Standard loopback interface address (localhost)
PORT = 65432 # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    """
    It's imperative to understand is that we now have a new socket object from
    accept(). It's the socket the server uses to communicate with the client.
    It's distinct from the listening socket that the server is using to accept
    new connections.
    """
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
