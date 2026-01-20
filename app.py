import streamlit as st
import langchain_helper

st.set_page_config(
    page_title="2023 Restaurant Generator",
    page_icon="👌",
    layout= "centered"

)

st.title("AI Restaurant Idea Generator")
st.markdown("""
            select a cuisine from the sidebar, and our AI Will Dream up a 
            **unique restaurant name** and a **signature menu** fro you!
""")
st.sidebar.image("C:\\Users\\nisha\\OneDrive\\Documents\\pics11.webp")
st.sidebar.title("Configuration")

cuisine = st.sidebar.selectbox(
    "Choose a Cuisine",
    ("Indian","Itailian", "Mexicon", "Japanese","Turkish")
)

if cuisine:
    with st.spinner(f" Our AI chef is creating {cuisine}  ideas..."):
        try:
            response = langchain_helper.generate_restaurant_name_and_items(cuisine)
            st.divider()
            st.markdown(f" ### Recommended Name")
            st.success(f"**{response['restaurant_name']}**")
            st.markdown(f"### Signature Menu")

            menu_items = response['menu_items'].split(",")
            for items in menu_items :
                st.write(f" {items.strip()}")


        except Exception as e :
            st.error ("Something went wrong. Please check your API Key or model set")
            st.exception(e)