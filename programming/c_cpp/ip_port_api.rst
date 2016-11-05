- int inet_aton(const char* cp, struct in_addr* inp); 

  - converts IPv4 address: string [cp] => binary(network byte order) [inp].
  - binary at struct in_addr.s_addr

- char* inet_ntoa(struct in_addr in);

  - converts IPv4 address: binary(network byte order) [in] => string [return value].
  - return value(string) is statically allocated buffer, subsequent calls will overwrite it.


- int inet_aton(const char* cp, struct in_addr* inp);
  - string => nbytes binary
- char* inet_ntoa(struct in_addr in);
  - nbytes binary => string

- in_addr_t inet_addr(const char* cp);
- in_addr_t inet_network(const char* cp);

- struct in_addr inet_makeaddr(in_addr_t net, in_addr_t host);
  - uint32_t (host byte) => struct in_addr
- in_addr_t inet_lnaof(struct in_addr in);
- in_addr_t inet_netof(struct in_addr in);
  - struct in_addr => uint32_t (host byte)
