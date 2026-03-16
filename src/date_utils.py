import ntptime


def is_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 1
    else:
        return 0


def cnt_days(timestamp: int) -> int:
    return timestamp // 86400


def cnt_year(days_since_1970: int) -> tuple[int, int]:
    year = 1970
    days = days_since_1970
    while days > 0:
        leap = is_leap(year)
        days_in_year = 365 + leap
        if days < days_in_year:
            break
        days -= days_in_year
        year += 1
    days += 1
    return (year, days)


def create_full_date_str(days_past_current: int = 0) -> str:
    timestamp = ntptime.time() - (days_past_current * 86400)
    offset_in_days = cnt_days(timestamp)
    year, days = cnt_year(offset_in_days)

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_days[1] += is_leap(year)

    for idx, days_amount in enumerate(month_days):
        if days <= days_amount:
            return f"{year}.{idx + 1:02d}.{days:02d}"
        days -= days_amount

    raise ValueError
