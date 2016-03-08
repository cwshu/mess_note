InterProcess Communication
--------------------------
- communication

  - File
  - pipe
  - FIFO
  - shared memory
  - socket

- locking

  - mutex
  - semaphore
  - conditional variable

pipe
----
* pipe(int pipefd[2]) 

  + create pipe connect with 2 fd
  + return 

    - pipefd[0]: read fd
    - pipefd[1]: write fd

* dup(int oldfd), dup2(int oldfd, int newfd)

  + duplicate file descriptor, make oldfd and newfd interchangable.

socket
------
.. image::

- headers

  - <sys/socket.h>
  - <sys/types.h>
  - <netinet/in.h>

    - struct sockaddr_in 

  - <arpa/inet.h> 

- int socket(int domain, int type, int protocol)

  - domain: AF_INET, AF_INET6, AF_UNIX (ipv4, ipv6, unix socket)
  - type: SOCK_STREAM, SOCK_DGRAM, SOCK_RAW (tcp, udp, ip)
  - protocol: 可先填 0, non-zero for multiple-protocol??
  
- int bind(int sockfd, const struct sockaddr* addr, socklen_t addrlen)

  - sockfd: socket 函式 return 的 socket file descriptor
  - (struct sockaddr*) addr

    - 此參數真實的型態根據 address family(AF_INET or AF_UNIX) 決定, sockaddr 像是 OO 中的 abstract class.
    - struct sockaddr_in (ipv4)
    - struct sockaddr_un (unix socket)

  - addrlen
    - sizeof(addr)

- int connect(int sockfd, const struct sockaddr* addr, socklen_t addrlen)

  - 跟 bind 參數一樣

- int listen(int sockfd, int backlog)

  - maximum length to which the queue of pending connections for sockfd may grow.

- int accept(int sockfd, struct sockaddr* addr, socklen_t* addrlen);

  - 如果 connection 建立成功, 此 connection 會開一個 fd.
  - return connection's fd.

- IO function

  - ssize_t read(int fd, void* buf, size_t count);
  - ssize_t write(int fd, const void* buf, size_t count); 

    - count: 要寫幾 bytes
    - return value: 總共寫了幾 bytes (有可能不完全寫入)

  - int send(int sockfd, const void* buf, int len, int flags)
    - return 實際傳送的 bytes
    - return -1 for error
  - int recv(int sockfd, void* buf, int len, int flags)
    - return 實際傳送的 bytes
    - return 0, 對方已終止 connection 
    - return -1 for error

- ipv4 ip address and port

  - 在 bind/connect 的 API 中皆為數字 (ip/port: 32/16 bits), 要考慮 endianness.

    - network bytes order: big endian, 應該大部份的網路 protocol 都使用, ip protocol 的數字全部使用

      - http://en.wikipedia.org/wiki/endianness#endianness_in_networking

    - host bytes order: cpu 的 endianness, 例如 x86 為 little-endian
    - BSD socket API 有設計 host 跟 network endianness 轉換的 API

      - host 跟 network 雙向 (hton, ntoh)
      - 16 跟 32 bits (short, long)

  - struct sockaddr_in::
  
       // This API is on Linux 3.11/LinuxMint 16
       // from /usr/include/netinet/in.h, gcc include path 可透過 ``gcc -E -v -`` 指令尋找.

       struct sockaddr_in {
           sa_family_t sin_family;      // unsigned short int 
           in_port_t sin_port;          // uint16_t 
           struct in_addr sin_addr;
           unsigned char sin_zero[xxx]; // for padding
       }

       struct in_addr {
           in_addr_t s_addr; // uint32_t 
       }

  - int inet_aton(const char* cp, struct in_addr* inp); 

    - converts IPv4 address cp from string into binary form (network byte order).
    - stores result in inp(struct in_addr).

  - char* inet_ntoa(struct in_addr in);

    - converts IPv4 address cp from string into binary form (network byte order).
    - return value(string) is statically allocated buffer, subsequent calls will overwrite it.

