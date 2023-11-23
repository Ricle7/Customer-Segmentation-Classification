import streamlit as st
import streamlit.components.v1 as stc

from ml_app2 import run_ml_appp

html_temp = """
            <div style="background-color:#3872fb;padding:10px;border-radius:10px">
            <h1 style="color:white;text-align:center;">Customer Segmentation Classification</h1>
            <h3 style="color:white;text-align:center;">Classify the customers into four segments</h3>
            </div>
            """

desc_temp = """
            ### Customer Segmentation Classification App
            Categorizing customers into four segments is a strategic move that enables companies to better understand 
            and respond more effectively to individual needs and preferences. By conducting in-depth analysis of purchasing behavior, 
            companies can identify underlying trends within the segments, opening up opportunities to improve customer experience and 
            optimize marketing strategies. This classification process not only helps in customizing service approaches, but also opens 
            up the potential for more targeted product development, creating stronger connections with customers, and ultimately, 
            increasing customer satisfaction and loyalty.

            #### Data Source
            https://www.kaggle.com/datasets/kaushiksuresh147/customer-segmentation/code 
            #### App Content
            Machine Learning Section
            """

def main():
    # st.title("Main App")
    stc.html(html_temp)

    menu = ['Home', 'Machine Learning']
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == 'Home':
        # st.subheader("Home")
        st.subheader("Welcome to Homepage")
        st.markdown(desc_temp)

    elif choice == "Machine Learning":
        # st.subheader("Welcome to Machine learning")
        run_ml_appp()


if __name__ == '__main__':
    main()