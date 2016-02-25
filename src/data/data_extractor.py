from datetime import date
from datetime import timedelta
import json

def extract_daily_viewcount(vid_path, json_path, out_path, start_date, days_2end, monitoring_length):
    # for date calculation
    day_delta = timedelta(days = 1)
    first_date = date(int(start_date[0 : 4]), int(start_date[5 : 7]), int(start_date[8 : 10]))
    
    # for each first date, from start to end of the monitoring period
    for i in range(0, days_2end):
        # get vid list
        vid_fd = open(vid_path + str(first_date))
        vid_vc_map = {}
        for line in vid_fd.readlines():
            vid_vc_map[line.strip()] = []
        vid_fd.close()
        
        # iterate monitoring period
        cur_date = first_date
        for j in range(0, monitoring_length):
            # put info for one certain day into the tmp map
            json_fd = open(json_path + str(first_date) + '_' + str(cur_date))
            vid_vc_tmpmap = {}
            for line in json_fd.readlines():
                video_json = json.loads(line)
                vid_vc_tmpmap[video_json['id']] = int(video_json['view_count'])
            json_fd.close()
            
            # fill map by tmp map
            for vid in vid_vc_map.keys():
                if vid_vc_tmpmap.has_key(vid):
                    vid_vc_map[vid].append(vid_vc_tmpmap[vid])
                else:
                    vid_vc_map[vid].append(-1)
            
            cur_date = cur_date + day_delta
        
        first_date = first_date + day_delta

if '__main__' == __name__:
    workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/'
    #extract_daily_viewcount('', '', '2015-12-06', 5, 30)