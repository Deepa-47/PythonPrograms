s= "Manohar singh"

for i in range(len(s)):
	for j in s[i::-1]:
		print(j, end=" ")
	print()
