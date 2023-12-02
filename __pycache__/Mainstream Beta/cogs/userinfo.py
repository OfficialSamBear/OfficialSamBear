import discord
from discord.ext import commands 


class userinfo(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

    
  @commands.command()
  @commands.cooldown(1,5, commands.BucketType.user)
  async def userinfo(self, ctx, member: discord.Member = None):

    if member is None:
      member = ctx.author
      roles = [role for role in ctx.author.roles]

      embed = discord.Embed(title=f"{member}", color=discord.Color.red(), timestamp=ctx.message.created_at)
      embed.set_footer(text=f"Requested by: {ctx.author.name}")
      embed.add_field(name="Member id", value=f"{member.id}")
      embed.add_field(name="Top Role", value=member.top_role.mention)
      embed.add_field(name="Discriminator", value=member.discriminator)
      embed.add_field(name="Current Status", value=str(member.status).title())
      embed.add_field(name="Current Activity", value=f"{str(member.activity.type).split('.')[-1].title() if member.activity else 'N/A'} {member.activity.name if member.activity else ''}")
      embed.add_field(name="Created At:", value=member.created_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"))
      embed.add_field(name="Joined At:", value=member.joined_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"))
      embed.add_field(name=f"Roles [{len(roles)}]", value=" **,**".join([role.mention for role in roles]))
      embed.add_field(name="Bot?:", value=member.bot)
      await ctx.send(embed=embed)
    else:
      roles = [role for role in member.roles]

      embed2 = discord.Embed(title=f"{member}", color=discord.Color.red(), timestamp=ctx.message.created_at)
      embed2.set_footer(text=f"Requested by: {ctx.author.name}")
      embed2.add_field(name="Member id", value=f"{member.id}")
      embed2.add_field(name="Top Role", value=member.top_role.mention)
      embed2.add_field(name="Discriminator", value=member.discriminator)
      embed2.add_field(name="Current Status", value=str(member.status).title())
      embed2.add_field(name="Current Activity", value=f"{str(member.activity.type).split('.')[-1].title() if member.activity else 'N/A'} {member.activity.name if member.activity else ''}")
      embed2.add_field(name="Created At:", value=member.created_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"))
      embed2.add_field(name="Joined At:", value=member.joined_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"))
      embed2.add_field(name=f"Roles [{len(roles)}]", value=" **,**".join([role.mention for role in roles]))
      embed2.add_field(name="Bot?:", value=member.bot)
      await ctx.send(embed=embed2)


    
    

async def setup(bot):
  await bot.add_cog(userinfo(bot))