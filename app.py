import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

st.set_page_config(page_title="E-Commerce AI Dashboard", layout="wide", page_icon="🛒")

# --- Custom CSS for Premium Look ---
st.markdown("""
<style>
.main { background-color: #f8f9fa; }
.metric-card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    border-left: 5px solid #7C3AED;
}
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("# 🛒 E-Commerce AI Dashboard")
st.markdown("#### Powered by AI Insights | Fatima's Project")
st.divider()

# --- Generate Dummy Data ---
@st.cache_data
def load_data():
    dates = [datetime.now() - timedelta(days=x) for x in range(30)][::-1]
    data = {
        'Date': dates,
        'Sales': [random.randint(1500, 5000) + i*50 for i in range(30)],
        'Orders': [random.randint(50, 200) for _ in range(30)],
        'Visitors': [random.randint(1000, 5000) for _ in range(30)],
        'Category': [random.choice(['Electronics', 'Fashion', 'Home', 'Beauty']) for _ in range(30)]
    }
    df = pd.DataFrame(data)
    
    products = pd.DataFrame({
        'Product': ['iPhone 15', 'Nike Shoes', 'Coffee Maker', 'Lipstick Set', 'Laptop Stand'],
        'Sales': [120, 95, 80, 70, 60],
        'Revenue': [120000, 45000, 20000, 15000, 12000],
        'Stock': [15, 3, 42, 8, 25]
    })
    return df, products

df, products_df = load_data()

# --- KPIs ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Revenue", "$ 89,430", "12.5%")
with col2:
    st.metric("Total Orders", "1,842", "8.2%")
with col3:
    st.metric("Conversion Rate", "3.24%", "-0.5%")
with col4:
    st.metric("AI Predicted Growth", "18.7%", "AI Forecast")

st.markdown("---")

# --- Tabs ---
tab1, tab2, tab3, tab4 = st.tabs(["📈 Sales Analytics", "🤖 AI Insights", "📦 Inventory", "👥 Customers"])

with tab1:
    c1, c2 = st.columns([2,1])
    with c1:
        st.subheader("Sales Trend - Last 30 Days")
        fig = px.line(df, x='Date', y='Sales', template="plotly_white")
        fig.update_traces(line_color='#7C3AED', line_width=3)
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        st.subheader("Category Wise Sales")
        fig2 = px.pie(df, names='Category', values='Sales', hole=0.5, color_discrete_sequence=px.colors.sequential.Purples_r)
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Top Selling Products")
    st.dataframe(products_df, use_container_width=True)

with tab2:
    st.subheader("🤖 AI-Powered Business Intelligence")
    col_a, col_b = st.columns(2)
    with col_a:
        st.info("**🔮 Demand Forecast:** Next week me Electronics ki demand 23% badhne wali hai. Stock badhao!")
        st.success("**💡 Price Optimization:** Nike Shoes ka price $5 badhane se profit 12% increase hoga - AI Suggestion")
        st.warning("**⚠️ Low Stock Alert:** Nike Shoes me sirf 3 pieces bache hain! Reorder karo.")
    with col_b:
        st.markdown("**AI Customer Sentiment**")
        sentiment_data = {'Positive': 68, 'Neutral': 22, 'Negative': 10}
        fig_s = px.bar(x=list(sentiment_data.keys()), y=list(sentiment_data.values()), color=list(sentiment_data.keys()), color_discrete_sequence=['#10B981','#6B7280','#EF4444'])
        st.plotly_chart(fig_s, use_container_width=True)
    
    st.markdown("### Chat with AI Assistant")
    user_q = st.text_input("Apna sawal likho (e.g., Which product is most profitable?)")
    if user_q:
        st.write(f"🤖 **AI Answer:** '{user_q}' ke liye, data ke mutabiq **iPhone 15** sabse zyada profitable hai with 120 units sold!")

with tab3:
    st.subheader("Inventory Management")
    st.dataframe(products_df.style.applymap(lambda x: 'background-color: #FECACA' if isinstance(x, int) and x < 10 else '', subset=['Stock']), use_container_width=True)
    fig_stock = px.bar(products_df, x='Product', y='Stock', color='Stock', color_continuous_scale='Reds')
    st.plotly_chart(fig_stock, use_container_width=True)

with tab4:
    st.subheader("Customer Analytics")
    st.markdown("Total Customers: **12,450** | New this Month: **890**")
    cust_df = pd.DataFrame({'Segment': ['Loyal', 'New', 'At Risk', 'VIP'], 'Count': [4500, 3200, 1800, 950]})
    fig_c = px.treemap(cust_df, path=['Segment'], values='Count', color='Count', color_continuous_scale='Purples')
    st.plotly_chart(fig_c, use_container_width=True)

st.divider()
st.caption("Made with ❤️ by Fatima | E-Commerce AI Dashboard v1.0")
