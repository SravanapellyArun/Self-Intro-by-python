name = "Arun"
DoB = " 27-Aug-2005 "
Qualification = "B-Tech"
age = 21
height = 163.6
weight = 68.6
personal_status = "Single"
skills = ["Python","MS office","Music"]
Hobbies = ["Music","Readingbooks","WatchingMoives"]
Education = ("B-Tech","CSM","2026","Inter","MPC","2022","SSC","English","2020")
language = {"Telugu","English"}
language1 = tuple(language)
Personal_Info = {"Name":"Arun","Father":"Sammaiah","Mother":"Swarupa","Vill":"Karimnagar","Mobile_no":9014078221}


print(f"My name is {name} My date of birth is {DoB}, and my age is {age} years. I have completed my {Education[0]} in {Education[1]}  in {Education[2]}. I have completed my {Education[3]} in {Education[4]}  in {Education[5]} and I have completed my {Education[6]} in {Education[7]}  in {Education[8]}. My height is {height} cm, and my weight is {weight} kg. My personal status is {personal_status}. My skills are {skills[0]},{skills[1]},{skills[2]} and hobbies  are {Hobbies[0]},{Hobbies[1]},{Hobbies[2]}. The languages I known is {language1[0]},{language1[0]} . My father's name is {Personal_Info["Father"]}, and my mother's name is {Personal_Info["Mother"]}. I belong to {Personal_Info['Vill']}, and my mobile number is {Personal_Info["Mobile_no"]}")

#BUILD-IN Functions and Methods

#String()

#name = "Arunn"
#print("name:",name)
#print("Type:",type(name))
#print("uppercase:",name.upper())
#print("lowercase:",name.lower())
#print("length:",len(name))
#print("count(n):",name.count("n"))
#print("index(r):",name.index("r"))
#print("Replace(n-v):",name.replace("n","v"))
#print("Strip:",name.strip())


#Integer() 

#age = 21
#print("Age:",age)
#print("Type:",type(age))
#print("Age+1:",age+1)
#print(str(age))
#print(float(age))

#Float()

#height = 163.5
#print("Height:",height)
#print("type:",type(height))
#print("Float-int:",int(height))

#Boolean()

#is_student = True
#is_teacher = False
#print("Student:",is_student)
#print("Teacher:",is_teacher)
#print("Type:",type(is_student))

#List[]

#skills = ["Python","MS office","MS office"]
#Hobbies = ["Music","Readingbooks","WatchingMoives"]
#print(skills)
#print(type(skills))
#print(len(skills))
#print(skills.index("Music"))
#print(skills.append("MYASQL"))
#print(skills)
#print(skills.insert(0,999))
#print(skills)
#print(skills.pop(1))
#print(skills)
#print(skills.count("MS office"))
#skills = ["Python","MS office","MS office"]

#Tuple()

#Education = ("B-Tech","CSM","2026","Inter","MPC","2022","SSC","English","2020")
#print(Education)
#print(type(Education))
#print(set(Education))
#print(list(Education))

#Set()

#language = {"Telugu","English"}
#print(type(language))
#print(language.add("Malyalam"))
#print(language)
#print(len(language))
#print(language.update("haii"))
#print(language)
#print(language.remove("i"))
#print(language)

#Dictionary{}

#Personal_Info = {"Name":"Arun","Father":"Sammaiah","Mother":"Swarupa","Vill":"Karimnagar","Mobile_no":9014078221}
#print(Personal_Info)
#print(type(Personal_Info))
#print(Personal_Info.keys())
#print(Personal_Info.values())
#print(Personal_Info.items())
#print(len(Personal_Info))
#Personal_Info["State"] = "Telangana"
#print(Personal_Info)
#print(Personal_Info["Mobile_no"])
#Personal_Info["Vill"] = "Hyderabad"
#print(Personal_Info)
#print(Personal_Info.pop("Name"))
#print(Personal_Info)
#print(str(Personal_Info))



#Finall output along with Each variable data type

#print(name)
#print(type(name))
#print(DoB)
#print(type(DoB))
#print(Qualification)
#print(type(Qualification))
#print(age)
#print(type(age))
#print(height)
#print(type(height))
#print(weight)
#print(type(weight))
#print(personal_status)
#print(type(personal_status))
#print(skills_Hobbies)
#print(type(skills_Hobbies))
#print(Education)
#print(type(Education))
#print(language)
#print(type(language))
#print(Personal_Info)
#print(type(Personal_Info))"""


#OUTPUT

#My name is Arun My date of birth is  27-Aug-2005 , and my age is 21 years. I have completed my B-Tech in CSM  in 2026. I have completed my Inter in MPC  in 2022 and I have completed my SSC in English  in 2020. My height is 163.6 cm, and my weight is 68.6 kg. My personal status is Single. My skills are Python,MS office,Music and hobbies  are Music,Readingbooks,WatchingMoives. The languages I known is Telugu,English . My father's name is Sammaiah, and my mother's name is Swarupa. I belong to Karimnagar, and my mobile number is 9014078221
