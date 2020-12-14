#made by ender
import random
o=open("seeds.txt","w")
e=int(input("number of seeds:\n>"))
for i in range(e):
	o.write(str(random.randint(-999999999999999,999999999999999))+"\n")
o.close()
print('[+]finished,results are in seeds.txt')