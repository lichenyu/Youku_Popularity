workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'

data = read.table(paste(workpath, 'characterization/popularity_metrics/metrics', sep = ''))

view_count = data$V2
comment_count = data$V3
favorite_count = data$V4
up_count = data$V5
down_count = data$V6
rate_count = data$V5 + data$V6

summary(view_count, digits = 8)
summary(comment_count, digits = 8)
summary(favorite_count, digits = 8)
summary(up_count, digits = 8)
summary(down_count, digits = 8)
summary(rate_count, digits = 8)

cor(view_count, comment_count, method = 'spearman')
cor(view_count, up_count, method = 'spearman')
cor(view_count, down_count, method = 'spearman')
cor(view_count, rate_count, method = 'spearman')

cc_p = which(0 < comment_count)
cor(view_count[cc_p], comment_count[cc_p], method = 'spearman')
uc_p = which(0 < up_count)
cor(view_count[uc_p], up_count[uc_p], method = 'spearman')
dc_p = which(0 < down_count)
cor(view_count[dc_p], down_count[dc_p], method = 'spearman')
rc_p = which(0 < rate_count)
cor(view_count[rc_p], rate_count[rc_p], method = 'spearman')



# idx = which(90 >= view_count)
# cor(view_count[idx], comment_count[idx], method = 'spearman')
# idx = which(91 <= view_count & 1029 >= view_count)
# cor(view_count[idx], comment_count[idx], method = 'spearman')
# idx = which(1030 <= view_count & 8756 >= view_count)
# cor(view_count[idx], comment_count[idx], method = 'spearman')
# idx = which(8757 <= view_count & 92395 >= view_count)
# cor(view_count[idx], comment_count[idx], method = 'spearman')
# idx = which(92396 <= view_count)
# cor(view_count[idx], comment_count[idx], method = 'spearman')


idx = which(0 < comment_count)
plot(comment_count[idx], view_count[idx], xlim = c(0, 10000), ylim = c(0, 10000000))


idx = which(0 < rate_count)
plot(rate_count[idx], view_count[idx], xlim = c(0, 10000), ylim = c(0, 10000000))
