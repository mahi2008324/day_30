def  except_primes():
    for num in range(2, 101):  
        count = 0
        for i in range(1, num + 1):  
            if num % i == 0:
                count = count + 1  
        if count == 2:  
          continue
        if count>2:
            print(num,end=" ")
except_primes()