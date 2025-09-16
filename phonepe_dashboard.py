import streamlit as st
import pandas as pd
import pymysql
import plotly.express as px
import requests

# -------------------------------
# DB CONNECTION FUNCTION
# -------------------------------
def run_query(query):
    connection = pymysql.connect(
        host='localhost', user='root', password='12345', database='phonepe_data'
    )
    df = pd.read_sql(query, connection)
    connection.close()
    return df

st.set_page_config(page_title="PhonePe Pulse Case Studies", layout="wide")
st.title("📊 PhonePe Pulse - Business Case Study Dashboard")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📈 Transactions Insights",
    "📱 User & Device Insights",
    "🛡 Insurance Insights",
    "🗺 Map Insights",
    "🏆 Top Performers",
    "🗺️ India Map"
])

# ==== 1. Transactions Insights ====
with tab1:
    st.subheader("Select Transaction Insight")
    options = [
        "Top 10 States by Total Transaction Amount",
        "Yearly Transaction Trend for Selected State",
        "Transaction Type Breakdown"
    ]
    choice = st.selectbox("Choose Insight", options, key="trans_insight")

    if choice == options[0]:
        df_top_states = run_query("""
            SELECT State, SUM(TransactionAmount) AS TotalAmount
            FROM Agg_transaction
            GROUP BY State
            ORDER BY TotalAmount DESC
            LIMIT 10
        """)
        fig1 = px.bar(df_top_states, x="State", y="TotalAmount", color="TotalAmount", text_auto=".2s")
        st.plotly_chart(fig1, use_container_width=True)

    elif choice == options[1]:
        df_top_states = run_query("""
            SELECT DISTINCT State FROM Agg_transaction
        """)
        states_list = df_top_states['State'].tolist()
        selected_state = st.selectbox("Select State", states_list, key="yearly_trend_state")
        df_year_trend = run_query(f"""
            SELECT Year, SUM(TransactionAmount) AS TotalAmount
            FROM Agg_transaction
            WHERE State = '{selected_state}'
            GROUP BY Year
            ORDER BY Year
        """)
        fig2 = px.line(df_year_trend, x="Year", y="TotalAmount", markers=True)
        st.plotly_chart(fig2, use_container_width=True)

    elif choice == options[2]:
        df_top_states = run_query("""
            SELECT DISTINCT State FROM Agg_transaction
        """)
        states_list = df_top_states['State'].tolist()
        selected_state = st.selectbox("Select State", states_list, key="type_breakdown_state")
        df_type = run_query(f"""
            SELECT TransactionType, SUM(TransactionAmount) AS TotalAmount
            FROM Agg_transaction
            WHERE State = '{selected_state}'
            GROUP BY TransactionType
        """)
        fig3 = px.pie(df_type, names="TransactionType", values="TotalAmount")
        st.plotly_chart(fig3, use_container_width=True)

# ==== 2. User & Device Insights ====
with tab2:
    st.subheader("Select User & Device Insight")
    options = [
        "Top 10 Device Brands by User Count",
        "State-wise User Engagement Rate"
    ]
    choice = st.selectbox("Choose Insight", options, key="user_device_insight")

    if choice == options[0]:
        df_brands = run_query("""
            SELECT Brands, SUM(Transaction_count) AS TotalUsers
            FROM aggregated_user
            GROUP BY Brands
            ORDER BY TotalUsers DESC
            LIMIT 10
        """)
        fig4 = px.bar(df_brands, x="Brands", y="TotalUsers", color="TotalUsers")
        st.plotly_chart(fig4, use_container_width=True)

    elif choice == options[1]:
        df_engagement = run_query("""
            SELECT m.States,
            SUM(m.RegisteredUser) AS RegisteredUsers,
            SUM(m.AppOpens) AS AppOpens,
            (SUM(m.AppOpens) / SUM(m.RegisteredUser)) AS EngagementRate
            FROM map_user m
            GROUP BY m.States
            ORDER BY EngagementRate DESC
            LIMIT 10
        """)
        fig5 = px.bar(df_engagement, x="States", y="EngagementRate", color="EngagementRate")
        st.plotly_chart(fig5, use_container_width=True)

