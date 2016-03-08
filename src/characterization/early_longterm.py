def get_ifiles_by_pattern(pattern_file, vci_file, pattern, out_file):
    vid_set = set()
    pattern_fd = open(pattern_file, 'r')
    for line in pattern_fd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, n30, pattern
        if pattern == fields[2]:
            vid_set.add(fields[0])
    pattern_fd.close()
    
    vci_fd = open(vci_file, 'r')
    out_fd = open(out_file, 'w')
    for line in vci_fd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, vci1, vci2, ..., vci30
        if fields[0] in vid_set:
            out_fd.write(line)
    vci_fd.close()
    out_fd.close()
    
# burst only in early stage
def get_ifiles_earlyburst(sequence_file, vci_file, out_file):
    vid_set = set()
    sequence_fd = open(sequence_file, 'r')
    for line in sequence_fd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, n30, sequence
        early_burst = False
        future_burst = False
        for i in range(0, 7):
            if '1' == fields[2][i]:
                early_burst = True
                break
        if False == early_burst:
            continue
        for i in range(7, 30):
            if '1' == fields[2][i]:
                future_burst = True
                break
        if True == future_burst:
            continue
        vid_set.add(fields[0])
    sequence_fd.close()
    
    vci_fd = open(vci_file, 'r')
    out_fd = open(out_file, 'w')
    for line in vci_fd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, vci1, vci2, ..., vci30
        if fields[0] in vid_set:
            out_fd.write(line)
    vci_fd.close()
    out_fd.close()
    
def get_ifiles_futureburst(sequence_file, vci_file, out_file):
    vid_set = set()
    sequence_fd = open(sequence_file, 'r')
    for line in sequence_fd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, n30, sequence
        future_burst = False
        for i in range(7, 30):
            if '1' == fields[2][i]:
                future_burst = True
                break
        if False == future_burst:
            continue
        vid_set.add(fields[0])
    sequence_fd.close()
    
    vci_fd = open(vci_file, 'r')
    out_fd = open(out_file, 'w')
    for line in vci_fd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, vci1, vci2, ..., vci30
        if fields[0] in vid_set:
            out_fd.write(line)
    vci_fd.close()
    out_fd.close()
    
# if a burst exists in the future, whats its frac
def get_futureburst_frac(sequence_file, vci_file, out_file):
    vid_set = set()
    sequence_fd = open(sequence_file, 'r')
    for line in sequence_fd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, n30, sequence
        future_burst = False
        for i in range(7, 30):
            if '1' == fields[2][i]:
                future_burst = True
                break
        if False == future_burst:
            continue
        vid_set.add(fields[0])
    sequence_fd.close()
    
    vci_fd = open(vci_file, 'r')
    out_fd = open(out_file, 'w')
    for line in vci_fd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, vci1, vci2, ..., vci30
        if fields[0] in vid_set:
            vci_list = []
            for i in range(1, 31):
                vci_list.append(int(fields[i]))
            out_fd.write(fields[0] + '\t' + str(1. * sum(vci_list[7 : 30]) / sum(vci_list)) + '\n')
    vci_fd.close()
    out_fd.close()
    
# for the 10 type, we exclude large future frac as 1010
# for the 0 type, we exclude large future frac as future burst
def futureburst_filter(vci_file, out_file, b_frac):
    vci_fd = open(vci_file, 'r')
    out_fd = open(out_file, 'w')
    for line in vci_fd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, vci1, vci2, ..., vci30
        vci_list = []
        for i in range(1, 31):
            vci_list.append(int(fields[i]))
        if b_frac <= (1. * sum(vci_list[7 : 30]) / sum(vci_list)):
            continue
        else:
            out_fd.write(line)
    vci_fd.close()
    out_fd.close()



if '__main__' == __name__:
    workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'
     
    get_ifiles_by_pattern(workpath + 'characterization/evolution_pattern/evolution_pattern', 
                          workpath + 'data/vci_files/vci', 
                          '0', 
                          workpath + 'characterization/early_longterm/early_longterm_pattern0')
     
    get_ifiles_earlyburst(workpath + 'characterization/evolution_pattern/state_sequence', 
                          workpath + 'data/vci_files/vci', 
                          workpath + 'characterization/early_longterm/early_longterm_earlyburst')
     
    get_ifiles_futureburst(workpath + 'characterization/evolution_pattern/state_sequence', 
                           workpath + 'data/vci_files/vci', 
                           workpath + 'characterization/early_longterm/early_longterm_futureburst')

    get_futureburst_frac(workpath + 'characterization/evolution_pattern/state_sequence', 
                         workpath + 'data/vci_files/vci', 
                         workpath + 'characterization/early_longterm/futureburst_frac')

    futureburst_filter(workpath + 'characterization/early_longterm/early_longterm_earlyburst', 
                       workpath + 'characterization/early_longterm/early_longterm_earlyburst_filter', 
                       0.6 * 23 / 30)
    futureburst_filter(workpath + 'characterization/early_longterm/early_longterm_pattern0', 
                       workpath + 'characterization/early_longterm/early_longterm_pattern0_filter', 
                       1.2 * 23 / 30)

    print('All Done!')
