#python program to write 25 questions and its answer and show 5 question when user says.
import random
ques = ("1) which among the following is not an operating system?", "2) 1 Terabyte=", "3)If you need to copy the contents of MS Word, which command will you give?", "4) How many keywords in C?", "5) How many data types in C?", "6) A computer keyboard has ........functions(F) keys.", "7) In a computer binary system, there are ...... choices.", "8) Address of a website is known as..", "9) which of the following method of class String is used to obtain length of String object in java","10) The standard C++ comment","11) Which of the following function that must contain in all C++ programs?","12) Which keyword is used by method to refer to the object that invoked it?","13) Which of the following acces specifiet can be used for a class so that its members can be accessed by a different class in the different package?","14) Which one of the following is not a correct variable type in C++ programs?","15) In Java, a class member declared protected becomes member of subclass of which type?","16) In Java, which function is used to perform some action when the object is to be destroyed?","17) All computers execute","18) Which of the following is the most powwrful computers?","19) Which is considered a direct entry input device?","20) The ability of an operating system to control the activities of multiple programs at the same time?","21)Which device in a computer can understand differences between data & programs?","22) PAN stands for?","23)Java is an example of:","24)Primary memory stores","25) Which of the following is the largest unit?")
opt = (("a.UNIX","b.LINUX","c.OS X","d.PITEX"), ("a.1,024 Gb","b.1,000 Gb","c.1,200 Gb","d.1,275 Gb"),("a.Ctrl + X","b.Ctrl + C","c.Ctrl + V","d.Ctrl + Z"),("a.24","b.30","c.32","d.43"),("a.4","b.6","c.2","d.8"),("a.12","b.13","c.14","d.15"),("a.5","b.3","c.2","d.6"),("a.Uniform Resources Locator","b.Website Resources Locator","c.Wireles Resource Locator","d.Electronic address"),("a.lenght()","b.Sizeof()","c.lenghtof()","d.limitof()"),("a./","b.//","c./* and */","d.#"),("a.main()","b.system()","c.start","d.end()"),("a.this","b.catch","c.abstract","d.import"),("a.Private","b.Protected","c.Public","d.None of these"),("a.float","b.int","c.real","d.double"),("a.privare member","b.public member","c.protected member","d.static member"),("a.delete()","b.main()","c.finalize()","d.destroyed()"),("a.BASIC programs","b.C programs","c.Machine language program","d.FORTRAN programs"),("a.Mainframe Computers","b.Mini Computers","c.Micro Computers","d.Super Computers"),("a.Optical Scanner","b.Mouse and digitizer","c.Both of these","d.None of these"),("a.Streamlining","b.Multiuser","c.Multitasking","d.Simulcasting"),("a.Input device","b.Output device","c.Memory","d.Microprocessor"),("a.Private area network","b.Personal aea network","c.Personal assistant network","d.Private assistant network"),("a.Operating System","b.Programming Language","c.Compiler","d.Machine Language"),("a.Data alone","b.Programs alone","c.Results alone","d.Al of these"),("a.data","b.field","c.record","d.database"))
ans = ("d","a","b","c","a","b","c","a","a","b","a","a","c","c","a","d","c","d","c","c","d","b","d","d")
givenAns = 0
rn = set()
while len(rn)<5:
    rn.add(random.randint(0, 24))
rn = tuple(rn)
i = 0
correct = 0
while i < 5:
   print(ques[rn[i]])
   print("1. ", opt[rn[i]][0])
   print("2. ", opt[rn[i]][1])
   print("3. ", opt[rn[i]][2])
   print("4. ", opt[rn[i]][3])
   givenAns = int(input("Answer(1-4): "))
   print(givenAns)
   print(ans[rn[i]])
   if givenAns==ans[rn[i]]:
       print("Correct Answer.")
       print("Answer: Option ",ans[rn[i]])
       correct = correct+1
   else:
       print("InCorrect Answer.")
       print("Answer: Option ", ans[rn[i]])
   i = i+1
print("Result: ", correct, "/5")
