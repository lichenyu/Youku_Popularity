# get i7 pattern and early burst by i1-i7
# get future burst by sequence file and (i7 pattern + threshold)

def add_futureburst_2ifiles(vci_file, scale_val, scale_inc, pattern_file, ear1_frac, ear0_frac, label_file):
    # whether early burst exists -> early burst set
    # get early pattern
    earlyburst_set = set()
    vci_fd = open(vci_file, 'r')
    pattern_fd = open(pattern_file, 'w')
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
        # get early pattern
        early_state_list = []
        if scale_val <= early_pct_list[0]:
            early_state_list.append(1)
            earlyburst_set.add(fields[0])
        else:
            early_state_list.append(0)
        for i in range(1, len(early_pct_list)):
            if scale_inc <= (early_pct_list[i] - early_pct_list[i-1]):
                early_state_list.append(1)
                earlyburst_set.add(fields[0])
            else:
                early_state_list.append(0)
        pattern_fd.write(fields[0] + '\n')
        for i in range(0, len(early_vci_list)):
            pattern_fd.write(str(early_vci_list[i]) + '\t')
        pattern_fd.write('\n')
        for i in range(0, len(early_pct_list)):
            pattern_fd.write(str(early_pct_list[i]) + '\t')
        pattern_fd.write('\n')
        for i in range(0, len(early_state_list)):
            pattern_fd.write(str(early_state_list[i]))
        pattern_fd.write('\n')
        for i in range(0, len(early_vci_list)):
            pattern_fd.write(str(sum(early_vci_list[0 : i + 1])) + '\t')
        pattern_fd.write('\n')
        pattern_fd.write('\n')
    vci_fd.close()
    pattern_fd.close()
    
#     out_fd = open(out_file, 'w')
#     vci_fd = open(vci_file, 'r')
#     for line in vci_fd.readlines():
#         fields = line.strip().split('\t', -1)
#         # vid, vci1, vci2, ..., vci30
#         # check early 0 future 0 with ear0_frac
#         if False == (fields[0] in earlyburst_set) and False == (fields[0] in futureburst_set):
#             vci_list = []
#             for i in range(1, 31):
#                 vci_list.append(int(fields[i]))
#             if 0 == sum(vci_list):
#                 continue
#             if ear0_frac <= (1. * sum(vci_list[7 : 30]) / sum(vci_list)):
#                 out_fd.write(line.strip() + '\tTrue\n')
#             else:
#                 pass#out_fd.write(line.strip() + '\tFalse\n')
#         # check early 1 future 0 with ear1_frac
#         elif True == (fields[0] in earlyburst_set) and False == (fields[0] in futureburst_set):
#             vci_list = []
#             for i in range(1, 31):
#                 vci_list.append(int(fields[i]))
#             if 0 == sum(vci_list):
#                 continue
#             if ear1_frac <= (1. * sum(vci_list[7 : 30]) / sum(vci_list)):
#                 out_fd.write(line.strip() + '\tTrue\n')
#             else:
#                 pass#out_fd.write(line.strip() + '\tFalse\n')
#         # for early 0 future 1
#         elif False == (fields[0] in earlyburst_set) and True == (fields[0] in futureburst_set):
#             pass#out_fd.write(line.strip() + '\tTrue\n')
#         # for early 1 future 1
#         elif True == (fields[0] in earlyburst_set) and True == (fields[0] in futureburst_set):
#             pass#out_fd.write(line.strip() + '\tTrue\n')
#         else:
#             print('Impossible: ' + fields[0])
#     vci_fd.close()    
#     out_fd.close()



if '__main__' == __name__:
    workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'
    
    add_futureburst_2ifiles(workpath + 'data/vci_files/vci', 
                            3. * 1 / 7, 2. * 1 / 7, 
                            workpath + 'prediction/early_pattern_future_burst/early_pattern', 
                            0.6 * 23 / 30, 1.2 * 23 / 30, 
                            '')

    print('All Done!')
