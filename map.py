import streamlit as st 
import pandas as pd
import numpy as np

map_data = pd.DataFrame(
    np.random.rand(100,2) / [10,10] + [37.76, -122.4],
    columns = ['lat', 'lon']
)

st.map(map_data)
