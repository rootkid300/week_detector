import asyncio
import unittest
import calendar
from datetime import datetime as dt, timedelta as td

from week_detector import detect_week_number

calendar.setfirstweekday(calendar.SUNDAY)
date_format = '%d.%m.%Y'
start_date = dt.strptime('01.01.2019', date_format)


class TestWeekDetector(unittest.TestCase):

    def test_first_week(self):
        week_number = 1
        number = asyncio.run(
            detect_week_number(
                target_date=start_date
            )
        )
        self.assertEqual(number, week_number)
        number = asyncio.run(
            detect_week_number(
                target_date=start_date + td(days=4)
            )
        )
        self.assertEqual(number, week_number)

    def test_second_week(self):
        week_number = 2
        number = asyncio.run(
            detect_week_number(
                target_date=start_date + td(days=5)
            )
        )
        self.assertEqual(number, week_number)
        number = asyncio.run(
            detect_week_number(
                target_date=start_date + td(days=11)
            )
        )
        self.assertEqual(number, week_number)


if __name__ == '__main__':
    unittest.main()

