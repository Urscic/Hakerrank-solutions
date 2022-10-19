import calendar 

# #CREATE A CALENDAR OBJECT
calendar_example=calendar.Calendar(0)

# #itering in calendar - it looks strange in the doc so let's make it clear
for day in calendar_example.iterweekdays():
    print(day)

for day in calendar_example.itermonthdates(2022, 10):
    print(day)


#print a calendar sheet
dec = calendar.TextCalendar(0)
dec.formatmonth(2020, 12) 
dec.prmonth(2020, 12) #same but printed