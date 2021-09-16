import hashlib
  
textoinit = input("O que deseja converter?")
  
result = hashlib.md5(textoinit.encode())
  
# printing the equivalent hexadecimal value.
print("O seu texto em md5 é: ", end ="")
print(result.hexdigest())

