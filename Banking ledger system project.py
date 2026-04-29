import pickle
import os

#-----------------------------
# ADD CUSTOMER
#------------------------------
def addCustomer():
    file = open('customers.bin','ab')
    cid = input("\n\t Enter Customer ID : ")
    cname = input("\t Enter Customer Name : ")
    cadd = input("\t Enter Customer Address : ")
    cmob = input("\t Enter Customer Mobile : ")
    accno = input("\t Enter Customer Account no. : ")
    balance = float(input("\t Enter Initial Balance : "))

    pickle.dump(cid,file)
    pickle.dump(cname,file)
    pickle.dump(cadd,file)
    pickle.dump(cmob,file)
    pickle.dump(accno,file)
    pickle.dump(balance,file)

    print("\n\t Customer Added Successfully!")
    file.close()
    input("\t Press Enter To Continue...")


# ----------------------------------
# VIEW ALL CUSTOMERS
# ---------------------------------
def viewAllCustomer():
    file = open('customers.bin','rb')
    try:
        while True:
            print("\n\t Customer ID :",pickle.load(file))
            print("\t Customer Name :",pickle.load(file))
            print("\t Customer Address :",pickle.load(file))
            print("\t Customer Mobile :",pickle.load(file))
            print("\t Account number :",pickle.load(file))
            print("\t Balance :",pickle.load(file))
            print("\t ----------------------------")
    except:
        print("\n\t End of customer list.")
    file.close()
    input("\t Press Enter To Continue...")


# -------------------------------
# DELETE CUSTOMER
# -------------------------------
def deleteCustomer():
    file1 = open('customers.bin','rb')
    file2 = open('tempe.bin','ab')
    cid_del = input("\t Enter Customer ID To Delete : ")
    flag = 0
    try:
        while True:
            cid = pickle.load(file1)
            cname = pickle.load(file1)
            cadd = pickle.load(file1)
            cmob = pickle.load(file1)
            acc = pickle.load(file1)
            bal = float(pickle.load(file1))

            if cid == cid_del:
                print("\n\t Customer Deleted Successfully!")
                flag = 1
            else:
                pickle.dump(cid,file2)
                pickle.dump(cname,file2)
                pickle.dump(cadd,file2)
                pickle.dump(cmob,file2)
                pickle.dump(acc,file2)
                pickle.dump(bal,file2)

              
    except:
        if flag == 0:
            print("\n\t Customer Not Found!")
    file1.close()
    file2.close()

    os.remove('customers.bin')
    os.rename('tempe.bin','customers.bin')
    input("\t Press Enter To Continue...")
    
# -------------------------------
# RECORD TRANSACTION
# -------------------------------
def recordTransaction(cid, accno, ttype, amount):
    file = open('transactions.bin','ab')
    pickle.dump(cid,file)
    pickle.dump(accno,file)
    pickle.dump(ttype,file)
    pickle.dump(amount,file)
    file.close()


# --------------------------------------
# VIEW ALL TRANSACTIONS
# --------------------------------------
def viewAllTransactions():
    try:
        file = open('transactions.bin', 'rb')
        n = 1001
        while True:
            cid = pickle.load(file)
            accno = pickle.load(file)
            ttype = pickle.load(file)
            amount = pickle.load(file)

            print("\n\t Transaction No.", n)
            print("\t CID:", cid)
            print("\t Account No:", accno)
            print("\t Type:", ttype)
            print("\t Amount:", amount)
            print("\t ---------------------------")
            n += 1
    except:
        print("\n\t End of transactions.")
    file.close()
    input("\t Press Enter To Continue...")


