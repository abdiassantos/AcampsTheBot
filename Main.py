import telebot
import postgresql as psql
from Connection import *
from Variables import *

con = Connection('pq://' + user + ':' + password + '@' + host + '/' + database)

token = botToken
bot = telebot.TeleBot(token)
marker = ''

#Comandos de boas vindas.
@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Seja bem vindo ao Bot do AcampsThe, {}, pressione o / para iniciar os comandos'.format(message.chat.username))
    bot.send_message(message.chat.id, 'Para mais informações falar com @AbdiasSantos')

@bot.message_handler(func = lambda m: True)
def echo_all(message):
    global marker
    ## Servos
    if(message.text == '/cafe_servo'):
        marker = 'cafe_servo'
        bot.send_message(message.chat.id, 'Insira o nome do Servo')
        print(message.text)
        print(marker)

    elif(message.text == '/almoco_servo'):
        marker = 'almoco_servo'
        bot.send_message(message.chat.id, 'Insira o nome do Servo')
        print(message.text)
        print(marker)

    elif(message.text == '/jantar_servo'):
        marker = 'jantar_servo'
        bot.send_message(message.chat.id, 'Insira o nome do Servo')
        print(message.text)
        print(marker)

    elif(message.text == '/checkin_servo'):
        marker = 'checkin_servo'
        bot.send_message(message.chat.id, 'Insira o nome do Servo')
        print(message.text)
        print(marker)

    ## Participantes
    elif (message.text == '/cafe_participante'):
        marker = 'cafe_participante'
        bot.send_message(message.chat.id, 'Insira o nome do Participante')
        print(message.text)
        print(marker)

    elif (message.text == '/almoco_participante'):
        marker = 'almoco_participante'
        bot.send_message(message.chat.id, 'Insira o nome do Participante')
        print(message.text)
        print(marker)

    elif (message.text == '/jantar_participante'):
        marker = 'jantar_participante'
        bot.send_message(message.chat.id, 'Insira o nome do Participante')
        print(message.text)
        print(marker)

    elif(message.text == '/checkin_participante'):
        marker = 'checkin_participante'
        bot.send_message(message.chat.id, 'Insira o nome do Participante')
        print(message.text)
        print(marker)

    ## Markers Servos
    elif(marker == 'cafe_servo'):
        name = message.text
        sql1 = "select cafe from servo where nome like '%{}%'".format(name)
        print('sql1: {}'.format(sql1))
        rs1 = con.consult(sql1)
        for linha1 in rs1:
            if(linha1[0]) == False:
                sql2 = "update servo set cafe = 'true' where nome like '%{}%'".format(name)
                print('sql2: {}'.format(sql2))
                if con.manipulate(sql2):
                    print('Café atualizado com sucesso')
                    bot.send_message(message.chat.id, 'Liberado para o café')
                else:
                    print('Café não atualizado com sucesso')
                    bot.send_message(message.chat.id, 'O servo não existe, contacte o Administrador @AbdiasSantos')
            else:
                bot.send_message(message.chat.id, 'Não liberado já tomou café')
        print(name)
        print(marker)

    elif(marker == 'almoco_servo'):
        name = message.text
        sql1 = "select almoco from servo where nome like '%{}%'".format(name)
        print('sql1: {}'.format(sql1))
        rs1 = con.consult(sql1)
        for linha1 in rs1:
            if(linha1[0]) == False:
                sql2 = "update servo set almoco = 'true' where nome like '%{}%'".format(name)
                print('sql2: {}'.format(sql2))
                if con.manipulate(sql2):
                    print('Almoço atualizado com sucesso')
                    bot.send_message(message.chat.id, 'Liberado para o almoço')
                else:
                    print('almoço não atualizado com sucesso')
                    bot.send_message(message.chat.id, 'O servo não existe, contacte o Administrador @AbdiasSantos')
            else:
                bot.send_message(message.chat.id, 'Não liberado já almoçou')
        print(name)
        print(marker)
    
    elif(marker == 'jantar_servo'):
        name = message.text
        sql1 = "select jantar from servo where nome like '%{}%'".format(name)
        print('sql1: {}'.format(sql1))
        rs1 = con.consult(sql1)
        for linha1 in rs1:
            if(linha1[0]) == False:
                sql2 = "update servo set jantar = 'true' where nome like '%{}%'".format(name)
                print('sql2: {}'.format(sql2))
                if con.manipulate(sql2):
                    print('Jantar atualizado com sucesso')
                    bot.send_message(message.chat.id, 'Liberado para o jantar')
                else:
                    print('Jantar não atualizado com sucesso')
                    bot.send_message(message.chat.id, 'O servo não existe, contacte o Administrador @AbdiasSantos')
            else:
                bot.send_message(message.chat.id, 'Não liberado já jantou')
        print(name)
        print(marker)

    elif(marker == 'checkin_servo'):
        name = message.text
        sql1 = "select checkin from servo where nome like '%{}%'".format(name)
        print('sql1: {}'.format(sql1))
        rs1 = con.consult(sql1)
        for linha1 in rs1:
            if(linha1[0]) == False:
                sql2 = "update servo set checkin = 'true' where nome like '%{}%'".format(name)
                print('sql2: {}'.format(sql2))
                if con.manipulate(sql2):
                    print('Checkin atualizado com sucesso')
                    bot.send_message(message.chat.id, 'Liberado para o embarque')
                else:
                    print('Checkin não atualizado com sucesso')
                    bot.send_message(message.chat.id, 'O servo não existe, contacte o Administrador @AbdiasSantos')
            else:
                bot.send_message(message.chat.id, 'Checkin já realizado')
        print(name)
        print(marker)

    ## Markers Participantes
    elif(marker == 'cafe_participante'):
        name = message.text
        sql1 = "select cafe from participante where nome like '%{}%'".format(name)
        print('sql1: {}'.format(sql1))
        rs1 = con.consult(sql1)
        for linha1 in rs1:
            if(linha1[0]) == False:
                sql2 = "update participante set cafe = 'true' where nome like '%{}%'".format(name)
                print('sql2: {}'.format(sql2))
                if con.manipulate(sql2):
                    print('Café atualizado com sucesso')
                    bot.send_message(message.chat.id, 'Liberado para o café')
                else:
                    print('Café não atualizado com sucesso')
                    bot.send_message(message.chat.id, 'O participante não existe, contacte o Administrador @AbdiasSantos')
            else:
                bot.send_message(message.chat.id, 'Não liberado já tomou café')        
        print(name)
        print(marker)

    elif(marker == 'almoco_participante'):
        name = message.text
        sql1 = "select almoco from participante where nome like '%{}%'".format(name)
        print('sql1: {}'.format(sql1))
        rs1 = con.consult(sql1)
        for linha1 in rs1:
            if(linha1[0]) == False:
                sql2 = "update participante set almoco = 'true' where nome like '%{}%'".format(name)
                print('sql2: {}'.format(sql2))
                if con.manipulate(sql2):
                    print('Almoço atualizado com sucesso')
                    bot.send_message(message.chat.id, 'Liberado para o almoço')
                else:
                    print('almoço não atualizado com sucesso')
                    bot.send_message(message.chat.id, 'O participante não existe, contacte o Administrador @AbdiasSantos')
            else:
                bot.send_message(message.chat.id, 'Não liberado já almoçou')
        print(name)
        print(marker)

    elif(marker == 'jantar_participante'):
        name = message.text
        sql1 = "select jantar from participante where nome like '%{}%'".format(name)
        print('sql1: {}'.format(sql1))
        rs1 = con.consult(sql1)
        for linha1 in rs1:
            if(linha1[0]) == False:
                sql2 = "update participante set jantar = 'true' where nome like '%{}%'".format(name)
                print('sql2: {}'.format(sql2))
                if con.manipulate(sql2):
                    print('Jantar atualizado com sucesso')
                    bot.send_message(message.chat.id, 'Liberado para o jantar')
                else:
                    print('Jantar não atualizado com sucesso')
                    bot.send_message(message.chat.id, 'O participante não existe, contacte o Administrador @AbdiasSantos')
            else:
                bot.send_message(message.chat.id, 'Não liberado já jantou')
        print(name)
        print(marker)

    elif(marker == 'checkin_participante'):
        name = message.text
        sql1 = "select checkin from participante where nome like '%{}%'".format(name)
        print('sql1: {}'.format(sql1))
        rs1 = con.consult(sql1)
        for linha1 in rs1:
            print(linha1[0])
            if(linha1[0]) == False:
                sql2 = "update participante set checkin = 'true' where nome like '%{}%'".format(name)
                print('sql2: {}'.format(sql2))
                if con.manipulate(sql2):
                    print('Checkin atualizado com sucesso')
                    bot.send_message(message.chat.id, 'Liberado para o embarque')
                else:
                    print('Checkin não atualizado com sucesso')
                    bot.send_message(message.chat.id, 'O participante não existe, contacte o Administrador @AbdiasSantos')
            else:
                bot.send_message(message.chat.id, 'Checkin já realizado')
        print(name)
        print(marker)

bot.polling()