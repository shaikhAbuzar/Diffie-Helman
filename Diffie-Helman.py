from sympy import isprime

q = int(input('Enter the value of q: '))
alpha = int(input('Enter the value of alpha: '))
Xa = int(input('Enter the value of Xa less than {q}: '))
Xb = int(input('Enter the value of Xb less than {q}: '))

if isprime(q):
    print(f'{q} is prime No.')
else:
    print(f'{q} is not a prime no.\n terminating the execution')
    exit(0)

if alpha < q:
    print(f'{alpha} < {q}')
else:
    print(f'{alpha} >= {q}')

alphanmodq = 0
zeroltnltq = 0
for n in range(1, q):
    zeroltnltq += n
    alphanmodq += (alpha ** n) % q
    # print(f'{n} | {alpha ** n} | {alphanmodq}')

if alphanmodq == zeroltnltq: 
    print('No repetions')
else: 
    print('There are repetitions, hence stopping')
    exit(0)

if Xa < q:
    print(f'{Xa} < {q}')
else:
    print(f'{Xa} >= {q}')

if Xb < q:
    print(f'{Xb} < {q}')
else:
    print(f'{Xb} >= {q}')

Ya = (alpha ** Xa) % q
Yb = (alpha ** Xb) % q

Ka = (Yb ** Xa) % q
Kb = (Ya ** Xb) % q

print(f'{Ka} and {Kb}')
