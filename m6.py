import discord, os
from discord.ext import commands
from random import choice
from time import sleep   

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='eco_', intents=intents)

info_bot = ["1. advice - советы",
            "2. problem - сайты, с решением проблем"]

advice_bot = [
    "Не выбрасывайте мусор и окурки на землю - да, их все равно уберет дворник, но если у дворников будет меньше работы, убирать улицы смогут меньше дворников, следовательно меньше потенциальных дворников приедут в мой большой город!",
    "Если вы здоровы, молоды и живете на низком этаже, чаще пользуйтесь лестницей - полезно для фигуры и экологии, так как экономит энергию, которую использует лифт",
    "Не используйте спреи или покупайте только, те, на которых есть маркировка «Ozone friendly». Альтернатива - шариковые и твердые дезодоранты, а освежать воздух в туалете поможет вентиляция и саше с вашими любимыми ароматами",
    "Маркировка 'Лента Мёбиуса' означает, что упаковка изготовлена из вторсырья - покупая товары в этой упаковке, вы поддержите экологически-сознательных производителей",
    "Замените лампочки в доме на энергосберегающие - но не забывайте их утилизировать, так как в таких лампах используется ртуть! Кстати, компания IKEA принимает такие лампы к утилизации",
    "Сделай compost для органических отходов – ты получишь питательное удобрение для растений",
    "Путешествуй с reusable набором столовых приборов, чтобы не использовать одноразовые пластиковые вилки и ложки",
    "Выбирай продукты с минимальной упаковкой – меньше пластика, больше экологии",
    "Забудь о пластиковых пакетах – всегда носи с собой reusable сумку для покупок",
    "Переходи на reusable пластиковые бутылки вместо одноразовых пластиковых бутылок"
]

problem_bot = [
    "https://bakertilly.ua/ru/id38401/",
    "https://www.kp.ru/family/ecology/ehkologicheskie-problemy/ ",
    "https://www.nur.kz/family/school/1940627-ekologiya-problemy-mirovogo-masshtaba-kotorye-s-ney-svyazany/",
    "https://rg.ru/2023/11/29/globalnye-ekologicheskie-problemy-chelovechestva-kotorye-uzhe-nelzia-ignorirovat.html"
]

@bot.command()
async def info(ctx):
    for i in info_bot:
        await ctx.send(i)
        sleep(0.5)

@bot.command()
async def advice(ctx):
    await ctx.send(choice(advice_bot))

@bot.command()
async def problem(ctx):
    await ctx.send(choice(problem_bot))


bot.run("")