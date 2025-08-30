list=["jose","maria","pedro","ana","carlos","luisa","carmen"]
print(list[5])
print(list[0])
print(list[2:5]) 
for i in list: print(i)
lista2=list 
print(lista2)
lista3=list[0:5]
print(lista3) 
lista4=list[:] 
print(lista4)
lista5=list [::-1] 
print(lista5)
lista6=list[-3]
print(lista6) 
lista7=list[-3:]
print(lista7)
listab=[1,2,5,7,9,8,10,12,15,20,30]
list[6]="pepe"
print(list) 
list.append("juan")
print(list) 
list.insert(6,"laura")
print(list)
list.extend(["marta","andres","sofia"]) 
print(list)
list.remove("pedro")
print(list) 
list.pop(3) 
print(list) 
for i in range(len(list)): print(i,"-",list[i]) 
lista3="jose" in list 
print(lista3) 
lista3="JULIANA" in list
print(lista3)
lista4=["a","a","b","b","c","c","a"] 
cantidad=lista4.count("a") 
print(cantidad) 
cantidad=list.count("jose")
print(cantidad) 
list.sort()
print(list) 
listab.sort() 
print(listab) 
lista6=sorted(listab)
print(lista6)
lista6=sorted(list)
print(lista6) 
list.reverse()
print(list)
lista6=list.copy() 
print(lista6) 