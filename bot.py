from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = "8422877792:AAFO6QMz4qLAQ6rukaFixUBLBE UWY4c2Hs4"


async def start(update: Update, context):
    await update.message.reply_text("机器人启动成功")


async def reply(update: Update, context):
    await update.message.reply_text(
        "你说：" + update.message.text
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(
    MessageHandler(filters.TEXT, reply)
)

app.run_polling()
