import json, time
    
def get_pubtime_count(in_files, out_file):
    pubtime_count_map = {}
    for f in in_files:
        in_fd = open(f, 'r')
        for line in in_fd.readlines():
            video_json = json.loads(line)
            date_str = video_json['published']
            pubtime = time.strptime(date_str, '%Y-%m-%d %H:%M:%S').tm_hour
            if pubtime_count_map.has_key(pubtime):
                pubtime_count_map[pubtime] = pubtime_count_map[pubtime] + 1
            else:
                pubtime_count_map[pubtime] = 1
        in_fd.close()
    out_fd = open(out_file, 'w')
    for t in pubtime_count_map:
        out_fd.write(str(t) + '\t' + str(pubtime_count_map[t]) + '\n')
    out_fd.write('\n')
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
    for date in date_strs:
        in_files.append(datapath + 'rawdata/detail_json/' + date + '_' + date)
    get_pubtime_count(in_files, workpath + 'characterization/pubtime_hist/pubtime_count')
    
    print('All Done!')