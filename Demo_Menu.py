choice =''

while choice !='0':
    choice = input ('<<< AppCop Menu Options >>> \nCapture User IP & Hostname 1: \nCard Validation 2: \nPassword Generate 3: \nExit 0: ')
    if choice =='1':
        print ("Returns Logged-in User IP & Hostname")
        import AppCopUtil as f_machine_details
        host_machine_detail = ''
        host_machine_detail = f_machine_details.get_Host_IP()
        print (host_machine_detail)
        break       
    elif choice =='2':
        print ('Enter Card Numner & It returns Vendor Name and Card validity')
        break
    elif choice =='3':
        print ('Returns auto generated password ')
        break
    elif choice =='0':
        break
    
