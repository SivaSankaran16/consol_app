
class cust:
    def __init__(self,cust_id,cur_amt=0,cur_pin=0000,bank="IOB") -> None:
        self.customerid=cust_id
        self.cur_pin=cur_pin
        self.cur_amt=cur_amt
        self.bank=bank

    def verify(self,d):
        if self.customerid in d and self.cur_pin==d[self.customerid][0]:
            return True
        else:
            print("enter the valid info")
            return False

    
    def widthdraw(self,d):
        width_amt=int(input("Enter the width draw amount  :"))
        try:
            self.cur_amt=d[self.customerid][1]
        except:
            d[self.customerid].append(self.cur_amt)
        if width_amt>self.cur_amt:
            print( "Insufficient Balance!!!")
        else:
            print("Please collect your cash")
            self.cur_amt=self.cur_amt-width_amt
            try:
                d[self.customerid][1]=self.cur_amt
            except:
                d[self.customerid].append(self.cur_amt)

            print(f"Your Balance {self.cur_amt}")


    def deposit(self,d):
        depo_amt=int(input("Enter the deposit amount  :"))
        try:
            self.cur_amt=d[self.customerid][1]
        except:
            d[self.customerid].append(self.cur_amt)
        self.cur_amt=self.cur_amt+depo_amt

        print("Your amonunt successfully Deposited!!!!")
        try:
                d[self.customerid][1]=self.cur_amt
                # print(d[self.customerid])
        except:
                d[self.customerid].append(self.cur_amt)
        # print(d[self.customerid])
        print( f"Your Balance {self.cur_amt}")


    def balance_check(self,d):
        try:
                print( f"Your Balance {d[self.customerid][1]}")
        except:
                d[self.customerid].append(self.cur_amt)
                print( f"Your Balance {self.cur_amt}")
        


    def pin_change(self,id,d):
        pin=int(input("Enter Your Pin  :"))
        if pin==self.cur_pin:
            new_pin=int(input("Enter Your New Pin"))
            self.cur_pin=new_pin
            d[id][0]=new_pin
            print("Succesfull pin change!!!")
        else:
            print("Enter the correct pin")


    def money_transfer(self,d):
        trnf_id=int(input("Enter the Trnf_id  :"))
        tranf_amt=int(input("enter the amount  :"))
        try:
            self.cur_amt=d[self.customerid][1]
        except:
            d[self.customerid].append(self.cur_amt)
        if tranf_amt>self.cur_amt:
            print("insufficient balance")
        else:
            self.cur_amt=self.cur_amt-tranf_amt
            print(f"Amount of {tranf_amt} transfered to {trnf_id}")
            print("Amount Transfered successfully!!!")
            print( f"Your Balance {self.cur_amt}")


class admin:
    def __init__(self,ad_id=0000,ad_pin=000) -> None:
        self.admin_id=ad_id
        self.admin_pin=ad_pin
        self.d={}
    def admin_verify(self):
        if self.admin_id==1 and self.admin_pin==1:
            return True
        else:
            return False
    def add_customer(self):
        id=int(input("Enter the customer account id  :"))
        pin=int(input("Enter the customer account pin  :"))
        bank=input("Enter the bank  :")
        print("Customer has been added succesfully!!!")
        
        
        self.d[id]=[pin]
        self.d[id].append(0)
        self.d[id].append(bank)
        # print(self.d)
    def print_cust(self):
        return self.d
    def view_customer(self,d):
        c=1
        for i in d:
            print(f" ----Customer {c} -----")
            print(f"customer_id= {i}\ncustomer_pin= {d[i][0]}\nbank= {d[i][2]}\ncustomer_balance= {d[i][1]}")
            print()
            c+=1
    def view_bank(self,d):
        val=list(d.values())
        print("_________IOB_________")
        tc=0
        ta=0
        for i in range(len(val)):
            if val[i][2].lower() =="iob":
                tc+=1
                ta+=val[i][1]
        print(f"TOTAL NUMBER OF CUSTOMER={tc}")
        print(f"TOTAL AMOUNT OF MONEY WITH CUSTOMER={ta}")


