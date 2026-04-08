
num=5

str_test= "h"
int_num= 100
for i in range(5):
    print("ee",i)


if num == 1 or num==5:
    print ('1')
elif num == 5:
	print ('66')
	print ('66')
    
    
i = 1
while i< 10:
    print("ttt",i)
    i+=1
    print(i) 

print(str_test+str(int_num))
print(hex(int_num))
print(ord("a"))
print(hex(ord("a")))


for i in range(2,5):
    print(i)

var = 10
for i in range(2,20):
    if i != var:
        continue
    print(i)

tup = (1,2,3,4,5,6,7)
print("tup:",tup[1:5])

list = [1,2,3,4,5,6,7]

list[0] = 100
print("lis:",list[0:5])