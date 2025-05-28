number=int(input("Enter the number tht how many want to print primes under 100 : "))
l=[]
for num in range(2, 101):  
    count = 0
    for i in range(1, num + 1):  
        if num % i == 0:
            count = count + 1  
    if count == 2:  
        l.append(num)
        if number==len(l):
            break
print(l)