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
        st.write(f"🤖 **AI Answer:** For '{user_q}', according to data, iPhone 15 is the most profitable with 120 units sold!")

with tab3:
    st.write("This dashboard analyzes E-Commerce data with AI insights.")
