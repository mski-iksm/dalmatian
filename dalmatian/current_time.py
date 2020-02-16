from datetime import datetime, timedelta, date
import jpholiday


class CurrentTime:
    DIFF_FROM_UTC = 9

    def __init__(self):
        dt = datetime.utcnow() + timedelta(hours=self.DIFF_FROM_UTC)

        self._minute: int = dt.minute
        self._hour: int = dt.hour
        self._date: int = dt.day
        self._month: int = dt.month
        self._year: int = dt.year
        int_day = dt.weekday()
        week_days = {0: 'mon', 1: 'tue', 2: 'wed', 3: 'thu', 4: 'fri', 5: 'sat', 6: 'sun'}

        self._day: str = week_days[int_day]

        current_date = date(self._year, self._month, self._date)
        self._weekday: bool = self._is_weekday(current_date, self._day)

    @staticmethod
    def _is_weekday(current_date, day):
        return day in {'mon', 'tue', 'wed', 'thu', 'fri'} and not jpholiday.is_holiday(current_date)
