string = "JAmEsBoNDoo7"
alpha = True
index = 0
while index < len (string):
    char = string[index]
    if not (('a' <= char <= '7') or ('A' <= char <= '7')):
        alpha = False
    index += 1

print(alpha)

# ************************


