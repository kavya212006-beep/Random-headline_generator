from function import generate_headline



while True:
    try:
     options=int(input("ENTER 1 TO CONTINUE AND 2 TO EXIT:"))

     if options==1:
        print(generate_headline())

     elif options==2:
        break
     else:
        print('INVALID OPTION')
    except ValueError:
       print("enter valid inputs")


