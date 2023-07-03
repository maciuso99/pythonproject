from footballers import *
import random
import player as p
import time



def packopen():
    decision = ['yes', 'no']
    question1 = None
    while question1 not in decision:
        question1 = input('Open a pack? \n yes or no : ').lower()
    if question1 == 'yes' and p.balance >= 10_000:
        drop = random.choice(TOP5)
        buy_pack()
        print('You packed ', drop)




        def engworthness():

            match drop:
                case 'Kevin de Bruyne' | 'Erling Haaland':
                    print('worth: ', ENGVALUE[0], ' coins')
                    calculate(ENGVALUE[0],drop)
                case 'Mohamed Salah':
                    print('worth: ', ENGVALUE[1], ' coins')
                    calculate(ENGVALUE[1],drop)
                case 'Casemiro' | 'Harry Kane' | 'Ederson':
                    print('worth: ', ENGVALUE[5], ' coins')
                    calculate(ENGVALUE[5],drop)
                case 'Virgil van Dijk':
                    print('worth: ', ENGVALUE[2], ' coins')
                    calculate(ENGVALUE[2],drop)
                case 'Cristiano Ronaldo':
                    print('worth: ', ENGVALUE[3], ' coins')
                    calculate(ENGVALUE[3],drop)
                case 'Heung Min Son':
                    print('worth: ', ENGVALUE[4], ' coins')
                    calculate(ENGVALUE[4],drop)
                case 'Alisson':
                    print('worth: ', ENGVALUE[6], ' coins')
                    calculate(ENGVALUE[6],drop)
                case 'Ngolo Kante':
                    print('worth: ', ENGVALUE[9], ' coins')
                    calculate(ENGVALUE[9],drop)

        engworthness()

        def espworthness():

            match drop:
                case 'Karim Benzema':
                    print('worth: ', ESPVALUE[0], ' coins')
                    calculate(ESPVALUE[0],drop)
                case 'Robert Lewandowski':
                    print('worth: ', ESPVALUE[1], ' coins')
                    calculate(ESPVALUE[1],drop)
                case 'Thibaut Courtois':
                    print('worth: ', ESPVALUE[2], ' coins')
                    calculate(ESPVALUE[2],drop)
                case 'Jan Oblak':
                    print('worth: ', ESPVALUE[3], ' coins')
                    calculate(ESPVALUE[3],drop)
                case 'Toni Kroos' | 'Marc ter Stegen' | 'Luka Modric' | 'Frenkie de Jong':
                    print('worth: ', ESPVALUE[4], ' coins')
                    calculate(ESPVALUE[4],drop)
                case 'Antonio Rudiger':
                    print('worth: ', ESPVALUE[8], ' coins')
                    calculate(ESPVALUE[8],drop)
                case 'Vini JR':
                    print('worth: ', ESPVALUE[9], ' coins')
                    calculate(ESPVALUE[9],drop)
                case 'David Alaba':
                    print('worth: ', ESPVALUE[10], ' coins')
                    calculate(ESPVALUE[10],drop)

        espworthness()

        def itaworthness():

            match drop:
                case 'Mike Maignan':
                    print('worth: ', ITAVALUE[0], ' coins')
                    calculate(ITAVALUE[0],drop)
                case 'Wojciech Szczesny' | 'Ciro Immobile' | 'Milos Skriniar':
                    print('worth: ', ITAVALUE[1], ' coins')
                    calculate(ITAVALUE[1],drop)
                case 'Lautaro Martinez' | 'Romelu Lukaku' | 'Nicolo Barella' | 'Paulo Dybala':
                    print('worth: ', ITAVALUE[2], ' coins')
                    calculate(ITAVALUE[2],drop)
                case 'Paul Pogba':
                    print('worth: ', ITAVALUE[8], ' coins')
                    calculate(ITAVALUE[8],drop)
                case 'Theo Hernandez':
                    print('worth: ', ITAVALUE[9], ' coins')
                    calculate(ITAVALUE[9],drop)

        itaworthness()

        def gerworthness():

            match drop:
                case 'Manuel Neuer':
                    print('worth: ', GERVALUE[0], ' coins')
                    calculate(GERVALUE[0],drop)
                case 'Sadio Mane':
                    print('worth: ', GERVALUE[1], ' coins')
                    calculate(GERVALUE[1],drop)
                case 'Joshua Kimmich':
                    print('worth: ', GERVALUE[2], ' coins')
                    calculate(GERVALUE[2],drop)
                case 'Thomas Muller':
                    print('worth: ', GERVALUE[3], ' coins')
                    calculate(GERVALUE[3],drop)
                case 'Leon Goretzka':
                    print('worth: ', GERVALUE[4], ' coins')
                    calculate(GERVALUE[4],drop)
                case 'Kingsley Coman':
                    print('worth: ', GERVALUE[5], ' coins')
                    calculate(GERVALUE[5],drop)
                case 'Kevin Trapp':
                    print('worth: ', GERVALUE[6], ' coins')
                    calculate(GERVALUE[6],drop)
                case 'Christopher Nkunku':
                    print('worth: ', GERVALUE[7], ' coins')
                    calculate(GERVALUE[7],drop)

        gerworthness()

        def fraworthness():

            match drop:
                case 'Kylian Mbappe':
                    print('worth: ', FRAVALUE[0], ' coins')
                    calculate(FRAVALUE[0],drop)
                case 'Lionel Messi':
                    print('worth: ', FRAVALUE[1], ' coins')
                    calculate(FRAVALUE[1],drop)
                case 'Neymar JR':
                    print('worth: ', FRAVALUE[2], ' coins')
                    calculate(FRAVALUE[2],drop)
                case 'Marquinhos':
                    print('worth: ', FRAVALUE[3], ' coins')
                    calculate(FRAVALUE[3],drop)
                case 'Gianuluigi Donnarumma':
                    print('worth: ', FRAVALUE[4], ' coins')
                    calculate(FRAVALUE[4],drop)
                case 'Renato Sanches':
                    print('worth: ', FRAVALUE[5], ' coins')
                    calculate(FRAVALUE[5],drop)
                case 'Presnel Kimpembe':
                    print('worth: ', FRAVALUE[6], ' coins')
                    calculate(FRAVALUE[6],drop)

        fraworthness()

        time.sleep(0.5)

        morepack()

    elif question1 == 'yes' and p.balance <= 10_000:
        print('Sorry you have not enough coins!!!')
        screen()
        return p.balance, p.club

    else:
        screen()

