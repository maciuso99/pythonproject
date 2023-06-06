import time
from scripts import *

print('Loading, please hold')
for i in range(100):
    print(i + 1)
    time.sleep(0.01)

print('Hello guest!')

nickname = ''
while len(nickname) == 0:
    nickname = input('What is your nickname?: ')

print('Its a pleasure to meet you ' + nickname)
time.sleep(0.1)

screen()

