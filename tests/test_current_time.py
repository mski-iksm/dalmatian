from dalmatian.current_time import CurrentTime
from datetime import date


class TestCurrentTime:

    def test_is_weekday(self):
        assert CurrentTime._is_weekday(date(2020, 1, 1), 'wed') is False
        assert CurrentTime._is_weekday(date(2020, 2, 17), 'mon') is True
        assert CurrentTime._is_weekday(date(2020, 2, 16), 'sun') is False
