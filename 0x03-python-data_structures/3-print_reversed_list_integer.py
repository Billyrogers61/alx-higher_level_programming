#!/src/bin/python3
def print_reversed_list_integer(my_list=[]):
    count = 0
    for num in range(len(my_list)):
        count = count + 1
        print("{:d}".format(my_list[-count]))
