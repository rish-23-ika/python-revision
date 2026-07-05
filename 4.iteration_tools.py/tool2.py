f = open("tool.py")

f.readline()
#readline is better in solving exceptions like when we continue reading the file line by line , one line at time
#at last where lines are over it will return empty string '' and we can handle it in our code

f.__next__()
#whereas , here it just gave error 

for line in f:
    print(line)





