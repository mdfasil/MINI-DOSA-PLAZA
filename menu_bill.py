#Funtion 1
#First type the print statement
def dosacorner():
    print("$#"*18,'"~WELCOME TO MINIDOSAPLAZA~"',"#$"*18)
    print("~~Select your favorite and yummy dosa")
    print("1--> SADA DOSA @ RS.50")
    print("2--> CHEESA DOSA @ RS.100")
    print("3--> MASAL DOSA @ RS.120")
    print("4--> PASTA DOSA @ RS.140")
    print(" ")

    chno = []
    no_of_q = []
    subtot1 = []
    subtot2 = 0

    ch = int(input("CHOOSE SOME ITEMS = ")) #type some single integer
    chno.extend([ch])
    q = int(input("Enter The Quantity - "))
    no_of_q.extend([q])

    

    for i in range(1,6):
        ans = input("Order More yes or no : ")
        if ans == "y":
            ch = int(input("CHOOSE SOME ITEMS = "))
            chno.extend([ch])
            q = int(input("Enter The Quantity - "))
            no_of_q.extend([q])
        else:
            break
    print(" ")

    #Type a Receipt statement to print output
    print("*"*18,"RECEIPT","*"*18)

    for i in chno:
        if i == 1:
            price = 50
            subtot0 = no_of_q[0] * price
            str1 = "Sada Dosa"
            print(f'{str1} : {no_of_q[0]} - {subtot0}')
            subtot1.extend([subtot0])
         
        elif i == 2:
            price = 100
            subtot0 = no_of_q[1] * price
            subtot1.extend([subtot0])
            str1 = "Cheese Dosa"
            print(f'{str1} : {no_of_q[1]} - {subtot0}')

        elif i == 3:
            price = 120
            subtot0 = no_of_q[2] * price
            subtot1.extend([subtot0])
            str1 = "Masal Dosa"
            print(f'{str1} : {no_of_q[2]} - {subtot0}')

        elif i == 4:
            price = 140
            subtot0 = no_of_q[3] * price
            subtot1.extend([subtot0])
            str1 = "Pasta Dosa"
            print(f'{str1} : {no_of_q[3]} - {subtot0}')

    for i in subtot1:
        subtot2 += i    
    print("SubTotal : %.2f" % subtot2)
    sgst = float(subtot2 * 0.02)
    cgst = float(subtot2 * 0.02)
    print("SGST  : %.2f" % sgst)
    print("CGST  : %.2f" % cgst)
    gst = sgst + cgst
    tot = subtot2 + gst
    print("Total : %.2f " % tot)
    print("")

    #Funtion 2 
    #different mode to pay a payment

    def cash():
        print("*"*10,"PAYMENT","*"*10)
        print("~Select Your Payment Mode")
        print("1--> Google Pay")
        print("2--> PhonePee")
        print("3--> Ready Cash")
        print(" ")

        p = int(input("Choose Any One Mode : "))
        if p == 1:
            if tot >= 500:
                cb = int(tot * 0.05)
                print(f'CASHBACK : {cb}')
                total = tot - cb
                print("Balance Amount : %.2f" %total)
                print("Payment Successfully")
            else:
                print("Payment Received")
        elif p == 2:
            if tot >= 400:
                cb = int(tot * 0.08)
                print(f'CASHBACK : {cb}')
                total = tot - cb
                print("Balance Amount : %.2f" %total)
                print("Payment Successfully")
            else:
                print("Payment Received")
        else: 
            if tot >= 1000:
                dis = int(tot * 7) / 100
                print(f'Discount : {dis}')
                total = tot - dis
                print("Balance Amount : %.2f" % total)
                print("Cash Received")
    print(" ")
    cash()
    print(" ")

    #funtion 3
    #Feedbacks statement to print
    def feedback():
        print("*"*18,"GIVE YOUR VALUABLE FEEDBACK","*"*18)
        print("^_Select your Opinion")
        print("1--> Excellent Service")
        print("2--> Good Service")
        print("3--> Can Do Better")
        print("4--> Bad Service")
        print(" ")

        s = int(input("Enter Your Opinion : "))
        if s == 1:
            print("Excellent Service")
        elif s == 2:
            print("Goood Service")
        elif s == 3:
            print("Can Do Better")
        else:
            print("Bad Service")
            print("sorrrryyyyy, Surely Improve My Service")

        print("Thanks for your Feedback")
        print(" ")
        print("~"*18,"Thank You Visit Again and Again","~"*18)
    feedback()
dosacorner()