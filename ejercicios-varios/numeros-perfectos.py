#Permite buscar números perfectos

number = int(input("Write a number: "))

def add_list(number_list):
    sum = 0
    summed_number_list = []
    for each_number in number_list:
        sum += each_number
        summed_number_list.append(each_number)
    return sum


def find_divisors(number):
    dividers_list=[]
    for each_number in range(1,number):
        if number % each_number == 0:
            dividers_list.append(each_number)
            print(each_number)
    return dividers_list

listing_number = find_divisors(number)
sum_result = add_list(number_list=listing_number)
if number == sum_result:
    print('The number',number, 'is perfect')
else:
    print('The number', number, 'is not perfect')



