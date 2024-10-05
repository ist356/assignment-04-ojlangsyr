'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl


st.title("UNIBROW")
st.caption("THE UNIVERSAL DATA BROWSER")

# TODO Write code here to complete the unibrow.py

file_uploaded = st.file_uploader("UPLOAD A FILE (ONLY CSV, JSON OR XLSX)", type=["csv", "xlsx","json"])

if file_uploaded:
    file_ext = pl.get_file_extension(file_uploaded.name)
    df = pl.load_file(file_uploaded, file_ext)

    if df is not None:
        all_cols = pl.get_column_names(df)
        selected_cols = st.multiselect("SELECT COLUMNS", all_cols)

        if selected_cols:
            st.write("FILTERED:")
            st.dataframe(df[selected_cols])

            apply_filter = st.toggle("APPLY FILTER", False)
            if apply_filter:
                text_cols = pl.get_columns_of_type(df, 'object')
                if text_cols:
                    selected_text_col = st.selectbox("SELECT COLUMN FILTER", text_cols)
                    unique_values = pl.get_unique_values(df, selected_text_col)
                    selected_value = st.selectbox("SELECT VALUE", unique_values)
                    st.write("FILTERED:")
                    st.dataframe(df[df[selected_text_col] == selected_value])
                else:
                    st.write("NO TEXT COLUMNS TO FILTER")
        show_stats = st.checkbox("SHOW SUMMARY STATS", False)
        if show_stats:
            st.write("SUMMARY STATS")
            st.write(df[selected_cols].describe())
        else:
            st.write("NO SELECTED COLUMNS")
    else:
        st.write("ERROR LOADING FILE")
else:
    st.write("NO FILE UPLOADED")