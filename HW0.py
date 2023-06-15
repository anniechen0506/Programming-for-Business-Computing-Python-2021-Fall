# HW0 (1) Classroom staff allocation problem 
# HW0 (1) 課堂人員分配問題

# Question
# There is a programming course, and in order to provide enough care and support for the students taking the course, the teacher has set the following course rules: for every m students taking the course, one teaching assistant (TA) must be hired, and each TA will be responsible for m students during office hours. If the total number of students taking the course, n, is not divisible by m, then the remaining students without a TA will be supervised by the teacher during office hours. For example, if n = 100 and m = 30, three TAs are needed, and the teacher must be responsible for 10 students. If n = 125 and m = 25, five TAs are needed, and the teacher does not need to be responsible for any students. If n = 10 and m = 11, no TAs need to be hired, and the teacher is responsible for 10 students during office hours.
# In this problem, please input the values of n and m, and calculate the number of TAs needed and the number of students the teacher will be responsible for during office hours.

# 有一門程式設計課，為了給修課學生們足夠多的照顧與支援，教師設定開課規則如下：每有m個學生修課，就要聘用一名助教，並在 office hour 時讓每位助教負責 m 位學生；若修課總人數 n 不能被 m 整除，則最後沒有助教負責的學生，就在 office hour 時由授課教師負責。舉例來說，如果 n=100 且 m=30，則需要 3 名助教，且教師必須負責 10 位學生；如果 n=125 且 m=25 ，則需要 5 名助教，而教師不用負責任何學生；如果 n=10 且 m=11，則不聘助教且教師負責 10 位學生。
# 在本題中，請讀入 n 跟 m 這兩個數字，並計算需要聘用的助教人數以及教師在 office hour 負責的學生人數。

# My Code
m = int(input())
n = int(input())
print(m // n,end = ",")
print(m % n)
