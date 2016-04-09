import csv
import pandas as pd
import matplotlib

#matplotlib.style.use('ggplot')
#with open('generation_profile.txt'):
#df = pd.read_csv('generation_profile.txt')

#print(df[0])
#plt = df.plot()
# #plt.show()

total_panels = 5332.0

rdr = csv.reader(open('input_data/generation_profile.txt'))
next(rdr)
minute = 60*5

generation_values = [0 for i in range(24*60)]

for row in rdr:
    #print(row)
    minute += 1
    value = float(row[1])
    #print(minute, value)
    generation_values[minute] = value


generation_values_30minute = [0 for j in range(24*2)]
minute = 0

for idx, half_hour in enumerate(generation_values_30minute):
    half_hour_gen = 0
    for m in range(30):
        half_hour_gen += generation_values[minute]

        value = half_hour_gen / 30.0 / total_panels
        assert value <= 1.0
        assert value >= 0.0
        generation_values_30minute[idx] = value
        minute += 1

for r in generation_values_30minute:
    print("%0.2f" % r)
#
# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
# plt.plot(generation_values_30minute)
# plt.ylabel('some numbers')
# plt.show()






