def olli_formula(num):
    calc = str(num)
    while len(calc) > 1:
        print("step 1- ", num)
        dig = num % 10
        num = int(num/10)
        print("step 2- ", num, "+ (", dig, "* 5 )")
        num += (dig * 5)
        print("step 3- ", num)
        calc = str(num)
        print("\n")

    if num == 7:
        return True
    else:
        return False


print(olli_formula(84))
