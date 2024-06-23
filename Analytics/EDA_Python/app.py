# from dataprep.eda import create_report
# import pandas as pd
# dataset_df = pd.read_csv("Salary Data.csv")
# report_df = create_report(dataset_df)
# report_df.save("EDA.html")

# report_df.show_browser()

# ----------------------------------------------------------------------- #
# from ascii_magic import AsciiArt
# art = AsciiArt.from_image('Picture1.png')
# art.to_terminal(columns=50)

# ----------------------------------------------------------------------- #
# from calendar import calendar
# y = calendar(2024)
# print(y)

# ----------------------------------------------------------------------- #
# import calendar
# m = calendar.month(2024, 2)
# print(m)

# ----------------------------------------------------------------------- #
# from colorama import Fore
# from pyfiglet import figlet_format
# f = figlet_format("Chirag")
# print(Fore.BLUE + f)

# ----------------------------------------------------------------------- #
# import sys
# import time
# def loading_spinner():
#     for _ in range(10):
#         sys.stdout.write("\rLoading |")
#         time.sleep(0.1)
#         sys.stdout.write("\rLoading /")
#         time.sleep(0.1)
#         sys.stdout.write("\rLoading -")
#         time.sleep(0.1)
#         sys.stdout.write("\rLoading \\")
#         time.sleep(0.1)
#     print("\nLoading complete!")
# loading_spinner()

# ----------------------------------------------------------------------- #
# import time
# def countdown_timer(seconds):
#     while seconds:
#         mins, secs = divmod(seconds, 60)
#         timeformat = '{:02d}:{:02d}'.format(mins, secs)
#         print(timeformat, end='\r')
#         time.sleep(1)
#         seconds -= 1
#     print("Time's up!")
# countdown_timer(10)


# %pip install xlsxwriter
# import pandas as pd
# import os
# import xlsxwriter
# data_df = pd.read_csv("fifa_eda_stats.csv", encoding='utf-8', encoding_errors='ignore')
# left_foot_df = data_df.groupby('Preferred Foot').get_group('Left')
# right_foot_df = data_df.groupby('Preferred Foot').get_group('Right')
# xlwriter = pd.ExcelWriter('final_excel.xlsx',engine='xlsxwriter')
# left_foot_df.to_excel(excel_writer=xlwriter, sheet_name='left_foot', index=False)
# right_foot_df.to_excel(excel_writer=xlwriter, sheet_name='right_foot', index=False)
# xlwriter.close()
