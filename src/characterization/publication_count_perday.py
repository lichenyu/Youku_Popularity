# -*- coding: utf-8 -*-

import codecs, json

def get_video_count(in_file):
    in_fd = codecs.open(in_file, 'r', 'utf-8')
    video_count = 0
    for line in in_fd.readlines():
        fields = line.strip().split('\t', -1)
        # cat, video_count_percat, collected_count_percat
        video_count = video_count + int(fields[1])
    in_fd.close()
    return video_count

def get_video_count_perday(in_files, out_file):
    video_perday = []
    for f in in_files:
        video_perday.append(get_video_count(f))
    out_fd = open(out_file, 'w')
    for p in video_perday:
        out_fd.write(str(p) + '\n')
    out_fd.close()
    
def get_uploader_count(in_file):
    in_fd = open(in_file, 'r')
    uploader_set = set()
    for line in in_fd.readlines():
        video_json = json.loads(line)
        if False == (video_json['user']['id'] in uploader_set):
            uploader_set.add(video_json['user']['id'])
    in_fd.close()
    return len(uploader_set)

def get_uploader_count_perday(in_files, out_file):
    uploader_perday = []
    for f in in_files:
        uploader_perday.append(get_uploader_count(f))
    out_fd = open(out_file, 'w')
    for p in uploader_perday:
        out_fd.write(str(p) + '\n')
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
    
#     in_files = []
#     for date in date_strs:
#         in_files.append(datapath + 'rawdata/total_count/' + date)
#     get_video_count_perday(in_files, workpath + 'characterization/publication_perday/video_count_perday')
    
#     in_files = []
#     for date in date_strs:
#         in_files.append(datapath + 'rawdata/detail_json/' + date + '_' + date)
#     get_uploader_count_perday(in_files, workpath + 'characterization/publication_perday/uploader_count_perday')
    
    print('All Done!')