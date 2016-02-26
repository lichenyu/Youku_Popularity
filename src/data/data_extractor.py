from datetime import date
from datetime import timedelta
import json

def extract_daily_viewcount(vid_path, json_path, out_path, start_date, days_2end, monitoring_length):
    # for date calculation
    day_delta = timedelta(days = 1)
    first_date = date(int(start_date[0 : 4]), int(start_date[5 : 7]), int(start_date[8 : 10]))
    
    # for each first date, from start to end of the monitoring period
    for i in range(0, days_2end):
        print('Processing videos published on ' + str(first_date))
        
        # get vid list
        vid_fd = open(vid_path + str(first_date), 'r')
        vid_vc_map = {}
        for line in vid_fd.readlines():
            vid_vc_map[line.strip()] = []
        vid_fd.close()
        
        # iterate monitoring period
        cur_date = first_date
        for j in range(0, monitoring_length):
            print('Iterating file ' + str(first_date) + '_' + str(cur_date))
            
            # put info for one certain day into the tmp map
            json_fd = open(json_path + str(first_date) + '_' + str(cur_date), 'r')
            vid_vc_tmpmap = {}
            for line in json_fd.readlines():
                video_json = json.loads(line)
                vid_vc_tmpmap[video_json['id']] = int(video_json['view_count'])
            json_fd.close()
            
            # fill map by tmp map for one-day vc
            for vid in vid_vc_map.keys():
                if vid_vc_tmpmap.has_key(vid):
                    vid_vc_map[vid].append(vid_vc_tmpmap[vid])
                else:
                    vid_vc_map[vid].append(-1)
            
            cur_date = cur_date + day_delta
            
        # output vid_vc_map
        out_fd = open(out_path + str(first_date), 'w')
        for vid in vid_vc_map.keys():
            out_fd.write(vid)
            for vc in vid_vc_map[vid]:
                out_fd.write('\t' + str(vc))
            out_fd.write('\n')
        out_fd.close()
        
        first_date = first_date + day_delta
        
def check_increase(in_path, out_path, start_date, days_2end):
    # for date calculation
    day_delta = timedelta(days = 1)
    first_date = date(int(start_date[0 : 4]), int(start_date[5 : 7]), int(start_date[8 : 10]))
    
    for i in range(0, days_2end):
        in_fd = open(in_path + str(first_date), 'r')
        out_fd = open(out_path + str(first_date), 'w')
        for line in in_fd.readlines():
            fields = line.strip().split('\t', -1)
            save_flag = False
            # vid, vc1, vc2, ..., vc30
            for j in range(30, 1, -1):
                if (-1 != int(fields[j])) and (int(fields[j-1]) > int(fields[j])):
                    save_flag = True
                    break
            for j in range(1, 31):
                if -1 == int(fields[j]):
                    save_flag = False
            if save_flag:
                out_fd.write(line)
        in_fd.close()
        out_fd.close()
        first_date = first_date + day_delta
        
def check_lost(in_path, out_path, start_date, days_2end):
    # for date calculation
    day_delta = timedelta(days = 1)
    first_date = date(int(start_date[0 : 4]), int(start_date[5 : 7]), int(start_date[8 : 10]))
    
    for i in range(0, days_2end):
        in_fd = open(in_path + str(first_date), 'r')
        out_fd = open(out_path + str(first_date), 'w')
        for line in in_fd.readlines():
            fields = line.strip().split('\t', -1)
            save_flag = False
            # vid, vc1, vc2, ..., vc30
            for j in range(1, 31):
                if -1 == int(fields[j]):
                    save_flag = True
                    break
            if save_flag:
                out_fd.write(line)
        in_fd.close()
        out_fd.close()
        first_date = first_date + day_delta
        
