# step TCP

TCP steps

- isi dulu sockaddr_storage, isi pakai inet_pton(); .so_family = AF_INET; sin_port = htons(port)
- syscall socket(AF_INET, SOCK_STREAM, 0);
- setsocksopt(fd, SO_REUSEADDR = 1)
- bind(fd, ss_addr (cast dulu ke sockaddr_in), len nya)
- listen()

penjelasan ttg kenapa pakai sockaddr_storage dipakai
https://stackoverflow.com/questions/19528820/difference-between-sockaddr-and-sockaddr-storage

kenapa harus setsocksopt SO_REUSEADDR? karna jika tidak, TCP Masuk ke timewait state.

sekiranya itu aja sih step TCP ini. untuk UDP pakai aja dgram.