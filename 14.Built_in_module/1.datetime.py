#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from datetime import datetime, timedelta, timezone

now = datetime.now() # 获取当前datetime
print(now)
print(type(now))

# 用参数构造一个datetime
dt = datetime(2015, 4, 19, 12, 20)
print(dt)
# Python的timestamp是一个浮点数，整数位表示秒
t = dt.timestamp()
print(t)

# 把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法
print(datetime.fromtimestamp(t)) #本地时间
print(datetime.utcfromtimestamp(t)) # UTC时间

# 把str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
# 注意转换后的datetime是没有时区信息的。

# datetime转换为str
print(now.strftime('%a, %b %d %H:%M'))

# datetime加减
print(now)
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))

# 一个datetime类型有一个时区属性tzinfo，但是默认为None
# 所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：

tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now = datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
print(dt)

# 时区转换
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# bj_dt到tokyo_dt的转换
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)


# 练习
# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
def to_timestamp(dt_str, tz_str):
    # 格式化时间
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')

    # 获取时区
    reg_tz = re.compile(r'\w+([+|-])(\d+)\:(\d+)')
    sign, h, m = reg_tz.match(tz_str).groups()

    # 重置时区
    dt = dt.replace(tzinfo=timezone(timedelta(hours=int(sign+h), minutes=int(sign+m))))

    return dt.timestamp()


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
