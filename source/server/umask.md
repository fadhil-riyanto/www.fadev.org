# umask

```
    Permission | Binary | Octal  | User  | Group | Other |
    ======================================================
      r        |  100   |   4    |       |       |       |
      w        |  010   |   2    |       |       |       |
      x        |  001   |   1    |       |       |       |
    =======================================================
```

for example
##
- the owner of file has read, write, and execute
- file group only read and execute
- the other only can read

the permission is like this
```
u   g   o
rwx r-x  r--
```


aka, because rwx has total point of 4 + 2 + 1, so the permission for user is 7
because group only have 4 & 1, so the permission is 5
and last. other only read, which is 4

the equalivalent command is `chmod 754`