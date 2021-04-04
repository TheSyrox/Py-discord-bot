import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'c!')

@client.event
async def on_ready():
  print ('Bot başarılı bir şekilde çalışmakta')

@client.command()
async def clsfull(ctx, amount =100000000000000):
 await ctx.channel.purge(limit=amount)
 await ctx.send('chat temizlendi efendim')

@client.command()
async def clear(ctx, amount =100):
 await ctx.channel.purge(limit=amount)
 await ctx.send('100 Mesaj silindi')

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send('Başarılı bir şekilde kullanıcı atıldı')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send('Başarılı bir şekilde kullanıcı banlandı')

@client.command()
async def unban(ctx, *,member):
  banned_users = await ctx.guild.bans()
  await ctx.send('Başarılı bir şekilde Unban uygulandı')
client.run('botun tokeni')
