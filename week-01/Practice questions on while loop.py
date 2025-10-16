#Print numbers from 1 to 100
i =1 
while i<101:
    print(i)
    i+=1

#Print numbers from 100 to 1
j = 100
while j>=1:
    print(j)
    j=j-1

#Print the multiplication table of number n
k = 1
while k<=10:
    print(5*k)
    k+=1
#Print the element of the following list using a loop
nums = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx<len(nums):
    print(nums[idx])
    idx+=1


g = [1,4,9,16,25,36,49,64,81,100]

d=36

x = 0
while x<len(g):
    if(g[x]== d):
       print("FOUND at idx", x )
    x+=1
