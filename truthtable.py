print("a b c | r")
print("---------")
for a in range(2):
	for b in range(2):
		for c in range(2):
			y = not((a==1) and (b==1)) and (c==1)
			r = int(y)
			print(a,b,c,"|",r)
