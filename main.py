from Sun import Sun

coords = {'longitude' : 145, 'latitude' : -38 }

sun = Sun()

# Sunrise time UTC (decimal, 24 hour format)
print sun.getSunriseTime( coords )['decimal']

# Sunset time UTC (decimal, 24 hour format)
print sun.getSunsetTime( coords )['decimal']