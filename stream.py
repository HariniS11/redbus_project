import streamlit as st
import pandas as pd
import pymysql


# Database connection function
def get_db_connection():
    return pymysql.connect(
        host="localhost",  # Replace with your MySQL host
        user="root",  # Replace with your MySQL user
        password="12345",  # Replace with your MySQL password
        database="redbus_project"  # Replace with your MySQL database name
    )


# Query function to fetch data
def fetch_data(route_name, star_rating, price):
    query = "SELECT * FROM bus_routes WHERE 1=1"
    params = []
    
    if route_name:
        query += " AND route_name LIKE %s"
        params.append(f"%{route_name}%")
    # if bus_type:
    #     query += " AND bus_type = %s"
        # params.append(bus_type)
    if star_rating > 0:  # Only apply filter if star_rating > 0
        query += " AND star_rating >= %s"
        params.append(star_rating)
    if price > 0:  # Only apply filter if price > 0
        query += " AND price <= %s"
        params.append(price)
    
    conn = get_db_connection()
    try:
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
        return pd.DataFrame(result)
    finally:
        conn.close()

def style_button():
    st.markdown("""
        <style>
        .stButton > button {
            background-color: #4CAF50; /* Green color */
            color: white;
            font-size: 16px;
            border-radius: 5px;
            padding: 10px 20px;
        }
        .stButton > button:hover {
            background-color: #45a049; /* Slightly darker green on hover */
        }
        </style>
    """, unsafe_allow_html=True)


# Call the function to apply CSS styling
style_button()



# Streamlit UI
st.title("Bus Search Application")

# Input filters
route_name = st.text_input("Route Name")
# bus_type = st.selectbox("Bus Type", ["", "AC", "Non-AC", "Sleeper", "Semi-Sleeper"])
star_rating = st.selectbox("Minimum Star Rating", [0.0, 1.0, 2.0, 3.0, 4.0, 5.0], index=0)
price = st.number_input("Maximum Price", min_value=0.0, value=0.0)

# Search button
if st.button("Search"):
    with st.spinner("Fetching data..."):
        try:
            # Fetch data using the input filters
            data = fetch_data(route_name,star_rating, price)
            if not data.empty:
                st.dataframe(data)
            else:
                st.warning("No records found matching the filters.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

