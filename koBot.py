import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def muppets(update, context):
    """Send a message when the command /muppet is issued."""
    update.message.reply_text('You are all fucking muppets.')

def commies(update, context):
    """Send a message when the command /commies is issued."""
    update.message.reply_text('Death to the commies.')

def rekt(update, context):
    """Send a message when the command /commies is issued."""
    update.message.reply_text('*sigh*\nTo be fair, you need to have a very high IQ to understand $ATOM. Its future applications are extremely subtle, and without a solid grasp of IBC and the world of possibilities it unlocks most of its value propositions will go over a typical investor’s head. There’s also Gravity Dex and Gravity Bridge, which will simply revolutionize the space.\nThe ATOM holders understand this stuff; they have the intellectual capacity to truly appreciate the depths of this token, to realise that it is not just speculation - it says something deep about LIFE. As a consequence, people who dislike Cosmos truly ARE idiots- of course they wouldn’t appreciate, for instance, the brilliance in having such a high staking rate. I’m smirking right now just imagining one of those addlepated simpletons scratching their heads in confusion as our devs’ genius wit unfolds itself on their computer screens. What fools.. how I pity them. 😂\nAnd yes, by the way, I DO have a Cosmos tattoo. And no, you cannot see it. It’s for the ladies’ eyes only- and even then they have to demonstrate that they’re within 5 IQ points of my own (preferably lower) beforehand. Nothin personnel kid 😎')

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(""
, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("muppets", muppets))

    dp.add_handler(CommandHandler("commies", commies))

    dp.add_handler(CommandHandler("rekt", rekt))

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