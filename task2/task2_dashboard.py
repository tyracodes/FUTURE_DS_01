import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Customer Retention & Churn Dashboard",
    page_icon="📊",
    layout="wide"
)


# Load Data


@st.cache_data
def load_data():
    df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    df = df.dropna()

    df["CustomerLifetimeValue"] = (
        df["MonthlyCharges"] * df["tenure"]
    )

    df["TenureGroup"] = pd.cut(
        df["tenure"],
        bins=[0,12,24,36,48,60,72],
        labels=[
            "0-12",
            "13-24",
            "25-36",
            "37-48",
            "49-60",
            "61-72"
        ]
    )

    return df

df = load_data()


# Title


st.title("📊 Customer Retention & Churn Analysis Dashboard")

st.markdown("""
This dashboard analyzes customer churn patterns, retention drivers,
and customer lifetime trends for a subscription-based business.
""")

# KPIs


churn_rate = (
    (df["Churn"] == "Yes").mean() * 100
)

retention_rate = (
    (df["Churn"] == "No").mean() * 100
)

avg_clv = (
    df["CustomerLifetimeValue"].mean()
)

avg_tenure = (
    df["tenure"].mean()
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Churn Rate",
    f"{churn_rate:.2f}%"
)

col2.metric(
    "Retention Rate",
    f"{retention_rate:.2f}%"
)

col3.metric(
    "Average CLV",
    f"${avg_clv:,.0f}"
)

col4.metric(
    "Average Tenure",
    f"{avg_tenure:.1f} Months"
)

st.divider()


# Row 1


col1, col2 = st.columns(2)

with col1:

    st.subheader("Customer Churn Distribution")

    fig, ax = plt.subplots()

    sns.countplot(
        data=df,
        x="Churn",
        ax=ax
    )

    st.pyplot(fig)

with col2:

    st.subheader("Churn Rate by Contract Type")

    contract_churn = pd.crosstab(
        df["Contract"],
        df["Churn"],
        normalize="index"
    ) * 100

    fig, ax = plt.subplots()

    contract_churn["Yes"].plot(
        kind="bar",
        ax=ax
    )

    ax.set_ylabel("Churn %")

    st.pyplot(fig)


# Row 2


col1, col2 = st.columns(2)

with col1:

    st.subheader("Churn Rate by Payment Method")

    payment_churn = pd.crosstab(
        df["PaymentMethod"],
        df["Churn"],
        normalize="index"
    ) * 100

    fig, ax = plt.subplots()

    payment_churn["Yes"].sort_values().plot(
        kind="barh",
        ax=ax
    )

    ax.set_xlabel("Churn %")

    st.pyplot(fig)

with col2:

    st.subheader("Retention by Tenure Group")

    retention = pd.crosstab(
        df["TenureGroup"],
        df["Churn"],
        normalize="index"
    ) * 100

    fig, ax = plt.subplots()

    retention["No"].plot(
        kind="bar",
        ax=ax
    )

    ax.set_ylabel("Retention %")

    st.pyplot(fig)


# Row 3


col1, col2 = st.columns(2)

with col1:

    st.subheader("Tenure Distribution")

    fig, ax = plt.subplots()

    sns.histplot(
        data=df,
        x="tenure",
        hue="Churn",
        bins=30,
        kde=True,
        ax=ax
    )

    st.pyplot(fig)

with col2:

    st.subheader("Customer Lifetime Value Distribution")

    fig, ax = plt.subplots()

    sns.histplot(
        df["CustomerLifetimeValue"],
        bins=30,
        ax=ax
    )

    st.pyplot(fig)


# Business Insights


st.divider()

st.header(" Key Insights")

st.markdown("""
### Churn Patterns

- Overall churn rate is **26.58%**.
- Customers on **month-to-month contracts** are the most likely to leave.
- Customers using **electronic checks** show the highest churn rate.
- Newer customers are significantly more likely to churn.

### Retention Drivers

- Long-term contracts strongly improve retention.
- Customers with longer tenure remain loyal.
- Customers retained beyond 60 months have very low churn.

### Customer Lifetime Trends

- Average Customer Lifetime Value is approximately **$2,283**.
- Customers with higher tenure generate substantially more value.
- Early churn significantly reduces lifetime revenue.
""")

# Recommendations


st.header(" Recommendations")

st.markdown("""
1. Offer incentives for customers to move from month-to-month plans to annual contracts.

2. Improve onboarding and engagement during the first 12 months.

3. Create targeted retention campaigns for electronic-check customers.

4. Introduce loyalty rewards for long-term subscribers.

5. Monitor high-risk customer segments and intervene before churn occurs.
""")

# --------------------------
# Raw Data
# --------------------------

with st.expander("View Dataset"):

    st.dataframe(df)
