import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

# ここから下を編集してください
ACTIVITY_NAME = "이몸 등장"  # ACTIVITY_NAMEをプレイ中と表示される
VIDEO_ID_FREE_CHAT = "0bPQXW54sj8"  # フリーチャットのvideo_id
EMBED_TITLE = "📌Sheep farm📌"  # チャット取得時のタイトル
CHANNEL_ID_STREAMER = "UC4ZltKc-wq12BjPZJYalPnw"  # 検知したいアカウントのchannelId
CHANNEL_ID_LIVECHAT = 962665921456009226  # Livechatを送信するDiscordチャンネルのID
