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

if '__main__' == __name__:
    workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'
    
#     get_ifiles_by_pattern(workpath + 'characterization/evolution_pattern/evolution_pattern', 
#                           workpath + 'data/vci_files/vci', 
#                           '10', 
#                           workpath + 'characterization/early_longterm/early_longterm_pattern10')
    
    get_ifiles_by_pattern(workpath + 'characterization/evolution_pattern/evolution_pattern', 
                          workpath + 'data/vci_files/vci', 
                          '0', 
                          workpath + 'characterization/early_longterm/early_longterm_pattern0')

    print('All Done!')
