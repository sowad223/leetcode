students <- data.frame(
  Name = c("Alice", "Bob", "Charlie", "David", "Eve"),
  Math = c(85, 78, 90, 65, 88),
  Science = c(80, 82, 75, 70, 92)
)
students$Average <- rowMeans(students[, 2:3])
high_achievers <- students[students$Average > 80, ]
print(students)
print(high_achievers)
