#!/usr/bin/env python

ybegin = 1006
yend = 1996

#jay 26 monday
def leap(year):
        if year%400==0:
                return True
        if year%100!=0 and year%4==0:
                return True
        return False

dayWNow = 6#today is satuaday
dayNow = 25 #0,
yearNow = 1006
monthNow = 0# 0, 11
months = [31,28,31,30,31,30,31,31,30,31,30,31]

while yearNow<1997:
	isLeap = leap(yearNow)
	if isLeap==True:
		months[1] = 29
	else:
		months[1] = 28
        #check
        if dayNow==25 and monthNow==0 and dayWNow==0 and (yearNow-6)%10==0 and isLeap:
                print 'Day:',dayWNow+1,' day:',dayNow+1,' month:',monthNow+1, ' year:',yearNow
        #clear day
        dayNow = dayNow + 1
	#just a day
	dayWNow = (dayWNow + 1) % 7
        #clear month 
        if dayNow==months[monthNow]-1:
                monthNow = monthNow + 1
                dayNow = 0
                if monthNow==11:
                        yearNow = yearNow + 1
                        monthNow = 0
