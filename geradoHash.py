
import hashlib
print("Gere um Hash a partir de uma frase ou senha.  :")
print()
try:
	txt = input("Informe :")
	print("Escolha o Tipo de Hash")
	menu = int(input("""[*] Hash

		1) md5
		2) sha1

"""))
	if menu not in [1,2]:
		print("Informe uma das Opçoes :")
	elif menu == 1:
		txtencriptado = hashlib.md5(txt.encode('utf-8'))
		print("A Hash Gerada e: ",txtencriptado.hexdigest())
	else:
		txtencriptado = hashlib.sha1(txt.encode('utf-8'))
		print("A Hash Gerada e: ",txtencriptado.hexdigest())
except:
	print("Você não informou uma das opções de hash.")

