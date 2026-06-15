import random

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = "YOUR_BOT_TOKEN"

stats = {
    "ideas": 0,
    "motivations": 0,
    "money": 0
}

ideas = [
    "Создать Telegram-бота",
    "Сделать сайт-визитку",
    "Изучить новую тему Python",
    "Написать полезный скрипт",
    "Добавить проект на GitHub"
]

motivations = [
    "Каждый день понемногу лучше, чем ничего.",
    "Навык важнее мотивации.",
    "Большие результаты складываются из маленьких действий.",
    "Не сдавайся после первой ошибки.",
    "Сегодняшняя работа — завтрашние деньги."
]

money_ideas = [
    "Сделать Telegram-бота для магазина",
    "Создать бота-напоминалку на заказ",
    "Сделать бота для записи клиентов",
    "Настроить Telegram-бота для школьного проекта",
    "Создать бота с викторинами",
    "Продавать готовых ботов на биржах",
    "Писать простые Python-скрипты на заказ",
    "Создать бота для учёта расходов",
    "Делать парсеры сайтов на Python",
    "Создать свой полезный Telegram-сервис и монетизировать его"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        ["💡 Идея"],
        ["🔥 Мотивация"],
        ["📅 План"],
        ["💰 Идея заработка"],
        ["🎯 Цель"],
        ["📊 Статистика"]
    ]

    markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "Выбери действие:",
        reply_markup=markup
    )
    
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    if text == "💡 Идея":
        await idea(update, context)

    elif text == "🔥 Мотивация":
        await motivation(update, context)

    elif text == "💰 Идея заработка":
        await money(update, context)

    elif text == "📅 План":
        await plan(update, context)
        
    elif text == "🎯 Цель":
        await goal(update, context)
        
    elif text == "📊 Статистика":
        await stats_command(update, context)
        
async def idea(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    idea_text = random.choice(ideas)
    
    stats["ideas"] += 1
    
    await update.message.reply_text(idea_text)
    
async def motivation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    motivation_text = random.choice(motivations)
    
    stats["motivations"] += 1
    
    await update.message.reply_text(motivation_text)
    
async def plan(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
📅 План на сегодня

1. 1 час Python
2. 30 минут Telegram-бот
3. 30 минут английский
4. Сделать 1 мини-проект
"""

    await update.message.reply_text(text)
    
async def money(update: Update, context: ContextTypes.DEFAULT_TYPE):

    money_text = random.choice(money_ideas)
    
    stats["money"] += 1
    
    await update.message.reply_text(money_text)
    
async def goal(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🎯 Цель: заработать 100 000 ₽

План:
1. Изучать Python каждый день
2. Делать Telegram-ботов
3. Собрать портфолио
4. Найти первый заказ
5. Получать отзывы
"""

    await update.message.reply_text(text)

async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = f"""
📊 Статистика

Идей: {stats["ideas"]}
Мотиваций: {stats["motivations"]}
Идей заработка: {stats["money"]}
"""

    await update.message.reply_text(text)
        
app = Application.builder().token(TOKEN).build()    

app.add_handler(CommandHandler("stats", stats_command))
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("money", money))
app.add_handler(MessageHandler(filters.TEXT, menu))
app.add_handler(CommandHandler("plan", plan))    
app.add_handler(CommandHandler("idea", idea))    
app.add_handler(CommandHandler("motivation", motivation))
    
app.run_polling()
    