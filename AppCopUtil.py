# Python3 code  
# Developed by Rishi Rao
# Developed on 30-03-2018

#**************Function to Captue Hostname & IP************
#

import socket
def get_Host_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return (host_ip,host_name)
    except:
        return "Unable to get Hostname and IP"
 

#**************End of function *******************
#*************************************************
        
#********Function to Auto Generate Password*******

import random
def gen_Password():
    try:
        CharsList = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
        PassLength = 8
        Password = ''

        #Below loop will execute 8 times or valuse in PassLength variable and
        #each time add single random character from variable CharsList
        for PassCount in range(int(PassLength)):
            Password += random.choice(CharsList)
        return(Password)
    except:
        return "Unable to generate password"

#**************End of function ******************* 
#************************************************* 
      

#**************Function to Validate Card *********

def card_validate(cc_number):
    ## EXAMPLES
    ##Invalid Card
    #cc_number = 123456789012356789
    ##AMEX CARD
    #cc_number = 3716820019271980
    ##VISA
    #cc_number = 4181570004067315
    ##MASTER CARD
    #cc_number = 5331360100720264
    
    return check_provider(cc_number)

def check_provider(number):
    if len(str(number)) < 13 or len(str(number)) > 16:
        return 'Card Numbers Digits Incorrect'

    if ((list(str(number)))[:2]) == ['3', '4'] or ((list(str(number)))[:2]) == ['3', '7']:
        return 'This is a valid AMEX card.'
    elif ((list(str(number)))[:2]) == ['5', '1'] or ((list(str(number)))[:2]) == ['5', '2'] \
            or ((list(str(number)))[:2]) == ['5', '3'] or ((list(str(number)))[:2]) == ['5', '4'] \
            or ((list(str(number)))[:2]) == ['5', '5']:
        return 'This is a valid MASTERCARD card.'
    elif ((list(str(number)))[0]) == '4':
        return 'This is a valid VISA card.'
    else:
        return 'This is a INVALID card.'

#************************************************* 









