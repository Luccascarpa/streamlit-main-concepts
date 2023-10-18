"""
# My first app
All the examples froma streamlit docs 'Main concepts'
"""

### Import packages ###
from email import charset
import streamlit as st
import numpy as np
import pandas as pd

### Examples ###

# Display and style data
st.write("")
st.title("Display and style data")

# Use magic

"Using magic to display a dataframe"
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df


# Write a data frame
st.write("")
st.title("Write a data frame")

## Using st.write
st.write("")
st.write("Using st.write()")
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

## Using st.dataframe
st.write("Using st.dataframe()")
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

## Using the pandas styler as well
st.write("Using the Pandas Styler to highlight elements")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

## Using st.table
st.write("Using st.table()")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)


# Draw charts and maps
st.write("")
st.write("")
st.title("Draw charts and maps")

## Draw a line chart
st.write("")
st.write("Draw a line chart")

char_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)

st.line_chart(char_data)

## Plot a map
st.write("")
st.write("Plot a map")

map_data = pd.DataFrame(
    np.random.randn(1000,2) / [50,50] + [37.76, -122.4],
    columns = ['lat', 'lon']
)

st.map(map_data)

# Widgets
st.write("")
st.title("Widgets")

## Slider
st.write("")
st.write("Slider")
x = st.slider('x')
st.write(x, 'squared is', x*x)

## Text inputs and key
st.write("")
st.write("Text inputs (and using keys)")

st.text_input("Your name", key="name")
st.session_state.name

## Use checkboxes to show/hide data
st.write("")
st.write("Use checkbox to show/hide data")
if st.checkbox('Show  dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a','b','c']
    )
    chart_data

## Use selectbox for options
st.write("")
st.write("Use selectbox for options")

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})

option = st.selectbox(
    'Which number do you like best?',
    df['first column']
)

'You selected: ', option

# Layout
st.write("")
st.write("")
st.title("Layout")

## Sidebar
st.write("")
st.write("Sidebar")

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

add_slider = st.sidebar.slider(
    'Select a range of value',
    0.0, 100.0, (25.0, 75.0)
)

## st columns
st.write("")
st.write("st.columns")

left_column, right_column = st.columns(2)
left_column.button('Press me!')

with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin")
    )
    st.write(f"You are in {chosen} house!")

# Show progress
st.write("")
st.write("")
st.title("Show Progress")

import time

st.write("")
'Starting a long computation...'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'... and now we\'re done!'

# Themes
# The theme can be switched directly in the app menu

# Caching
# Store results of expensive function calls and return the cached result when the 
# same inputs occur again rather than calling the function on subsequent runs

# decorators for caching: st.cache_data (for serializable data) or st.cache_resource  (for global resources)

@st.cache_data
def long_running_function(param1, param2):
   pass


# Pages
st.write("")
st.write("")
st.title("Pages")
