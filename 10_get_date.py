from datetime import date

# get today's date
today = date.today()

# Get day, month and year as indiidual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = f"The current date is {day}/{month}/{year}"
filename = f"MMF_{year}_{month}_{day}"


print(heading)
print(f"The filename will be {filename}.txt")
