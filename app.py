import discord
from discord import Member
from discord.ext import commands

import scrap

client = commands.Bot(command_prefix='!', case_insensitive=True)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')


@client.event
async def on_member_join(member: Member):
    await discord.utils.get(member.guild.channels, id=731611391135318017).send(
        f"**Bienvenue <@{member.id}> !**\n\n"
        f"Envoyez `!subscribe` dans {discord.utils.get(member.guild.channels, id=731611428498440193).mention} pour être notifié lors de la sortie de nouveaux articles"
    )
    role = discord.utils.get(member.guild.roles, name="Membre")
    print(role.id)
    await member.add_roles(role)


@client.command()
async def subscribe(ctx):
    print(f"Add role Abonné to {ctx.message.author.name}")
    await ctx.message.author.add_roles(discord.utils.get(ctx.guild.roles, name="Abonné"))
    await ctx.message.add_reaction("✅")


@client.command()
async def unsubscribe(ctx):
    print(f"Remove role Abonné of {ctx.message.author.name}")
    await ctx.message.author.add_roles(discord.utils.get(ctx.guild.roles, name="Abonné"))
    await ctx.message.add_reaction("✅")


@client.command()
async def update(ctx):
    new_article = await scrap.get_new_articles()
    if new_article == "":
        await ctx.send(":x: **Il n'y a pas de nouvel article sur le site**")
        return
    role = discord.utils.get(ctx.guild.roles, name="Abonné")
    await client.get_channel(731620991767150603).send(f"**{role.mention} :newspaper: Nouvel article:**\nhttps://www.lemondedupc.fr" + new_article)
    pass


client.run(open("TOKEN", "r").read())
