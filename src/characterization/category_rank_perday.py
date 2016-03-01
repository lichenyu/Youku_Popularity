# -*- coding: utf-8 -*-

import codecs

# get trans_name by the first day
def get_transmap(in_file, out_file):
    in_fd = codecs.open(in_file, 'r', 'utf-8')
    cat_count_map = {}
    for line in in_fd.readlines():
        fields = line.strip().split('\t', -1)
        # cat, video_count_percat, collected_count_percat
        cat_count_map[fields[0]] = int(fields[1])
    in_fd.close()
    
    sorted_map = sorted(cat_count_map.items(), lambda i1, i2: cmp(i1[1], i2[1]))
    for i in range(0, len(sorted_map)):
        cat_count_map[sorted_map[i][0]] = i + 1
    
    out_fd = open(out_file, 'w')
    for k in cat_count_map.keys():
        out_fd.write(k.encode('utf-8') + '\t' + str(cat_count_map[k]) + '\n')
    out_fd.close()
    return cat_count_map

# get (transformed) rank of each cat
def get_cat_rank_perday(in_files, out_file, transmap):
    out_fd = open(out_file, 'w')
    for f in in_files:
        # get count of each cat
        in_fd = codecs.open(f, 'r', 'utf-8')
        cat_count_map = {}
        for line in in_fd.readlines():
            fields = line.strip().split('\t', -1)
            # cat, video_count_percat, collected_count_percat
            cat_count_map[transmap[fields[0]]] = int(fields[1])
        in_fd.close()
        # rank
        sorted_map = sorted(cat_count_map.items(), lambda i1, i2: cmp(i1[1], i2[1]))
        for i in range(0, len(sorted_map)):
            cat_count_map[sorted_map[i][0]] = i + 1
        # output
        for i in range(0, len(transmap)):
            out_fd.write(str(cat_count_map[i + 1]) + '\t')
        out_fd.write('\n')
    out_fd.close()

def get_cat_pct(infile):
    in_fd = codecs.open(infile, 'r', 'utf-8')
    cat_count_map = {}
    total_count = 0
    for line in in_fd.readlines():
        fields = line.strip().split('\t', -1)
        # cat, video_count_percat, collected_count_percat
        cat_count_map[fields[0]] = int(fields[1])
        total_count = total_count + int(fields[1])
    in_fd.close()
    sorted_map = sorted(cat_count_map.items(), lambda i1, i2: cmp(i1[1], i2[1]), reverse = True)
    cat_pct = []
    for i in range(0, len(cat_count_map)):
        cat_pct.append([sorted_map[i][0], sorted_map[i][1] * 1. / total_count])
    return cat_pct


if '__main__' == __name__:
    datapath = '/Users/ouyangshuxin/Documents/Youku_Popularity/'
    workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'
#     datapath = 'F:/Youku_Popularity/'
#     workpath = 'F:/Youku_Popularity/Youku_Popularity/'
    
    date_strs = ['2015-12-06', '2015-12-07', '2015-12-08', '2015-12-09', '2015-12-10', 
                '2015-12-11', '2015-12-12', '2015-12-13', '2015-12-14', '2015-12-15', 
                '2015-12-16', '2015-12-17', '2015-12-18', '2015-12-19', '2015-12-20', 
                '2015-12-21', '2015-12-22', '2015-12-23', '2015-12-24', '2015-12-26', 
                '2015-12-27', '2015-12-28', '2015-12-29', '2015-12-30', '2015-12-31', 
                '2016-01-01', '2016-01-02', '2016-01-03', '2016-01-04']
   
    transmap = get_transmap(datapath + 'rawdata/total_count/' + date_strs[0], 
                            workpath + 'characterization/category_rank/category_nametrans')
    
    in_files = []
    for date in date_strs:
        in_files.append(datapath + 'rawdata/total_count/' + date)
    get_cat_rank_perday(in_files, 
                        workpath + 'characterization/category_rank/cat_rank_perday', 
                        transmap)
    
    print('All Done!')