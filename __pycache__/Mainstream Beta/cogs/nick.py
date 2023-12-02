import discord
from discord.ext import commands


class nick(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  @commands.command()
  @commands.cooldown(1,15, commands.BucketType.user)
  @commands.has_permissions(manage_nicknames=True)
  async def nick(self, ctx, member: discord.Member, *, nick):
    if member is ctx.guild.owner:
      await ctx.send("I can not nickname the owner of the server")
    else:
      await member.edit(nick=nick)
      embed = discord.Embed(title="Success!", description=f"**{member.name}\'s** nickname has been set to `{nick}`", color=discord.Color.green())
      embed2 = discord.Embed(title="Success!", description=f"Your nickname has been set to `{nick}` in {ctx.guild.name}", color=discord.Color.green())
      await ctx.send(embed=embed)
      await member.send(embed=embed2)

  @commands.command()
  @commands.cooldown(1,15, commands.BucketType.user)
  @commands.has_permissions(manage_nicknames=True)
  async def reset_nick(self, ctx, member: discord.Member):
    if member is ctx.guild.owner:
      await ctx.send("I can not nickname the owner of the server")
    else:
      await member.edit(nick=ctx.member.name)
      await ctx.send(f"{member.name}\'s nickname has been reset")



async def setup(bot):
  await bot.add_cog(nick(bot))