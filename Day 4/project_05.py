pin = int(input("Enter ATM Pin: "))



balance = 50000

if pin == 1234:
    print("Login Successful")
    # print("Available Balance =", balance)  
    amount = float(input("Enter withdrawal amount: "))
    if amount <= balance:
        print("Transaction Successful")
        balance = balance - amount
        print(f"Remaining Balanc = {balance}" )
    else:
        print("Insufficient Balance")
  

else:
    print("Incorrect PIN") 