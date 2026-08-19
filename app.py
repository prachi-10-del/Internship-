import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(
    page_title="My Expense Tracker",
    page_icon="💰"
)

# =========================
# BLUE + GREEN + WHITE THEME
# =========================
st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(
        135deg,
        #ffffff 0%,
        #e8f8f5 50%,
        #dbeafe 100%
    );
    min-height: 100vh;
}

/* Top Header */
header[data-testid="stHeader"] {
    background: linear-gradient(
        90deg,
        #064e3b,
        #087f5b,
        #2563eb
    ) !important;
}

div[data-testid="stToolbar"] {
    background: transparent !important;
}

/* Main Title */
h1 {
    background: linear-gradient(
        90deg,
        #064e3b,
        #087f5b,
        #2563eb
    ) !important;

    color: white !important;
    text-align: center !important;
    padding: 15px !important;
    border-radius: 10px !important;
    margin-bottom: 20px !important;
}

/* Headings */
h2, h3, h4 {
    color: #064e3b !important;
    font-weight: bold !important;
}

/* Section Heading */
.expense-heading {
    background: linear-gradient(
        90deg,
        #064e3b,
        #087f5b
    );

    color: white !important;
    padding: 12px;
    border-left: 7px solid #2563eb;
    border-radius: 8px;
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 15px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #ffffff 0%,
        #e8f8f5 60%,
        #dbeafe 100%
    );

    overflow-y: hidden !important;
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 1rem !important;
    padding-bottom: 0rem !important;
}

/* Sidebar Heading */
[data-testid="stSidebar"] .expense-heading {
    font-size: 19px;
    padding: 10px;
    margin-bottom: 10px;
}

/* Sidebar Labels */
[data-testid="stSidebar"] label {
    color: #064e3b !important;
    font-weight: bold !important;
    font-size: 14px !important;
}

[data-testid="stSidebar"] [data-testid="stWidgetLabel"] {
    color: #064e3b !important;
    font-weight: bold !important;
}

[data-testid="stSidebar"] [data-testid="stWidgetLabel"] p {
    color: #064e3b !important;
    font-weight: bold !important;
}

/* Sidebar Inputs */
[data-testid="stSidebar"] [data-testid="stNumberInput"],
[data-testid="stSidebar"] [data-testid="stTextInput"],
[data-testid="stSidebar"] [data-testid="stDateInput"] {
    margin-bottom: 4px !important;
}

[data-testid="stSidebar"] input {
    min-height: 34px !important;
}

/* Sidebar Button */
[data-testid="stSidebar"] .stButton {
    margin-top: 8px !important;
}

[data-testid="stSidebar"] .stButton > button {
    height: 38px !important;
    min-height: 38px !important;
    padding: 5px 10px !important;

    background-color: #087f5b !important;
    color: white !important;

    border: 2px solid #087f5b !important;
    border-radius: 6px !important;

    width: 100%;
    font-weight: bold !important;
}

/* Sidebar Button Hover */
[data-testid="stSidebar"] .stButton > button:hover {
    background-color: #2563eb !important;
    border-color: #2563eb !important;
    color: white !important;
}

/* Sidebar Line */
[data-testid="stSidebar"] hr {
    margin-top: 8px !important;
    margin-bottom: 8px !important;
    border-color: #087f5b !important;
}

/* All Labels */
label {
    color: #064e3b !important;
    font-weight: bold !important;
}

/* Input Border */
div[data-baseweb="input"] {
    border: 1px solid #087f5b;
}

/* Main Buttons */
.stButton > button {
    background-color: #087f5b !important;
    color: white !important;

    border: 2px solid #087f5b !important;
    border-radius: 6px !important;

    width: 100%;
    font-weight: bold !important;
}

/* Main Button Hover */
.stButton > button:hover {
    background-color: #2563eb !important;
    color: white !important;
    border: 2px solid #2563eb !important;
}

/* Button Focus */
.stButton > button:focus {
    background-color: #064e3b !important;
    color: white !important;
}

