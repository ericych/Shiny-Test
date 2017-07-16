library(rPython)

a <- c(1,2,3,4)
python.load("24.py")
test= as.data.frame(python.call("get_solutions",a))
colnames(test) = "Solutions"
renderTable(test,rownames= TRUE)





