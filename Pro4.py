## Banking Program
def show_Balance():
    print("--------------")
    print(f"Your Balance : ${balance:.2f}")
    print("--------------")
    

def Deposit():
    amount = float(input("Enter the amount to be deposited : "))
    
    if amount < 0:
        print("That's a invalid amount!")
        return 0
    else:
        return amount 
            

def Withdrawl():
    withdraw = float(input("Enter the amount to be withdrawn : "))
    if withdraw > balance :
        print("Insufficient Balance!")
    elif withdraw < 0:
        print("That's a invalid amount!")
        return 0
    else:
        return withdraw

balance =0
is_running = True             
            
while is_running:
    print("---Bank Program---") 
    print("1.Show_Balance")
    print("2.Deposit")     
    print("3.Withdrawl")   
    print("4.Exit")
    
    choice = input("Enter the choice (1-4):")
    
    if choice =="1":
        show_Balance()
    elif choice == "2":
        balance += Deposit()
    elif choice =="3":
        balance -= Withdrawl() 
    elif choice =="4":
        is_running = False 
    else:
        print("That is not a valid choice!")              
            
print("THANK YOU!")             
             
