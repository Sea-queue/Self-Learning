
/*
struct addrinfo:
This structure is used to prep the socket addresses structures for
subsequent use. It's also used in host name lookups, and service
name lookups.
*/

struct addrinfo {
    int             ai_flags; //AI_PASSIVE, AI_CANONNAME, est.
    int             ai_family; //AF_INET, AF_INET6, AF_UNSPEC
    int             ai_socktype; // SOCK_STREAM, SOCK_DGRAM
    int             ai_protocol; //use 0 for "any"
    size_t          ai_addrlen; // size of ai_addr in bytes
    struct sockaddr *ai_addr; //struct sockaddr_in or _in6
    char            *ai_canonname; // full canonical hostname

    struct addrinfo *ai_next; // linked list, next node
};

//holds socket address information for many types of sockets.
//sa_family will be AF_INET(IPv4) or AF_INET6(IPv6).
//sa_data contains a destination address and port number for the socket
struct sockaddr {
    unsigned short      sa_family; //address family AF_xxx
    char                sa_data[14];  // 14 bytes of protocol address
};

//"in" for "Internet" used for IPv4.
struct sockaddr_in {
    short int       sin_family; //Address family, AF_INET
    unsigned short  sin_port;  // Port number
    struct in_addr  sin_addr; //Internet address
    unsigned char   sin_zero[8]; //Same size as struct sockaddr
};

//Internet address (a structure for historical reasons)
struct in_addr {
    uint32_t    s_addr; //that's a 32-bit int (4 bytes)
};

//(IPv6 only)
struct sockaddr_in6 {
    u_int16_t       sin6_family; //address family,AF_INET6
    u_int16_t       sin6_port; //port number, Network Byte Order
    u_int32_t       sin6_flowinfo; //IPv6 flow information
    struct in6_addr sin6_addr;  //IPv6 address
    u_int32_t       sin6_scope_id; //Scope ID
};

struct in6_addr {
    unsigned char       s6_addr[16]; //IPv6 address
};

/*
To hold both IPv4 and IPv6 structures
What's important is that you can see the address family in the
ss_family filed - check this to see if it's AF_INET or AF_INET6
(for IPv4 or IPv6). Then you can cast it to a struct sockaddr_in
or struct sockaddr_in6 if you wanna.
*/
struct sockaddr_storage {
    sa_family_t     ss_family; //address family

    //all this is padding, implementation specific, ignore it:
    char            __ss_pad1[_SS_PAD1SIZE];
    int64_t         __ss_align;
    char            __ss_pad2[_SS_PAD2SIZE];
};

/*
You have a struct sockaddr_in ina, and an IP address that you want
to store into it. You need to use the function: inet_pton().
*/

struct sockaddr_in sa; //IPv4
struct sockaddr_in6 sa6; //IPv6

//inet_pton() returns -1 on error, or 0 if the address is messed up
//check to make sure the result is greater than 0 before using!
inet_pton(AF_INET, "10.12.110.57", &(sa.sin_addr)); //IPv4
inet_pton(AF_INET6, "2001:db8:63b3:1::3490", &(sa6.sin6_addr)); //IPv6


//have sockaddr_in/in6 want the numbers-and-dots/hex-and-colons notation
//IPv4:
char ip4[INET_ADDRSTRLEN]; //space to hold the IPv4 string
struct sockaddr_in sa; //pretend this is loaded with something

inet_ntop(AF_INET, &(sa.sin_addr), ip4, INET_ADDRSTRLEN);

printf("the IPv4 address is: %s\n", ip4);

//IPv6:
char ip6[INET_ADDRSTRLEN]; //space to hold the IPv6 string
struct sockaddr_in6 sa6; //pretend this is loaded with something

inet_ntop(AF_INET6, &(sa6.sin_addr), ip6, INET6_ADDRSTRLEN);

printf("The address is: %s\n", ip6);


//Prepare to launch -- getaddrinfo()
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>

int getaddrinfo(const char *node, // e.g. "www.example.com" or IP
                const char *service, // e.g. "http" or port number
                const struct addrinfo *hints,
                struct addrinfo **res);

//here is a sample call if you're a server who wants to listen on
//you host's IP address, port 3490.
//this doesn't actually do any listening or network setup;
//it merely sets up structures we'll use later

int status;
struct addrinfo hints;
struct addrinfo *servinfo; //will point to the results

memset(&hints, 0, sizeof hints); //make sure the struct is empty
hints.ai_family = AF_UNSPEC; //don't care IPv4 or IPv6
hints.ai_socktype = SOCK_STREAM; //TCP stream sockets
hints.ai_flags = AI_PASSIVE;  //fill in my IP for me

if ((status = getaddrinfo(NULL, "3490", &hints, &servinfo)) != 0) {
    fprintf(stderr, "getaddrinfo  error: %s\n", gai_strerror(status));
    exit(1);
}

//servinfo now points to a linked list of 1 or more struct addrinfos
// ...do everything until you don't need servinfo anymore ...
freeaddrinfo(servinfo); //free the linked-list

//Here's a sample call if you're a client who wants to connect to a
//particular server, say "www.example.net", port 3490. Again, this
//doesn't actually connect, but it sets up the structures we'll use later:

int status;
struct addrinfo hints;
struct addrinfo *servinfo; //will point to the results

memset(&hints, 0, sizeof hints); //make sure the struct is empty
hints.ai_family = AF_UNSPEC; //don't care IPv4 or IPv6
hints.ai_socktype = SOCK_STREAM; //TCP stream sockets

