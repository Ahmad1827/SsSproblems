from pwn import *

elf = ELF('./one_by_one')
flag = ""
i = 0

while True:
    sym_name = f"part{i}"
    if sym_name in elf.symbols:
        addr = elf.symbols[sym_name]
        flag += chr(elf.read(addr, 1)[0])
        i += 1
    else:
        break

print(flag)