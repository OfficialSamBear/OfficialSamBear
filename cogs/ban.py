import discord
import asyncio
import datetime
from discord.ext import commands

class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.Member, *, reason="None was provided"):
        role = discord.utils.get(ctx.guild.roles, name="Mod Utilities")
        if member.top_role.position > ctx.author.top_role.position:
          return await ctx.send(f":x: **You cant do that silly, {member.name} is higher than you**")
        elif member.top_role.position > role.position:
          return await ctx.send(f"**:x: i need to be above {member.name}\'s top role**")
        else:
          print(f"{member.name} was banned from {ctx.guild.name}\nReason: {reason}\nAuthor: {ctx.author.name}\n")
          embed = discord.Embed(title=f"Success!", description=f":white_check_mark: | {member.name} was banned for\n\nReason: `{reason}`", color=discord.Color.red())
          embed.timestamp = datetime.datetime.utcnow()
          await ctx.send(embed=embed)
          embed2 = discord.Embed(title="Banned!", description=f"You have been banned from {member.guild.name}!!\n\nReason: `{reason}`", color=discord.Color.red())
          embed2.timestamp = datetime.datetime.utcnow()
          await member.send(embed=embed2)
          await member.ban(reason = reason)


async def setup(bot):
  await bot.add_cog(ban(bot))