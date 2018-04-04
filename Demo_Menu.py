choice =''

while choice !='0':

    choice = input ('<<< AppCop Menu Options >>> \n\nCapture User IP & Hostname 1: \nPassword Generate 2: \nCard Validation 3: \nExit 0: \n\nEnter your choice >>> ')

    if choice =='1':
        import AppCopUtil as f_machine_details
        host_machine_detail = ''
        host_machine_detail = f_machine_details.get_Host_IP()
        print ('\nLogged-in User IP & Hostname :',host_machine_detail)
        print ('\n')       
    
    elif choice =='2':
        import AppCopUtil as f_auto_password
        auto_password_gen = ''
        auto_password_gen = f_auto_password.gen_Password()
        print ('\nAuto generated password :',auto_password_gen)
        print ('\n')

    elif choice =='3':
        import AppCopUtil as f_card_validate
        Card_Details = ''
        Card_Number = ''
        Card_Number = input ('Enter Card Number to Validate >>>')
        Card_Details = f_card_validate.card_validate(Card_Number)
        print ('Card Status :',Card_Details)
        print ('\n')

            
    elif choice =='0':
        break

    else:
       print("Invalid choice")
