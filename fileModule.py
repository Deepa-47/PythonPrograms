f = open("ganesha.txt","r+")
print("File pointer is at:",f.tell())
f.seek(0,2)
print("File pointer is at:",f.tell())
#data = input("enter data")
#write entered data to file
#f.write(data)
#f.write("\n")
print("Data written to file successfully!")
print("File Content=")

data = f.read()
print(data)
f.close()
