import datetime
def needingDate() -> str:
    today = datetime.datetime.now()
    need_date = datetime.datetime.now()
    print(today.weekday())
    if today.weekday() > 4:
        weekday = datetime.datetime.weekday(today)
        needing_day = (weekday+1)-5
        need_date = datetime.datetime(today.year, today.month, today.day-needing_day)
    print(need_date.date())
    return str(need_date.date())
