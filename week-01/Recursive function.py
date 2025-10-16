#Recursive function
#prints n to 1 from backwords
def show(n):
    if (n == -1): #base case
        return
    print(n)
    show(n-1)
show(5)
    