def getMyName(name=' deepak'):
    print(f"hello{name}, How are you.")
    print("hello"+name+",How are you.")

getMyName(' Yatin')

#default argument

getMyName()

def getMyStudent(*std):
    print("Hello "+std[2])

getMyStudent("RAVI","RAHUL","RITIK")


def addMyNumber(x,y):

    return x+y

result =addMyNumber(45,56)

print(f"the number is {result}")
