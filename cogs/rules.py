import discord
from discord.ext import commands 

class rules(commands.Cog):
  def __init__(self, bot):
      self.bot = bot 

  @commands.command()
  async def rules(self, ctx, *, rules = None):
    if rules == None:
      await ctx.send("Please put in the rules for your server!")
    else:
      embed = discord.Embed(title=f"Server Rules", description=rules, color=discord.Color.blue())
      await ctx.send(embed=embed)

async def setup(bot):
  await bot.add_cog(rules(bot))