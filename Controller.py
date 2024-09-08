import pyfirmata as pyf
import pyttsx3
import random
import winsound
import time
import os

engine = pyttsx3.init()
COM = int(input('COM: '))
print(f'Using COM{COM} as Arduino Device.')
board = pyf.Arduino(f'COM{COM}')
pin_7 = board.get_pin('d:7:i')
pin_8 = board.get_pin('d:8:i')
pin_9 = board.get_pin('d:9:i')
os.system('cls')
it = pyf.util.Iterator(board)
it.start()
data = [1,2,3]
user_input = []
level = 1
temp = 0
Code = []
mem = []

def GameOver():
    global Code
    global data
    global user_input
    global mem
    global level
    user_input = []
    mem = []
    engine.say(f'Game Over! You managed to reach level {level}. Press pin 8 to restart.')
    engine.runAndWait()
    while True:
        if pin_8.read() == 1:
            Code = []
            data = [1,2,3]
            print('Restarting..')
            break

    global temp
    user_input = []
    data = [1,2,3]
    Code = []
    temp = 0
    level = 1
    Main()

def Main():
    global user_input
    global data
    global Code
    global temp
    global level
    global mem
    engine.say(f'Level {level}')
    engine.runAndWait()
    while True:
        if len(Code) != level:
            random.shuffle(data)
            Code.append(data[0])
            print(Code)
            mem.append(data[0])
        else:
            break
    i = 0
    while True:
        if Code[i] == 1:
            os.system('cls')
            print(f'Code : {Code[i]}')
            winsound.Beep(750, 150)
        if Code[i] == 2:
            os.system('cls')
            print(f'Code : {Code[i]}')
            winsound.Beep(1000, 150)
        if Code[i] == 3:
            os.system('cls')
            print(f'Code : {Code[i]}')
            winsound.Beep(1250, 150)
        time.sleep(0.25)
        i += 1
        if i == len(Code):
            break
    os.system('cls')
    print('Code : ')

    while len(user_input) != len(Code):
        if pin_7.read() == 1:
            user_input.append(1)
            os.system('cls')
            print(f'Code : {user_input}')
            winsound.Beep(750, 150)
        if pin_8.read() == 1:
            user_input.append(2)
            os.system('cls')
            print(f'Code : {user_input}')
            winsound.Beep(1000, 150)
        if pin_9.read() == 1:
            user_input.append(3)
            os.system('cls')
            print(f'Code : {user_input}')
            winsound.Beep(1250, 150)
    if user_input == Code:
        level += 1
        temp = 0
        user_input = []
        Main()
    else:
        GameOver()

if __name__ == '__main__':
    engine.say('Press pin 8 to start.')
    engine.runAndWait()
    while True:
        if pin_8.read() == 1:
            engine.say('Remember these sounds..')
            engine.runAndWait()
            break
    engine.say('Left Button.')
    engine.runAndWait()
    os.system('cls')
    print('Left Pin : 1')
    winsound.Beep(750,150)
    engine.say('Middle Button.')
    engine.runAndWait()
    os.system('cls')
    print('Middle Pin : 2')
    winsound.Beep(1000,150)
    engine.say('Right Button.')
    engine.runAndWait()
    os.system('cls')
    print('Right Pin : 3')
    winsound.Beep(1250,150)
    engine.say('I repeat.')
    engine.runAndWait()
    engine.say('Left Button.')
    engine.runAndWait()
    os.system('cls')
    print('Left Pin : 1')
    winsound.Beep(750,150)
    engine.say('Middle Button.')
    engine.runAndWait()
    os.system('cls')
    print('Middle Pin : 2')
    winsound.Beep(1000,150)
    engine.say('Right Button.')
    engine.runAndWait()
    os.system('cls')
    print('Right Pin : 3')
    winsound.Beep(1250,150)
    time.sleep(1)
    engine.say('Game Started.')
    engine.runAndWait()
    time.sleep(0.5)
    Main()