#2-1
head(trees)

#2-2
mean(trees$Girth)
median(trees$Girth)
mean(trees$Girth, trim = 0.15)
sd(trees$Girth)

#2-3
hist(trees$Girth, main = "나무 지름(Girth)", xlab = "Girth", ylab = "Girth", border= "black", col = "brown", breaks = 5)

#2-4
boxplot(trees$Girth, main = "나무 지름(Girth)")

#2-5
mean(trees$Height)
median(trees$Height)
mean(trees$Height, trim = 0.15)
sd(trees$Height)

#2-6
hist(trees$Height, main = "나무 높이(Height)", xlab = "Height", ylab = "Frequency", border = "black", col = "brown", breaks=5)

#2-7
boxplot(trees$Height, main = "나무 높이(HEight)")
