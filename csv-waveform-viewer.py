import pandas as pd
import streamlit as st

"""
# CSV Waveform Viewer
"""

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    """
    ## Data
    """
    # Show data
    st.write(df)

    """
    ## Plot
    """
    # Get column names
    columns = df.columns.tolist()

    # Axis selection
    col1, col2 = st.columns(2)
    with col1:
        # Select x axis column
        x_axis = st.selectbox("Select x axis", columns)
    with col2:
        # Select y axis column
        y_axis = st.selectbox("Select y axis", columns, index=1)

    # Plot data
    if x_axis and y_axis:
        # Add space
        st.write("")

        # Plot line chart
        st.line_chart(df, x=x_axis, y=y_axis)
