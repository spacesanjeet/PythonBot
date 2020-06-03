import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='kick',
        description='Kicks a user!',
        usage='<user>'
    )
    @commands.has_permissions(kick_members=True)
    async def kick_command(self, ctx, member: discord.Member):
        try:
            await ctx.message.guild.kick(member)
            await ctx.send(f"**{member.name}#{member.discriminator}** has been kicked!")
        except Exception as error:
            await ctx.send(f"Unable to kick user : **{error}**")

        return

    @commands.command(
        name='ban',
        description='Bans a user!',
        usage='<user>'
    )
    @commands.has_permissions(ban_members=True)
    async def ban_command(self, ctx, member: discord.Member):
        try:
            await ctx.message.guild.ban(member)
            await ctx.send(f"**{member.name}#{member.discriminator}** has been banned!")
        except Exception as error:
            await self.bot.say(f"Unable to ban user : **{error}**")

        return

    @commands.command(
        name='nickname',
        description='Changes the nickname!',
        aliases=['nick'],
        usage='<user> <nick>'
    )
    @commands.has_permissions(manage_nicknames=True)
    async def nickname_command(self, ctx, member: discord.Member, *, name: str = None):
        name = name or None
        try :
            await member.edit(nick=name)
            await ctx.send('Nickname changed!')
        except Exception as error:
            await self.bot.say(f"Unable to change nickname : **{error}**")

        return

def setup(bot):
    bot.add_cog(Moderation(bot))
    # Adds the Basic commands to the bot
    # Note: The "setup" function has to be there in every cog file
