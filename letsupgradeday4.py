# write a program which has a function to find out a number is prime or not.

def checkprime(n):
  #logic prime numbers can be divisible by 2 , 3 , 5 , 7
  
  if n==0:
    print(f'{n} is neither prime nor not prime')
  elif n==1:
    print(f'{n} is neither prime nor not prime')
  elif n==2:
    print(f'{n} is prime')
  elif n==3:
    print(f'{n} is prime')
  elif n==5:
    print(f'{n} is prime')
  elif n==7:
    print(f'{n} is prime')
  elif n%2==0:
    print(f'{n} is not prime')
  elif n%3==0:
    print(f'{n} is not prime')
  elif n%5==0:
    print(f'{n} is not prime')
  elif n%7==0:
    print(f'{n} is not prime')
  else:
    print(f'{n} is prime')

# taking input from user for checkprime method
x = int(input())
checkprime(x)
