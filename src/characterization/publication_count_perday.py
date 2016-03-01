# -*- coding: utf-8 -*-

import json
    
def get_uploader_count(vid_file, json_file):
    vid_set = set()
    vid_fd = open(vid_file, 'r')
    for line in vid_fd.readlines():
        vid_set.add(line.strip())
    vid_fd.close()
    
    json_fd = open(json_file, 'r')
    uploader_set = set()
    for line in json_fd.readlines():
        video_json = json.loads(line)
        if (video_json['id'] in vid_set) and (False == (video_json['user']['id'] in uploader_set)):
            uploader_set.add(video_json['user']['id'])
    json_fd.close()
    
    return len(uploader_set)

def get_uploader_count_perday(vid_files, json_files, out_file):
    out_fd = open(out_file, 'w')
    for i in range(0, len(vid_files)):
        print('Processing ' + vid_files[i])
        uc = get_uploader_count(vid_files[i], json_files[i])
        out_fd.write(str(uc) + '\n')
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
    for date in date_strs:
        vid_files.append(workpath + 'data/vid/' + date)
    json_files = []
    for date in date_strs:
        json_files.append(datapath + 'rawdata/detail_json/' + date + '_' + date)
    get_uploader_count_perday(vid_files, 
                              json_files, 
                              workpath + 'characterization/publication_perday/uploader_count_perday')
    
    print('All Done!')