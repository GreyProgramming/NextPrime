bool = 1

def nextprime(n):
    p=n+1
    for i in range(2,p):
        if(p%i==0):
            p=p+1
    else:
        bool = 1
        return(p)

n = int(input("What is the first number? "))
p=nextprime(n)
print(p)

while bool == 1:
    o = input('Do you want the next prime? Y/N: \n')[0]
    m=o.upper()
    if m=="Y":
        n = p+1
        p=nextprime(n)
        print(p)
    else:
        print ("Thank you for using primefinder")
        bool = 0