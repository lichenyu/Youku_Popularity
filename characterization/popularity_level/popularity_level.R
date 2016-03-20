workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'

data = read.table(paste(workpath, 'data/clean_data/vc', sep = ''))

n30 = data$V31

summary(n30, digits = 10)

c(0, floor(quantile(n30, 0.50)))
c(floor(quantile(n30, 0.50)) + 1, floor(quantile(n30, 0.85)))
c(floor(quantile(n30, 0.85)) + 1, floor(quantile(n30, 0.95)))
c(floor(quantile(n30, 0.95)) + 1, floor(quantile(n30, 0.99)))
c(floor(quantile(n30, 0.99)) + 1, max(n30))
