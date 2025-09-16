# AT&T asm prelude

push eax
equal with:
mov [esp], eax
sub esp, 4

pop eax
get values out of stack
equal with

add rsp, 4
mov eax, [esp]