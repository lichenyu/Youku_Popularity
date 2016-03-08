def get_vci_pct(in_file, out_file):
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
        # get pct
        out_fd.write(fields[0] + '\n')
        for i in range(0, 30):
            out_fd.write(str(vci_list[i]) + '\t')
        out_fd.write('\n')
        for i in range(0, 30):
            out_fd.write(str(pct_list[i]) + '\t')
        out_fd.write('\n')
    in_fd.close()
    out_fd.close()
    
def get_state_sequence(in_file, out_file, min_inc, avg_scale):
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
        state_list = []
        if avg_scale <= pct_list[0]:
            state_list.append(1)
        else:
            state_list.append(0)
        for i in range(1, 30):
            if min_inc <= (pct_list[i] - pct_list[i-1]):
                state_list.append(1)
            else:
                state_list.append(0)
        # --------------------------------------------------
        # for two pct >= 0.8 * burst_rel, 00 - > 11
        for i in range(0, 29):
            if (0.8 * avg_scale <= pct_list[i]) and (0.8 * avg_scale <= pct_list[i+1]):
                state_list[i] = 1
                state_list[i+1] = 1
        # --------------------------------------------------
        # for three pct >= 0.7 * burst_rel, 000 - > 111
        for i in range(0, 28):
            if (0.7 * avg_scale <= pct_list[i]) and (0.7 * avg_scale <= pct_list[i+1]) and (0.7 * avg_scale <= pct_list[i+2]):
                state_list[i] = 1
                state_list[i+1] = 1
                state_list[i+2] = 1
        # --------------------------------------------------
        # for four pct >= 0.6 * burst_rel, 0000 - > 1111
        for i in range(0, 27):
            if (0.6 * avg_scale <= pct_list[i]) and (0.6 * avg_scale <= pct_list[i+1]) and \
            (0.6 * avg_scale <= pct_list[i+2]) and (0.6 * avg_scale <= pct_list[i+3]):
                state_list[i] = 1
                state_list[i+1] = 1
                state_list[i+2] = 1
                state_list[i+3] = 1
        # --------------------------------------------------
        out_fd.write(fields[0] + '\t' + str(sum(vci_list)) + '\t')
        for i in range(0, 30):
            out_fd.write(str(state_list[i]))
        out_fd.write('\n')
    in_fd.close()
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
    
def merge_sequence(in_file, out_file):
    in_fd = open(in_file, 'r')
    out_fd = open(out_file, 'w')
    for line in in_fd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, n30, seq
        sequence = []
        for i in range(0, 30):
            sequence.append(fields[2][i])
        for i in range(1, 29):
            if '0' == sequence[i] and '1' == sequence[i - 1] and '1' == sequence[i + 1]:
                sequence[i] = '1'
        out_fd.write(fields[0] + '\t' + fields[1] + '\t')
        cur_state = ''
        for i in range(0, 30):
            if cur_state != sequence[i]:
                out_fd.write(sequence[i])
                cur_state = sequence[i]
        out_fd.write('\n')
    in_fd.close()
    out_fd.close()

if '__main__' == __name__:
    workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'
    
    get_vci_pct(workpath + 'data/vci_files/vci',
                workpath + 'characterization/evolution_pattern/vci_pct')
    
    
    
    get_state_sequence(workpath + 'data/vci_files/vci', 
                       workpath + 'characterization/evolution_pattern/state_sequence', 
                       1. * 2 / 30, 1. * 3 / 30)
     
    count_results(workpath + 'characterization/evolution_pattern/state_sequence', 
                  workpath + 'characterization/evolution_pattern/state_sequence_count', 
                  2)
    
    merge_sequence(workpath + 'characterization/evolution_pattern/state_sequence', 
                   workpath + 'characterization/evolution_pattern/evolution_pattern')
    
    count_results(workpath + 'characterization/evolution_pattern/evolution_pattern', 
                  workpath + 'characterization/evolution_pattern/evolution_pattern_count', 
                  2)
       
       
       
    get_state_sequence(workpath + 'data/vci_files/vci_level1', 
                       workpath + 'characterization/evolution_pattern/state_sequence_level1', 
                       1. * 2 / 30, 1. * 3 / 30)
    merge_sequence(workpath + 'characterization/evolution_pattern/state_sequence_level1', 
                   workpath + 'characterization/evolution_pattern/evolution_pattern_level1')
    count_results(workpath + 'characterization/evolution_pattern/evolution_pattern_level1', 
                  workpath + 'characterization/evolution_pattern/evolution_pattern_count_level1', 
                  2)
        
    get_state_sequence(workpath + 'data/vci_files/vci_level2', 
                       workpath + 'characterization/evolution_pattern/state_sequence_level2', 
                       1. * 2 / 30, 1. * 3 / 30)
    merge_sequence(workpath + 'characterization/evolution_pattern/state_sequence_level2', 
                   workpath + 'characterization/evolution_pattern/evolution_pattern_level2')
    count_results(workpath + 'characterization/evolution_pattern/evolution_pattern_level2', 
                  workpath + 'characterization/evolution_pattern/evolution_pattern_count_level2', 
                  2)
        
    get_state_sequence(workpath + 'data/vci_files/vci_level3', 
                       workpath + 'characterization/evolution_pattern/state_sequence_level3', 
                       1. * 2 / 30, 1. * 3 / 30)
    merge_sequence(workpath + 'characterization/evolution_pattern/state_sequence_level3', 
                   workpath + 'characterization/evolution_pattern/evolution_pattern_level3')
    count_results(workpath + 'characterization/evolution_pattern/evolution_pattern_level3', 
                  workpath + 'characterization/evolution_pattern/evolution_pattern_count_level3', 
                  2)
        
    get_state_sequence(workpath + 'data/vci_files/vci_level4', 
                       workpath + 'characterization/evolution_pattern/state_sequence_level4', 
                       1. * 2 / 30, 1. * 3 / 30)
    merge_sequence(workpath + 'characterization/evolution_pattern/state_sequence_level4', 
                   workpath + 'characterization/evolution_pattern/evolution_pattern_level4')
    count_results(workpath + 'characterization/evolution_pattern/evolution_pattern_level4', 
                  workpath + 'characterization/evolution_pattern/evolution_pattern_count_level4', 
                  2)
        
    get_state_sequence(workpath + 'data/vci_files/vci_level5', 
                       workpath + 'characterization/evolution_pattern/state_sequence_level5', 
                       1. * 2 / 30, 1. * 3 / 30)
    merge_sequence(workpath + 'characterization/evolution_pattern/state_sequence_level5', 
                   workpath + 'characterization/evolution_pattern/evolution_pattern_level5')
    count_results(workpath + 'characterization/evolution_pattern/evolution_pattern_level5', 
                  workpath + 'characterization/evolution_pattern/evolution_pattern_count_level5', 
                  2)
        
    print('All Done!')
    
    
    