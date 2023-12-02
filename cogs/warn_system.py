import discord
import asyncio
import json
import mysql.connector
from discord.ext import commands
from cogs.utils.checks import load_env_vars, read_json, write_json
from cogs.events import conn

class warn_system(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(description="Warn Command")
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, member: discord.Member, *, reason="None was provided"):
        mycursor = conn.cursor()

        # Check if the member is warned in the database
        mycursor.execute("SELECT * FROM warnings WHERE member_id = %s AND guild_id = %s", (member.id, ctx.guild.id))
        result = mycursor.fetchone()

        if result is None:
            # Insert the warning into the database if the member has no warnings
            mycursor.execute("INSERT INTO warnings (member_id, guild_id, total_warnings, warnings) VALUES (%s, %s, %s, %s)",
                             (member.id, ctx.guild.id, 1, f"Warned by {ctx.author.name}. Reason - {reason}"))
            conn.commit()

            embed = discord.Embed(title="Success!", description=f":white_check_mark: | `{reason}` has been added to **{member.name}'s** warn list", color=discord.Color.green())
            embed2 = discord.Embed(title="Warned!", description=f"You have been warned in **{ctx.message.guild.name}** for `{reason}`", color=discord.Color.red())
            msg = await ctx.send(embed=embed)
            await member.send(embed=embed2)
            print(f"{member.name} has been warned in {ctx.guild.name}\nAuthor: {ctx.author.name}\nWarn: {reason}\n")
            await asyncio.sleep(5)
            await msg.delete()
            await ctx.message.delete()
        else:
            # Increment the warning count if the member is already warned
            total_warnings = result[2] + 1
            warnings = result[3] + f"\nWarned by {ctx.author.name}. Reason - {reason}"
            mycursor.execute("UPDATE warnings SET total_warnings = %s, warnings = %s WHERE member_id = %s AND guild_id = %s",
                             (total_warnings, warnings, member.id, ctx.guild.id))
            conn.commit()

            embed = discord.Embed(title="Success!", description=f":white_check_mark: | `{reason}` has been added to **{member.name}'s** warn list", color=discord.Color.green())
            embed2 = discord.Embed(title="Warned!", description=f"You have been warned in **{ctx.message.guild.name}** for `{reason}`", color=discord.Color.red())
            msg = await ctx.send(embed=embed)
            await member.send(embed=embed2)
            print(f"{member.name} has been warned in {ctx.guild.name}\nAuthor: {ctx.author.name}\nWarn: {reason}\n")
            await asyncio.sleep(5)
            await msg.delete()
            await ctx.message.delete()

    @commands.hybrid_command(description="Search Warns")
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def warnings(self, ctx, member: discord.Member = None):
        mycursor = conn.cursor()

        if member is None:
            member = ctx.author

        mycursor.execute("SELECT * FROM warnings WHERE member_id = %s AND guild_id = %s", (member.id, ctx.guild.id))
        result = mycursor.fetchone()

        if result is not None:
            embed = discord.Embed(title=f"Warnings for {member.name}", description=f"**Total number of warnings : {result[2]}**\n\n Warnings: \n{result[3]}", color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="ERROR!", description=f":x:{member.name} has no warns!", color=discord.Color.red())
            await ctx.send(embed=embed)

    @commands.hybrid_command(description="Delete Warn", with_app_command=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def delwarn(self, ctx, member: discord.Member):
        mycursor = conn.cursor()

        mycursor.execute("SELECT * FROM warnings WHERE member_id = %s AND guild_id = %s", (member.id, ctx.guild.id))
        result = mycursor.fetchone()

        if result is not None:
            mycursor.execute("DELETE FROM warnings WHERE member_id = %s AND guild_id = %s", (member.id, ctx.guild.id))
            conn.commit()

            embed = discord.Embed(title="Success!", description=f":white_check_mark: | All warns for {member.name} have been deleted", color=discord.Color.green())
            msg = await ctx.send(embed=embed)
            print(f"All warns for {member.name} have been deleted\nGuild: {ctx.guild.name}\nAuthor: {ctx.author.name}\n")
            await asyncio.sleep(5)
            await msg.delete()
            await ctx.message.delete()
        else:
            embed = discord.Embed(title="ERROR!", description=f":x:{member.name} has no warns!", color=discord.Color.red())
            await ctx.send(embed=embed)



async def setup(bot):
    await bot.add_cog(warn_system(bot))