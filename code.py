Coding:
  
string = input()
freq = {} 
for i in string: 
    if i!=" ":
     if i in freq: 
        freq[i] += 1
     else: 
        freq[i] = 1
res = min(freq, key = freq.get)  
print (res,end=" ") 
print(freq[res])
