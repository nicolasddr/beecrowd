n = int(input())
hexadecimal = input()

hexadecimal = hexadecimal.replace(' ', '')

bytes_frase = bytes.fromhex(hexadecimal)

ascii_frase = bytes_frase.decode('ASCII')

print(ascii_frase)