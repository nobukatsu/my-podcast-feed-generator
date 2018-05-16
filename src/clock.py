from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timezone, timedelta
from podcast.tbs_radio_cloud import TbsRadioCloud


scheduler = BlockingScheduler()


# After 6 Junction
@scheduler.scheduled_job("cron", hour="0,8", minute=10, timezone="Asia/Tokyo")
def after_6_junction():
    target_date = __get_yesterday()
    top_url = "https://radiocloud.jp/archive/a6j"
    channel_title = "アフター6ジャンクション"
    folder_name = "after_6_junction"

    podcast = TbsRadioCloud(top_url, channel_title, folder_name)
    if podcast.has_new_episode(target_date):
        podcast.generate(target_date)


# My Game My Life
@scheduler.scheduled_job("cron", hour="23", minute=0, timezone="Asia/Tokyo")
def my_game_my_life():
    target_date = __get_yesterday()
    top_url = "https://radiocloud.jp/archive/mygame"
    channel_title = "プレイステーション presents ライムスター宇多丸とマイゲーム・マイライフ"
    folder_name = "my_game_my_life"

    podcast = TbsRadioCloud(top_url, channel_title, folder_name)
    if podcast.has_new_episode(target_date):
        podcast.generate(target_date)


# Saikou Radio
# TODO Implement


def __get_yesterday() -> datetime:
    today = datetime.now(timezone(timedelta(hours=+9), "JST"))
    yesterday = today - timedelta(days=1)
    return yesterday.replace(hour=0, minute=0, second=0, microsecond=0)


scheduler.start()
