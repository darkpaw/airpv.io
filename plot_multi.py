import pandas as pd
from load_data import load_combined
import matplotlib


import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.style.use('fivethirtyeight')

# plt.plot([1,2,3,4])
# plt.ylabel('some numbers')
# plt.show()

df = load_combined()
assert isinstance(df, pd.DataFrame)
#gen = df['Gen_1']

people = (df['Load_0'] + df['Load_1'] + df['Load_3']) * 5.0
print(people)

plt.plot(df['Gen_4'] * 10.0)
#plt.plot(df['Gen_0'] * 10.332)
#plt.plot(people)

plt.plot(df['Load_3'] * 5)

# plt.plot(df['Load_3'] * 5)
# plt.plot(df['Gen_3'])
# plt.plot(df['Gen_4'])
# plt.plot(df['Gen_5'])

plt.ylabel('Generation kW')
plt.xlabel('1 day - 48 half hours')
plt.show()

