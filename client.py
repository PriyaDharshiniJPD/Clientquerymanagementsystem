import streamlit as st
import psycopg2
from datetime import datetime

# step 1 DB connection
def get_connection():
    return psycopg2.connect(
            host="localhost",
            database="Querytable",
            user="postgres",
            password="scuro",
            port="5432"
    )

#step 2 background image and page name
st.markdown("""
<h1 style= 'text-aling: center'> Welcome To Query Support</h1>
                       
""", unsafe_allow_html=True)
page_bg_color = """
<style>
.stApp {
    background-color: #E8F8F5;   /* Light gray background */
    padding: 20px;
}
</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

#step 3 get input 
mail_id = st.text_input("Email ID")
mobile_number = st.text_input("Mobile Number")
query_heading = st.text_input("Query Heading")
query_description = st.text_area("Enter your detailed query here")

#step 4 submit
if st.button("Submit"):
    if not mail_id or not mobile_number or query_heading =="" or not query_description:
        st.warning("Please fill all the fields before submitting")
    else: 
        conn = get_connection()
        cur = conn.cursor()
        insert_sql="""INSERT INTO queries(mail_id,mobile_number,query_heading,query_description,status,query_created_time,query_closed_time)
        VALUES (%s, %s, %s, %s, %s, %s, %s)"""

        cur.execute(insert_sql,(
            mail_id,mobile_number,query_heading,query_description,"Open",datetime.now(),None
        ))

        conn.commit()
        cur.close()
        conn.close()


        st.success("Query Submitted Successfully")

#step 5 logout 
if st.button("Log Out"):
    st.switch_page("abc.py")
