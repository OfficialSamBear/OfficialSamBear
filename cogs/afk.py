import discord
from discord.utils import get
from discord.ext import commands
from afks import afks

def remove(afk):
  if "[afk]" in afk.split():
    return " ".join(afk.split()[1:])

class afk(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author.id in afks.keys():
      afks.pop(message.author.id)
      try:
        await message.author.edit(nick = remove(message.author.display_name))
      except:
        pass
      await message.channel.send(f"Welcome back {message.author.name}, your afk is removed")

    for id,reason in afks.items():
      member = get(message.guild.members, id = id)
      if (message.reference and member == (await message.channel.fetch_message(message.reference.message_id)).author) or member.id in message.raw_mentions:
        await message.reply(f"{member.name} is afk, please do not ping or dm them until they come back!\nAFK Note: {reason}")

  @commands.command(pass_context=True)
  async def afk(self, ctx, *, reason="afk"):
    member = ctx.author
    if member.id in afks.keys():
      afks.pop(member.id)
    else:
      try:
       await member.edit(nick = f"[AFK] {member.display_name}")
      except:
        pass

    afks[member.id] = reason
    embed = discord.Embed(title="AFK", description=f"{member.mention} has gone afk", color=member.color)
    embed.add_field(name="AFK Note:", value=f"{reason}")
    await ctx.send(embed=embed)

async def setup(bot):
	await bot.add_cog(afk(bot))