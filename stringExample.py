name = "Deepa Bharti"
cat = "girl"
age = 19
marks = 72.5
# My name is name. I am a girl. I am age years old. I have obtained marks marks in last examination.
#method 1
msg = "My name is %s. I am a %s. I am %d years old. I have obtained %6.2f%% marks in last examination." %(name,cat,age,marks)
print(msg)
#method 2.1
msg = "My name is {}. I am a {}. I am {} years old. I have obtained {}% marks in last examination."
msg = msg.format(name,age,cat,marks)
print(msg)
#method 2.2
msg = "My name is {sname}. I am a {scat}. I am {sage} years old. I have obtained {smarks}% marks in last examination."
mag = msg.format(sname = name.upper(), scat = cat, sage = age, smarks = marks)
print(msg)
#method 3 f-string
msg = f"My name is {name}. I am a {cat}. I am {age} years old. I have obtained {marks}% in last examination."
print(msg)