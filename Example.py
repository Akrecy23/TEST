csv_data = [
    {"Number": 0, "Drink": 30, "Amount": 1},
    {"Number": 1, "Drink": 25, "Amount": 2},
    {"Number": 2, "Drink": 23, "Amount": 3},
    {"Number": 3,  "Drink": 35, "Amount": 4},
    {"Number": 4, "Drink": 32, "Amount": 5},
    {"Number": 5, "Drink": 40, "Amount": 6}
]

def get_amount(drink_number):
    amount_val = ""

    for item in csv_data:
        #code
        if int(item["Number"]) == int(drink_number):
            amount_val = item["Amount"]
            print(amount_val)

def main():
    keypad_num = 3
    get_amount(keypad_num)

if __name__=='__main__':
    main()