# ==== 3. Insurance Insights ====
with tab3:
    st.subheader("Select Insurance Insight")
    options = [
        "Top States by Insurance Transaction Amount",
        "Yearly Insurance Growth for Selected State"
    ]
    choice = st.selectbox("Choose Insight", options, key="insurance_insight")

    if choice == options[0]:
        df_insur = run_query("""
            SELECT States, SUM(Insurance_amount) AS TotalAmount
            FROM aggregated_insurance
            GROUP BY States
            ORDER BY TotalAmount DESC
            LIMIT 10
        """)
        fig6 = px.bar(df_insur, x="States", y="TotalAmount", color="TotalAmount")
        st.plotly_chart(fig6, use_container_width=True)

    elif choice == options[1]:
        df_insur = run_query("""
            SELECT DISTINCT States FROM aggregated_insurance
        """)
        states_ins = df_insur['States'].tolist()
        selected_state_ins = st.selectbox("Select State (Insurance)", states_ins, key="insurance_state")
        df_insur_trend = run_query(f"""
            SELECT Years, SUM(Insurance_amount) AS TotalAmount
            FROM aggregated_insurance
            WHERE States = '{selected_state_ins}'
            GROUP BY Years
            ORDER BY Years
        """)
        fig7 = px.line(df_insur_trend, x="Years", y="TotalAmount", markers=True)
        st.plotly_chart(fig7, use_container_width=True)

# ==== 4. Map Insights (Charts only) ====
with tab4:
    st.subheader("Select Map Insight")
    options = [
        "Top 15 States by Transaction Amount",
        "Top 20 Districts by Transaction Amount",
        "Quarterly Transaction Amount Trend (All India)"
    ]
    choice = st.selectbox("Choose Insight", options, key="map_insight")

    if choice == options[0]:
        df_state_amount = run_query("""
            SELECT States AS State, SUM(Transaction_amount) AS TotalAmount
            FROM map_trans
            GROUP BY States
            ORDER BY TotalAmount DESC
            LIMIT 15
        """)
        fig_state = px.bar(
            df_state_amount,
            x='State', y='TotalAmount',
            color='TotalAmount',
            labels={'TotalAmount': 'Transaction Amount'},
            title="Top 15 States by Transaction Amount",
            text_auto=".2s",
            color_continuous_scale='Blues'
        )
        st.plotly_chart(fig_state, use_container_width=True)

    elif choice == options[1]:
        df_district = run_query("""
            SELECT District, SUM(Transaction_amount) AS TotalAmount
            FROM map_trans
            GROUP BY District
            ORDER BY TotalAmount DESC
            LIMIT 20
        """)
        fig_district = px.bar(
            df_district,
            y='District', x='TotalAmount',
            orientation='h',
            color='TotalAmount',
            labels={'TotalAmount': 'Transaction Amount'},
            title="Top 20 Districts by Transaction Amount",
            text_auto=".2s",
            color_continuous_scale='Oranges'
        )
        st.plotly_chart(fig_district, use_container_width=True)

    elif choice == options[2]:
        df_quarterly = run_query("""
            SELECT Year, Quater, SUM(TransactionAmount) AS TotalAmount
            FROM Agg_transaction
            GROUP BY Year, Quater
            ORDER BY Year, Quater
        """)
        df_quarterly['Year-Quater'] = df_quarterly['Year'].astype(str) + '-Q' + df_quarterly['Quater'].astype(str)
        fig_quarterly = px.line(
            df_quarterly,
            x='Year-Quater', y='TotalAmount',
            markers=True,
            title="Quarterly Transaction Amount Trend",
            labels={'Year-Quater': 'Year-Quarter', 'TotalAmount': 'Transaction Amount'}
        )
        st.plotly_chart(fig_quarterly, use_container_width=True)

