import io
import pandas as pd


df = pd.read_csv("Resources/cities.csv",index_col=False)
df = df.set_index("City_ID")
# print(df.head())
str_io = io.StringIO()
df.to_html(buf=str_io, classes='table table-striped')
html_str = str_io.getvalue()

html_file = open("output.html","w")
html_file.write(html_str)
html_file.close()