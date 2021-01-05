name = "Raju Kumar"
fname = "Vijay Yadav"
gen = "male"
age = 21
om = 67.56
print("My name is ", name, ". My father's name is Sri ", fname, ". I am ", gen, ". I am ",age ," years old.", " I have obtained ", om , "marks in examination" )
# insert into students(name,fname,gen,age,om) values('Raju Kumar','Vijay Yadav','male',21,66.56)
s1 = "insert into students(name,fname,gen,age,om) values('%s','%s','%s',%d,%.2f)"%(name,fname,gen,age,om)
print(s1)
s2= "insert into students(name,fname,gen,age,om) values('{}','{}','{}',{},{})".format(name, fname, gen, age, om)
print(s2)
s3= "insert into students(name,fname,gen,age,om) values('{sn}','{sfn}','{g}',{a},{m})".format(m=om,a=age,sn=name,sfn=fname, g=gen)
print(s3)
s4= f"insert into students(name,fname,gen,age,om) values('{name.upper()}','{fname}','{gen}',{age},{om})"
print("s4=",s4)
d ={"name":"Piyush sinha","fname":"Devraj Kumar sinha","gen":"Male","age":22,"om":89.67}
s5 = "insert into students(name,fname,gen,age,om) values('%s','%s','%s',%d,%.2f)"%(d["name"],d["fname"],d["gen"],d["age"],d["om"])
print(s5)
#d is a dictionary
s6="insert into students(name,fname,gen,age,om) values('{name}','{fname}','{gen}',{age},{om})".format(**d)
print(s6)
d1= ("Brajesh Kumar", "Santosh Kumar", "Male", 21, 56.78)
#d1 is a tuple
s7= "insert into students(name,fname,gen,age,om) values('{}','{}','{}',{},{})".format(*d1)
print("s7=",s7)
tr = '<tr><td>{name}</td><td>{fname}</td><td>{gen}</td><td>{age}</td><td>{om}</td></tr>'.format(**d)
print(tr)

