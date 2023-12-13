'''
Description: wtite program to genearate a list of the number of random numbers

'''


import random

def unique_random_ints(how_many, max_num):

    num_list = []
    global retries
    retries = 0
    
    while len(num_list) < how_many:
        num = random.randint(0, max_num)
        if num not in num_list:
            num_list.append(num)
        else:
            retries += 1

    return num_list

if __name__ == "__main__":
    
    seed = int(input())
    how_many = int(input())
    max_num = int(input())

    random.seed(seed)

    num_list = unique_random_ints(how_many, max_num)

    
    for i in num_list:
        print(i, end=' ')
    print(f' retries={retries}')
        

   
    
