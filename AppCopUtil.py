# Python3 code  
# Developed by Rishi Rao
# Developed on 30-03-2018

#**************Function to Captue Hostname & IP************
#https://docs.python.org/3/library/socket.html
#
import socket
def get_Host_IP():
    try:
        #print("In Function")
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        #print("Hostname :  ",host_name)
        #print("IP : ",host_ip)
        return (host_ip,host_name)
    except:
        print("Unable to get Hostname and IP")
 

#**************End of function *************************** 

#**************Function to Validate Card *****************
##
##def card_main():
##    # cc_number = int(input("Enter a valid credit card number: "))
##    ##Invalid Card
##    #cc_number = 12345678912356789
##    ##AMEX CARD
##    #cc_number = 3716820019271980
##    ##VISA
##    #cc_number = 4181570004067315
##    ##MASTER CARD
##    cc_number = 5331360100720264
##    
##    if not checksum(cc_number):
##        print("INVALID")
##    else:
##        print(check_provider(cc_number))
##
##
##def check_provider(number):
##    if len(str(number)) < 13 or len(str(number)) > 16:
##        return 'INVALID'
##
##    if ((list(str(number)))[:2]) == ['3', '4'] or ((list(str(number)))[:2]) == ['3', '7']:
##        return 'AMEX'
##    elif ((list(str(number)))[:2]) == ['5', '1'] or ((list(str(number)))[:2]) == ['5', '2'] \
##            or ((list(str(number)))[:2]) == ['5', '3'] or ((list(str(number)))[:2]) == ['5', '4'] \
##            or ((list(str(number)))[:2]) == ['5', '5']:
##        return 'MASTERCARD'
##    elif ((list(str(number)))[0]) == '4':
##        return 'VISA'
##    else:
##        return 'INVALID'
##
##
##def checksum(number):
##    list_number = list(str(number))
##    odd_indices = []
##    even_indices = []
##
##    last_index = len(list_number) - 1
##
##    rev_list = list(reversed(list_number))
##
##    for i in rev_list[1::2]:
##        odd_indices.append(i)
##
##    for i in rev_list[::2]:
##        even_indices.append(i)
##
##    sum_odd = sum(split_to_digits(''.join(int_to_str(mul(odd_indices, 2)))))
##    sum_even = sum(split_to_digits(''.join(int_to_str(even_indices))))
##    s = sum_odd + sum_even
##
##    print(s)
##
##    if s % 10 == 0:
##        return True
##    return False
##
##
##def mul(list, x):
##    return [(int(n) * 2) for n in list]
##
##
##def split_to_digits(n):
##    return [int(i) for i in str(n)]
##
##
##def int_to_str(n):
##    return [str(x) for x in n]
##
##
##def str_to_int(n):
##    return [int(x) for x in n]
##
##
##card_main()

#************************************************* 

#********Function to Auto Generate Password*******

##import random
##
##CharsList = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
##PassLength = 8
##Password = ''
##
###Below loop will execute 8 times and each time add single random character from variable CharsList
##for PassCount in range(int(PassLength)):
##    Password += random.choice(CharsList)
##
##return(Password)

#************************************************* 







