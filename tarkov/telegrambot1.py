import pyautogui
import telegram
from telegram.ext import Updater, CommandHandler
import time

notification_list = []

def is_image_on_screen():
    try:
        position = pyautogui.locateOnScreen('./imgs/start_game.png', confidence=0.5)
        if position is not None:
            return True
        else:
            return False
    except Exception as e:
        print("Error occurred:", e)
        return False





# Telegram bot token
TOKEN = '6076055331:AAEPdQU7i0FnZymQPSoaVdKGEysa_QkP0-4'

# Create an instance of the Telegram Bot
bot = telegram.Bot(token=TOKEN)

# Function to send a message to a specific user
def send_message_to_user(chat_id, text):
    bot.send_message(chat_id=chat_id, text=text)

# Function to send a message to all connected users
def send_message_to_users(text):
    for chat_id in notification_list:
        send_message_to_user(chat_id, text)

# Function to add a user to the notification list
def add_user_to_notification_list(update, context):
    chat_id = update.effective_chat.id
    if chat_id not in notification_list:
        notification_list.append(chat_id)
        send_message_to_user(chat_id, "You have been added to the notification list.")
    else:
        send_message_to_user(chat_id, "You are already in the notification list.")

# Function to check the image status and send messages if needed
def check_image_status(context):
    if is_image_on_screen():
        # Send a message to all connected users
        send_message_to_users("The image is on the screen!")
        exit()

# Create an updater object and attach it to the Telegram bot
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Register the /start command handler
start_handler = CommandHandler('start', add_user_to_notification_list)
dispatcher.add_handler(start_handler)

# Start the updater
updater.start_polling()

# Schedule the check_image_status function to run every second
job_queue = updater.job_queue
job_queue.run_repeating(check_image_status, interval=2, first=0)

# Keep the bot running until interrupted
updater.idle()
