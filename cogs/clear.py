import discord
import asyncio
from discord.ext import commands

class clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1,15, commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, num: int = None, user: discord.Member = None):
      if num is None:
        await ctx.send("Please specify a certain number so I can delete it")
      else:
        if user:
            check_func = lambda msg: msg.author == user and not msg.pinned
        else:
            check_func = lambda msg: not msg.pinned

        await ctx.message.delete()
        await ctx.channel.purge(limit=num, check=check_func)

        if num < 2:
          embed2 = discord.Embed(title="", description=f"A message has been cleared from {ctx.channel.name}")
          await ctx.send(embed=embed2, delete_after=5)
          print(f"A message was deleted\nGuild: {ctx.guild.name}\nChannel: {ctx.channel.name}\nAuthor: {ctx.author.name}\n")
        else:
          embed = discord.Embed(title="", description=f"{num} messages have been cleared from {ctx.channel.name}")
          await ctx.send(embed=embed, delete_after=5)
          print(f"{num} messags have been deleted\nGuild: {ctx.guild.name}\nChannel: {ctx.channel.name}\nAuthor: {ctx.author.name}\n")
      


async def setup(bot):
  await bot.add_cog(clear(bot))