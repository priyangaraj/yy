def reverse(n,r):
	if(num>=1):
		r=r*10
		r=r+(n%10)
		reverse(int(n/10),r)
	elif num<1 :
		print(r)
		return 0
a=int(input("Number"))
rev(a,0)
