import os
import telebot


bot = telebot.TeleBot("6999982337:AAHCUhWMmrV5dck5cJ_6KT6gg83lbMfzhOc")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm Uvindu Bro Chat Bot")


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "https://youtube.com/c/Uvindubro")



bot.polling()