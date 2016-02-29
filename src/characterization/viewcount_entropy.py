from math import log10

def get_viewcount_entropy(in_file, out_file):
    in_fd = open(in_file, 'r')
    out_fd = open(out_file, 'w')
    for line in in_fd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, vci1, vci2, ..., vci30
        vci_list = []
        for i in range(1, 1+ 30):
            vci_list.append(int(fields[i]))
        h = 0
        s = sum(vci_list)
        if 0 == s:
            continue
        for vci in vci_list:
            if 0 == vci:
                continue
            p = vci * 1. / s
            h = h + p * log10(1 / p)
        out_fd.write(fields[0] + '\t' + str(h) + '\n')
    in_fd.close()
    out_fd.close()

if '__main__' == __name__:
    workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'
    
    get_viewcount_entropy(workpath + 'data/vci_files/vci', 
                          workpath + 'characterization/viewcount_entropy/viewcount_entropy')
    
    print('All Done!')
    
    
    