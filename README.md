# YouTube Video Downloader Bot

## Introduction

This is a simple Telegram bot built in Python using the `pytube` library to download YouTube videos based on user-provided links. The bot allows users to select the desired video quality and then downloads and sends the video as a file.

## Setup

1. Install the required libraries:

   ```bash
   pip install pytube python-telegram-bot
   ```

2. Set up your Telegram bot:

   - Create a new bot on Telegram using the BotFather.
   - Obtain the bot token.

3. Update the script:

   - Replace the placeholder in the `TOKEN` variable with your Telegram bot token.

   ```python
   TOKEN = 'your-telegram-bot-token'
   ```

   Ensure your bot token is kept confidential and not shared publicly.

4. Run the script:

   ```bash
   python your_script_name.py
   ```

   This will start the bot, and you can interact with it on Telegram.

## Usage

1. Start the bot by sending the "/start" command.

2. Send a valid YouTube link to the bot.

3. The bot will prompt you to select the video quality.

4. Choose the desired quality using the provided inline keyboard.

5. The bot will start downloading the video and send it to your Telegram chat.

## Commands

- `/start`: Start the bot and receive a welcome message.
- `/help`: Get information about how to use the bot.

## Screenshots

Include screenshots of the bot in action, showing the interaction with users, and the downloaded videos.

## Notes

- The bot uses the `pytube` library to interact with YouTube. Ensure the library is up to date.
- This bot is a simple example and may have limitations or dependencies that need further consideration in a production environment.
