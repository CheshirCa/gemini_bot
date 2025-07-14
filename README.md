**Инструкция по установке и запуску Telegram-бота с Gemini AI (Русский / English)**  

---

### **🇷🇺 Русская версия**  

#### **1. Установка необходимых компонентов**  
Перед началом убедитесь, что у вас установлены:  
- **Python 3.10 или новее** (скачать: [python.org](https://www.python.org/downloads/))  
- **Менеджер пакетов pip** (обычно идет с Python)  

#### **2. Установка зависимостей**  
Откройте терминал (CMD/PowerShell на Windows, Terminal на macOS/Linux) и выполните:  
```bash
pip install python-telegram-bot google-generativeai python-dotenv
```  

#### **3. Получение API-ключей**  
- **Telegram Bot Token**:  
  - Откройте Telegram, найдите **@BotFather**.  
  - Создайте бота командой `/newbot`.  
  - Скопируйте выданный токен (например, `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`).  

- **Google Gemini API Key**:  
  - Перейдите в [Google AI Studio](https://aistudio.google.com/app/apikey).  
  - Создайте новый API-ключ.  

#### **4. Настройка бота**  
Создайте файл `.env` в папке с ботом и добавьте:  
```
TELEGRAM_BOT_TOKEN=ваш_токен_бота  
GEMINI_API_KEY=ваш_gemini_api_ключ
TARGET_CHAT_IDS=-1001234567890,-1000987654321  # ID чатов через запятую  
TRIGGER=ИИ запрос:  # Триггерное слово  
```  
или напрямую укажите в тексте скрипта указанные значения:
```
GEMINI_API_KEY = "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"  # Получить тут: https://aistudio.google.com/app/apikey
TELEGRAM_BOT_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Токен бота от @BotFather
TARGET_CHAT_IDS = [-1001234567890, -1000987654321]  # Список ID чатов/каналов
TRIGGER = "ИИ запрос:" # Триггерное слово  
MODEL_NAME = "gemini-1.5-flash" # Модель ИИ
MAX_PROMPT_LENGTH = 1000  # Максимальная длина промта
```

#### **5. Запуск бота**  
Сохраните код бота в файл `bot.py` и запустите:  
```bash
python bot.py
```  
Бот начнет работать и отвечать на сообщения с триггером.  

#### **6. Как пользоваться**  
- В любом чате из `TARGET_CHAT_IDS` напишите:  
  ```  
  ИИ запрос: Напиши рецепт пасты  
  ```  
- Бот ответит сгенерированным текстом.  

---

### **🇬🇧 English Version**  

#### **1. Install Required Components**  
Ensure you have:  
- **Python 3.10+** (download: [python.org](https://www.python.org/downloads/))  
- **pip package manager** (comes with Python)  

#### **2. Install Dependencies**  
Run in terminal (CMD/PowerShell on Windows, Terminal on macOS/Linux):  
```bash
pip install python-telegram-bot google-generativeai python-dotenv
```  

#### **3. Get API Keys**  
- **Telegram Bot Token**:  
  - Open Telegram, find **@BotFather**.  
  - Create a bot with `/newbot`.  
  - Copy the token (e.g., `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`).  

- **Google Gemini API Key**:  
  - Go to [Google AI Studio](https://aistudio.google.com/app/apikey).  
  - Create a new API key.  

#### **4. Configure the Bot**  
Create a `.env` file in the bot folder and add:  
```
TELEGRAM_BOT_TOKEN=your_bot_token  
GEMINI_API_KEY=your_gemini_api_key  
TARGET_CHAT_IDS=-1001234567890,-1000987654321  # Chat IDs separated by commas  
TRIGGER=AI query:  # Trigger phrase  
```  

#### **5. Run the Bot**  
Save the bot code as `bot.py` and run:  
```bash
python bot.py
```  
The bot will start and respond to messages with the trigger.  

#### **6. How to Use**  
- In any chat from `TARGET_CHAT_IDS`, send:  
  ```  
  AI query: Write a pasta recipe  
  ```  
- The bot will reply with generated text.  

---

### **🛠 Troubleshooting (Общие проблемы)**  
- **VPN Required?** If you see `400 User location not supported`, use a VPN (USA/Germany).  
- **Bot Not Responding?** Check `.env` file and API keys.  
- **Logs**: Run `python bot.py` and check the terminal for errors.  

Готово! Теперь у вас работает Telegram-бот с Gemini AI. / Done! Your Telegram bot with Gemini AI is ready. 🚀
