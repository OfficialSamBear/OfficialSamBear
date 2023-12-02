import discord
import datetime
from discord.ext import commands

class give(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.has_permissions(manage_roles=True)
    async def give(self, ctx, member: discord.Member, role: discord.Role):
        if role.position > ctx.author.top_role.position:
          return await ctx.send('**:x: | You cant do that! That role is above you!!**')
        if member.top_role.position > role.position:
          return await ctx.send(f"**:x: i need to be above {member.name}\'s top role**")
        if role in member.roles:
          await user.remove_roles(role)
          await ctx.send(f"Removed {role} from {user.mention}")
        else:
          await member.add_roles(role)
          embed = discord.Embed(title=f"", description=f":white_check_mark: | {member.name} was given {role}", color=discord.Color.green())
          embed.timestamp = datetime.datetime.utcnow()
          await ctx.send(embed=embed)
          embed2 = discord.Embed(title="Congrats!", description=f"You know have {role} in {ctx.guild.name}!", color=discord.Color.green())
          embed2.timestamp = datetime.datetime.utcnow()
          await member.send(embed=embed2)
          print(f"{member.name} has been given {role} in {ctx.guild.name}\nAuthor: {ctx.author.name}\n")

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.has_permissions(manage_roles=True)
    async def remove(self, ctx, member: discord.Member, *, role: discord.Role):
        if role.position > ctx.author.top_role.position:
          return await ctx.send('**:x: | You cant do that! That role is above you!!**')
        if member.top_role.position > role.position:
          return await ctx.send(f"**:x: i need to be above {member.name}\'s top role**")
        if role in member.roles:
          await member.remove_roles(role)
          embed = discord.Embed(title=f"", description=f":white_check_mark: | {member.name} no longer has {role}", color=discord.Color.green())
          embed.timestamp = datetime.datetime.utcnow()
          await ctx.send(embed=embed)
          embed2 = discord.Embed(title="ATTENTION!!", description=f"You no longer have {role} in {ctx.guild.name}!", color=discord.Color.red())
          embed2.timestamp = datetime.datetime.utcnow()
          await member.send(embed=embed2)
          print(f"{role} has been removed from {member.name} roles list in {ctx.guild.name}\nAuthor: {ctx.author.name}\n")
        else:
          await ctx.send("Something weird happened!! Try again")


async def setup(bot):
  await bot.add_cog(give(bot))