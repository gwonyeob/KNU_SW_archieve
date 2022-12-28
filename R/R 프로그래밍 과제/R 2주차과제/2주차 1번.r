#1-1
score <- c(90, 85, 73, 80, 85, 65, 78, 50, 68, 96) 
names(score) <- c("KOR", "ENG", "ATH", "HIST", "SOC", "MUSIC", "BIO", "EARTH", "PHY", "ART")

#1-2
score

#1-3
mean(score) 
median(score)

#1-4
sd(score)

#1-5
which.max(score)

#1-6
boxplot(score, main = "성적") 

#1-7
hist(score, main = "학생 성적", xlab = "성적", ylab = "빈도수", border = "black", col = "purple") 




