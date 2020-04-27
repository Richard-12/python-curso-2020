#Establece si un número dado es primo o no
def isprime(num):
    if num <1:
        return False
    elif num ==2:
        return True
    else:
        for i in range(2,num):
            if num%i==0:
                return False
        return True


def app():
    num = int(input('write a number \n '))
    result = isprime(num)

    if result is True:
        print('The number is prime!!')
    else:
        print('The number is not prime!!')


app()