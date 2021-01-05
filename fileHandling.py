# open file
# open(fileName,Mode)
f= open("ganesha.txt","wt")
f.write("Jai sri ganesh\nJai Sri Ram\n Jai Hanuman")
f.close()
f = open("Biodata.txt", "at")
Bio = input("Enter Your biodata.:")
str = ""
while "~" not in str:
    str = input()
    if "~" in str:
        Bio = Bio + "\n" + str[:str.find("~")]
    else:
        Bio = Bio + "\n" + str
f.write(Bio)
f.write("\n")
f.close()