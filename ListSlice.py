def first_4(shopping):
 	return (shopping[0:4])

def first_and_last_4(shopping):
    items = (shopping [0:4]) + (shopping [-4:]) 
    return(items)

def odds (shopping):
    return (shopping[1::2])

def reverse_evens (shopping):
    print (shopping)
    evens = shopping[::2]
    print(list(reversed(evens)))

def sillycase (word):
    first = int((len(word)) / 2)
    print (((word [:first]).lower()) + (word [first:]).upper())  

     

sillycase (input("What?   "))