import math
import string

def create_codeword():
    '''
    This Function will create a hamming codeword
    '''
    d = {c: bin(ord(c))[2:] for c in string.ascii_lowercase}

    print(f'The list of alphabet charachter {" ".join(list(string.ascii_lowercase))}')
    #message
    try:
        message = d[input("Please add a charachter to create a codeword: ")]
    except:
        print("Please chose a char from charset below")
        create_codeword()
    else:
        #message length
        M = len(message)
        #redundant bits is calculated by this formula M + R + 1 <= 2**R
        R=0
        flag = True
        while(flag):
            if (M + R + 1 <= 2**R):
                flag = False
            else:
                R += 1
        # Tmessage length
        ML = M + R
        # idnex to add bits
        checkIndex =[2**i for i in range(R) if 2**i<=ML]
        #Total message
        Tmessage = []
        for i in range(1, ML+1):
            if(i in checkIndex):
                Tmessage.append("")
            else:
                Tmessage.append(message[0])
                message = message[1:]
        #checkings needed to create hamming codeword
        check1 = [3, 5, 7, 9, 11]
        check2 = [3, 6, 7, 10, 11]
        check4 = [5, 6, 7]
        check8 = [9, 10, 11]
        check = [check1, check2, check4, check8]
        #Creating total message that will be sent
        for i in range(len(checkIndex)):
            checkList = check[i]
            bitSum=0
            for index in checkList:
                bitSum += int(Tmessage[index - 1])
            Tmessage[checkIndex[i] -1] = str((bitSum % 2))

        return "".join(Tmessage)




print(create_codeword())

def hamming_correcting_single_error():
    '''
    Checking and correcting the single bit error
    '''
    print("The length of code word should be less than 16 for correct answer")
    ReceivedM = list(input("Please enter the received message for checking: "))
    #message length
    ML = len(ReceivedM)
    #checkbits
    R = math.ceil(math.log2(ML))
    checkIndex =[2**i for i in range(R) if 2**i<=ML]
    #checkings needed to create hamming codeword
    check1 = [3, 5, 7, 9, 11]
    check2 = [3, 6, 7, 10, 11]
    check4 = [5, 6, 7]
    check8 = [9, 10, 11]
    check = [check1, check2, check4, check8]
    #Checking the message received
    c = 0
    for i in range(len(checkIndex)):
        checkList = check[i]
        bitSum=0
        for index in checkList:
            bitSum += int(ReceivedM[index - 1])
        if(ReceivedM[checkIndex[i] -1] != str((bitSum % 2))):
            c +=  checkIndex[i]
    if(c==0):
        print("Message was recieved without any corruption")
    else:
        if(ReceivedM[c-1]=='0'):
            ReceivedM[c-1]='1'
        else:
            ReceivedM[c-1] = '0'
        print("The message was changed!!!!")
        print(f'The correct message is {"".join(ReceivedM)}')



hamming_correcting_single_error()
