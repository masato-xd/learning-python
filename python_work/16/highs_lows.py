# coding: utf-8
import csv
import matplotlib.pyplot as plt
from datetime import datetime as dt

# filename = 'sitka_weather_07-2014.csv'
filename = 'sitka_weather_2014.csv'
# filename = '2017-05-13.csv'

# 取出最高温度和日期
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    # 打印头行
    # print(header_row)

    # enumerate，取出索引以及值
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # 取出最高温度和日期
    # for high_temperature in reader:
    #     high = int(high_temperature[1])
    #     highs.append(high_temperature[1])
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = dt.strptime(row[0], '%Y-%m-%d')
        # print type(dates)
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = row[3]
        lows.append(int(low))

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(8, 4))
plt.plot(dates, highs, c='red', alpha=0.2)
plt.plot(dates, lows, c='blue', alpha=0.2)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.5)

# 设置图形格式
plt.title("Daily high temperatures, July 2014", fontsize=14)
plt.xlabel('', fontsize=10)
fig.autofmt_xdate()
plt.ylabel("Temperatures (F)", fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=9)
plt.show()