/* Metric Box */
div[data-testid="stMetric"] {
    background: linear-gradient(
        90deg,
        #064e3b,
        #087f5b,
        #2563eb
    );

    border-left: 8px solid #10b981;
    border-radius: 8px;

    padding: 18px;
    margin-top: 10px;
    margin-bottom: 20px;
}

/* Metric Label */
div[data-testid="stMetric"] label {
    color: white !important;
    font-size: 24px !important;
    font-weight: bold !important;
}

/* Metric Value */
div[data-testid="stMetricValue"] {
    color: #a7f3d0 !important;
    font-size: 30px !important;
    font-weight: bold !important;
}

/* Dropdown Menu */
div[role="menu"] {
    background: #064e3b !important;
    border: 2px solid #087f5b !important;
    border-radius: 10px !important;
}

/* Popover */
div[data-baseweb="popover"] {
    background: #064e3b !important;
    border: 2px solid #087f5b !important;
    border-radius: 10px !important;
}

/* Menu Items */
div[role="menu"] div[role="menuitem"] {
    background: #087f5b !important;
    color: white !important;
    border-radius: 6px !important;
}

div[role="menu"] div[role="menuitem"] * {
    color: white !important;
}

/* Menu Hover */
div[role="menu"] div[role="menuitem"]:hover {
    background: #2563eb !important;
}

/* Header Button */
header[data-testid="stHeader"] button:hover {
    background-color: #087f5b !important;
    color: white !important;
    border-radius: 6px !important;
}

header[data-testid="stHeader"] button:hover * {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)


# =========================
# TITLE
# =========================

st.markdown(
    '<h1>MY EXPENSE TRACKER 💸</h1>',
    unsafe_allow_html=True
)


# =========================
# CSV FILE
# =========================

csv_path = Path(__file__).parent / "expenses.csv"

try:
    df = pd.read_csv(csv_path)

except FileNotFoundError:
    df = pd.DataFrame(
        columns=[
            "Date",
            "Category",
            "Note",
            "Amount"
        ]
    )

except pd.errors.EmptyDataError:
    df = pd.DataFrame(
        columns=[
            "Date",
            "Category",
            "Note",
            "Amount"
        ]
    )


# =========================
# REQUIRED COLUMNS
# =========================

required_columns = [
    "Date",
    "Category",
    "Note",
    "Amount"
]

for column in required_columns:

    if column not in df.columns:
        df[column] = ""


# =========================
# DATA CONVERSION
# =========================

df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
).dt.date

df["Amount"] = pd.to_numeric(
    df["Amount"],
    errors="coerce"
).fillna(0)


# =========================
# SIDEBAR
# =========================

with st.sidebar:

    st.markdown(
        '<div class="expense-heading">Add Your Expense 👇</div>',
        unsafe_allow_html=True
    )

    amount = st.number_input(
        "Amount (₹)",
        min_value=0,
        step=10,
        value=0
    )

    category = st.text_input(
        "Category"
    )

    date = st.date_input(
        "Date"
    )

    note = st.text_input(
        "Note"
    )

    add_expense = st.button(
        "ADD EXPENSE"
    )


# =========================
# ADD EXPENSE
# =========================

if add_expense:

    if amount <= 0:

        st.sidebar.error(
            "⚠️ Please enter a valid amount."
        )

    elif category.strip() == "":

        st.sidebar.error(
            "⚠️ Please enter a category."
        )

    elif note.strip() == "":

        st.sidebar.error(
            "⚠️ Please enter a note."
        )

    else:

        new_expense = {
            "Date": date,
            "Category": category.strip(),
            "Note": note.strip(),
            "Amount": amount
        }

        df.loc[len(df)] = new_expense

        df.to_csv(
            csv_path,
            index=False
        )

        st.sidebar.success(
            "✅ Expense added!"
        )

        st.rerun()


# =========================
# TOTAL SPENT
# =========================

total_spent = float(
    df["Amount"].sum()
)

st.subheader(
    "TOTAL SPENT"
)

