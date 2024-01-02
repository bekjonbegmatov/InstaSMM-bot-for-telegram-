import asyncio
from aiogram import Bot, Dispatcher
from handlers import command_heandler , admin_commands, servises_command
# Importing API tocen of bot from ./config.py 
from config import TOKEN 

# Запуск бота
async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_routers(
        admin_commands.router,
        command_heandler.router,
        servises_command.router,
        )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())