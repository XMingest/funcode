# -*- coding: utf-8 -*-
import datetime

import fire
import win32evtlog


class ComputerOn:
    def __init__(self):
        evt_obj = win32evtlog.OpenEventLog('localhost', 'System')
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
        self.day_during = {}
        while True:
            events = win32evtlog.ReadEventLog(evt_obj, flags, 0)
            if events:
                for event in events:
                    evt_time = datetime.datetime.strptime(f'{event.TimeGenerated}', '%Y-%m-%d %H:%M:%S')
                    during = self.day_during.setdefault(evt_time.year,
                                                        {}).setdefault(evt_time.month,
                                                                       {}).setdefault(evt_time.day, {})
                    if evt_time.hour == 18 and evt_time.minute < 31:
                        evt_time = evt_time.replace(microsecond=0, minute=0, second=0)
                    elif evt_time.hour < 8 or (evt_time.hour == 8 and evt_time.minute < 30):
                        evt_time = evt_time.replace(hour=8, microsecond=0, minute=30, second=0)
                    elif evt_time.hour == 12 or (evt_time.hour == 13 and evt_time.minute < 30):
                        evt_time = evt_time.replace(hour=12, microsecond=0, minute=0, second=0)
                    earliest = during.setdefault('start', evt_time)
                    latest = during.setdefault('end', evt_time)
                    if evt_time > latest:
                        during['end'] = evt_time
                    elif evt_time < earliest:
                        during['start'] = evt_time
            else:
                break
        return

    def calc_month(self, month=None, year=None):
        """
        通过电脑开启时间计算某年某月工时
        :param month: 默认当月
        :param year: 默认当年
        :return:
        """
        now_tmp = datetime.datetime.now()
        year = year if year else now_tmp.year
        month = month if month else now_tmp.month
        try:
            day_during = self.day_during[year][month]
        except KeyError:
            print(f'no found event log in {year}-{month}')
            return None
        data = {'total': datetime.timedelta(0)}
        for day in range(1, 32):
            if day in day_during:
                start_time = day_during[day]['start']
                end_time = day_during[day]['end']
                during = end_time - start_time
                if end_time.hour > 13 or (end_time.hour == 13 and end_time.minute):
                    during -= datetime.timedelta(hours=1, minutes=30)
                if end_time.hour > 18 or (end_time.hour == 18 and end_time.minute):
                    during -= datetime.timedelta(minutes=30)
                data[day] = {
                    'during': during,
                    'end': end_time,
                    'start': start_time,
                }
                data['total'] += during
                print(f'{day}: {during} ({day_during[day]["start"]} - {day_during[day]["end"]})\n')
        print(f'TOTAL: {round(data["total"].total_seconds() / 3600, 2)} H\n')
        return data


if __name__ == '__main__':
    fire.Fire(ComputerOn().calc_month)
