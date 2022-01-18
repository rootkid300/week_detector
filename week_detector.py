import asyncio
from datetime import datetime as dt
import logging
from argparse import ArgumentParser
import calendar
import numpy as np

logger = logging.getLogger('WeekDetector')
logger.setLevel(logging.INFO)

calendar.setfirstweekday(calendar.SUNDAY)
date_format = '%d.%m.%Y'
start_date = dt.strptime('01.01.2019', date_format)


async def detect_week_number(target_date: dt.date) -> int:
    week_map = np.array(
        calendar.monthcalendar(target_date.year, target_date.month)
    )
    rows, _ = np.where(week_map == target_date.day)
    return int(rows[0]) + 1


async def main():
    desc = f'use date in {date_format} format'
    parser = ArgumentParser(description=desc)
    parser.add_argument(
        'date',
        type=str,
    )
    try:
        args = parser.parse_args()
        target_date = dt.strptime(args.date, date_format)
        if start_date > target_date:
            raise ValueError
        result = await detect_week_number(target_date=target_date)
        logger.warning(result)
    except ValueError:
        logger.error(
            f'Please {desc} greater then {start_date.date()}'
        )

if __name__ == '__main__':
    asyncio.run(main=main())

