import json
from datetime import date
from datetime import timedelta
    
def get_category_level(vid_files, json_files, out_file):
    out_fd = open(out_file, 'w')
    for i in range(0, len(vid_files)):
        vid_set = set()
        print('Processing ' + vid_files[i])
        vid_fd = open(vid_files[i], 'r')
        for line in vid_fd.readlines():
            vid_set.add(line.strip())
        vid_fd.close()
        
        json_fd = open(json_files[i], 'r')
        for line in json_fd.readlines():
            video_json = json.loads(line)
            if False == (video_json['id'] in vid_set):
                continue
            n30 = video_json['view_count']
            if n30 <= 90:
                out_fd.write(video_json['category'].encode('utf-8') + '\t')
                out_fd.write('1\n')
            elif n30 <= 1029:
                out_fd.write(video_json['category'].encode('utf-8') + '\t')
                out_fd.write('2\n')
            elif n30 <= 8756:
                out_fd.write(video_json['category'].encode('utf-8') + '\t')
                out_fd.write('3\n')
            elif n30 <= 92395:
                out_fd.write(video_json['category'].encode('utf-8') + '\t')
                out_fd.write('4\n')
            else:
                out_fd.write(video_json['category'].encode('utf-8') + '\t')
                out_fd.write('5\n')
        json_fd.close()
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
    
    vid_files = []
    json_files = []
    for start_date in date_strs:
        day_delta = timedelta(days = 29)
        first_date = date(int(start_date[0 : 4]), int(start_date[5 : 7]), int(start_date[8 : 10]))
        last_date = first_date + day_delta
        vid_files.append(workpath + 'data/vid/' + str(first_date))
        json_files.append(datapath + 'rawdata/detail_json/' + str(first_date) + '_' + str(last_date))
    get_category_level(vid_files, json_files, workpath + 'characterization/category_level/category_level')
    
    # pop metrics like this file 
    
    print('All Done!')