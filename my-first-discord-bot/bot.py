import discord
import random
import os
import asyncio
import aiohttp
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix=">")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))
    print('Bot is ready!')

@client.event
async def on_member_join(member):
    channel = client.get_channel(869791935504744448) # replace id with the welcome channel's id
    await channel.send(f"{member} has arrived!")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You can't do that :(")
        await ctx.message.delete()
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter all the required arguments.")
        await ctx.message.delete()
    else:
        raise error

@client.event
async def on_raw_reaction_add(payload):
    ourmessageID = 961342600483323924

    if ourmessageID == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name
        if emoji == "🟦":
            role = discord.utils.get(guild.roles, name ="Blue")
        elif emoji == "🟨":
            role = discord.utils.get(guild.roles, name="Yellow")

        await member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):
    ourmessageID = 961342600483323924

    if ourmessageID == payload.message_id:
        guild = await(client.fetch_guild(payload.guild_id))

        emoji = payload.emoji.name
        if emoji == "🟦":
            role = discord.utils.get(guild.roles, name="Blue")
        elif emoji == "🟨":
            role = discord.utils.get(guild.roles, name="Yellow")

        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)
        else:
            print("Member is not found.")


#etiketlenen kişi beni seviyor mu?
@client.command()
async def love(ctx, member: discord.Member):
    embed = discord.Embed(description=f"{ctx.author.mention}, {member.mention} seni çok seviyor! ❤", color=0xffcbdb)
    await ctx.send(embed=embed)

#etiketlenen kişiye sevgi mesajı gönderir.
@client.command()
async def sendlove(ctx, member: discord.Member):
    await member.send(f"{ctx.author.mention} seni çok seviyor! ❤")
    await ctx.send("Mesaj gönderildi!")

#klasik ping komutu, bot gecikmesini ölçer.
@client.command(name="ping", pass_context=True, aliases=["latency"])
async def ping(ctx):
    embed = discord.Embed(title="**Latency**", colour=discord.Color.dark_blue(), timestamp=ctx.message.created_at)
    embed.add_field(name= "Latency of bot", value=f"`{round(client.latency * 1000)} ms`")
    await ctx.send(embed=embed)

#controyu yoklar.
@client.command(aliases=["Contro"])
async def contro(ctx):
    embed = discord.Embed(description=f"Buradayım {ctx.author.mention}!", color=0x587246)
    await ctx.send(embed=embed)

#kanaldaki gerektiği kadar mesajı siler.
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit = amount + 1)

#üyeyi sunucudan atar.
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member,*,reason= "No reason provided."):
    embed = discord.Embed(description=member.mention + " has been kicked from Türk Oyuncu Topluluğu!", color=0xf0dd1f)
    await ctx.send(embed=embed)
    embed2 = discord.Embed(description="You have been kicked from Türk Oyuncu Topluluğu!", color=0xf0dd1f)
    embed3 = discord.Embed(description="The member has their dms closed.", color=0xf0dd1f)
    try:
        await member.send(embed=embed2)
    except:
        await ctx.send(embed3)

    await member.kick(reason=reason)

#üyeyi sunucudan yasaklar.
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member,*,reason= "No reason provided."):
    embed = discord.Embed(description=member.mention + " has been banned!", color=discord.Colour.red())
    await ctx.send(embed=embed)
    embed2 = discord.Embed(description=f"You have been banned from {member.guild.name}!", color=discord.Colour.red())
    embed3 = discord.Embed(description="The member has their dms closed.", color=discord.Colour.red())
    try:
        await member.send(embed=embed2)
    except:
        await ctx.send(embed=embed3)

    await member.ban(reason=reason)

#üyenin banını kaldırır.
@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()

    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.channel.send(f"Unbanned: {user.mention}")

#üyenin kullanıcı ismini değişir.
@client.command()
@commands.has_permissions(manage_nicknames=True)
async def nick(ctx, member:discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f"Nickname was change for {member.mention}")

#üyenin kullanıcı ismini resetler.
@client.command()
@commands.has_permissions(manage_nicknames=True)
async def resetnick(ctx, member:discord.Member):
    await member.edit(nick=None)
    await ctx.send(f"Nickname was change for {member.mention}")

#embed mesajlar oluşturabiliriz.
@client.command()
@commands.has_permissions(manage_messages=True)
async def makeembed(ctx, *, content: str):
    title, description = content.split('|')
    embed = discord.Embed(title=title, description=description, color=discord.Color.dark_grey())
    await ctx.send(embed=embed)

#üye hakkında bilgi verir.
@client.command()
@commands.has_permissions(kick_members=True)
async def whois(ctx, *, member:discord.Member = None):
    if not member:
        member = ctx.message.author
    embed = discord.Embed(title=member.name, description=member.mention, color=discord.Colour.yellow)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Joined at", value=member.joined_at.strftime("%a, %d %B %Y, %I:%M  UTC"))
    embed.add_field(name="Joined Server On:", value=(member.joined_at.strftime("%a, %d %B %Y, %I:%M %p UTC")))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    embed.add_field(name="Voice:", value=member.voice)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
    await ctx.send(embed=embed)

#üyenin avatarını gösterir.
@client.command()
async def avatar(ctx, *, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    em = discord.Embed(title=str(member), color=member.color)
    em.set_image(url=member.avatar_url)
    await ctx.reply(embed=em, mention_author=False)


#sunucu hakkında bilgi verir.
@client.command(aliases=['server'])
@commands.has_permissions(kick_members=True)
async def serverinfo(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)

#belirtilen rolü sunucudan siler.
@client.command(pass_context=True)
async def delrole(ctx, *, role_name):
    role = discord.utils.get(ctx.message.guild.roles, name=f"{role_name}")
    await role.delete()
    await ctx.send(f"[{role_name}] Has been deleted!")


#KOD DENEMELERİ
@client.command()
async def kayıt(ctx, name, *,age):

    member = ctx.author

    role = discord.utils.get(ctx.guild.roles, name="18+")
    role2 = discord.utils.get(ctx.guild.roles, name="18-")
    role3 = discord.utils.get(ctx.guild.roles, name="Kayıtsız",)

    embed = discord.Embed(description=f"Kayıt tamamlandı {ctx.author.mention}", colour=discord.Colour.blurple())
    embed2 = discord.Embed(description="Burası kayıt kanalı değil!", colour=discord.Colour.red())

    if ctx.channel.name == ('kayıt-işleri'):

        if age.endswith(('18', '19', '20', '21', '22', '23', '24')):
            #await member.edit(nick=name + "#" + age)
            await ctx.send(embed=embed)
            await member.send(embed=embed)
            await member.add_roles(role)
            await member.remove_roles(role2, role3)

        elif age.endswith(('10', '11', '12', '13', '14', '15', '16', '17')):
            #await member.edit(nick=name + "#" + age)
            await ctx.send(embed=embed)
            await member.send(embed=embed)
            await member.add_roles(role2)
            await member.remove_roles(role, role3)

    else:
        await ctx.send(embed=embed2)

    await member.edit(nick=None)





client.run("NzgzMDY0NjE1MDEyNjYzMzI2.X8VTwA.RioPjmb3wC80372ClxhKs--NgZg")


#Denenecekler:
#Sunucudaki tüm emojileri gösterme.

#Yapılacaklar:
#Dizi ve filmler hakkında bilgi çekeceğim.
#Kayıt komutu yapacağım.
