from dalmatian.schedule import Schedule
from unittest.mock import MagicMock


class TestSchedule:

    def test_schedule(self):
        schedule = Schedule(minute=8, hour=10, command='ls')
        current_time = MagicMock()
        current_time._minute = 8
        current_time._hour = 10
        current_time._date = None
        current_time._month = None
        current_time._year = None
        current_time._day = None
        current_time._weekday = None

        assert schedule.should_run_now(current_time) is True
