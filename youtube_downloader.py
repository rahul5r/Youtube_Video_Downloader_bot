import threading
import os
from pytube import YouTube
from telegram import Update, ChatAction, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler, CallbackQueryHandler

# Set up the bot token
TOKEN = '5884816644:AAGDp597Fz9XAdFqIBRYmjwVsEjG0zA_M6E'

# Create an Updater object
updater = Updater(TOKEN)

# Define a message handler for handling all incoming messages
def handle_message(update: Update, context: CallbackContext):
    # Get the text message sent by the user
    message_text = update.message.text

    # Ask the user to select the video quality
    keyboard = [
        [
            InlineKeyboardButton("Low Quality (144p)", callback_data='144'),
            InlineKeyboardButton("Medium Quality (360p)", callback_data='360'),
            InlineKeyboardButton("High Quality (720p)", callback_data='720')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Please select the video quality:", reply_markup=reply_markup)

    # Store the message text and user ID for later use in the callback function
    context.user_data['message_text'] = message_text
    context.user_data['user_id'] = update.effective_chat.id

# Function to download a YouTube video
def download_video(update: Update, context: CallbackContext, url, quality):
    try:
        # Create a YouTube object
        video = YouTube(url)

        # Get the selected resolution stream
        stream = video.streams.filter(res=f"{quality}p").first()

        # Send "Downloading" message
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.UPLOAD_VIDEO)

        # Download the video
        video_path = stream.download()

        # Send the downloaded video to the user's chat as a file
        context.bot.send_document(chat_id=update.effective_chat.id, document=open(video_path, 'rb'))

        # Delete the downloaded video file
        os.remove(video_path)
    except Exception as e:
        # Send an error message if the video cannot be downloaded
        error_message = "This is not a valid YouTube video link. Please send a valid YouTube link."
        update.message.reply_text(error_message)

# Command handler for "/start" command
def start_command(update: Update, context: CallbackContext):
    start_message = "The bot has been started."
    update.message.reply_text(start_message)

# Command handler for "/help" command
def help_command(update: Update, context: CallbackContext):
    help_message = "This is a YouTube video downloader bot. It downloads YouTube videos based on the provided link. Just send a valid YouTube link and the video will be downloaded."
    update.message.reply_text(help_message)

# Callback handler for handling the video quality selection
def video_quality_callback(update: Update, context: CallbackContext):
    # Get the selected quality from the callback data
    selected_quality = update.callback_query.data

    # Get the stored message text and user ID
    message_text = context.user_data['message_text']
    user_id = context.user_data['user_id']

    # Start downloading the video with the selected quality
    download_thread = threading.Thread(target=download_video, args=(update, context, message_text, selected_quality))
    download_thread.start()

    # Send a "Downloading" message to the user
    context.bot.send_message(chat_id=user_id, text="Downloading the video...")

# Register the message handler
updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), handle_message))

# Register the command handlers
updater.dispatcher.add_handler(CommandHandler("start", start_command))
updater.dispatcher.add_handler(CommandHandler("help", help_command))

# Register the callback handler for video quality selection
updater.dispatcher.add_handler(CallbackQueryHandler(video_quality_callback))

# Start the bot and display "Bot Started" message
def start_bot():
    print("Bot Started")
    updater.start_polling()
    updater.idle()

start_bot()