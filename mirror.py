import time, requests, random
from telegram.ext import MessageHandler, filters, ApplicationBuilder
import logging

logging.basicConfig(filename="E:\YandexDisk\Python\[2023] Amanda Lizard\log.log", level=logging.ERROR)
# logging.basicConfig(filename="log.log", level=logging.INFO) WARNING  ERROR CRITICAL

from settings import * # в конце - поменять!!!
# TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN") # print("TOKEN: ", TOKEN)

# CHAT_ID = -1001670463029 # work
CHAT_ID = -1001729154400 # test
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






async def message_handler(update, context):
    print("update:", update)
    # print(update.message.chat.id) -1001670463029

    # if update.message.chat.title == "Зазеркалье твича":
    if update.message.chat.id == CHAT_ID:
        user_message = update.message.text
        print("0 user_message:", user_message)
        print("0 user_message:", member.full_name)

        if "миша" in user_message.lower():
            await update.message.reply_text('Но я не Миша!')
    # else:
    #     print("22:", update.message.chat.username)
    #     print("33:", update.message.date)

    #     print("1:", update.message.from_user.first_name)
    #     print("2:", update.message.from_user.id) # effective_chat
    #     print("3:", update.message.from_user.is_bot)
    #     print("4:", update.message.from_user.last_name)
    #     print("5:", update.message.from_user.username)
    #     print(" ")


    
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

    application = ApplicationBuilder().token(TOKEN).build()
    # start_handler = MessageHandler(filters.TEXT, message_handler)
    start_handler = MessageHandler(filters.StatusUpdate.NEW_CHAT_PHOTO, message_handler)
    application.add_handler(start_handler)
    application.run_polling()


if __name__ == '__main__':
    task2()
    # asyncio.run(task2())
    task1()
