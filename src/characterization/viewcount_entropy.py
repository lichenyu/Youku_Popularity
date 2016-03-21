from scipy.stats import entropy
from math import log

def get_viewcount_entropy(in_file, out_file):
    in_fd = open(in_file, 'r')
    out_fd = open(out_file, 'w')
    for line in in_fd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, vci1, vci2, ..., vci30
        vci_list = []
        for i in range(1, 1+ 30):
            vci_list.append(int(fields[i]))
        s = sum(vci_list)
        if 0 == s:
            continue
        else:
            for i in range(0, 30):
                vci_list[i] = vci_list[i] * 1. / s
            h = entropy(vci_list) / log(30)
            out_fd.write(fields[0] + '\t' + str(round(h, 4)) + '\n')
    in_fd.close()
    out_fd.close()

if '__main__' == __name__:
    workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'
    
    get_viewcount_entropy(workpath + 'data/vci_files/vci', 
                      workpath + 'characterization/viewcount_entropy/viewcount_entropy')
    
    get_viewcount_entropy(workpath + 'data/vci_files/vci_level1', 
                      workpath + 'characterization/viewcount_entropy/viewcount_entropy_level1')
    get_viewcount_entropy(workpath + 'data/vci_files/vci_level2', 
                      workpath + 'characterization/viewcount_entropy/viewcount_entropy_level2')
    get_viewcount_entropy(workpath + 'data/vci_files/vci_level3', 
                      workpath + 'characterization/viewcount_entropy/viewcount_entropy_level3')
    get_viewcount_entropy(workpath + 'data/vci_files/vci_level4', 
                      workpath + 'characterization/viewcount_entropy/viewcount_entropy_level4')
    get_viewcount_entropy(workpath + 'data/vci_files/vci_level5', 
                      workpath + 'characterization/viewcount_entropy/viewcount_entropy_level5')
    
    print('All Done!')
    
    
    