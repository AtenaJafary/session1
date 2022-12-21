import math 
while True :
  a=int(input("please enter a number: "))
  op=input("please entrer operation: ")

  if op=="+" :
    b=int(input("please enter second number: "))
    result = a+b
  if op=="-" :
     b=int(input("please enter second number: "))
     result = a-b
  if op=="*" :
     b=int(input("please enter second number: "))
     result = a*b
  if op =="/" :
      b=int(input("please enter second number: "))
      if b==0:
       result= "error"
      if b!=0:
        result= a/b
  if op =="sin" :
     D1= math.radians(a)
     result=math.sin(D1)
  if op =="cos" :
    D2= math.radians(a)
    result= math.cos(D2)
  if op =="tan" :
    D3=math.radians(a)  
    result=math.tan(D3)  
  if op == "cot" :
    if a==0 :
        result("error")
    elif a!=0 : 
        D4= math.radians(a)   
        result=1/math.tan(D4)
  if op =="factorial" :
     result= math.factorial(a)  
  if op =="radical" :
     if a>=0 :
        result =math.sqrt(a)
  if op == "quit" :
     break      
  print(result)