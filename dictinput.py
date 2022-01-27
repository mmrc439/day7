import os
listemp=[]
n=int(input('how many data :'))
for i in range(1,n+1):
    os.system('cls')
    employees={}
    print('id number : %s'%(i))
    employees['id']= i
    employees['name']=input('enter your name :')
    employees['salary']=input('enter your salary :')
    listemp.append(employees)

print(listemp)


