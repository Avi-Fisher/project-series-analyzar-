def input_series():
    series = []

    while True:
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

               if n <= -1:
                   print("error try again only postive number")
                   continue
        except:
            print("error try again without word")
            continue

        if len(series) < 3:
            print("error try again and enter minimum 3 words")
            continue

        break

    return series


