# ==== 5. Top Performers ====
with tab5:
    st.subheader("Select Top Performer Insight")
    options = [
        "Top 10 Pincodes by Transaction Amount",
        "Top 10 Pincodes by Registered Users",
        "Top 10 Pincodes by Insurance Transaction Amount"
    ]
    choice = st.selectbox("Choose Insight", options, key="top_performers_insight")

    if choice == options[0]:
        df_top_pincode_trans = run_query("""
            SELECT Pincodes, SUM(Transaction_amount) AS TotalAmount
            FROM top_transaction
            GROUP BY Pincodes
            ORDER BY TotalAmount DESC
            LIMIT 10
        """)
        fig9 = px.bar(df_top_pincode_trans, x="Pincodes", y="TotalAmount", color="TotalAmount", text_auto=".2s")
        st.plotly_chart(fig9, use_container_width=True)

    elif choice == options[1]:
        df_top_pincode_users = run_query("""
            SELECT Pincodes, SUM(RegisteredUser) AS TotalUsers
            FROM top_user
            GROUP BY Pincodes
            ORDER BY TotalUsers DESC
            LIMIT 10
        """)
        fig10 = px.bar(df_top_pincode_users, x="Pincodes", y="TotalUsers", color="TotalUsers", text_auto=".2s")
        st.plotly_chart(fig10, use_container_width=True)

    elif choice == options[2]:
        df_top_pincode_ins = run_query("""
            SELECT Pincodes, SUM(Transaction_amount) AS TotalAmount
            FROM top_insurance
            GROUP BY Pincodes
            ORDER BY TotalAmount DESC
            LIMIT 10
        """)
        fig11 = px.bar(df_top_pincode_ins, x="Pincodes", y="TotalAmount", color="TotalAmount", text_auto=".2s")
        st.plotly_chart(fig11, use_container_width=True)

# ==== 6. India Map ====
with tab6:
    st.subheader("India State-wise Transaction Amount")

    df_map = run_query("""
        SELECT State, SUM(TransactionAmount) AS total_amount, COUNT(*) AS transaction_count
        FROM Agg_transaction
        GROUP BY State
    """)

    geojson_url = (
        "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/"
        "e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    )
    india_states = requests.get(geojson_url).json()

    state_name_mapping = {
        "andhra-pradesh": "Andhra Pradesh",
        "karnataka": "Karnataka",
        "madhya-pradesh": "Madhya Pradesh",
        "arunachal-pradesh": "Arunachal Pradesh",
        "meghalaya": "Meghalaya",
        "nagaland": "Nagaland",
        "punjab": "Punjab",
        "delhi": "Delhi",
        "rajasthan": "Rajasthan",
        "goa": "Goa",
        "kerala": "Kerala",
        "sikkim": "Sikkim",
        "andaman-&amp;-nicobar-islands": "Andaman & Nicobar Is.",
        "lakshadweep": "Lakshadweep",
        "jharkhand": "Jharkhand",
        "jammu-&amp;-kashmir": "Jammu & Kashmir",
        "chandigarh": "Chandigarh",
        "telangana": "Telangana",
        "manipur": "Manipur",
        "uttar-pradesh": "Uttar Pradesh",
        "haryana": "Haryana",
        "west-bengal": "West Bengal",
        "chhattisgarh": "Chhattisgarh",
        "assam": "Assam",
        "tamil-nadu": "Tamil Nadu",
        "ladakh": "Ladakh",
        "uttarakhand": "Uttarakhand",
        "himachal-pradesh": "Himachal Pradesh",
        "mizoram": "Mizoram",
        "dadra-&amp;-nagar-haveli-&amp;-daman-&amp;-diu": "Dadra & Nagar Haveli",
        "gujarat": "Gujarat",
        "maharashtra": "Maharashtra",
        "bihar": "Bihar",
        "puducherry": "Puducherry",
        "odisha": "Odisha",
        "tripura": "Tripura"
    }

    df_map['State'] = df_map['State'].replace(state_name_mapping)

    data_states = set(df_map['State'].unique())
    geojson_states = set(feature["properties"]["ST_NM"] for feature in india_states["features"])
    unmatched_states = data_states - geojson_states
    if unmatched_states:
        st.warning(f"Warning: Found unmatched states not in GeoJSON: {unmatched_states}")

    fig_map = px.choropleth(
        df_map,
        geojson=india_states,
        locations='State',
        color='total_amount',
        featureidkey='properties.ST_NM',
        color_continuous_scale='Reds',
        hover_data={
            'total_amount': ':,.2f',
            'transaction_count': True
        },
        labels={'total_amount': 'Transaction Amount'},
        title='PhonePe Total Transaction Amount by State'
    )

    fig_map.update_geos(fitbounds='locations', visible=False)
    fig_map.update_layout(margin={"r":0, "t":30, "l":0, "b":0}, height=500)
    st.plotly_chart(fig_map, use_container_width=True)
