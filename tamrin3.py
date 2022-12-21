name = input("please enter your name: ")
avarage1=float(input("please enter your avarage1: ")) 
avarage2= float(input("please enter your avarage2: "))
avarage3= float(input("please enter your avarage3: "))
mean =(avarage1+avarage2+avarage3)/3
if mean>=17 :
  avarage="greate"
if 17>mean>=12 :
    avarage="normal"
elif mean<12 :
  avarage="fail"
print (avarage)   