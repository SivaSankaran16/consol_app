from members import *
d1={}

while True:
    print("\n")
    print("Select the role\n1.Admin\n2.Customer\n3.Exit")
    print()
    ch=int(input("Choose the role  :"))
    print()
   
    if ch==1:
        t=0
        aid=int(input("Enter the admin id  :"))
        ap=int(input("Enter the admin pin  :"))
        adm=admin(aid,ap)
        if adm.admin_verify():
            print("\n")
            print("___________Admin login___________")
            
            while True:

                print()
                print("select the function:")
                print()
                print("1.add customer\n2.view customer\n3.view_banks\n4.Exit\n")
                c=int(input("Enter the choice  :"))
                if c==1:
                    
                    adm.add_customer()
                    d=adm.print_cust()
                    l=list(d.keys())
                    l1=list(d.values())
                    # print(t)
                    d1[l[t]]=[l1[t][0]]
                    d1[l[t]].append(l1[t][1])
                    d1[l[t]].append(l1[t][2])
                    t+=1
                    print('------------------------------------------------------------')
                    print()
                elif c==2:
                    
                    adm.view_customer(d1)
                    print('------------------------------------------------------------')
                    print()
                elif c==3:
                    # print(d1)
                    adm.view_bank(d1)
                    print('------------------------------------------------------------')
                    print()
                elif c==4:
                    break
                else:
                    print("Invalid choice")
                    print('------------------------------------------------------------')
                    break
        else:

            print("\nEnter valid admin login!!!!")


    elif ch==2:
        
        id=int(input("Enter the id  :"))
        pin=int(input("Enter the pin  :"))
        custo=cust(cust_id=id,cur_pin=pin)
        vf=custo.verify(d1)
        
        if vf:
            print("___________CUSTOMER LOGIN____________")
            while True:
                print()
                print('------------------------------------------------------------')
                print()
                print("select the function")
                print()
                print("1.deposit the money\n2.widthdraw the money\n3.check Balance\n4.change pin\n5.Money Transfer\n6.Exit\n")
                n=int(input("Enter the choice  :"))
                if n==1:
                    custo.deposit(d1)
                elif n==2:
                    custo.widthdraw(d1)
                elif n==3:
                    custo.balance_check(d1)
                elif n==4:
                    custo.pin_change(id,d1)
                elif n==5:
                    custo.money_transfer(d1)
                else:
                    print('------------------------------------------------------------')

                    break
        else:
            print('------------------------------------------------------------')
            break



    elif ch==3:
        print('------------------------------------------------------------')
        break
    else:
        print("Enter a valid choice")
