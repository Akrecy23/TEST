
def get_user_input():
    numbers = input()
    user_list = numbers.split(",")
    #for i in user_list:
        #new_list = [float(i)] //cannot work cause causes list to only contain last element
    new_list = [float(i) for i in user_list]
    return new_list

def calc_average(common_list):
    #print(common_list)
    average = sum(common_list)/len(common_list)
    print()
    print("The average value is " + str(average))
    print()

def main():
    common_list = get_user_input()
    calc_average(common_list)

if __name__=='__main__':
    main()