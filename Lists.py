def remove_from_list():
    try: 
        my_things.remove(1)
    except ValueError:
        pass
        

my_things = [1]
my_things += [2,3]
my_things.append("this")
#del my_things[-1]
my_things.extend([8,7,1])
my_things.extend("abc")
my_things.insert(0, my_things.pop(3))

#Removes only takes out first time this occurrs
#my_things.remove (1)
remove_from_list


print("{}. {}".format("Here you go",my_things))
print(list("home"))


thing = my_things.pop(0)
print(thing)
print(my_things)


