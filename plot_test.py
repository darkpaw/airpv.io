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
gen = df['Generation']

plt.plot(gen)
plt.ylabel('Generation kW')
plt.xlabel('24 hours')
plt.show()