import tweepy
import os
import random
import time
from datetime import datetime

# 23時台のランダムなタイミングで実行するための待機（0〜3540秒）
wait_seconds = random.randint(0, 3540)
print(f"Waiting for {wait_seconds} seconds...")
time.sleep(wait_seconds)

# X APIの認証情報をGitHub Secretsから取得
client = tweepy.Client(
    consumer_key=os.environ["API_KEY"],
    consumer_secret=os.environ["API_SECRET"],
    access_token=os.environ["ACCESS_TOKEN"],
    access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]
)

# カウントダウン計算（2027年4月1日 00:00:00まで）
target = datetime(2027, 4, 1, 0, 0, 0)
now = datetime.now()
diff = target - now

# 残り時間のフォーマット
days = diff.days
hours, remainder = divmod(diff.seconds, 3600)
minutes, seconds = divmod(remainder, 60)
total_minutes = int(diff.total_seconds() // 60)

# 4. ツイート文面
# 日、時間、分をきれいに並べた文面です
message = (
    f"mura様配信、出禁解除まで\n"
    f"【 {days}日と{hours}時間{minutes}分 】です。\n\n"
    f"（総計：{total_minutes:,} 分）\n"
    f"#mura #シャドバ"
)

# 5. 投稿実行
try:
    client.create_tweet(text=message)
    print(f"Successfully tweeted: {message}")
except Exception as e:
    print(f"Error: {e}")
