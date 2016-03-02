
def get_video_lifetime(in_file, out_file, adv_abs, adv_rel, min_inactive_days):
    in_fd = open(in_file, 'r')
    out_fd = open(out_file, 'w')
    for line in in_fd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, vci1, vci2, ..., vci30
        vci_list = []
        pct_list = []
        for i in range(1, 1 + 30):
            vci_list.append(int(fields[i]))
        s = sum(vci_list)
        if 0 == s:
            continue
        for i in range(0, 30):
            pct_list.append(1. * vci_list[i] / s)
        inactive_day_count = 0
        for i in range(29, -1, -1):
            if adv_abs > vci_list[i] and adv_rel > pct_list[i]:
                inactive_day_count = inactive_day_count + 1
            else:
                break
        if min_inactive_days <= inactive_day_count:
            lifetime = 30 - inactive_day_count
        else:
            lifetime = 31 
        out_fd.write(fields[0] + '\t' + str(lifetime) + '\n')
#         out_fd.write(fields[0])
#         out_fd.write('\n')
#         for i in range(0, 30):
#             out_fd.write(str(vci_list[i]) + '\t')
#         out_fd.write('\n')
#         for i in range(0, 30):
#             out_fd.write(str('%.02f' % pct_list[i]) + '\t')
#         out_fd.write('\n')
#         out_fd.write(str(lifetime) + '\n')
    in_fd.close()
    out_fd.close()
    
def get_video_first_lifetime(in_file, out_file, adv_abs, adv_rel, min_inactive_days):
    in_fd = open(in_file, 'r')
    out_fd = open(out_file, 'w')
    for line in in_fd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, vci1, vci2, ..., vci30
        vci_list = []
        pct_list = []
        for i in range(1, 1 + 30):
            vci_list.append(int(fields[i]))
        s = sum(vci_list)
        if 0 == s:
            continue
        for i in range(0, 30):
            pct_list.append(1. * vci_list[i] / s)
        inactive_day_count = 0
        idx = -1
        for i in range(0, 30):
            if adv_abs > vci_list[i] and adv_rel > pct_list[i]:
                inactive_day_count = inactive_day_count + 1
            else:
                inactive_day_count = 0
            if min_inactive_days <= inactive_day_count:
                idx = i
                break
        if 0 < idx:
            lifetime = idx + 1 - min_inactive_days
        else:
            lifetime = 31
        out_fd.write(fields[0] + '\t' + str(lifetime) + '\n')
#         out_fd.write(fields[0])
#         out_fd.write('\n')
#         for i in range(0, 30):
#             out_fd.write(str(vci_list[i]) + '\t')
#         out_fd.write('\n')
#         for i in range(0, 30):
#             out_fd.write(str('%.02f' % pct_list[i]) + '\t')
#         out_fd.write('\n')
#         out_fd.write(str(lifetime) + '\n')
    in_fd.close()
    out_fd.close()

if '__main__' == __name__:
    workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'
    
    get_video_lifetime(workpath + 'data/vci_files/vci', 
                       workpath + 'characterization/video_lifetime/video_lifetime', 
                       100, 1.5 / 30, 5)

    get_video_first_lifetime(workpath + 'data/vci_files/vci', 
                             workpath + 'characterization/video_lifetime/video_first_lifetime', 
                             100, 1.5 / 30, 5)
        
    print('All Done!')
    
    
    