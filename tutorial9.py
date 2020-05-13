fact = 1 
n = int(input("Dame un numero: "))
# for(i=1;i<=n;i++)
for i in range(1,n+1):
	fact = fact * i
print(fact)
input()