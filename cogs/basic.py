import discord
from discord.ext import commands
from datetime import datetime as d


class Basic(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Define a new command
    @commands.command(
        name='ping',
        description='The ping command',
        aliases=['p']
    )
    async def ping_command(self, ctx):
        start = d.timestamp(d.now())
        msg = await ctx.send(content='Pinging')
        await msg.edit(content=f'🏓Pong! One message round-trip took {int((d.timestamp(d.now())-start) * 1000)}ms.')

        return

    @commands.command(
        name='info',
        description='Info about the bot',
        aliases=['bot', 'about']
    )
    async def info_command(self, ctx):
        embed = discord.Embed(title="TestBotPy", description="Test bot with python" ,color = 0xf5f5dc)
        embed.add_field(name= "Name " , value="TestBotPy" , inline=True)
        embed.add_field(name= "Prefix for commands" , value = "!, t!, ==" , inline =True)
        embed.set_footer(text = "Feel free to provide suggestions to my owner!")
        await ctx.send(embed=embed)

        return

    @commands.command(
        name='server',
        description='Get the guild/server info.',
        aliases=['guild', 'serverinfo']
    )
    async def server_command(self, ctx):
        embed = discord.Embed(title="{}'s info".format(ctx.message.guild.name), description="Here's what I could find in my bag...", color=0xf5f5dc)
        embed.add_field(name="Servername", value=ctx.message.guild.name, inline=True)
        embed.add_field(name="ID", value=ctx.message.guild.id, inline=True)
        embed.add_field(name="Verification Level", value=ctx.message.guild.verification_level, inline=True)
        embed.add_field(name="Server Region", value=ctx.message.guild.region, inline=True)
        embed.add_field(name="Owner" , value=ctx.message.guild.owner, inline=True)
        embed.add_field(name="Channels",value=len(ctx.message.guild.channels))
        embed.add_field(name="Roles", value=len(ctx.message.guild.roles))
        embed.add_field(name="Members", value=len(ctx.message.guild.members))
        embed.add_field(name="Emojis", value=len(ctx.message.guild.emojis))
        embed.set_thumbnail(url=ctx.message.guild.icon_url)
        await ctx.send(embed=embed)

        return

    @commands.command(
        name='user',
        description='Get userinfo',
        aliases=['userinfo', 'whois'],
        usage='<user>'
    )
    async def user(self, ctx, user: discord.Member = None):
        user = user or ctx.message.author
        try:
            join_date = user.joined_at
            create_date = user.created_at
            embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find in my bag...", color=0xf5f5dc)
            embed.add_field(name="Username", value=user.name, inline=True)
            embed.add_field(name="Nickname" , value = user.nick , inline = True)
            embed.add_field(name="ID", value=user.id, inline=True)
            embed.add_field(name="Bot", value=user.bot ,inline=True)
            embed.add_field(name="Status", value=user.status,inline=True)
            embed.add_field(name="Highest role", value=user.top_role)
            embed.add_field(name="Ceated At", value=join_date.strftime("%d/%m/%Y, %H:%M:%S"))
            embed.add_field(name="Joined At" , value=create_date.strftime("%d/%m/%Y, %H:%M:%S"))
            embed.set_thumbnail(url=user.avatar_url)
            await ctx.send(embed=embed)
        except:
            await ctx.send("Error")

        return

    @commands.command(
        name='avatar',
        description='Get someones avatar',
        aliases=['a', 'ava', 'pfp'],
        usage='<user>'
    )
    async def avatar(self, ctx, user: discord.Member = None):
        user = user or ctx.message.author
        try:
            embed = discord.Embed(title="{}'s avatar".format(user.name), color=0xf5f5dc)
            embed.set_image(url=user.avatar_url)
            await ctx.send(embed=embed)
        except:
            await ctx.send("Error")

        return


    @commands.command(
        name='say',
        description='The say command',
        aliases=['repeat', 'parrot'],
        usage='<text>'
    )
    async def say_command(self, ctx):
        msg = ctx.message.content
        await ctx.message.delete()
        prefix_used = ctx.prefix
        alias_used = ctx.invoked_with
        text = msg[len(prefix_used) + len(alias_used):]

        # Next, we check if the user actually passed some text
        if text == '':
            # User didn't specify the text

            await ctx.send(content='You need to specify the text!')

            pass
        else:
            # User specified the text.

            await ctx.send(content=f"**{text}**")

            pass

        return


def setup(bot):
    bot.add_cog(Basic(bot))
    # Adds the Basic commands to the bot
    # Note: The "setup" function has to be there in every cog file
