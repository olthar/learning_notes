"""

def packer (name=None, **kwargs):
        print (kwargs)

def unpacker (first_name=None, last_name=None):
    if first_name and last_name:
        print ("hi {} {}".format(first_name, last_name))
    else:
        print("Hi no name!")

#packer (name = "Oliver" , age= 32,)
#unpacker (**{"last_name":"Rayner", "first_name":"Oliver"})

def favorite_food(name=None,food=None):
    if name and food:
        print ( "Hi, I'm {} and I love to eat {}!".format(name,food))
    else:
        print ("No")

#favorite_food (**{"name":"Rayner", "food":"Pizza"})

def favorite_food(dict):
    return "Hi, I'm {name} and I love to eat {food}!".format(**dict)


#looping through dict

def courses (**kwargs):    
    course = kwargs
    for c in course:
        print (c)
        print (course[c])

courses (python= "hard", Django=38, Ruby="Not Tried")

course_minutes = {"Python":212, "Ruby":218, "Java":122}
for key in course_minutes.keys():
    print(key)
for value in course_minutes.values():
    print(value)
for item in course_minutes.items():
    print(item)


def word_count(sentence):
    sentence_l=sentence.lower()
    counts = dict()
    words = sentence_l.split(" ")
    
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    print (counts)
word_count(input("What?   "))


def num_teachers (dict):
    count = 0
    for key in dict.keys():
        count += 1
    print(count)
num_teachers ({'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],'Kenneth Love': ['Python Basics', 'Python Collections']})

def num_course (dict):
    count = 0
    for value in dict.values():
        count += len(value)
    print(count)
num_courses ({'oliverAndrew Chalkley': ['jQuery Basics', 'Node.js Basics'],'Kenneth Love': ['Python Basics', 'Python Collections']})

def courses (dict):
    course = []
    for value in dict.values():
        course += value
    print (course)
            
courses ({'oliverAndrew Chalkley': ['jQuery Basics', 'Node.js Basics'],'Kenneth Love': ['Python Basics', 'Python Collections']})

def most_courses(dict):
    count = 0
    teacher = ()
    for teachers,subjects in dict.items():
        if (len(subjects)) > count :
            count += len(subjects)
            teacher = teachers
        
    print(teacher)


most_courses ({'oliver':['fucking','nothing'],'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics','yep'],'Kenneth Love': ['Python Basics','test','test2','test3', 'Python Collections']})
"""

def stats (dict):
    teachers_list= []
    for teachers,subjects in dict.items():
        teachers_list.append(teachers) 
        teachers_list.append(len(subjects))
    print(teachers_list)

stats ({'oliver':['fucking','nothing'],'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics','yep'],'Kenneth Love': ['Python Basics','test','test2','test3', 'Python Collections']})
