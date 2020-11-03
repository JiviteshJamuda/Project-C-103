# Importing modules 
# Idk why do we have pandas
import pandas as pd
# Choo choo trains gonna leave in 30 secs
import plotly.express as px

# Pandas finally being helpful rather than eating bamboos all day
data = pd.read_csv("cases.csv")
# Creating a weird looking graph by scattering like more than thousand of dots to make an masterpiece
fig = px.scatter(data, x="date", y="cases", color="country", title="Rise of cases on covid-19 per day")
# fig.show() because it is the only way to show the masterpiece
fig.show()