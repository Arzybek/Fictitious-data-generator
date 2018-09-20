import statistics as stats

file = open('dates.txt','r')
data = file.readlines()
dates = []
for line in data:
    dates.append(int(line))
avg = stats.mean(dates)
print(avg)

disp = stats.stdev(dates)
print(disp)