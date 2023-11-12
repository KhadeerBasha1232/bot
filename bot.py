import asyncio
import pandas as pd
from datetime import datetime, timedelta
from telegram import Bot

async def send_telegram_message(bot_token, chat_id, message):
    bot = Bot(token=bot_token)

    await bot.send_message(chat_id=chat_id, text=message)

async def main():
    bot_token = '6418979988:AAH9wfr2XeiKGRM621-H-0UK0HKFf0wu5zw'
    chat_id = '1954098115'

    sheet_id = "18D8q03FW_4w510T1xriecFbpQrSEYSTk-LAm_hvT66s"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv"

    while True:
        df = pd.read_csv(url)
        df["dateTime"] = pd.to_datetime(df["dateTime"])  
        print(df["dateTime"])
        current_time = datetime.now()

        for index, row in df.iterrows():
            schedule_time = row['dateTime']
            message = row['message']
            print(message)
            if current_time < schedule_time:
                time_difference = (schedule_time - current_time).total_seconds()
                print(time_difference)
                await asyncio.sleep(time_difference)

                await send_telegram_message(bot_token, chat_id, message)

if __name__ == '__main__':
    asyncio.run(main())