def clean_data(in_path, out_path, start_date, days_2end):
    # for date calculation
    day_delta = timedelta(days = 1)
    first_date = date(int(start_date[0 : 4]), int(start_date[5 : 7]), int(start_date[8 : 10]))
    
    for i in range(0, days_2end):
        in_fd = open(in_path + str(first_date), 'r')
        out_fd = open(out_path + str(first_date), 'w')
        for line in in_fd.readlines():
            fields = line.strip().split('\t', -1)
            # vid, vc1, vc2, ..., vc30
            # process lost
            lost_count = 0
            lost_idx = -1
            for j in range(1, 31):
                if -1 == int(fields[j]):
                    lost_count = lost_count + 1
                    lost_idx = j
            if 1 == lost_count:
                if 30 == lost_idx:
                    fields[30] = fields[29]
                elif 1 == lost_idx:
                    fields[1] = fields[2]
                else:
                    fields[lost_idx] = str((int(fields[lost_idx + -1]) + int(fields[lost_idx + 1])) / 2)
            elif 1 < lost_count:
                continue
            # process increase
            for j in range(30, 1, -1):
                if int(fields[j-1]) > int(fields[j]):
                    fields[j-1] = fields[j]
            # output
            out_fd.write(fields[0])
            for j in range(1, 31):
                out_fd.write('\t' + fields[j])
            out_fd.write('\n')
        in_fd.close()
        out_fd.close()
        
        first_date = first_date + day_delta
        
def merge_files(in_files, out_file):
    out_fd = open(out_file, 'w')
    for f in in_files:
        in_fd = open(f, 'r')
        for line in in_fd.readlines():
            out_fd.write(line)
        in_fd.close()
    out_fd.close()
    
def get_vci(in_file, out_file):
    in_fd = open(in_file, 'r')
    out_fd = open(out_file, 'w')
    for line in in_fd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, vc1, vc2, ..., vc30
        out_fd.write(fields[0] + '\t' + fields[1])
        for i in range(2, 31):
            out_fd.write('\t' + str(int(fields[i]) - int(fields[i-1])))
        out_fd.write('\n')
    in_fd.close()
    out_fd.close()

if '__main__' == __name__:
    workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'
    
    # do not get list on 2015-12-25
#     extract_daily_viewcount(workpath + 'rawdata/vid/', 
#                             workpath + 'rawdata/detail_json/', 
#                             workpath + 'data/all_extracted/', 
#                             '2015-12-06', 19, 30)
#     extract_daily_viewcount(workpath + 'rawdata/vid/', 
#                             workpath + 'rawdata/detail_json/', 
#                             workpath + 'data/all_extracted/', 
#                             '2015-12-26', 10, 30)

#     check_lost(workpath + 'data/all_extracted/', 
#                workpath + 'data/check_lost/', 
#                '2015-12-06', 19)
#     check_lost(workpath + 'data/all_extracted/', 
#                workpath + 'data/check_lost/', 
#                '2015-12-26', 10)
#     check_increase(workpath + 'data/all_extracted/', 
#                    workpath + 'data/check_increase/', 
#                    '2015-12-06', 19)
#     check_increase(workpath + 'data/all_extracted/', 
#                    workpath + 'data/check_increase/', 
#                    '2015-12-26', 10)

#     clean_data(workpath + 'data/all_extracted/', 
#                workpath + 'data/clean_data/', 
#                '2015-12-06', 19)
#     clean_data(workpath + 'data/all_extracted/', 
#                workpath + 'data/clean_data/', 
#                '2015-12-26', 10)
    
#     check_lost(workpath + 'data/clean_data/', 
#                workpath + 'data/check_lost2/', 
#                '2015-12-06', 19)
#     check_lost(workpath + 'data/clean_data/', 
#                workpath + 'data/check_lost2/', 
#                '2015-12-26', 10)
#     check_increase(workpath + 'data/clean_data/', 
#                    workpath + 'data/check_increase2/', 
#                    '2015-12-06', 19)
#     check_increase(workpath + 'data/clean_data/', 
#                    workpath + 'data/check_increase2/', 
#                    '2015-12-26', 10)

    date_strs = ['2015-12-06', '2015-12-07', '2015-12-08', '2015-12-09', '2015-12-10', 
                '2015-12-11', '2015-12-12', '2015-12-13', '2015-12-14', '2015-12-15', 
                '2015-12-16', '2015-12-17', '2015-12-18', '2015-12-19', '2015-12-20', 
                '2015-12-21', '2015-12-22', '2015-12-23', '2015-12-24', '2015-12-26', 
                '2015-12-27', '2015-12-28', '2015-12-29', '2015-12-30', '2015-12-31', 
                '2016-01-01', '2016-01-02', '2016-01-03', '2016-01-04']
    
#     for date in date_strs:
#         get_vci(workpath + 'data/clean_data/' + date, workpath + 'data/vci_files/' + date)
    
    in_files = []
    for date in date_strs:
        in_files.append(workpath + 'data/vci_files/' + date)
    merge_files(in_files, workpath + 'data/vci_files/vci')
    
    print('All Done!')
    
    