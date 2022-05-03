import re

import discord
import pytchat

import config


client = discord.Client()


@client.event
async def on_ready():
    print("-----------------------------------")
    print("Logged in as " + client.user.name)
    print("Running " + client.user.name)
    print("-----------------------------------")
    # type=playing, listening, watching, streaming
    activity = discord.Activity(
        name=config.ACTIVITY_NAME,
        type=discord.ActivityType.playing)
    await client.change_presence(activity=activity)

    livechat = pytchat.create(video_id=config.VIDEO_ID_FREE_CHAT)
    while livechat.is_alive():
        chatdata = livechat.get()
        for c in chatdata.items:
            msg = f"{c.author.name}: {c.message}"
            await send_livechat(c, msg)


async def send_livechat(c, msg):
    if msg != "":
        # if str(c.author.channelId) != config.CHANNEL_ID_STREAMER:
        channel = client.get_channel(config.CHANNEL_ID_LIVECHAT)
        subed_msg = re.sub(
            r":_[0-9a-zA-Z]*:",
            lambda x: str(emoji) if (emoji := discord.utils.get(channel.guild.emojis, name=x.group(0)[1:-1])) else x.group(0),
            msg)
        # embed = discord.Embed(
        #     title=subed_msg,
        #     color=0xFFF8C8
        # )
        # embed.set_author(
        #     name=config.EMBED_TITLE,
        #     url="https://youtu.be/" + config.VIDEO_ID_FREE_CHAT
        # )
        # embed.set_footer(
        #     text=c.author.name
        # )
        await channel.send(subed_msg)  # embed=embed


client.run(config.DISCORD_BOT_TOKEN)
