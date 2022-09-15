import pandas as pd
a = pd.read_csv("cities.csv")
a.to_html("data.html")