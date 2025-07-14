import os
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import google.generativeai as genai
from google.api_core import exceptions as google_exceptions

# Конфигурация (лучше через переменные окружения)
#GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # Получить тут: https://aistudio.google.com/app/apikey
#TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Токен бота от @BotFather
GEMINI_API_KEY = "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"  # Получить тут: https://aistudio.google.com/app/apikey
TELEGRAM_BOT_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Токен бота от @BotFather
#TARGET_CHAT_IDS = list(map(int, os.getenv("TARGET_CHAT_IDS", "").split(",")))  # Список ID через запятую
TARGET_CHAT_IDS = [-1001234567890, -1000987654321]  # Список ID чатов/каналов
#TRIGGER = os.getenv("TRIGGER", "ИИ запрос:")
TRIGGER = "ИИ запрос:"
#MODEL_NAME = os.getenv("MODEL_NAME", "gemini-1.5-flash")
MODEL_NAME = "gemini-1.5-flash"
MAX_PROMPT_LENGTH = 1000  # Максимальная длина промта



# Настройка логов
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Инициализация Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(MODEL_NAME)

async def handle_all_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Определяем тип сообщения
        if update.message:
            message = update.message
            chat = update.effective_chat
        elif update.channel_post:
            message = update.channel_post
            chat = update.channel_post.chat
        else:
            return

        # Проверка чата
        if chat.id not in TARGET_CHAT_IDS:
            logger.warning(f"Ignoring chat {chat.id} (not in allowed list)")
            return

        # Проверка текста
        if not message.text:
            logger.warning("No text in message")
            return

        logger.info(f"Received in {chat.type} {chat.id}: {message.text}")

        # Проверка триггера (без учета регистра)
        if not message.text.lower().startswith(TRIGGER.lower()):
            logger.warning("Trigger not found")
            return

        prompt = message.text[len(TRIGGER):].strip()
        
        # Проверка длины промта
        if len(prompt) > MAX_PROMPT_LENGTH:
            await message.reply_text(f"⚠️ Запрос слишком длинный (максимум {MAX_PROMPT_LENGTH} символов)")
            return
            
        logger.info(f"Processing request: {prompt}")

        # Индикатор печати (не работает в каналах)
        if chat.type != "channel":
            await context.bot.send_chat_action(chat_id=chat.id, action="typing")

        try:
            # Запрос к Gemini с таймаутом
            response = await model.generate_content_async(
                prompt,
                request_options={"timeout": 30}
            )
            answer = response.text
            
            # Форматирование ответа
            reply = (
                f"🔍 <b>Ответ на запрос:</b>\n\n"
                f"{answer}\n\n"
                f"<i>⚠️ Ответ сгенерирован ИИ ({MODEL_NAME})</i>"
            )
            
            # Отправка ответа с Markdown
            await message.reply_text(reply, parse_mode="HTML")
            
        except google_exceptions.DeadlineExceeded:
            await message.reply_text("⌛ Время ожидания ответа истекло. Попробуйте позже.")
        except google_exceptions.ResourceExhausted:
            await message.reply_text("⚠️ Достигнут лимит запросов. Попробуйте позже.")
        except Exception as e:
            await message.reply_text(f"⚠️ Ошибка при обработке запроса: {str(e)}")
            raise

    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)
        if 'message' in locals():
            await message.reply_text("⚠️ Произошла внутренняя ошибка. Пожалуйста, попробуйте позже.")

def main():
    # Проверка конфигурации
    if not all([GEMINI_API_KEY, TELEGRAM_BOT_TOKEN, TARGET_CHAT_IDS]):
        raise ValueError("Missing required configuration!")
        
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Обработчик для всех типов сообщений
    app.add_handler(MessageHandler(
        filters.Chat(chat_id=TARGET_CHAT_IDS) &
        filters.TEXT &
        (~filters.COMMAND) &
        (filters.UpdateType.MESSAGE | filters.UpdateType.CHANNEL_POST),
        handle_all_messages
    ))

    logger.info(f"Bot started in universal mode (groups + channels) with model {MODEL_NAME}")
    app.run_polling()

if __name__ == "__main__":
    main()
