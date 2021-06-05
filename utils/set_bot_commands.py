from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Start bot🛫"),
            types.BotCommand("help", "Get help💁"),
            types.BotCommand("menu", "Get menu🛍"),
            types.BotCommand("test", "Start testing🤯"),
            types.BotCommand("products", "Ger products list🛒")
        ]
    )
