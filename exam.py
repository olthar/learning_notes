def reverse_evens (shopping):
    print(shopping)
    last_value = shopping[-1]
    if (last_value % 2) == 0:
    	print (shopping[-1:1:-2])
    else:
        print (shopping[-2::-2])

reverse_evens (input("what?   "))