import streamlit as st
import pandas as pd

st.set_page_config(page_title="E-Commerce AI Dashboard", layout="wide")
st.title("🛒 E-Commerce AI Dashboard")
st.markdown("Made with ❤️ by Fatima | E-Commerce AI Dashboard v1.0")

data = {'Product': ['iPhone 15', 'Coffee Maker', 'Nike Shoes', 'Samsung TV'], 'Units_Sold': [120, 85, 95, 60], 'Revenue': [120000, 4250, 9500, 30000]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["Overview", "AI Assistant", "About"])

with tab1:
    st.subheader("Sales Overview")
    st.dataframe(df)
    st.bar_chart(df.set_index('Product')['Units_Sold'])

with tab2:
    st.markdown("### Chat with AI Assistant")
    user_q = st.text_input("Enter your question (e.g., Which product is most profitable?)")
    if user_q:
        q = user_q.lower()
        if "coffee" in q:
            st.write(f"🤖 **AI Answer:** Coffee Maker sold 85 units with revenue of $4,250.")
        elif "nike" in q or "shoe" in q:
            st.write(f"🤖 **AI Answer:** Nike Shoes sold 95 units with revenue of $9,500.")
        elif "iphone" in q or "phone" in q or "profitable" in q:
            st.write(f"🤖 **AI Answer:** iPhone 15 is the most profitable! Sold 120 units with revenue of $120,000.")
        else:
            st.write(f"🤖 **AI Answer:** Based on data, total 360 units sold. iPhone is top product.")

with tab3:
    st.write("This dashboard analyzes E-Commerce data with AI insights.")
    elif "iphone" in q or "phone" in q or "profitable" in q or "revenue" in q or "highest" in q:
