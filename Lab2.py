def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    y = display_main_menu()
    num_list = get_user_input(y)
    calc_average(num_list)
    calc_min_max_temperature(num_list)

def display_main_menu():
    x = input("Enter some numbers separated by commas (e.g. 5, 67, 32): ")
    return x

def get_user_input(y):
    values = y.split(",")
    floats = [float(item) for item in values]
    return floats

def calc_average(z):
    average = sum(z) / len(z)
    average = round(average, 2)
    print(average)

def calc_min_max_temperature(z):
    print(max(z))
    print(min(z))

if __name__ == "__main__":
    main()