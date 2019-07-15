import telebot
import postgresql as psql
from Connection import *
from Variables import *

con = Connection('pq://' + user + ':' + password + '@' + host + '/' + database)

token = botToken
bot = telebot.TeleBot(token)

cafeReset = 0
almocoReset = 0
jantarReset = 0
checkinReset = 0

#Comandos de boas vindas.
@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Seja bem vindo ao Bot do AcampsThe, {}, pressione o / para iniciar os comandos'.format(message.chat.username))
    bot.send_message(message.chat.id, 'Para mais informações falar com @AbdiasSantos')

## Servos e Participantes
# @bot.message_handler(commands = ['cafe_servo', 'cafe_participante', 
#                                     'almoco_servo', 'almoco_participante', 
#                                     'jantar_servo', 'jantar_participante'])
@bot.message_handler(func = lambda m: True)
def echo_all(message):
    if(message.text == '/cafe_servo' or message.text == '/almoco_servo' or message.text == '/jantar_servo'):
        bot.send_message(message.chat.id, 'Insira o nome do Servo')
        print(message.text)

    elif (message.text == '/cafe_participante' or message.text == '/almoco_participante' or message.text == '/jantar_participante'):
        bot.send_message(message.chat.id, 'Insira o nome do Participante')
        print(message.text)
    
    elif(message.text == '/checkin_servo'):
        bot.send_message(message.chat.id, 'Insira o nome do Servo')
        print(message.text)

    elif(message.text == '/checkin_participante'):
        bot.send_message(message.chat.id, 'Insira o nome do Participante')
        print(message.text)

    else:
        bot.send_message(message.chat.id, 'Não compreendi o que dissestes')
        send_welcome(message)
        print(message.text)

bot.polling()