# -*- coding: utf-8 -*-
import datetime

import fire
from win32evtlog import EVENTLOG_BACKWARDS_READ, EVENTLOG_SEQUENTIAL_READ, OpenEventLog, ReadEventLog


class ComputerOn:
    @staticmethod
    def time_minus(time1: datetime.time, time2: datetime.time) -> datetime.timedelta:
        """
        计算时间差
        :param time1:
        :param time2:
        :return:
        """
        td = datetime.date.today()
        return datetime.datetime.combine(td, time1) - datetime.datetime.combine(td, time2)

    relax_during = ((0, 0, 8, 30), (12, 0, 13, 30), (18, 0, 18, 30))

    @classmethod
    def get_during(cls, start_time: datetime.time, end_time: datetime.time) -> datetime.timedelta:
        """
        通过起始时间计算间隔时长，将会计算8:30开始并排除12:00-13:30与18:00-18:30（输入要求年月日一致）
        :param start_time:
        :param end_time:
        :return:
        """
        if start_time > end_time:
            return cls.get_during(end_time, start_time)
        si = 0
        # 处理开始时间
        while si < len(cls.relax_during):
            hs, ms, he, me = cls.relax_during[si]
            si += 1
            if start_time.replace(hour=hs, minute=ms) <= start_time < start_time.replace(hour=he, minute=me):
                start_time = start_time.replace(hour=he, minute=me)
                break
            elif start_time < start_time.replace(hour=hs, minute=ms):
                si -= 1
                break
        ei = si
        # 处理结束时间
        while ei < len(cls.relax_during):
            hs, ms, he, me = cls.relax_during[ei]
            if end_time.replace(hour=hs, minute=ms) < end_time <= end_time.replace(hour=he, minute=me):
                end_time = end_time.replace(hour=hs, minute=ms)
                break
            elif end_time <= end_time.replace(hour=hs, minute=ms):
                break
            ei += 1
        during = cls.time_minus(end_time, start_time)
        for i in range(si, ei):
            hs, ms, he, me = cls.relax_during[i]
            during -= datetime.timedelta(hours=he - hs, minutes=me - ms)
        return during

    def __init__(self, relax_during=None):
        if relax_during:
            self.relax_during = relax_during
        evt_obj = OpenEventLog('localhost', 'System')
        flags = EVENTLOG_BACKWARDS_READ | EVENTLOG_SEQUENTIAL_READ
        self.day_during = {}
        while True:
            events = ReadEventLog(evt_obj, flags, 0)
            if events:
                for event in events:
                    evt_time = datetime.datetime.strptime(f'{event.TimeGenerated}', '%Y-%m-%d %H:%M:%S')
                    during = self.day_during.setdefault(evt_time.year,
                                                        {}).setdefault(evt_time.month,
                                                                       {}).setdefault(evt_time.day, {})
                    evt_time = evt_time.time()
                    earliest = during.setdefault('start', evt_time)
                    latest = during.setdefault('end', evt_time)
                    if evt_time > latest:
                        during['end'] = evt_time
                    elif evt_time < earliest:
                        during['start'] = evt_time
            else:
                break
        return

    def calc_day(self,
                 mday: int = None,
                 month: int = None,
                 year: int = None,
                 ) -> dict or None:
        """
        通过电脑开启时间计算某年某月某日工时
        :param mday:
        :param month:
        :param year:
        :return:
        """
        now_tmp = datetime.date.today()
        year = year if year else now_tmp.year
        month = month if month else now_tmp.month
        mday = mday if mday else now_tmp.day
        try:
            day_during = self.day_during[year][month][mday]
        except KeyError:
            print(f'no found event log in {year}-{month}-{mday}')
            return None
        return {
            'during': self.get_during(day_during["start"], day_during["end"]),
            'end': day_during["end"],
            'start': day_during["start"],
        }

    def calc_month(self,
                   contain_weekends: bool = False,
                   month: int = None,
                   year: int = None,
                   ) -> dict or None:
        """
        通过电脑开启时间计算某年某月工时
        :param month: 默认当月
        :param year: 默认当年
        :return:
        """
        now_tmp = datetime.date.today()
        year = year if year else now_tmp.year
        month = month if month else now_tmp.month
        try:
            day_during = self.day_during[year][month]
        except KeyError:
            print(f'no found event log in {year}-{month}')
            return None
        data = {}
        total = datetime.timedelta(0)
        for day in range(1, 32):
            if day in day_during:
                start_time = day_during[day]['start']
                end_time = day_during[day]['end']
                during = self.get_during(start_time, end_time)
                data[day] = {
                    'during': f'{round(during.total_seconds() / 3600, 2)}',
                    'end': end_time,
                    'start': start_time,
                }
                if contain_weekends or datetime.date(year, month, day).weekday() < 5:
                    total += during
        data['total'] = f'{round(total.total_seconds() / 3600, 2)}'
        return data


if __name__ == '__main__':
    obj = ComputerOn()
    cli_inteface = {
        'day': obj.calc_day,
        'month': obj.calc_month,
    }
    fire.Fire(cli_inteface)
