a = input("Ingresa el valor de a: ")
a = int(a)

b = input("Ingresa el valor de b: ")
b = int(b)

#para usar condicionales se utilizan if-else
if a > b: # el valor de if de ser un valor boleano
    print(a)
else:
    print(b)
    
    
# para comparar dos valores se utilizan los sig simbolos
# > == < !=

if a == b:
  print("el valor de a y b son iguales")
  
if a != b:
  print("el valor de a y b no son iguales")
  
if a > b:
  print("a es mayor")
  
if a < b:
  print("a es menor")
  
  
# keyword 'and'
print()
salary = 5700
vacation_days= 23

if salary > 5000 and vacation_days > 40:
    print ("I will take this job.")
else: 
    print("This job sucks! Give it to Jerry.")
    
    
# keyword 'or'

money = 100
extra_income = True

if money > 1000 or extra_income:
  print("necesito vacaciones")
else:
  print("necesito trabajar..")





    

