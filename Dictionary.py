import pandas as pd
import Combinations as c

my_dict = c.combinations(N=100, n=10)[0]

df = pd.DataFrame.from_dict(my_dict, orient = "index")
df.to_csv("win_rate.csv")

