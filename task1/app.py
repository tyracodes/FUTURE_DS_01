import streamlit as st
import pandas as pd

#  PAGE CONFIG
st.set_page_config(
    page_title="Superstore Dashboard",
    page_icon="📊",
    layout="wide"
)

# LOAD DATA
@st.cache_data
def load_data():
    file_path = os.path.join(os.path.dirname(__file__), "Superstore_Cleaned.csv")

    df = pd.read_csv(file_path, encoding="ISO-8859-1")

    return df


df = load_data()

# CUSTOM CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fb;
    }
    h1 {
        color: #1f4e79;
        font-size: 40px;
    }
    .stMetric {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

#  TITLE
st.title(" Superstore Sales Dashboard")

# SIDEBAR FILTERS
st.sidebar.header("🔍 Filters")

region = st.sidebar.multiselect(
    "Select Region",
    df["Region"].unique(),
    default=df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    df["Category"].unique(),
    default=df["Category"].unique()
)

segment = st.sidebar.multiselect(
    "Select Segment",
    df["Segment"].unique(),
    default=df["Segment"].unique()
)

#  FILTER DATA
filtered_df = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category)) &
    (df["Segment"].isin(segment))
]

#KPI ROW
col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${filtered_df['Sales'].sum():,.2f}")
col2.metric("Total Profit", f"${filtered_df['Profit'].sum():,.2f}")
col3.metric("Total Orders", filtered_df["Order ID"].nunique())

st.divider()

# CHARTS
st.subheader("Sales by Category")
st.bar_chart(filtered_df.groupby("Category")["Sales"].sum())

st.subheader("Profit by Category")
st.bar_chart(filtered_df.groupby("Category")["Profit"].sum())

st.subheader("Sales by Region")
st.bar_chart(filtered_df.groupby("Region")["Sales"].sum())

st.subheader("Monthly Sales Trend")
monthly = filtered_df.groupby("Month-Year")["Sales"].sum()
st.line_chart(monthly)

st.subheader("Top 10 Products")
top_products = filtered_df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_products)
