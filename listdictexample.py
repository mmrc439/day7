# person1={'id':1,'name':'Moshiur','salary':20000}
# person2={'id':2,'name':'Rezaul','salary':40000}
# person3={'id':3,'name':'Nazmul','salary':30000}
# person4={'id':4,'name':'Sonjoy','salary':45000}
# person5={'id':5,'name':'Sunny','salary':10000}
# person6={'id':6,'name':'Fahim','salary':25000}

persons=[
    {'id':1,'name':'Moshiur','salary':20000},
    {'id':2,'name':'Rezaul','salary':40000},
    {'id':3,'name':'Nazmul','salary':30000},
    {'id':4,'name':'Sonjoy','salary':45000},
    {'id':5,'name':'Sunny','salary':10000},
    {'id':6,'name':'Fahim','salary':25000}
]

print("%-5s %-25s %-10s"%('Id','Name','Salary'))
print('='*80)
for per in persons:
    print("%-5s %-25s %-10s"%(per['id'],per['name'],per['salary']))

