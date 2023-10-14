import sys

c = sys.argv[1]

c = atoi(c)


#for i in range(0, 255):

 #  print(f"Input: {i} Output: {(i * 7) - 97}")


print(f"Input: {c} Output: {( (c * 7) - (c * 7 // 25) * 25 + 97 )}")


