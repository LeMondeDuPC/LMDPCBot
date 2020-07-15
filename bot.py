import discord
from discord import Reaction, Member
from discord.ext import commands
from discord.ext.commands import has_permissions

import scrap

client = commands.Bot(command_prefix='!', case_insensitive=True)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')


@client.event
async def on_member_join(member: Member):
    await discord.utils.get(member.guild.channels, name="bienvenue").send_message("**Bienvenue <@" + member.id + "> !**")
    await member.add_roles(discord.utils.get(member.guild.roles, name="Abonné"))


@client.event
async def on_reaction_add(reaction: Reaction, user):
    member = reaction.message.author
    channel = reaction.message.channel
    if channel.id not in [729106157150535680, 483164509675061248] or reaction.emoji != '📰':
        return
    await member.add_roles(discord.utils.get(member.guild.roles, name="Abonné"))


@client.event
async def on_reaction_remove(reaction: Reaction, user):
    member = reaction.message.author
    channel = reaction.message.channel
    if channel.id not in [729106157150535680, 483164509675061248] or reaction.emoji != '📰':
        return
    await member.remove_roles(discord.utils.get(member.guild.roles, name="Abonné"))


@client.command()
async def search(ctx):
    pass


@client.command()
async def update(ctx):
    new_article = await scrap.get_new_articles()
    if new_article == "":
        await ctx.send(":x: **Il n'y a pas de nouvel article sur le site**")
        return
    await client.get_channel(731620991767150603).send("**:newspaper: Nouvel article:**\nhttps://www.lemondedupc.fr" + new_article)
    pass


@client.command()
@has_permissions(administrator=True)
async def updatesubscriberroles(ctx):
    message = await client.get_channel(729106157150535680).history().get()
    role = discord.utils.get(ctx.guild.roles, name="Abonné")
    added_roles = 0
    for reaction in message.reactions:
        if reaction.emoji in ["📰"]:
            for user in await reaction.users().flatten():
                added_roles += 1
                await user.add_roles(role)
    if added_roles > 0:
        await ctx.send(":white_check_mark: **" + str(added_roles) + " rôles ajoutés**")
    else:
        await ctx.send(":x: **Aucun rôle n'a été ajouté**")


client.run(open("TOKEN", "r").read())
