import time, requests, random, asyncio
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
# import telegram
import logging

logging.basicConfig(filename="E:\YandexDisk\Python\[2023] Amanda Lizard\log.log", level=logging.DEBUG)
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
    text = update.message.text
    print("text:", text)
    # print("Вызывал /start") # /start
    # update.message.reply_text(text)

def task2():
    print("1")
    logging.info("1й")

    mybot = Updater(TOKEN, update_queue=asyncio.Queue)

    # dp = mybot.dispatcher
    # mybot.add_handler(CommandHandler("start", greet))
    mybot.MessageHandler(filters.Text , greet)

    mybot.start_polling()



if __name__ == '__main__':
    task2()
    task1()
