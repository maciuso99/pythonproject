


account = 0
value = 450000
balance = account + value

print('Current balance: ' + str(balance) + ' coins')

# chance = 2.5
# print('GZ, chance was:' + str(chance) + '%')


# goat = True
# print('Is' + name + ' a goat?' + str(goat))

# multiple assignment task
id, worthness, skilled, = 'Lionel Messi', 280000, True
# print('You packed' + id + 'worth' + str(worthness))


import random

lower_case = 'abcdefghijklmnoprstuwxyz'
Upper_case = 'ABCDEFGHIJKLMNOPRSTUWXYZ'
numbers = '1234567890'

password = lower_case + Upper_case 
lenght = 8
yourpassword = ''.join(random.sample(password, lenght))
print(yourpassword)

#import time
# ask about name then print hello + given

#nickname = input("What is your nickname?: ")
#print('Hello {0}'.format(nickname))

#temp = int(input('What is the temperature outside?: '))

#if temp >= 0 and temp <= 30:
    #print('its okay')
    #print('go outside!')
#elif temp < 0 or temp > 30:
    #print('omg end of the world')
#else :
    #pass


#action = ''
#while len(action) == 0:
    #action = input('What will you do then?: ')
#print('hf ' + action)

#for seconds in range(10,0,-1):
    #print(seconds)
    #time.sleep(1)
#print('move your ass')




def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to" \
                                                                             " share and connect code together"
def build_sentence(benefit):
    return('its a good function' + benefit)

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

class Drops(object):

    def __init__(self,players,values,id):
        self.id = id
        self.players = players
        self.values = values

    def new_game(self):
        pass
class Pack(object):

    def __init__(self, footballers, coins, player_id):
        self.footballers = footballers
        self.coins = coins
        self.player_id = player_id
        self.pack_open()
    def pack_open(self):
        """
        defines a function that opens a pack
        :return: None
        """
        pass

    def decision(self):
        """
        asks what to do next
        :return: int
        """
        pass

    def randomize_drop(self):
        pass
    # todo make a random drop of all the footballers list