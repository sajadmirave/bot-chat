import telebot
from telebot import types

# Replace 'YOUR_BOT_TOKEN' with your actual bot token obtained from BotFather on Telegram
token = 0
bot = telebot.TeleBot(token)
admin_id = 1

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    username = message.from_user.username
    user_id = message.from_user.id

    # save user name and user id
    with open('data.txt','a',encoding='utf-8') as file:
        data_to_write = ""
        data_to_write += f"username: @{username}\n"
        data_to_write += f"user id: {user_id}\n"
        data_to_write += "-"*50+"\n"
        file.write(data_to_write)

    # save user messages
    with open('messages.txt','a',encoding='utf-8') as file:
        data_to_write = ""        
        data_to_write += f"from: @{username}\n"
        data_to_write += f"with user id: {user_id}\n"
        data_to_write += f"message: {message.text}\n"
        data_to_write += "-"*50+"\n"
        file.write(data_to_write)

    print(f'username: @{username} send message')
    print(f'user id: {user_id}')
    print('-'*50)

    # reply to user
    bot.reply_to(message, "پیام شما ارسال شد.")

    # send user message to admin
    admin_message = ""
    admin_message += f"user: @{username} says: \n"
    admin_message += message.text
    bot.send_message(admin_id, admin_message)

# Run the bot
print("bot is running...")
bot.polling()
