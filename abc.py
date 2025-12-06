import streamlit as st
import psycopg2
import hashlib
#step 1 page name and background image
st.markdown("""
 <h1 style='text-align: center;'>Welcome To Customer Helpdesk</h1>
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


#step 2 get input
username = st.text_input("Enter Your Name")
password = st.text_input("Password", type='password')
roles = st.selectbox("Select role", ["client", "support"])

#step 3 submit
if st.button("Submit"):

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="Querytable",
            user="postgres",
            password="scuro",
            port="5432"
        )
        cur = conn.cursor()

        # Hash entered password
        hash_pass = hashlib.sha256(password.encode()).hexdigest()

        # Fetch stored hash
        cur.execute(
            "SELECT hashed_password FROM users WHERE username=%s AND roles=%s",
            (username, roles)
        )
        result = cur.fetchone()

        if result:
            stored_hash = result[0]

            # Debug
            # st.write("DEBUG values:")
            # st.write("Entered Hash:", hash_pass)
            # st.write("Stored Hash:", stored_hash)

            # Compare to client or support
            if hash_pass == stored_hash:
                st.success("Login Successful!")

                if roles == "client":
                    st.switch_page("pages/client.py")
                if roles == "support":
                    st.switch_page("pages/support.py")

            else:
                st.error("Incorrect password")

        else:
            st.error("User does not exist")

    except Exception as e:
        st.error(f"Database error: {e}")