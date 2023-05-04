import os
import telebot

bot=telebot.TeleBot("API KEY")

@bot.message_handler(commands-["start"])
def send_welcome(message):
    bot.reply_to(message,"hellow kavindu bot")

@bot.message_handler(commands-["how"]) 
def send_welcome(message):
     bot.send_to(message,"Link")

bot.polling()