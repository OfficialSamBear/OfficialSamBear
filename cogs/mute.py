import discord
from discord.ext import commands
import datetime
import humanfriendly

class mute(commands.Cog):
  def __init__(self, bot):
      self.bot = bot 
#pip install -U git+https://github.com/discord/discord.git#master 
  @commands.command()
  @commands.has_permissions(manage_roles=True)
  async def mute(self, ctx, member: discord.Member, time=None, *, reason="None was provided"):
    if time == None:
      await ctx.send("Please provide a time")
    role = discord.utils.get(ctx.guild.roles, name="Mod Utilities")
    if member.top_role.position > ctx.author.top_role.position:
      return await ctx.send(f":x: **You cant do that silly, {member.name} is higher than you**")
    elif member.top_role.position > role.position:
      return await ctx.send(f"**:x: i need to be above {member.name}\'s top role**")
    else:
      time = humanfriendly.parse_timespan(time)
      await member.edit(timeout=discord.utils.utcnow() + datetime.timedelta(seconds=time))
      embed = discord.Embed(title="Muted", description=f"{member.mention} as been muted for {reason}", color=discord.Color.red())
      await ctx.send(embed = embed)
      embed2 = discord.Embed(title="Muted", description=f"You as been muted for {reason} in {ctx.guild.name}", color=discord.Color.red())
      await member.send(embed = embed2)

  @commands.command()
  @commands.has_permissions(manage_roles=True)
  async def unmute(self, ctx, member: discord.Member):
    await member.edit(timeout=None)
    embed = discord.Embed(title="Unmuted", description=f"{member.mention} as been unmuted", color=discord.Color.green())
    await ctx.send(embed = embed)
    embed2 = discord.Embed(title="Unmuted", description=f"You as been unmuted in {ctx.guild.name}", color=discord.Color.green())
    await member.send(embed = embed2)

  @mute.error
  async def mute_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      embed = discord.Embed(title="ERROR!", description="Some where I do not have permissions\nMake sure I have permissions to timeout people as well as the role have the same permissions\n\nIf that does not work please send a modmail message.", color=discord.Color.red())
      await ctx.send(embed=embed)

  @unmute.error
  async def unmute_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      embed = discord.Embed(title="ERROR!", description="Some where I do not have permissions\nMake sure I have permissions to timeout people as well as the role have the same permissions\n\nIf that does not work please send a modmail message.", color=discord.Color.red())
      await ctx.send(embed=embed)
    
    

async def setup(bot):
  await bot.add_cog(mute(bot))