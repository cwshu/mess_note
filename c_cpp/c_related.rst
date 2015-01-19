fork and exec
-------------
- execl(path, argv[0], argv[1], ... , NULL)

file IO
-------
POSIX
+++++
- int open(const char* pathname, int flags, mode_t mode);
  - flags
    - O_RDONLY
    - O_WRONLY | O_CREAT | O_TRUNC

fd control in POSIX
-------------------
- dup2(int oldfd, int newfd);
  - oldfd => newfd;
    - close(newfd), copy oldfd content to newfd number.

file status and existence
-------------------------
POSIX
+++++
- access: check if you can access file

  - access(const char* path, int mode)

    - mode

      - F_OK
      - R_OK, W_OK, X_OK

- stat


socket API
----------
- fcntl: manipulate fd
- ioctl: control device

- recv 

  - flags

    - MSG_DONTWAIT

      - nonblocking read, 等同 fcntl set O_NONBLOCK
   
    - MSG_PEEK
      
      - 收資料, 但不從 recieve queue 清掉收的資料 (代表下次 recv 會在收到一樣的資料).

