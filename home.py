import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Fifa Test', divider='rainbow')
st.image('fifa_app\\images\\fifa_title_image.jpg',width=500)

st.markdown("""---""")

df = pd.read_csv('../FIFA_PROJECT/fifa_eda.csv')

# print size
print(df.shape)

# print duplicated
print(df.duplicated(keep=False).count())

# print info
df.info()

# remove null values
df.dropna(inplace=True)

# view df head
st.dataframe(df.head(), use_container_width=True)

# draw histogram
dfg = df.groupby(['Club']).size().to_frame().sort_values([0],ascending=False).head(10).reset_index()
fig = px.histogram(dfg,x='Club')


col1, col2 = st.columns(2)

with col1:
   st.header("Histogram on Club feature")
   st.plotly_chart(fig)