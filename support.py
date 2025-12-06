import streamlit as st
import pandas as pd
from datetime import datetime
import psycopg2

# -------- PostgreSQL Connection --------
def get_connection():
    return psycopg2.connect(
        host="localhost",
            database="Querytable",
            user="postgres",
            password="scuro",
            port="5432"
    )
    
page_bg_color = """
<style>
.stApp {
    background-color: #E8F8F5;   /* Light gray background */
    padding: 20px;
}
</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

# -------- Load PostgreSQL Data --------
def load_queries_db():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM queries ORDER BY query_id ASC", conn)
    conn.close()
    return df

# -------- Load OLD CSV History --------
def load_csv_history():
    df = pd.read_csv("E:/python project/project1/pages/synthetic_client_queries.csv")

    # Rename CSV columns → match DB structure
    df = df.rename(columns={
        "client_email": "email",
        "client_mobile": "mobile",
        "query_heading": "category",
        "query_description": "query_description",
        "date_raised": "query_created_time",
        "date_closed": "query_closed_time"
    })

    # Ensure query_id is string
    df["query_id"] = df["query_id"].astype(str)

    return df

# -------- Streamlit App --------
st.title("Client Query Portal")

# Load CSV History
st.subheader("CSV History Data")
df_csv = load_csv_history()
st.dataframe(df_csv)

# Load Live DB Records
st.subheader("Live PostgreSQL Records")
df_db = load_queries_db()
st.dataframe(df_db)

st.subheader("Close a Query ")

if not df_db.empty:
    open_db_queries = df_db[df_db["status"] == "Open"]

    if open_db_queries.empty:
        st.info("No open queries in database.")
    else:
        selected_query = st.selectbox(
            "Select Query ID to Close",
            open_db_queries["query_id"].tolist()
        )

        if st.button("Close Selected Query"):
            try:
                conn = get_connection()
                cur = conn.cursor()

                update_sql = """
                    UPDATE queries
                    SET status = %s,
                        query_closed_time = %s
                    WHERE query_id = %s
                """

                cur.execute(update_sql, ("Closed", datetime.now(), selected_query))
                conn.commit()
                cur.close()
                conn.close()

                st.success(f"Query ID {selected_query} closed successfully!")
                st.rerun()

            except Exception as e:
                st.error(f"Error updating query: {e}")


# step 10 LOGOUT BUTTON 
if st.button("Log out"):
    st.switch_page("abc.py")
