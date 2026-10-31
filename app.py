import streamlit as st
import pandas as pd

st.set_page_config(page_title="E-Commerce AI Dashboard", layout="wide")

st.title("🛒 E-Commerce AI Dashboard")

tab1, tab2, tab3 = st.tabs(["Sales Overview", "Chat with AI", "About"])

with tab1:
    st.subheader("Sales Overview")
    
    data = {
        'Product': ['iPhone 15', 'Nike Shoes', 'Coffee Maker', 'T-Shirt'],
        'Units Sold': [120, 95, 85, 60],
        'Revenue': [120000, 9500, 4250, 1200]
    }
    df = pd.DataFrame(data)
    
    st.dataframe(df, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Revenue by Product (Bar Chart)")
        st.bar_chart(df.set_index('Product')['Revenue'])

    with col2:
        st.subheader("Units Sold (Line Chart)")
        st.line_chart(df.set_index('Product')['Units Sold'])
    
    col3, col4 = st.columns(2)
    col3.metric("Total Revenue", "$134,950")
    col4.metric("Total Units", "360")

with tab2:
    st.markdown("### Chat with AI Assistant")
    user_q = st.text_input("Enter your question (e.g., Which product is most profitable?)")
    if user_q:
        q = user_q.lower()
        if "coffee" in q:
            st.write(f"🤖 **AI Answer:** Coffee Maker sold 85 units with revenue of $4,250.")
        elif "nike" in q or "shoe" in q:
            st.write(f"🤖 **AI Answer:** Nike Shoes sold 95 units with revenue of $9,500.")
        elif "iphone" in q or "phone" in q or "profitable" in q or "revenue" in q or "highest" in q or "higest" in q or "most" in q:
            st.write(f"🤖 **AI Answer:** iPhone 15 is the most profitable! Sold 120 units with revenue of $120,000.")
        else:
            st.write(f"🤖 **AI Answer:** Based on data, total 360 units sold. iPhone is top product.")

with tab3:
    st.write("This dashboard analyzes E-Commerce data with AI Assistant.")
