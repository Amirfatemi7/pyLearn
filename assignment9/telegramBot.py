import random
import qrcode
import telebot
from telebot import types
from khayyam import JalaliDate,JalaliDatetime
from gtts import gTTS

state = None
pcNumber = 0

my_keyboard = types.ReplyKeyboardMarkup(row_width=3)
key1 = types.KeyboardButton("/game")
key2 = types.KeyboardButton("/age")
key3 = types.KeyboardButton("/voice")
key4 = types.KeyboardButton("/max")
key5 = types.KeyboardButton("/argmax")
key6 = types.KeyboardButton("/QRcode")
key7 = types.KeyboardButton("/help")
my_keyboard.add(key1,key2,key3,key4,key5,key6,key7)

token = " "
bot = telebot.TeleBot(token,parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    # bot.reply_to(message,"hi, how are you?!")
    msg = "Hi " +" "
    if message.chat.first_name:
        msg += str(message.chat.first_name)
    msg +=" "
    if message.chat.last_name:
        msg += str(message.chat.last_name)
    msg += ",welcome to my bot."
    bot.send_message(message.chat.id,msg)
    bot.send_message(message.chat.id, "Choose one menu:", reply_markup=my_keyboard)

@bot.message_handler(commands=['game'])
def send_welcome(message):
    global state,i,pcNumber
    i=0
    pcNumber = random.randint(10,100)
    state = 'game'
    bot.reply_to(message,"you selected game")
    bot.send_message(message.chat.id,"enter your number")
    game(message)

@bot.message_handler(commands=['age'])
def send_welcome(message):
    global state
    state = 'age'
    bot.reply_to(message,"write your birthday like this : 1375,5,22")

@bot.message_handler(commands=['voice'])
def send_welcome(message):
    global state
    state = 'voice'
    bot.reply_to(message,"write text in English")

@bot.message_handler(commands=['max'])
def send_welcome(message):
    global state
    state = 'max'
    bot.reply_to(message,"write your list like this: \n 12,5,8,100,500")

@bot.message_handler(commands=['argmax'])
def send_welcome(message):
    global state
    state = 'argmax'
    bot.reply_to(message,"write your list like this: \n 12,5,8,100,500")

@bot.message_handler(commands=['QRcode'])
def send_welcome(message):
    global state
    state = 'QRcode'
    bot.reply_to(message,"selected QRcode")
    bot.send_message(message.chat.id,"write your anything you want to show on QRcode")
    

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id,"game: user guss a number and bot help to fint it")
    bot.send_message(message.chat.id,"age: calculate your age")
    bot.send_message(message.chat.id,"voice: text to voice converter")
    bot.send_message(message.chat.id,"max: find maximum fo your array")
    bot.send_message(message.chat.id,"argmax: find index of maximum number in your list")
    bot.send_message(message.chat.id,"QRcode: convert your text to QRcode", reply_markup=my_keyboard)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    # bot.send_message(message.chat.id,message.text)
    match state:
        case 'game':
            game(message)
        case 'age':
            age(message)
        case 'voice':
            txtToVoice(message)
        case 'max':
            findMax(message)
        case 'argmax':
            findArgmax(message)
        case 'QRcode':
            print(message.text)
            qr = qrcode.make(message.text)
            qr.save('photo.png')
            photo = open('photo.png', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_photo(message.chat.id, "FILEID")
 




i = 0

def game(message):
    global i
    global pcNumber
    # for i in range(10):
    if i < 10:
        i += 1
        if i > 6:
            
            msg = 'you have {} times !!!!'.format(10-i)
            bot.send_message(message.chat.id,msg)
        userNumber = int(message.text)
        
        if pcNumber == userNumber:
            bot.send_message(message.chat.id,"afaaaariiiiin barande shodi")
            msg = "number of your guess is :" + str(i+1)
            bot.send_message(message.chat.id,msg,reply_markup=my_keyboard)
            state = 0
        elif pcNumber > userNumber:
            bot.send_message(message.chat.id,"go up")
        elif pcNumber < userNumber:
            bot.send_message(message.chat.id,"go down")
    else:
        bot.send_message(message.chat.id,"you lost, play again",reply_markup=my_keyboard)

def age(message):
    msg = message.text
    born = msg.split(",")
    diffrent = JalaliDatetime.now() - JalaliDatetime(int(born[0]),int(born[1]),int(born[2]))
    # print(diffrent.date)
    bot.send_message(message.chat.id,"age is : "+ str(int(diffrent.days/365)),reply_markup=my_keyboard)

def txtToVoice(message):
    language = 'en'
    myobj = gTTS(text=message.text, lang=language, slow=False)
    myobj.save("voice.mp3")
    voice = open('voice.mp3', 'rb')
    bot.send_voice(message.chat.id, voice,reply_markup=my_keyboard)
    bot.send_voice(message.chat.id, "FILEID",reply_markup=my_keyboard)

def findMax(message):
    msg = message.text
    list = msg.split(",")
    print(list)
    compare = 0
    for l in list:
        if int(l) > compare:
            compare = int(l)
    print(compare)
    bot.send_message(message.chat.id,compare,reply_markup=my_keyboard)

def findArgmax(message):
    msg = message.text
    list = msg.split(",")
    print(list)
    compare = 0
    C = 0
    CC = 0
    for l in list:
        if int(l) > compare:
            compare = int(l)
            CC = C
        C+=1

    print(compare)
    bot.send_message(message.chat.id,CC,reply_markup=my_keyboard)


bot.infinity_polling()
