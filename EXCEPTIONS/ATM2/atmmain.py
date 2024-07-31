import atmmenu, atmexceptions,atmoperations
while(True):
    atmmenu.menu()
    try:
        ch=int(input("Enter Your Choice: "))
    except ValueError:
        print("Dont try to select alnums, strs & special symbols as menu option")
    match(ch):
        case 1:
            try:
                atmoperations.deposit()
            except ValueError:
                print("Dont try to deposit alnums, strs & special symbols")
            except atmexceptions.DepositError:
                print("Dont try deposit zero/-ve values")
        case 2:
            try:
                atmoperations.withdraw()
            except ValueError:
                print("Dont try to withdraw alnums, strs & special symbols")
            except atmexceptions.WithDrawError:
                print("Dont try withdraw zero/-ve values")
            except atmexceptions.InsufficientFundError:
                print("Your account does not have sufficient funds")
        case 3:
            atmoperations.balenq()
        case 4:
            print("Thanks for using this program")
            atmoperations.exit()
            break
        case _:
            print("Your selection of operations is wrong--Try again")
