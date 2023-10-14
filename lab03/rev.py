password = "ThePassword"
output = ""

for c in password:
    result = ((ord(c) * 7 ) % 25 + 97)
    output += chr(int(result))

print(output)
