import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
from datetime import date, datetime

lst_date = pd.date_range(date(2022, 9, 1), date(2022, 9, 30)).to_list()
lst_senko = [np.random.randint(2, 5) for i in range(0, 30)]
lst_toujitsu = [np.random.randint(1, 3) for i in range(0, 30)]
lst_okure = [np.random.randint(2, 4) for i in range(0, 30)]
lst_keikaku = [np.random.randint(8, 10) for i in range(0, 30)]
lst_delay = [np.random.randint(30, 50) for i in range(0, 30)]

dataset = pd.DataFrame({
    'date': lst_date,
    'senko': lst_senko,
    'toujitsu': lst_toujitsu,
    'okure': lst_okure,
    'keikaku': lst_keikaku,
    'delay': lst_delay})

def make_bar_plot(dataset, date_column, delay_amount_column, plan_column, title='Plan_vs_Result_daily'):
    """
    1軸目: 積み上げ棒グラフと系列棒グラフ組み合わせ
    2軸目: 折れ線グラフ
    """
    fig, ax = plt.subplots(1,1,figsize=(10,2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
    lst_column = dataset.columns.to_list()
    lst_column.remove(str(date_column))
    lst_column.remove(str(delay_amount_column))
    
    lst_color = ['#1B66DF', '#E45F2B', '#F6C445', '#72FA93', 'green', 'blue'] # 色
    color_palette = lst_color[:(len(lst_column) - 1)]
    print((len(lst_column) - 1))
    bottom = 0
    counter = 0
    for column in lst_column:
        width = 0.4
        if column == plan_column: # 計画値は左側に表示
            ax.bar(dataset[date_column], dataset[column], align='edge', width=-0.4, color="grey", label=column)
        else: # その他は右側に積み上げて表示
            ax.bar(dataset[date_column], dataset[column], align='edge', width=width, bottom=bottom, color=color_palette[counter], label=column)
            bottom += np.array(dataset[column])
            counter += 1
    ax.set_xticks(dataset[date_column])
    ax.legend()
    ax.set_ylim(0, 20)
    ax.set_title(title)
    # 2軸目
    ax2 = ax.twinx() #2軸目を作成
    ax2.plot(dataset[date_column], dataset[delay_amount_column], marker='o', markerfacecolor='grey', markeredgecolor='blue', linestyle='--')
    
    for x, y in zip(dataset[date_column], dataset[delay_amount_column]):
        # TODO 表示文字のフォントサイズの変数化
        ax2.text(x , y, int(y), ha='center', va='bottom', weight='bold')

    ax2.set_ylim(0, 50)
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
    ax2.grid(False)
    plt.show()
if __name__ == '__main__':
    make_bar_plot(dataset, date_column='date', delay_amount_column='delay', plan_column='keikaku')