import discord
import asyncio
import datetime
from discord.ext import commands

class suggest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    @commands.cooldown(1,10, commands.BucketType.user)
    async def modmail(self, ctx, *, suggestion):
      channel = self.bot.get_channel(1170530685753237511)
      embed = discord.Embed(title=f"Suggestion from {ctx.author.name}", description=suggestion, color=discord.Color.blue())
      embed.set_footer(text=f"Suggestion created by {ctx.author} in {ctx.guild.name} through botQuestion Command")
      embed.timestamp = datetime.datetime.utcnow()
      message = await channel.send(embed=embed)
      await message.add_reaction("✅")
      await message.add_reaction("❌")
      await ctx.message.delete()
      await ctx.send(f"**:white_check_mark: | A message was successfully sent to {channel}**")
      embed2 = discord.Embed(title="Thank you for your suggestion!", description=f"Your suggestion: {suggestion}", color=discord.Color.blue())
      await ctx.author.send(embed=embed2)

    
    @commands.command()
    @commands.cooldown(1,10)
    async def suggest(self, ctx, *, suggestion):
      channel = discord.utils.get(ctx.guild.channels, name="suggestion-channel")
      if channel is None:
        guild = ctx.guild
        channel = await guild.create_text_channel('suggestion-channel')
        await ctx.send(f"**You dont have a channel called suggestion-channel so we added it for you**")
      channel = discord.utils.get(ctx.guild.channels, name="suggestion-channel")
      embed = discord.Embed(title=f"Suggestion from {ctx.author.name}", description=suggestion, color=discord.Color.blue())
      embed.set_footer(text=f"Suggestion created by {ctx.author} through Suggest Command")
      embed.timestamp = datetime.datetime.utcnow()
      message = await channel.send(embed=embed)
      await message.add_reaction("✅")
      await message.add_reaction("❌")
      await ctx.message.delete()
      await ctx.send(f"**:white_check_mark: | A message was successfully sent to {channel}**")
      embed2 = discord.Embed(title="Thank you for your suggestion!", description=f"Your suggestion: {suggestion}", color=discord.Color.blue())
      await ctx.author.send(embed=embed2)

async def setup(bot):
  await bot.add_cog(suggest(bot))