st.metric(
    label="Total amount spent",
    value=f"₹ {total_spent:,.0f}"
)


# =========================
# FILTER EXPENSES
# =========================

st.markdown(
    '<div class="expense-heading">Filter Expenses 🔎</div>',
    unsafe_allow_html=True
)

filter_col1, filter_col2, filter_col3 = st.columns(3)


# Category Filter
with filter_col1:

    categories = (
        ["All"]
        +
        sorted(
            df["Category"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )
    )

    selected_category = st.selectbox(
        "Filter by Category",
        categories
    )


# Minimum Amount
with filter_col2:

    if not df.empty:

        maximum_amount = int(
            df["Amount"].max()
        )

    else:

        maximum_amount = 0

    min_amount = st.number_input(
        "Minimum Amount (₹)",
        min_value=0,
        value=0,
        step=10
    )


# Maximum Amount
with filter_col3:

    max_amount = st.number_input(
        "Maximum Amount (₹)",
        min_value=0,
        value=maximum_amount,
        step=10
    )


# =========================
# DATE RANGE
# =========================

if (
    not df.empty
    and df["Date"].notna().any()
):

    min_date = df["Date"].dropna().min()

    max_date = df["Date"].dropna().max()

else:

    min_date = pd.Timestamp.today().date()

    max_date = pd.Timestamp.today().date()


date_col1, date_col2 = st.columns(2)


with date_col1:

    start_date = st.date_input(
        "From Date",
        value=min_date
    )


with date_col2:

    end_date = st.date_input(
        "To Date",
        value=max_date
    )


# =========================
# APPLY FILTERS
# =========================

filtered_df = df.copy()


if selected_category != "All":

    filtered_df = filtered_df[
        filtered_df["Category"].astype(str)
        == selected_category
    ]


if min_amount <= max_amount:

    filtered_df = filtered_df[
        (filtered_df["Amount"] >= min_amount)
        &
        (filtered_df["Amount"] <= max_amount)
    ]

else:

    st.warning(
        "⚠️ Minimum amount cannot be greater than maximum amount."
    )

    filtered_df = filtered_df.iloc[0:0]


if start_date <= end_date:

    filtered_df = filtered_df[
        (filtered_df["Date"] >= start_date)
        &
        (filtered_df["Date"] <= end_date)
    ]

else:

    st.warning(
        "⚠️ From Date cannot be after To Date."
    )

    filtered_df = filtered_df.iloc[0:0]


# =========================
# SHOWING EXPENSE COUNT
# =========================

st.markdown(
    f"""
    <div style="
        color: #064e3b;
        font-size: 18px;
        font-weight: bold;
        margin-top: 10px;
        margin-bottom: 10px;
    ">
        Showing {len(filtered_df)} expense(s)
    </div>
    """,
    unsafe_allow_html=True
)


# =========================
# FILTERED TOTAL
# =========================

filtered_total = float(
    filtered_df["Amount"].sum()
)

st.subheader(
    "FILTERED TOTAL"
)

st.metric(
    label="Amount after applying filters",
    value=f"₹ {filtered_total:,.0f}"
)


# =========================
# SPENDING BY CATEGORY
# =========================

st.subheader(
    "Spending by Category"
)


if not filtered_df.empty:

    category_total = (
        filtered_df
        .groupby("Category")["Amount"]
        .sum()
    )

    fig, ax = plt.subplots(
        figsize=(8, 4)
    )

    ax.bar(
        category_total.index,
        category_total.values,
        color="#087f5b"
    )

    ax.set_xlabel(
        "Category",
        labelpad=8
    )

    ax.set_ylabel(
        "Amount (₹)"
    )

    ax.set_title(
        "Expenses by Category"
    )

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)

else:

    st.warning(
        "⚠️ No expenses found for the selected filters."
    )


# =========================
# RECENT EXPENSES
# =========================

st.subheader(
    "Recent Expenses"
)


if not filtered_df.empty:

    display_df = (
        filtered_df
        .sort_values(
            by="Date",
            ascending=False
        )
    )

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "No expenses available to display."
    )