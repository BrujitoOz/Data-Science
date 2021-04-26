mylist = list( a = c(1,2,3), b =c("cat","dog","duck"), d=factor("a","b","a"))


sapply(mylist,mode) 
sapply(mylist,class)

x = c(one=1,two=2,three=3)
x

names(x)[1:2] = c("uno", "dos")
x

nums <- 1:10
nums + 2
nums + c(3,1)

rmat = matrix(1, 5, 3)
rmat

x[!is.na(x)]