#workpath = 'F:/Youku_Popularity/Youku_Popularity/'
workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'

data = read.table(paste(workpath, 'characterization/category_level/category_level', sep = ''), fileEncoding = 'utf-8')

cat_list = levels(data$V1)
for(i in seq(1, length(cat_list))){
  pop_levels = data[which(data$V1 == cat_list[i]), ][, 2]
  #cdf = ecdf(pop_levels)
  #plot(cdf, main = cat_list[i])
  hist(pop_levels, breaks = seq(0, 5), main = i)
}

cat_list
