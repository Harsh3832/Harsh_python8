#list is a group of elements with same type or different type
#list is where we can store different type of data

l=[] #blank list
l = [1,2,1.1,2.2,'tops',10,True,'python',1,2,100]

print(l)
print(len(l))
l.append(11) #append will always add single element only and not group of elements and will always add element at last
print(l)
# l.clear() # to clear list
# print(l)
#koi pan function ni pa6al round bracket lagse like ()
''' important functions
l1=l.copy() #l1 ne alag memory allocate thse
print(l1)
l1.append(l2)
print(l1)
print(l)

l2=l #l2 ne alag memory allocate nai thay
l.append(13)
print(l2)
print(l)
'''
a = [100,200,300]
l.extend(a) #only add a list
print(l)
print(l.count(1)) # true = 1 and false = 0 like excel.. this will get counted while calculating count
print(l.index(10)) #10 kaya position par 6 e batavse
l.insert(5,50) #5th position par 50 print thase
print(l)
l.pop() #pop ma kai declare nathi kryu hoy to last element remove thase
print(l)
l.pop(10) #pop ma 10th index par j declarekryu hse e remove thase
print(l)
l.remove(10) #ek j 10 remove thase
print(l)
l.reverse()
print(l)
l.sort() # can only be used for integers

for i in l:
    print(i)

s = 'Tops Technologies'
for i in s:
    print(i,end='*')

#list as stack
l = []
l.append(10)
print(l)
l.append(20)
print(l)
l.append(30)
print(l)
l.append(40)
print(l)
l.append(50)
print(l)
l.pop()
print(l)
l.pop()
print(l)
l.pop()
print(l)
l.pop()
print(l)