# ------------------------------------------
# VIEW TRANSACTIONS BY CID
# ------------------------------------------
def viewTransactionsByCID():
    cid_search = input("\n\t Enter Customer ID : ")
    flag = 0
    try:
        file = open('transactions.bin', 'rb')
        n = 1001   
        while True:
            cid = pickle.load(file)
            accno = pickle.load(file)
            ttype = pickle.load(file)
            amount = pickle.load(file)

            if cid == cid_search:
                print("\n\t Transaction No.", n)
                print("\t CID:", cid)
                print("\t Account No:", accno)
                print("\t Type:", ttype)
                print("\t Amount:", amount)
                print("\t ---------------------------")
                flag = 1
            n += 1
    except:
        if flag == 1:
            print("\n\t End of transactions for CID", cid_search)
        else:
            print("\n\t No transactions found for CID:", cid_search)
    file.close()
    input("\t Press Enter To Continue...")


# ------------------------------------------------
# DEPOSIT MONEY (by Customer ID)
# ------------------------------------------------
def depositMoney():
    file1 = open('customers.bin','rb')
    file2 = open('tempe.bin','ab')
    cid_input = input("\t Enter Customer ID To Deposit : ")
    amount = float(input("\t Enter Amount : "))
    flag = 0
    try:
        while True:
            cid = pickle.load(file1)
            cname = pickle.load(file1)
            cadd = pickle.load(file1)
            cmob = pickle.load(file1)
            acc = pickle.load(file1)
            bal = float(pickle.load(file1))

            if cid == cid_input:
                bal += amount
                recordTransaction(cid, acc, "Deposit", amount)
                print("\n\t Money Deposited Successfully!")
                flag = 1

            pickle.dump(cid,file2)
            pickle.dump(cname,file2)
            pickle.dump(cadd,file2)
            pickle.dump(cmob,file2)
            pickle.dump(acc,file2)
            pickle.dump(bal,file2)
    except:
        if flag == 0:
            print("\n\t Customer ID Not Found!")
    file1.close()
    file2.close()
    os.remove('customers.bin')
    os.rename('tempe.bin','customers.bin')
    input("\t Press Enter To Continue...")


# ----------------------------------------------------
# WITHDRAW MONEY (by Customer ID)
# ----------------------------------------------------
def withdrawMoney():
    file1 = open('customers.bin','rb')
    file2 = open('tempe.bin','ab')
    cid_input = input("\t Enter Customer ID To Withdraw : ")
    amount = float(input("\t Enter Amount : "))
    flag = 0
    try:
        while True:
            cid = pickle.load(file1)
            cname = pickle.load(file1)
            cadd = pickle.load(file1)
            cmob = pickle.load(file1)
            acc = pickle.load(file1)
            bal = float(pickle.load(file1))

            if cid == cid_input:
                if bal >= amount:
                    bal -= amount
                    recordTransaction(cid, acc, "Withdraw", amount)
                    print("\n\t Withdrawal Successful!")
                else:
                    print("\n\t Insufficient Balance!")
                flag = 1

            pickle.dump(cid,file2)
            pickle.dump(cname,file2)
            pickle.dump(cadd,file2)
            pickle.dump(cmob,file2)
            pickle.dump(acc,file2)
            pickle.dump(bal,file2)
    except:
        if flag == 0:
            print("\n\t Customer ID Not Found!")
    file1.close()
    file2.close()
    os.remove('customers.bin')
    os.rename('tempe.bin','customers.bin')
    input("\t Press Enter To Continue...")




# -------------------------------
# DASHBOARD
# -------------------------------
while True:
    print("\n\t ************************************************")
    print("\t         BANKING LEDGER SYSTEM          ")
    print("\t ************************************************")
    print('''
            1- Add Customer
            2- View All Customers
            3- Delete Customer
            4- Deposit Money
            5- Withdraw Money
            6- View All Transactions
            7- View Transactions By CID
            0- Exit
    ''')
    ch = int(input("\t Enter Your Choice : "))
    if ch==0:
        print("\n\t\tBye-Bye Admin!")
        break
    elif ch==1:
        addCustomer()
    elif ch==2:
        viewAllCustomer()
    elif ch==3:
        deleteCustomer()
    elif ch==4:
        depositMoney()
    elif ch==5:
        withdrawMoney()
    elif ch==6:
        viewAllTransactions()
    elif ch==7:
        viewTransactionsByCID()
    else:
        input("\n\t Wrong Entered\n\t Try Again!")





