import os, time, requests, random
from telegram.ext import MessageHandler, filters, ApplicationBuilder
# from settings import * # в конце - поменять!!!
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN") # print("TOKEN: ", TOKEN)


CHAT_ID = -1001670463029 # work
# CHAT_ID = -1001729154400 # test
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
    if update.message.chat.id == CHAT_ID:
        user_message = update.message.text
        if "миша" in user_message.lower():
            await update.message.reply_text('Но я не Миша!')

def task2():
    application = ApplicationBuilder().token(TOKEN).build()
    start_handler = MessageHandler(filters.TEXT, message_handler)
    application.add_handler(start_handler)
    application.run_polling()


if __name__ == '__main__':
    task2()
    task1()
