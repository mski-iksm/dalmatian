import subprocess

from dalmatian.current_time import CurrentTime


class Schedule:

    def __init__(
        self,
        command: str,
        minute: int = None,
        hour: int = None,
        date: int = None,
        month: int = None,
        year: int = None,
        day: str = None,
        weekday: bool = None,
    ):
        assert minute is None or (minute <= 59 and minute >= 0), f'minute={minute} must be 0~59'
        assert hour is None or (hour <= 23 and hour >= 0), f'hour={hour} must be 0~23'
        assert date is None or (date <= 31 and date >= 1), f'date={date} must be 1~31'
        assert month is None or (month <= 12 and month >= 1), f'month={month} must be 1~12'
        assert day is None or day in {'sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'}, f'day={day} must be sun, mon, tue, wed, thu, fri, sat, or None'

        self._minute = minute
        self._hour = hour
        self._date = date
        self._month = month
        self._year = year
        self._day = day  # sun, mon, tue, wed, thu, fri, sat, or None
        self._weekday = weekday
        self._command = command  # linux command

    def should_run_now(self, current_time: CurrentTime):
        return (self._is_none_or_same(self._minute, current_time._minute) and self._is_none_or_same(self._hour, current_time._hour) and
                self._is_none_or_same(self._date, current_time._date) and self._is_none_or_same(self._month, current_time._month) and
                self._is_none_or_same(self._year, current_time._year) and self._is_none_or_same(self._day, current_time._day) and
                self._is_none_or_same(self._weekday, current_time._weekday))

    @staticmethod
    def _is_none_or_same(left, right):
        return left is None or left == right

    def run(self):
        print(self._command.split())
        subprocess.call(self._command.split())
