from datetime import datetime
now = datetime.now()

print now

from datetime import datetime
now = datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day


print now.year
print now.month
print now.day

print '%s/%s/%s' % (now.month, now.day, now.year)

print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)
