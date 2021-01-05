import os
# posix, nt, os2, ce, java and riscos
print(os.name)
print(os.getcwd())
print(os.path.exists("Raju"))
os.mkdir("Raju")
print(os.path.exists("Raju"))
print("is file-",os.path.isfile("Raju"))
print("is dir-",os.path.isdir("Raju"))
os.chdir("Raju")
print(os.getcwd())
os.chdir("C:\\Users\\DEEPA BHARTI\\PycharmProjects\\PythonProgramms")
print(os.getcwd())
os.rmdir("C:\\Users\\DEEPA BHARTI\\PycharmProjects\\PythonProgramms\\Raju")
print(os.listdir())
print(os.listdir("c:\\"))

