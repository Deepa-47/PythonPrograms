def anish():
    print("My name is Anish Anand")


# functin can be assigned to variable
anand = anish


# Function can be defined within function
def student():
    def boy():
        print("Hi!. I am Boy")

    def girl():
        print("I am Girl")

    boy()
    girl()


# A function can return function
def person(personType):
    def male(age):
        if (age >= 21):
            print(f"I am male and my age is {age} years so I am eligible for marriage")
        else:
            print(F"I am male. I am {age} years old. {21 - age} year remaining for eligible for marriage")

    def female(age):
        if (age >= 18):
            print(f"I am female and my age is {age} years so I am eligible for marriage")
        else:
            print(F"I am female. I am {age} years old. {18 - age} year remaining for eligible for marriage")

    if (personType == 1):
        return male
    else:
        return female


# A function can be passes as argument
def slower(str):
    return str.lower()


def supper(str):
    return str.upper()


def sreverse(str):
    return str[::-1]


def printList(list, pfunction):
    print("Your list items are:")
    for i in list:
        print(pfunction(i))
    print("complete")


# Anonymous Function- It is created with lambda keyword. It is of only one expression function.
# This function is also known as lamda function.
# Syntax lambda arglist:exp
# create a function that accept a number and return its twice
def twice(n):
    return n * 2


thrice = lambda n: n * 3

anish()
anand()
student()
piyush = person(1)
piyush(12)
deepa = person(0)
deepa(20)
deepa(17)
sl = ["Raju Kumar", "Brajesh Kumar", "Shubham Vatsa", "Piyusha sinha", "Ankit Kumar", "Gautam Kumar", "Manohar Singh",
      "Deepu ", "Karan Kumar", "Deepa Bharati", "aradhya Singh", "Pooja Kumari"]
printList(sl, slower)
printList(sl, supper)
printList(sl, sreverse)
print(twice(20))
print(thrice(40))


