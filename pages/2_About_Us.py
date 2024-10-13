import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("About Us Page")

st.markdown('''**Use Cases for Navigating Healthcare Coverage and Protection (MediShield Life and Medisave):** \n
        Hospital Ward Class Planning Simulator: \n
        This use case will allow users to simulate various hospital ward class scenarios 
        based on information, such as benefits, government subsidies, deductible, co-insurance 
        and exclusions under the MediShield Life Scheme. Users can use this information to plan 
        the hospital ward class that suits their budget and helping them make informed decision 
        if additional private insurance coverage is required.\n
        
        MediSave Explainer with Interactive Scenarios based on User Inputs: \n
        Users can explore usage of MediSave savings through interactive scenarios that illustrate 
        how it can help with their healthcare expenses. This feature will enhance understanding 
        by allowing users to see the practical implications of using MediSave savings in their 
        healthcare financing.''')

st.markdown('''**Objectives:** \n

                •	To simplify the process of finding and comparing hospital ward class options.
                •	To provide clear and concise information about healthcare financing features and benefits.''')

st.write("This is a Streamlit App that demonstrates how to use the OpenAI API to generate text completions.")

st.write("This is a Streamlit App that demonstrates how to use the OpenAI API to generate text completions.")