//get ready to connect
status = getaddrinfo("www.example.net", "3490", &hints, &servinfo);

//servinfo now points to a linked list of 1 or more struct addrinfos


//Get the File Descriptor! -- socket()

#include <sys/types.h>
#include <sys/socket.h>

//IPv4 or IPv6; stream or datagram; TCP or UDP
int socket(int domain, int type, int protocol);

//Use the values from the results of the call to getaddrinfo(),
//and feed them into socket() derectly like this:

int s;
struct addrinfo hints, *res;

getaddrinfo("www.example.com", "http", &hints, $res);

//socket() simply returns to you a socket descriptor that you can
//use in later system calls, or -1 on error.
s = socket(res->ai_family, res->ai_socktype, res->ai_protocol);


//What port am I on? -- bind()
#include <sys/types.h>
#include <sys/socket.h>

//sockfd is the socket file descriptor returned by socket()
//my_addr is a pointer to a struct sockaddr that contains information
//about your address, namely port and IP address.
//addrlen is the length in bytes of the address.
int bind(int sockfd, struct sockaddr *my_addr, int addlen);

struct addrinfo hints, *res;
int sockfd;

//first load up address structs with getaddrinfo()

memset(&hints, 0, sizeof hints);
hints.ai_family = AF_UNSPEC; //use IPv4 or IPv6,
hitns.ai_socktype = SOCK_STREAM;
hints.ai_flags = AI_PASSIVE; //fill in  my IP for me

getaddrinfo(NULL, "3490", &hints, &res);

//make a socket;
sockfd = socket(res->ai_family, res->ai_socktype, res->ai_protocol);

//bind it to the port we passed in ot getaddrinfo();

bind(sockfd, res->ai_addr, res->ai_addrlen);

//"Address already in use" ERROR
//you can eithe wait for it to clear (a minute or so)
//or add code to your program allowing it to reuse the port
int yes = 1;

if (setsockopt(listener, SOL_SOCKET, SO_REUSEADDR, &yes, sizeof yes) == -1) {
    perror("setsockopt");
    exit(1);
}

//Hey, you! -- connect()
#include <sys/types.h>
#include <sys/socket.h>

//sockfd is socket file descriptor as returned by the socket() call,
//serv_addr is a struct sockaddr containing the destination port and IP address
//addrlen is the length in bytes of the server address structure.
//all of this information can be gleaned from the results of the getaddrinfo() call which rocks.
int connect(int sockfd, struct sockaddr *serv_addr, int addrlen);

struct addrinfo hints, *res;
int sockfd;

//first load up address structs with getaddrinfo();

memset(&hints, 0, sizeof hints);
hints.ai_family = AF_UNSPEC;
hints.ai_socktype = SOCK_STREAM;

getaddrinfo("www.example.com", "3490", &hints, &res);

//make a socket;

sockfd = socket(res->ai_family, res->ai_socktype, res->ai_protocol);

//connect!

connect(sockfd, res->ai_addr, res->addrlen);

//Will somebody please call me? -- listen()

//sockfd is the usual socket file descriptor from the socket() system call
//backlog is the number of connections allowed on the incoming queue
int listen(int sockfd, int backlog);

/*
sequence of system call:
getaddrinfo();
socket();
bind();  so that the server is running on a specific port.
listen();
accept();
*/


//"thank you for calling port 3490" -- accept()

#include <sys/types.h>
#include <sys/socket.h>

//sockfd: is the listen()ing socket descriptor.
//addr will usually be a pointer to a local struct sockaddr_storage
//this is where the information about the incoming connection will go
//addrlen is a local integer variable that should be set to
//sizeof(struct sockaddr_storage) before its address is passed to accept()
int accept(int sockfd, struct sockaddr *addr, socklen_t *addrlen);

#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>

#define MYPORT "3490" //the port users will be connecting to
#define BACKLOP 10 //how many pending connections queue will hold

int main(void) {
    struct sockaddr_storage their_addr;
    socklen_t addr_size;
    struct addrinfo hints, *res;
    int sockfd, new_fd;

    //!!don't forget error checking for these calls

    //first, load up address structs with getaddrinfo();
    memset(&hints, 0, sizeof hints);
    hints.ai_family = AF_UNSPEC; //IPv4 or IPv6
    hints.ai_socktype = SOCK_STREAM;
    hints.ai_flags = AI_PASSIVE; //fill in my IP for me

    getaddrinfo(NULL, MYPORT, &hints, &res);

    //make a socket, bint it, and listen on it

    sockfd = socket(res->ai_family, res->ai_socktype, res->ai_protocol);
    bind(sockfd, res->ai_addr, res->ai_addrlen);
    listen(sockfd, BACKLOG);

    //now accept an incoming connection:

    addr_size = sizeof their_addr;
    new_fd = accept(sockfd, (struct sockaddr *)&their_addr, &addr_size);

}

//Talk to me, tell me your name -- send() and recv()

//sockfd is the socket descriptor you want to send data to
//msg is a pointer to the data you want to send,
//len is the length of that data in bytes
//set flags to 0.
int send(int sockfd, const void *msg, int len, int flags);

//sample:
char *msg = "Beej was here!";
int len, bytes_sent;

len = strlen(msg);
bytes_sent = send(sockfd, msg, len, 0);


//sockfd is the socket descriptor to read from,
//buf is the buffer to read the information into,
//len is the maximum length of the buffer,
//flags can be set to 0
int recv(int sockfd, void *buf, int len, int flags);
