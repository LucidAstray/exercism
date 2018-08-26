import calendar as cal

def meetup_day(year, month, day_of_the_week, which):

    c = cal.Calendar()

    #making a dict containing weekdays arranged to a number
    dow = dict(zip(list(cal.day_name), range(7)))


    #making a list of days that are included in particular month -> d for d in c.itermonthdates(year, month)
    #with a restriction that the day of the week in dict has to have a matching number to day passed in the function -> iterweekdays()
    days = [d for d in c.itermonthdates(year, month) if d.weekday() == dow[day_of_the_week] and d.month == month]


    if which.lower() == 'teenth':
        return [d for d in days if d.day > 12 and d.day < 20][0]
    elif which == 'last':
        return days[-1]
    else:
        return days[int(which[0]) - 1]
