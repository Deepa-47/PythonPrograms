import os, stat
try:
	os.mkdir("Deepa")
	os.chmod("Deepa",stat.S_IREAD|stat.S_IWRITE)
except FileExistsError as e:
	print(e)

f = open("Deepa\\kumar.txt","a+")
d = input("enter data:")
f.write(d)
# move file pointer on begining of file
f.seek(0)
d = f.read()
f.close()
print(d)
