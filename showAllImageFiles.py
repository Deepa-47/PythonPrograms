import os

def show(path):
	if os.path.isfile(path):
		print(path)
	else:
		os.chdir(path)
		for i in os.listdir():
			show(i)
		print("============================")
		os.chdir("..")


os.chdir("D://.jpg")
os.getcwd()
for i in os.listdir():
	show(i)