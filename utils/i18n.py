import locale

def get_system_lang() -> str:
    try:
        lang, _ = locale.getdefaultlocale()
        if lang and lang.startswith("ru"):
            return "ru"
    except Exception:
        pass
    return "en"

LANG = get_system_lang()

MESSAGES = {
    "ru": {
        "bot_working": "🟢 Бот работает",
        "bot_stopped": "🔴 Бот остановлен",
        "target": "Цель: {}",
        "stop": "ОСТАНОВИТЬ 🛑",
        "init": "Инициализация...",
        "wait_vortex": "Ожидание окна Vortex...",
        "wait_web": "Ожидание вкладки...",
        "click_vortex": "Нажатие кнопки загрузки Vortex",
        "click_continue": "Нажатие кнопки Continue (ошибка)",
        "click_web": "Нажатие {}",
        "downloading": "Скачивание... ({} сек)",
        "close_tab": "Закрытие вкладки...",
        "stall_vortex": "Пробуем сфокусировать Vortex...",
        "1h_timeout": "Бот простаивает более 1 часа! Загрузки завершены или Вортекс завис.\nВремя остановки: {}",
        "stop_title": "NexusAutoDL - Остановка",
        "stopped_by_user": "Остановлен пользователем из интерфейса.",
    },
    "en": {
        "bot_working": "🟢 Bot is running",
        "bot_stopped": "🔴 Bot stopped",
        "target": "Target: {}",
        "stop": "STOP 🛑",
        "init": "Initializing...",
        "wait_vortex": "Waiting for Vortex window...",
        "wait_web": "Waiting for web tab...",
        "click_vortex": "Clicking Vortex download button",
        "click_continue": "Clicking Continue button (Error)",
        "click_web": "Clicking {}",
        "downloading": "Downloading... ({}s)",
        "close_tab": "Closing tab...",
        "stall_vortex": "Trying to focus Vortex...",
        "1h_timeout": "Bot has been idle for over 1 hour! Downloads finished or Vortex hung.\nStop time: {}",
        "stop_title": "NexusAutoDL - Stopped",
        "stopped_by_user": "Stopped by user from GUI.",
    }
}

def _(key: str, *args) -> str:
    text = MESSAGES.get(LANG, MESSAGES["en"]).get(key, MESSAGES["en"].get(key, key))
    if args:
        return text.format(*args)
    return text
