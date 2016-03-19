
def sort_vci_pct(in_file, out_file):
    in_fd = open(in_file, 'r')
    out_fd = open(out_file, 'w')
    for line in in_fd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, vci1, vci2, ..., vci30
        vci_list = []
        for i in range(1, 1 + 30):
            vci_list.append(int(fields[i]))
        s = sum(vci_list)
        if 0 == s:
            continue
        for i in range(0, 30):
            vci_list[i] = 1. * vci_list[i] / s
        vci_list.sort(reverse = True)
        out_fd.write(fields[0])
        for i in range(0, 3):
            out_fd.write('\t' + str(vci_list[i]))
        out_fd.write('\n')
    in_fd.close()
    out_fd.close()

if '__main__' == __name__:
    workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'
    
    sort_vci_pct(workpath + 'data/vci_files/vci', 
                 workpath + 'characterization/peakday_pct/peakday_pct')
    
    sort_vci_pct(workpath + 'data/vci_files/vci_level1', 
                 workpath + 'characterization/peakday_pct/peakday_pct_level1')
    sort_vci_pct(workpath + 'data/vci_files/vci_level2', 
                 workpath + 'characterization/peakday_pct/peakday_pct_level2')
    sort_vci_pct(workpath + 'data/vci_files/vci_level3', 
                 workpath + 'characterization/peakday_pct/peakday_pct_level3')
    sort_vci_pct(workpath + 'data/vci_files/vci_level4', 
                 workpath + 'characterization/peakday_pct/peakday_pct_level4')
    sort_vci_pct(workpath + 'data/vci_files/vci_level5', 
                 workpath + 'characterization/peakday_pct/peakday_pct_level5')
    
    print('All Done!')
    
    
    