# get i7 pattern and early burst by i1-i7
# get future burst by sequence file and (i7 pattern + threshold)

def get_early_pattern(vci_file, burst_rate, quasi_burst_rate, out_file):
    vci_fd = open(vci_file, 'r')
    out_fd = open(out_file, 'w')
    for line in vci_fd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, vci1, vci2, ..., vci30
        early_vci_list = []
        for i in range(1, 1 + 7):
            early_vci_list.append(int(fields[i]))
        early_pct_list = []
        for i in range(0, len(early_vci_list)):
            if 0 == sum(early_vci_list):
                early_pct_list.append(0)
            else:
                early_pct_list.append(1. * early_vci_list[i] / sum(early_vci_list))
        early_pattern_list = []
        for i in range(0, len(early_vci_list)):
            if burst_rate <= early_pct_list[i]:
                early_pattern_list.append(1)
            else:
                early_pattern_list.append(0)
        for i in range(0, len(early_vci_list) - 1):
            if (1 == early_pattern_list[i]) and (0 == early_pattern_list[i + 1]) and (quasi_burst_rate < early_pct_list[i + 1]):
                early_pattern_list[i + 1] = 1
        for i in range(len(early_vci_list) - 1, 0, -1):
            if (1 == early_pattern_list[i]) and (0 == early_pattern_list[i - 1]) and (quasi_burst_rate < early_pct_list[i - 1]):
                early_pattern_list[i - 1] = 1
        out_fd.write(fields[0] + '\t')
        for i in range(0, len(early_pattern_list)):
            out_fd.write(str(early_pattern_list[i]))
        out_fd.write('\n')
        
#         out_fd.write(fields[0] + '\n')
#         for i in range(0, len(early_vci_list)):
#             out_fd.write(str(early_vci_list[i]) + '\t')
#         out_fd.write('\n')
#         for i in range(0, len(early_pct_list)):
#             out_fd.write(str(early_pct_list[i]) + '\t')
#         out_fd.write('\n')
#         for i in range(0, len(early_pattern_list)):
#             out_fd.write(str(early_pattern_list[i]))
#         out_fd.write('\n')
#         for i in range(0, len(early_vci_list)):
#             out_fd.write(str(sum(early_vci_list[0 : i + 1])) + '\t')
#         out_fd.write('\n')
#         out_fd.write('\n')
    vci_fd.close()
    out_fd.close()
    
def count_results(in_file, out_file, result_idx):
    in_fd = open(in_file, 'r')
    result_map = {}
    total = 0
    for line in in_fd.readlines():
        fields = line.strip().split('\t', -1)
        rslt = fields[result_idx]
        if False == (rslt in result_map):
            result_map[rslt] = 1
        else:
            result_map[rslt] = result_map[rslt] + 1
        total = total + 1
    in_fd.close()
    sorted_list = sorted(result_map.items(), lambda i1, i2: cmp(i1[1], i2[1]), reverse = True)
    out_fd = open(out_file, 'w')
    for v in sorted_list:
        out_fd.write(v[0] + '\t' + str(v[1]) + '\t%.02f' % (v[1] * 100. / total) + '%\n')
    out_fd.close()
    
def get_future_label(earlypattern_file, vci_file, ear1_frac, ear0_frac, out_file):
    earlyburst_set = set()
    earlypattern_fd = open(earlypattern_file, 'r')
    for line in earlypattern_fd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, early_pattern
        for i in range(0, len(fields[1])):
            if '1' == fields[1][i]:
                earlyburst_set.add(fields[0])
                break
    earlypattern_fd.close()
    
    vci_fd = open(vci_file, 'r')
    out_fd = open(out_file, 'w')
    for line in vci_fd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, vci1, vci2, ..., vci30
        vci_list = []
        for i in range(1, 1 + 30):
            vci_list.append(int(fields[i]))
        
        # 1 in early pattern
        if fields[0] in earlyburst_set:
            if 0 == sum(vci_list):
                continue
            if ear1_frac <= (1. * sum(vci_list[7 : 30]) / sum(vci_list)):
                out_fd.write(line.strip() + '\tTrue\n')
            else:
                out_fd.write(line.strip() + '\tFalse\n')
        # no 1 in early pattern
        else:
            if 0 == sum(vci_list):
                continue
            if ear0_frac <= (1. * sum(vci_list[7 : 30]) / sum(vci_list)):
                out_fd.write(line.strip() + '\tTrue\n')
            else:
                out_fd.write(line.strip() + '\tFalse\n')
    vci_fd.close()
    out_fd.close()
    
    

if '__main__' == __name__:
    workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'
    
#     get_early_pattern(workpath + 'data/vci_files/vci', 
#                       2.5 * 1 / 7, 1. * 1 / 7, 
#                       workpath + 'prediction/early_pattern_future_burst/early_pattern')
#     
#     count_results(workpath + 'prediction/early_pattern_future_burst/early_pattern', 
#                   workpath + 'prediction/early_pattern_future_burst/early_pattern_count', 
#                   1)

    get_future_label(workpath + 'prediction/early_pattern_future_burst/early_pattern', 
                     workpath + 'data/vci_files/vci', 
                     0.8 * 23 / 30, 1.2 * 23 / 30, 
                     workpath + 'prediction/early_pattern_future_burst/future_label')

    print('All Done!')
