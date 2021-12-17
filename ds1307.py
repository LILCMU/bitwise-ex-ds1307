# Bitwise operation excercise with DS1307 Realtime Clock simulation
#
# CC-BY-NC Arnan Sipitakiat


DS1307_register = [23,          # Seconds = 17       
                   51,          # Minutes = 33           
                   112,         # Hourse = 10 PM
                   3,           # Day = 3 (Tue)
                   36,          # Date = 24
                   18,          # Month = 12
                   33           # Year = 21 (2021)
                   ]

# 1. Example - Read Day of week
dow = DS1307_register[3] & 0b111 
print ("Day of week = ", dow)

# 2. read date

# write your code to set the variables from the DS1307 registers
date = 0
month = 0
year = 0

print ("Date DD/MM/YY = ", date, "/", month,"/", year)

# 3. set date
# write code to set the DS1307 date to the current date

# your code here

# 4. set time (Optional)
# write code to set the time to the current time using the AM/PM notation (not 24 hrs format) 
# Note. becareful to set the AM/PM bit
