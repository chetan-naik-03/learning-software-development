i = 1
while i<=5:
    print(i)
    if (i==3):
      break  
    i+=1
    


    print("end of loop")

nums = (1,4,9,16,25,36,49,36,81,100)

x=36

idx = 0
while idx<len(nums):
    if(nums[idx]== x):
       print("Found at idx", idx)
       break
    else:
       print("finding ..")
    idx+=1

i=0
while i<=5:
   if(i==3):
      i+=1
      continue
   print(i)
   i+=1

i=1
while i<=10:
   if(i%2 == 0):
      i+=1
      continue
      print(i)
      i+=1