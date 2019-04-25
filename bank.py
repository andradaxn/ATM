import time


class Card(object):
    """represents a credit card
        attributes: account number, ballance, pin, """

    def __init__(self, accnumber = 0, ballance = 0, pin = '0000'):
        self.accnumber = accnumber
        self.ballance = ballance
        self.pin = pin 

    def withdraw(self, other):
        if self.ballance<other:
            print 'Insufficient funds! Please make a deposit.'
        else:
            self.ballance-=other
            return self.ballance

    def deposit(self,other):
        self.ballance+=other
        return self.ballance

    def currentBallance(self):
        return self.ballance

    def transaction(self):
        loop=True
        while loop:
            choice = raw_input('Please select a transaction: ')
            if choice == '1':
                other=int(raw_input('Please select the amount for withdrawal: '))
                card.withdraw(other)

            if choice == '2':
                other=int(raw_input('Please select the amount for deposit: '))
                card.deposit(other)

            if choice == '3':
                print "Your current ballance is: ", self.currentBallance()

            if choice == '4':
                clients[int(accnumber)]['pin'] = raw_input("Please choose a new pin: ")

            if choice == '0':
                break


def menu():
            print "Choose (1) for withdrawal"
            print "Choose (2) for deposit"
            print "Choose (3) to check your current ballance"
            print "Choose (4) to change your pin"
            print "Choose (0) to exit"
            


card = Card()
clients = {1: {'pin': '0000', 'ballance': 0, 'account_number' : '1'}}
dictlen = len(clients)

print "Insert your credit card"
time.sleep(3)
print "Please wait"
time.sleep(3)
accnumber = raw_input("We are sorry. The ATM has a malfunction. Please introduce your account number: ")


for key in clients:
    if clients[key]['account_number'] == accnumber:
        pinint = raw_input("Insert your pin: ")
        if clients[int(accnumber)]['pin'] == pinint:
            menu()
            card.transaction()
        
    else:
        print "Unfortunately, there is no account with the number you entered."
        clients[dictlen+1] = {}
        clients[dictlen+1]['pin'] = raw_input("Insert a pin: ")
        clients[dictlen+1]['ballance'] = 0
        clients[dictlen+1]['account_number'] = dictlen+1
        break
    





    
