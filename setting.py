import time, requests, random, asyncio
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, ApplicationBuilder, ContextTypes
# import telegram
import logging

logging.basicConfig(filename="E:\YandexDisk\Python\[2023] Amanda Lizard\log.log", level=logging.INFO)
# logging.basicConfig(filename="log.log", level=logging.INFO) WARNING  ERROR CRITICAL

from settings import * # в конце - поменять!!!
# TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN") # print("TOKEN: ", TOKEN)

# CHAT_ID = -1001670463029 # work
CHAT_ID = -1001744761688 # test
text_for_send = "man is weak" # человек слаб

random_time_list1 = [5, 6, 7, 8]
random_time_list2 = [11, 12, 13, 14]
random_time_list3 = [18, 19, 20, 22, 23]
choice1 = random.choice(random_time_list1)
choice2 = random.choice(random_time_list2)
choice3 = random.choice(random_time_list3)

def Send_to_zazerkalie():
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text_for_send}")


def task1():
    logging.info("2й")
    print("2й")
    while True:
        current_time = time.localtime()
        h, m, s = current_time.tm_hour, current_time.tm_min, current_time.tm_sec

        # task
        if (h == choice1 and m == 0 and s == 0):
            Send_to_zazerkalie()

        if (h == choice2 and m == 0 and s == 0):
            Send_to_zazerkalie()

        if (h == choice3 and m == 0 and s == 0):
            Send_to_zazerkalie()

        # test
        # if (h == 21 and m == 9 and s == 0):
            # Send_to_zazerkalie()

        time.sleep(1)


def greet(update, context):
    # print(update)
    chat = update.message.chat.id
    chat1 = update.message.chat
    text = update.message.text
    print("chat", chat, type(chat))
    print("chat", chat1, type(chat1))
    print("text", text)
 

    # if chat == CHAT_ID:
        # print("==")
        # print("text:", text)
    # else:
        # print("Я ловлю только ТАМ а не тут ", update.message.chat.id)

    # print("Вызывал /start") # /start
    # update.message.reply_text(text)
    if "миша" in text.lower():
        update.message.reply_text("Но я не Миша!")

def message_handler(update, context):
    user_message = update.message.text
    print(user_message, user_message)
    update.message.reply_text("I'm sorry Dave I'm afraid I can't do that.")

    
# async def task2():
#     bot = telegram.Bot(TOKEN)
#     async with bot:
#         print(await bot.get_me())
#         print((await bot.get_updates())[0])
#         await bot.send_message(text='Hi John!', chat_id=CHAT_ID)
#         print(await bot.get_my_default_administrator_rights(CHAT_ID))
#         print(await bot.get_chat_administrators(chat_id=-1001670463029))
#         print(await bot.get_chat_member_count(chat_id=-1001670463029))

def task2():
    print("1")
    logging.info("1й")
    # updater = Updater()
    # dispatcher = updater.dispatcher
    # updater.start_polling()

    application = ApplicationBuilder().token(TOKEN).build()
    start_handler = MessageHandler(filters.TEXT, message_handler)
    application.add_handler(start_handler)
    application.run_polling()


if __name__ == '__main__':
    task2()
    # asyncio.run(task2())
    task1()
