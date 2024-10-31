a = "Harry Potter and Goblet of fire"

w = a.split()

for i in range (len(w)):
    w[i] = w[i].lower()
  
w.sort()    
print(w)

for i in w:
    print(i)