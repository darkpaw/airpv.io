import pandas as pd
from load_data import load_combined
import matplotlib


import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.style.use('fivethirtyeight')

df = load_combined()
assert isinstance(df, pd.DataFrame)

people = (df['Load_0'] + df['Load_1'] + df['Load_3']) * 5.0

for gen in range(6):
    plt.plot(df['Gen_%d' % gen] * 10.0)
    plt.plot(people)
    plt.ylabel('Generation kW')
    plt.xlabel('1 day - 48 half hours')
    plt.tight_layout()
    plt.savefig('day_%d.png' % gen)
    plt.close()
