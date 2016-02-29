import json
from datetime import date
from datetime import timedelta
    
def get_popularity_metrics(in_files, out_file):
    out_fd = open(out_file, 'w')    
    for f in in_files:
        print('Processing ' + f)
        in_fd = open(f, 'r')
        for line in in_fd.readlines():
            video_json = json.loads(line)
            out_fd.write(video_json['id'] + '\t' + str(video_json['view_count']) + '\t' + str(video_json['comment_count']) + '\t' + \
                         str(video_json['favorite_count']) + '\t' + str(video_json['up_count']) + '\t' + str(video_json['down_count']) + '\n')
        in_fd.close()
    out_fd.close()

if '__main__' == __name__:
    datapath = '/Users/ouyangshuxin/Documents/Youku_Popularity/'
    workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'
    
    date_strs = ['2015-12-06', '2015-12-07', '2015-12-08', '2015-12-09', '2015-12-10', 
                '2015-12-11', '2015-12-12', '2015-12-13', '2015-12-14', '2015-12-15', 
                '2015-12-16', '2015-12-17', '2015-12-18', '2015-12-19', '2015-12-20', 
                '2015-12-21', '2015-12-22', '2015-12-23', '2015-12-24', '2015-12-26', 
                '2015-12-27', '2015-12-28', '2015-12-29', '2015-12-30', '2015-12-31', 
                '2016-01-01', '2016-01-02', '2016-01-03', '2016-01-04']
    
    in_files = []
    for start_date in date_strs:
        day_delta = timedelta(days = 29)
        first_date = date(int(start_date[0 : 4]), int(start_date[5 : 7]), int(start_date[8 : 10]))
        last_date = first_date + day_delta
        in_files.append(datapath + 'rawdata/detail_json/' + str(first_date) + '_' + str(last_date))
    get_popularity_metrics(in_files, workpath + 'characterization/popularity_metrics/metrics')
    
    print('All Done!')