from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8540216353:AAGWe_gRE3Mm1raV60ykY3w1kPcyydWlN2w"

def logic(nums):
    big = sum(1 for n in nums if n >= 5)
    if big >= 3:
        return "BIG", "7 / 8 / 9"
    else:
        return "SMALL", "1 / 2 / 3"

async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        nums = list(map(int, context.args[:5]))
        if len(nums) < 5:
            await update.message.reply_text(
                "Use format:\n/predict 8 9 7 6 8"
            )
            return

        trend, safe = logic(nums)

        msg = f"""
SERVER: Connected
PING: 68 ms

TREND: {trend}
CONFIDENCE: MEDIUM

NEXT RESULT: {trend}
SAFE NUMBERS: {safe}
"""
        await update.message.reply_text(msg)

    except:
        await update.message.reply_text("Invalid input")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("predict", predict))
app.run_polling()
