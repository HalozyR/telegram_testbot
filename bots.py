from telegram import Bot, Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, InlineQueryHandler

import logging
from os import getenv

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

application = ApplicationBuilder().token(getenv('TELEGRAM_BOT_TOKEN')).build()
conType = ContextTypes.DEFAULT_TYPE

async def start(update: Update, context: conType):
    await context.bot.send_message(
        chat_id = update.effective_chat.id,
        text="I'm a bot, please talk to me!"
    )

async def echo(update: Update, context: conType):
    print(update.message)
    date = (update.message.date).strftime("%d/%m/%Y %H:%M:%S")
    await context.bot.sendMessage(
        chat_id=update.effective_chat.id, 
        text=update.message.text
        )

async def caps(update: Update, context: conType):
    print(context.args)
    text_caps = ' '.join(context.args).upper()
    await context.bot.sendMessage(
        chat_id = update.effective_chat.id,
        text="Converting to caps"
        )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text_caps
        )

async def inline_caps(update: Update, context: conType):
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)

if __name__ == '__main__':

    echo_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    start_handler = CommandHandler('start', start)
    caps_handler = CommandHandler('caps',caps)
    inline_caps_handler = InlineQueryHandler(inline_caps)

    handlers_list = [
        caps_handler,
        start_handler,
        echo_handler,
        inline_caps_handler
    ]

    application.add_handlers(handlers_list)
    application.run_polling()

