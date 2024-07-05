import statistics

print ("ET0735 (DevOps for AIot) - Lab 2 - Introduction to Python")
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67,32) without spacing")

def get_user_input():
    numbers = input()
    user_list = numbers.split(",")
    #print(user_list)
    new_list = [float(i) for i in user_list]
    return new_list

def calc_average(common_list):
    #print(common_list)
    average = sum(common_list)/len(common_list)
    print()
    print("The average value is " + str(average))
    print()
    return str(average)

    #Below code shows method 2 of finding sum of list
    #total = 0
    #for number in common_list:
        #total += number

def find_min_max(common_list):
    min_max_list = [min(common_list),max(common_list)]
    print("The min value and max value are ")
    print(min_max_list)
    print()
    return min_max_list

def sort_temperature(common_list):
    sort_list = common_list
    sort_list.sort()
    #print(sort_list)
    return sort_list

def calc_median(sorted_list):
    median_value = statistics.median(sorted_list)
    print("The median value is " + str(median_value))
    return str(median_value)

def main():
    display_main_menu()
    common_list = get_user_input()
    average = calc_average(common_list)
    min_max_list = find_min_max(common_list)
    sorted_list = sort_temperature(common_list)
    med_val = calc_median(sorted_list)

if __name__=='__main__':
    main()