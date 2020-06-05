#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import logging, telegram, json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import time, os                         # For Time and Timezone Support
os.environ['TZ'] = 'Asia/Shanghai'      # Timezone Name "Asia/Shanghai" "America/New_York"
time.tzset()                            # Set Timezone
import requests
import server_check_ip

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

original_ip = '0.0.0.0'

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def get_public_ip(update, context):
    update.message.reply_text(server_check_ip.main_public_ip())

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def callback_minute(context: telegram.ext.CallbackContext):
    ip_addr_json = json.load(open('/YOUR_PATH/current_ip.json'))
    current_ip = ip_addr_json['current_ip']
    global original_ip
    if current_ip != original_ip:
        context.bot.send_message(
                chat_id='YOUR_CHAT_ID', 
                text='IP Address Changed: \n{} -> {}'.format(original_ip, current_ip)
            )
        original_ip = current_ip

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("YOUR_TOKEN", use_context=True)
    j = updater.job_queue

    job_minute = j.run_repeating(callback_minute, interval=10, first=0)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("ip", get_public_ip))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()