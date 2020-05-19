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
        name='server',
        description='Get the guild/server info.',
        aliases=['guild', 'guildinfo', 'serverinfo']
    )
    async def server_command(self, ctx):
        servercreate = ctx.message.guild.created_at
        embed = discord.Embed(title=f"**{ctx.message.guild.name} [{ctx.message.guild.id}]**", color=0xf5f5dc)
        embed.set_thumbnail(url=ctx.message.guild.icon_url)
        embed.add_field(name="Members", value=f"> **{len(ctx.message.guild.members)}** members\n > Owner: **{ctx.message.guild.owner}** (ID: **{ctx.message.guild.owner.id})**", inline=False)
        embed.add_field(name="Other", value=f'> Roles: **{len(ctx.message.guild.roles)}**\n > Region: **{ctx.message.guild.region}**\n > Created At: **{servercreate.strftime("%d/%m/%Y, %H:%M:%S")}**\n > Verification Level: **{ctx.message.guild.verification_level}**')
        embed.add_field(name='Misc', value=f"> Channels: **{len(ctx.message.guild.channels)}**\n > Emojis: **{len(ctx.message.guild.emojis)}**", inline=False)
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
        if user.bot == True:
            ubot = "Yes"
        else:
            ubot = "No"
        try:
            join_date = user.joined_at
            create_date = user.created_at
            embed = discord.Embed(title="Here is {}'s info".format(user.name), color=0xf5f5dc)
            embed.add_field(name='Here are the details', value=f'> ID: **{user.id}**\n > Tag: **{user.name}#{user.discriminator}**\n > Nickname: **{user.nick}**\n > Created At: **{create_date.strftime("%d/%m/%Y, %H:%M:%S")}**\n > Joined At: **{join_date.strftime("%d/%m/%Y, %H:%M:%S")}**\n > Bot: **{ubot}**\n > Status: **{user.status}**')
            embed.set_thumbnail(url=user.avatar_url)
            embed.set_footer(
                text=f'{ctx.message.guild.name}',
                icon_url=ctx.message.guild.icon_url
            )
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f'There was an error: {e}')

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
