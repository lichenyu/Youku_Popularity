from datetime import date
from datetime import timedelta

def extract_daily_viewcount(inpath, outfile, start_date, days_2end, monitoring_length):
    day_delta = timedelta(days = 1)
    first_date = date(int(start_date[0 : 4]), int(start_date[5 : 7]), int(start_date[8 : 10]))
    # from start to end of the first day
    for i in range(0, days_2end):
        print(first_date)
        cur_date = first_date
        # total monitoring period
        for j in range(0, monitoring_length):
            print('\t' + str(first_date) + '_' + str(cur_date))
            cur_date = cur_date + day_delta
        first_date = first_date + day_delta

if '__main__' == __name__:
    workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/'
    extract_daily_viewcount('', '', '2015-12-06', 5, 30)