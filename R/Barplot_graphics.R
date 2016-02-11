tN <- table(Ni <- stats::rpois(100, lambda = 5))
r <- barplot(tN, col = rainbow(20))
counts <- table(mtcars$gear)
barplot(counts, main="Car Distribution", xlab="Number of Gears", col="blue")

