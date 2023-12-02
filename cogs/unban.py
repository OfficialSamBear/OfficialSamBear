import discord
import asyncio
import datetime
from discord.ext import commands

class unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
      banned_users = await ctx.guild.bans()
      member_name, member_discriminator = member.split('#')

      for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
          await ctx.guild.unban(user)
          embed = discord.Embed(title="Success!", description=f":white_check_mark: | {user.name} has been unbanned from the {ctx.guild.name}!", color=discord.Color.green())
          embed.timestamp = datetime.datetime.utcnow()
          await ctx.send(embed=embed)
          '''embed = discord.Embed(title="ATTENTION!!", description=f"You have been unbanned from {ctx.guild.name}!", color=discord.Color.green())
          await member.send(embed=embed)'''
          print(f"A member was unbanned from {ctx.guild.name}\nAuthor: {ctx.author.name}\n")
          return


async def setup(bot):
  await bot.add_cog(unban(bot))