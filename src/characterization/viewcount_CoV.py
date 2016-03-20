import numpy

def get_viewcount_CoV(in_file, out_file):
    in_fd = open(in_file, 'r')
    out_fd = open(out_file, 'w')
    for line in in_fd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, vci1, vci2, ..., vci30
        vci_list = []
        for i in range(1, 1+ 30):
            vci_list.append(int(fields[i]))
        arr = numpy.array(vci_list)
        std = numpy.std(arr)
        mean = numpy.mean(arr)
        if 0 == sum(vci_list):
            CoV = 0
        else:
            CoV = std / mean
        out_fd.write(fields[0] + '\t' + str(round(std, 2)) + '\t' + str(round(mean, 2)) + '\t' + str(round(CoV, 2)) + '\n')
    in_fd.close()
    out_fd.close()

if '__main__' == __name__:
    workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'
    
    get_viewcount_CoV(workpath + 'data/vci_files/vci', 
                      workpath + 'characterization/viewcount_CoV/viewcount_CoV')
    
    get_viewcount_CoV(workpath + 'data/vci_files/vci_level1', 
                      workpath + 'characterization/viewcount_CoV/viewcount_CoV_level1')
    get_viewcount_CoV(workpath + 'data/vci_files/vci_level2', 
                      workpath + 'characterization/viewcount_CoV/viewcount_CoV_level2')
    get_viewcount_CoV(workpath + 'data/vci_files/vci_level3', 
                      workpath + 'characterization/viewcount_CoV/viewcount_CoV_level3')
    get_viewcount_CoV(workpath + 'data/vci_files/vci_level4', 
                      workpath + 'characterization/viewcount_CoV/viewcount_CoV_level4')
    get_viewcount_CoV(workpath + 'data/vci_files/vci_level5', 
                      workpath + 'characterization/viewcount_CoV/viewcount_CoV_level5')
    
    print('All Done!')
    
    
    