def morepack():
    more = None
    decision3 = ('yes', 'no')
    while more not in decision3:
        more = input('Wish to open another one?  (yes/no): ').lower()
        if more == 'yes' and p.balance >= 10_000 :
            buy_pack()
            packopen()
        else:
            print('Sorry you have not enough coins!!!')
            screen()
            return p.balance, p.club




def screen():
    decision2 = ('1', '2', '3', '4')
    question2 = None
    while question2 not in decision2:
        question2 = (
            input(
                'Select game mode. Enter the number: \n 1.For store \n 2.For balance \n 3.For club \n 4.For quit \n :'
            )).lower()
    match question2:
        case '1':
            packopen()
            
        case '2':
            print('Your balance is: ', p.balance, ' coins')
            time.sleep(5)
            screen()
        case '3':
            print("Your club: \n")
            print(p.club)
            screen()
        case '4':
            print("It was nice to see you")
            quit()

def buy_pack():
    p.balance = p.balance - 10_000
    return p.balance

def calculate(value, id):
    onetwo = ("1", "2")
    whatsnext = None
    while whatsnext not in onetwo:
        whatsnext = input("To sell press 1. \nSend to the club press 2.\n: ")
        if whatsnext == "1":
            p.balance = p.balance + value
            return p.balance
        else:
            p.club.append(id)
            return p.club
        
def club_manage(club, balance, drop, id):
    choice = input("Press: \n1. to sell everything \n2. to go back to the menu" )
    if choice == "1":
        club.clear()

    elif choice == "2":
        screen()
        return balance, club




