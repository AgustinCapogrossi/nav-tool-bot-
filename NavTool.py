import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from modules.Gpt import ask
from modules.resources import Resources
from modules.embed import D_Embeds
import numpy as np
import calendar

load_dotenv()

NAVTOOL_PROJECT_TOKEN = os.getenv("NAVTOOL_PROJECT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents, help_command=None)
resource = Resources()
embeds = D_Embeds()
cal = calendar.Calendar()

### Commands


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


### Help


@bot.command()
async def help(ctx):
    em = discord.Embed(
        color=discord.Color.from_rgb(0, 255, 0),
        title="Ayuda",
        description="$question [prompt]: Realiza una consulta a la IA\n $code [prompt]: Realiza una petición de código a la IA\n $resource_add [resource_name] [resource_value]: Agrega un recurso a tu lista de recursos.\n $resource_drop: Elimina tu lista de recursos.\n $resource_delete [resource_name]: Elimina un recurso de tu lista de recursos.\n $resource_list: Lista tus recursos.\n $resource_find [resource_name]: Encuentra uno de tus recursos en tu lista.\n",
    )
    await ctx.send(embed=em)


### IA


@bot.command()
async def question(ctx, arg):
    await ctx.send("Por favor espere mientras se procesa su consulta")
    response = ask(arg)
    await ctx.send(response)


@bot.command()
async def code(ctx, prompt):
    await ctx.send("Por favor espere mientras se procesa su consulta")
    pr_result = ask(prompt)
    response = "``` {} ```".format(pr_result)
    await ctx.send(response)


### Resources


@bot.command()
async def resource_add(ctx, resource_name, resource_value):
    user = ctx.author.id
    resource.add(user, resource_name, resource_value)
    await ctx.send(embed=embeds.pass_embed("Recurso añadido correctamente"))


@bot.command()
async def resource_drop(ctx):
    try:
        user = ctx.author.id
        resource.drop(user)
        em = embeds.pass_embed("La lista de recursos fue eliminada correctamente")
    except:
        em = embeds.fail_embed("El archivo ya ha sido eliminado o no existe.")
    await ctx.send(embed=em)


@bot.command()
async def resource_delete(ctx, resource_name):
    data = {}
    try:
        user = ctx.author.id
        resource.delete(user, data, resource_name)
        data = {}
        em = embeds.pass_embed("Se ha eliminado la entrada correctamente")
    except:
        em = embeds.fail_embed(
            "La entrada que desea encontrar no existe, verifique los elementos existentes con $resource_list."
        )
    await ctx.send(embed=em)


@bot.command()
async def resource_find(ctx, resource_name):
    data = {}
    try:
        user = ctx.author.id
        em = resource.find(user, data, resource_name)
    except:
        em = embeds.fail_embed(
            "La entrada que desea encontrar no existe, verifique los elementos existentes con $resource_list."
        )
    await ctx.send(embed=em)


@bot.command()
async def resource_list(ctx):
    data = {}
    try:
        user = ctx.author.id
        response = resource.list(user, data)
        em = embeds.pass_embed(response)
        data = {}
    except:
        em = embeds.fail_embed(
            "El archivo no existe, intente añadir un recurso utilizando $resource_add antes de empezar."
        )
    await ctx.send(embed=em)


"""
@bot.command()
async def resource_list_other(ctx, username: discord.User):
    data = {}
    try:
        user = username.id
        response = resource.list(user, data)
        em = embeds.pass_embed(response)
        data = {}
    except:
        em = embeds.fail_embed(
            "El archivo no existe, intente añadir un recurso utilizando $resource_add antes de empezar."
        )
    await ctx.send(embed=em)
"""

### Schedule


@bot.command()
async def schedule_dump(ctx, year: int, month: int):
    response = np.zeros((5, 7))
    calendar_iter = cal.itermonthdays(year, month)

    suma = 0
    for i in response:
        for j in i:
            suma += 1
    row = 0
    column = 0
    for i in calendar_iter:
        response[row][column] = i
        column += 1
        if column >= 7:
            row += 1
            column = 0
    print(response)
    em = embeds.pass_embed(response)
    await ctx.send(embed=em)


bot.run(NAVTOOL_PROJECT_TOKEN)
