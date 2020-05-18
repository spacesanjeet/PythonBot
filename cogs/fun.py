import chucknorris.quips as q
import random
import xkcd as comic
import discord
from discord.ext import commands

list1 = [":8ball: | It is certain", ":8ball: | It is decidedly so", ":8ball: | Without a doubt", ":8ball: | Yes, definitely", ":8ball: | You may rely on it", ":8ball: | Most likely", ":8ball: | As I see it ,yes", ":8ball: | Yes", ":8ball: | Signs point to yes", ":8ball: | Ask again later", ":8ball: | Reply hazy , Try again", ":8ball: | Better not tell you now", ":8ball: | Cannot tell you now", ":8ball: | Concentrate and ask again", ":8ball: | Don't count on it", ":8ball: | My reply is no", ":8ball: | My sources say no", ":8ball: | Very doubtful", ":8ball: | Outlook not so good"]


class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='choice',
        description='Bot selects one among many options provided!',
        aliases=['choose', 'pick'],
        usage='<option1 option2 option3>'
    )
    async def choice_command(self, ctx, *choices : str):
        try:
            await ctx.send(random.choice(choices))
        except:
            await ctx.send('I select spacesanjeet!')

        return

    @commands.command(
        name='8ball',
        description='Ask holy 8ball questions!',
        aliases=['8b'],
        usage='<question>'
    )
    async def ball_command(self, ctx, *, message = None):
        if message is None:
            await ctx.send('No nothing here!')
        else:
            await ctx.send(random.choice(list1))

        return

    @commands.command(
        name='emoji',
        description='Enlarge the emoji!',
        aliases=['emote'],
        usage='<emoji>'
    )
    async def emoji(self, ctx, emo):
        emo = emo.split(':')[-1].replace('>' , '')
        await ctx.send("https://cdn.discordapp.com/emojis/{}.png?v=1".format(emo))

        return

    @commands.command(
        name='chuck',
        description='Random chuck norris jokes!',
        aliases=['norris'],
    )
    async def chuck(self, ctx, member: discord.Member = None):
        if member is not None:
               text = q.random(member.name)
        else:
             text = q.random()
        embed = discord.Embed(title = ' ' , description = text , color = 0xf5f5dc)
        await ctx.send(embed=embed)

        return

    @commands.command(
        name='xkcd',
        description='Get xkcd comics!',
        aliases=['comic'],
        usage='<number>'
    )
    async def xkcd_command(self, ctx, *, number=None):
        try:
            if number==None:
                a=comic.getRandomComic()
                title=a.getTitle()
                link=a.getImageLink()
                exp=a.getExplanation()
                embed=discord.Embed(title=f"xkcd - {title}", description=f"{a.altText}", color=0xf5f5dc)
                embed.set_footer(text=("For explanation refer to: "+exp))
                embed.set_image(url=link)
                await ctx.send(embed=embed)
            else:
                number=int(number)
                limit=comic.getLatestComicNum()
                if number<1 or number>limit:
                    await ctx.send("Please enter a number between 1 to 1988")
                else:
                    a=comic.getComic(number, silent=True)
                    title=a.getTitle()
                    link=a.getImageLink()
                    exp=a.getExplanation()
                    embed=discord.Embed(title=f"xkcd - {title}", description=f"{a.altText}", color=0xf5f5dc)
                    embed.set_footer(text=("For explanation refer to: "+exp))
                    embed.set_image(url=link)
                    await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f'There was an error trying to fetch comic: {e}')

def setup(bot):
    bot.add_cog(Fun(bot))
    # Adds the Basic commands to the bot
    # Note: The "setup" function has to be there in every cog file
