def split_nfile_bylevel(in_file, out_path):
    in_fd = open(in_file, 'r')
    out_fd_l1 = open(out_path + 'vc_level1', 'w')
    out_fd_l2 = open(out_path + 'vc_level2', 'w')
    out_fd_l3 = open(out_path + 'vc_level3', 'w')
    out_fd_l4 = open(out_path + 'vc_level4', 'w')
    out_fd_l5 = open(out_path + 'vc_level5', 'w')
    for line in in_fd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, vc1, vc2, ..., vc30
        n30 = int(fields[30])
        if n30 <= 90:
            out_fd_l1.write(line)
        elif n30 <= 1029:
            out_fd_l2.write(line)
        elif n30 <= 8756:
            out_fd_l3.write(line)
        elif n30 <= 92395:
            out_fd_l4.write(line)
        else:
            out_fd_l5.write(line)
    in_fd.close()
    out_fd_l1.close()
    out_fd_l2.close()
    out_fd_l3.close()
    out_fd_l4.close()
    out_fd_l5.close()
    
def split_ifile_bylevel(in_file, out_path):
    in_fd = open(in_file, 'r')
    out_fd_l1 = open(out_path + 'vci_level1', 'w')
    out_fd_l2 = open(out_path + 'vci_level2', 'w')
    out_fd_l3 = open(out_path + 'vci_level3', 'w')
    out_fd_l4 = open(out_path + 'vci_level4', 'w')
    out_fd_l5 = open(out_path + 'vci_level5', 'w')
    for line in in_fd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, vci1, vci2, ..., vci30
        vci_list = []
        for i in range(1, 31):
            vci_list.append(int(fields[i]))
        n30 = sum(vci_list)
        if n30 <= 90:
            out_fd_l1.write(line)
        elif n30 <= 1029:
            out_fd_l2.write(line)
        elif n30 <= 8756:
            out_fd_l3.write(line)
        elif n30 <= 92395:
            out_fd_l4.write(line)
        else:
            out_fd_l5.write(line)
    in_fd.close()
    out_fd_l1.close()
    out_fd_l2.close()
    out_fd_l3.close()
    out_fd_l4.close()
    out_fd_l5.close()

if '__main__' == __name__:
    workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'
    
#     split_nfile_bylevel(workpath + 'data/clean_data/vc', 
#                         workpath + 'data/clean_data/')
    split_ifile_bylevel(workpath + 'data/vci_files/vci', 
                        workpath + 'data/vci_files/')
    
    print('All Done!')