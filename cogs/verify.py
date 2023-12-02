import discord
from discord.ext import commands

class verify(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def sendvm(self, ctx, *, command=None):
    if command is None:
      embed = discord.Embed(title="Welcome New Members!", description=f"Hello! We Warmly Welcome You into {ctx.guild.name}\'s Server. Please Type `m.verify` Here To Get Verified and Engage With The Community!", color=discord.Color.green())
      embed.set_footer(text="Verification Module")
      embed.set_author(name=f"{ctx.guild.name}")
      await ctx.send(embed=embed)
    else:
      embed = discord.Embed(title="Welcome New Members!", description=f"Hello! We Warmly Welcome You into {ctx.guild.name}\'s Server. Please Type `{command}` Here To Get Verified and Engage With The Community!", color=discord.Color.green())
      embed.set_footer(text="Verification Module")
      embed.set_author(name=f"{ctx.guild.name}")
      await ctx.send(embed=embed)
  
  @commands.command()
  async def verify(self, ctx):
    memRole = discord.utils.get(ctx.guild.roles, name="Member")
    unvRole = discord.utils.get(ctx.guild.roles, name="Unverified")
    if memRole is None:
      await ctx.send("**Please create a role called `Member` and put it below my role!**")
    if unvRole is None:
      await ctx.send("**Please create a role called `Unverified` and put it below my role!**")
    if unvRole in ctx.author.roles:
      await ctx.author.remove_roles(unvRole)
      await ctx.author.add_roles(memRole)
      await ctx.message.delete()
      await ctx.author.send(f"Thank you for verifying in {ctx.guild.name}. I hope you have a great day!")
    else:
      await ctx.send(f"You need to have `{unvRole}` in order to use this command")

async def setup(bot):
  await bot.add_cog(verify(bot))