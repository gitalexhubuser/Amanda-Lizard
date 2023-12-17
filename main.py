import os, time, requests, random
from telegram.ext import MessageHandler, filters, ApplicationBuilder
from dotenv import load_dotenv

load_dotenv()

text_for_send = "man is weak" # человек слаб

random_time_list1 = [5, 6, 7, 8]
random_time_list2 = [11, 12, 13, 14]
random_time_list3 = [18, 19, 20, 22, 23]
choice1 = random.choice(random_time_list1)
choice2 = random.choice(random_time_list2)
choice3 = random.choice(random_time_list3)

def Send_to_zazerkalie():
    requests.post(f"https://api.telegram.org/bot{os.getenv('TOKEN')}/sendMessage?chat_id={os.getenv('CHAT_ID')}&text={text_for_send}")

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
    print(type(update.channel_post.chat.id))
    # print(update.channel_post.text)
    # if update.message.chat.id == os.getenv("CHAT_ID"):
    if update.channel_post.chat.id == int(os.getenv("CHAT_ID")):
        print("DA")
        # user_message = update.message.text
        user_message = update.channel_post.text
        if "миша" in user_message.lower():
            # await update.message.reply_text('Но я не Миша!')
            await update.channel_post.reply_text('Но я не Миша!')

def task2():
    application = ApplicationBuilder().token(os.getenv("TOKEN")).build()
    start_handler = MessageHandler(filters.TEXT, message_handler)
    application.add_handler(start_handler)
    application.run_polling()

if __name__ == '__main__':
    Send_to_zazerkalie()
    task2()
    task1()
