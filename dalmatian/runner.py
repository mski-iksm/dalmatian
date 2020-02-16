from typing import List
import yaml

from dalmatian.schedule import Schedule
from dalmatian.current_time import CurrentTime


def load_schedules():
    # yamlの設定ファイルを読み込む
    yaml_schedules = get_yaml()

    schedules: List[Schedule] = []
    for schedule_dict in yaml_schedules:
        schedules.append(Schedule(**schedule_dict))

    return schedules


def get_yaml():
    with open('yamls/secret_cron_settings.yml', 'r') as yf:
        yaml_schedules = yaml.load(yf)
        return yaml_schedules


def get_current_datetime():
    # 現在日時・曜日・祝日フラグを取得
    return CurrentTime()


def run_schedule(schedule, current_time):
    # 各スケジューリングを確認して実行
    if schedule.should_run_now(current_time):
        schedule.run()


def runner():
    schedules: List[Schedule] = load_schedules()
    current_time = get_current_datetime()

    for schedule in schedules:
        run_schedule(schedule, current_time)
