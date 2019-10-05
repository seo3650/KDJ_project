#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""KDJ_notification Bot to reply to Telegram messages.

"""
import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep


update_id = None


def main():
    """Run the bot."""
    global update_id
    # Telegram Bot Authorization Token
    bot = telegram.Bot('982782338:AAHKjHSLHUawMesQHFgs9zcOHXo-V1sdLeg')

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    signal = True # send notification?

    # bot send notification to latest person
    chat_id = 677916148

    contents = "test notification"
    bot.sendMessage(chat_id=chat_id, text="Hello! I am KAIST message delivering service")
    bot.sendMessage(chat_id=chat_id, text="I support 3 category: marketing, loss, love")
    bot.sendMessage(chat_id=chat_id, text="You can set category that you want to receive using keyword: !set")
    bot.sendMessage(chat_id=chat_id, text="ex) !set loss")

    while True:
        try:
            category_option = set_option(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1
        if signal:
            print(contents)
            bot.sendMessage(chat_id=chat_id, text=contents)


def set_option(bot):
    """Echo the message the user sent."""
    global update_id
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1
        if update.message:  # your bot can receive updates without messages
            # Reply to the message
            print(update)
            message = update.message.text.lower()
            print(message)
            if message == "!set marketing":
                update.message.reply_text("Ok I'll send information about marketing")
                return "marketing"
            elif message == "!set love":
                update.message.reply_text("Ok I'll send information about love")
                return "love"
            elif message == "!set loss":
                update.message.reply_text("Ok I'll send information about loss")
                return "loss"
            else:
                update.message.reply_text("I can't understand your message!")


if __name__ == '__main__':
    main()
