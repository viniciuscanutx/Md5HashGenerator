import hashlib
  
textoinit = input("O que deseja converter?")
  
result = hashlib.md5(textoinit.encode())
  
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", end ="")
print(result.hexdigest())

