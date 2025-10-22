def input_series():

    while True:
        series = []

        input_user = input("""
Welcome please enter your number 
atntion:
        # You must enter at least 3 numbers.
        # All numbers must be positive (> 0).
        # Separate the numbers using spaces.
        :
        """)

        user_list = input_user.split(" ")

        try:
           for n in user_list:
               n = float(n)
               series.append(n)
        except:
            print("error try again without word")
            continue

        if min(series) < 0:
            print("error try again only postive number")
            continue

        if len(series) < 3:
            print("error try again and enter minimum 3 words")
            continue

        break

    return series
def menu():
    series = input_series()

    while True:

        menu = input("""
    Series Analyzer - Menu
1. Input a new series
2. Display the series (original order)
3. Display the series (reversed order)
4. Display the series (sorted low→high)
5. Display the Max value
6. Display the Min value
7. Display the Average value
8. Display the Number of elements
9. Display the Sum of the series
0. Exit
        """)
        match menu:
            case "1":
                series = input_series()
                continue
            case "2":
                print(series)
                continue
            case "3":
                print(series[::-1])
                continue
            case "4":
                print(sorted(series))
                continue
            case "5":
                print(max(series))
                continue
            case "6":
                print(min(series))
                continue
            case "7":
                print(sum(series) / len(series))
                continue
            case "8":
                print(len(series))
                continue
            case "9":
                print(sum(series))
                continue
            case "0":
                print("Goodbye")
                break

        print("Error please pike a number")














