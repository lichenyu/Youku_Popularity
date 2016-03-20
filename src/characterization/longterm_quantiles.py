import numpy

# calculate the .25 .5 .75 quantiles of each input
def get_quantiles(in_files, out_file):
    out_fd = open(out_file, 'w')
    for f in in_files:
        in_fd = open(f, 'r')
        n30_list = []
        for line in in_fd.readlines():
            fields = line.strip().split('\t', -1)
            # vid, vc1, vc2, ..., vc30
            n30_list.append(int(fields[30]))
        arr = numpy.array(n30_list)
        out_fd.write(str(numpy.percentile(arr, 25)) + '\t' + \
                     str(numpy.percentile(arr, 50)) + '\t' + \
                     str(numpy.percentile(arr, 75)) + '\n')
        in_fd.close()
    out_fd.close()

if '__main__' == __name__:
    workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'

    date_strs = ['2015-12-06', '2015-12-07', '2015-12-08', '2015-12-09', '2015-12-10', 
                '2015-12-11', '2015-12-12', '2015-12-13', '2015-12-14', '2015-12-15', 
                '2015-12-16', '2015-12-17', '2015-12-18', '2015-12-19', '2015-12-20', 
                '2015-12-21', '2015-12-22', '2015-12-23', '2015-12-24', '2015-12-26', 
                '2015-12-27', '2015-12-28', '2015-12-29', '2015-12-30', '2015-12-31', 
                '2016-01-01', '2016-01-02', '2016-01-03', '2016-01-04']
    
    in_files = []
    for date in date_strs:
        in_files.append(workpath + 'data/clean_data/' + date)
    get_quantiles(in_files, workpath + 'characterization/longterm_distribution/quantiles')
    
    print('All Done!')