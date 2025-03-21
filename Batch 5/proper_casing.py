while True:
    try:
        name = input("Please enter your full name: ")
        print("your full name will be printed with proper casing")
        fixed_name = (name.title())
        print (fixed_name)
    except RuntimeError:
        print("Something went wrong please restart the program !")
        
    while True:
        loop = input("Type yes or no to loop: ")
        if loop in ["yes"]:
            break
        elif loop in ["no"]:
            exit("Thankyou for using my program !")
        else:
            ("please enter yes or no only !") 