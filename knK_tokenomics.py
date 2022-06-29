import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


#@st.cache
def load_data():
    df1 = pd.read_pickle('cost_df')
    df2 = pd.read_pickle('cost_df_cumulative')
    return df1, df2


st.subheader('Daily $KAGE token emissions')
cost_df, cost_df_cumulative= load_data()
#df_T = df.T

cost_df

st.subheader('$KAGE token emissions (cumulative)')

cost_df_cumulative['difference'] =cost_df_cumulative.sum(1)

cost_df_cumulative

# source = pd.DataFrame({
#   'days': df.index,
#   '$KAGE': df['cumulative']
# })
transformed_df = cost_df_cumulative.reset_index().melt('index')
c = alt.Chart(transformed_df).mark_line().encode(
    x='index',
    y='value',
    color='variable',
    tooltip=['variable', 'value']    
).interactive()





st.altair_chart(c, use_container_width=True)




source = pd.DataFrame({
  'days': cost_df_cumulative.index,
  '$KAGE over time': cost_df_cumulative['difference']
})


c2 = alt.Chart(source).mark_circle().encode(
    x='days',
    y='$KAGE over time',
    color='$KAGE over time',
    tooltip=['$KAGE over time', 'days']    
).interactive()

st.altair_chart(c2, use_container_width=True)
