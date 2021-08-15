num = int(input("enter the number"))
sum =0
abc = num

while abc > 0:
	digit = abc % 10 
	sum += digit**3
	abc//= 10

if sum == num:
	print("it is a amstrong number")
else:
  	print("it is not a amstrong number")

