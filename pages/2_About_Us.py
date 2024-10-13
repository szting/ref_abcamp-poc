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
This use case will allow users to simulate various hospital ward class 
scenarios based on information, such as benefits, government subsidies, 
deductible, co-insurance and exclusions under the MediShield Life Scheme. 
Users can use this information to plan the hospital ward class that suits 
their budget and helping them make informed decision if additional private 
insurance coverage is required.\n
        
MediSave Explainer with Interactive Scenarios based on User Inputs: \n
Users can explore usage of MediSave savings through interactive scenarios 
that illustrate how it can help with their healthcare expenses. This 
feature will enhance understanding by allowing users to see the practical
implications of using MediSave savings in their healthcare financing.
''')

st.markdown('''**Project Scope:** \n
Your MediShield Life and MediSave's Info Buddy app aims to provide users with easy access 
to information about MediShield Life Scheme and usage of MediSave savings. It will serve as 
a one-stop platform for users to compare different hospital ward class plans that suits their 
budget and using MediSave savings in their healthcare financing to make informed decisions.
''')

st.markdown('''**Objectives:** \n
•	To simplify the process of finding and comparing hospital ward class options.\n
•	To provide clear and concise information about healthcare financing features and benefits.\n
•	To assist users in selecting the best hospital ward class plan based on their personal requirements and financial constraints.\n
•	To offer guidance on usage of MediSave savings in their healthcare financing.\n
•	Provide 24/7 access to information, making it easier for users to understand their options healthcare financing needs.\n
•	Decrease the workload on customer service representatives by automating responses to common queries.
''')

st.markdown('''**Data Sources**: This app will aggregate data from the following official government websites: \n
https://www.cpf.gov.sg/content/dam/web/member/healthcare/documents/InformationBookletForTheNewlyInsured.pdf \n
https://www.cpf.gov.sg/member/healthcare-financing/using-your-medisave-savings \n
https://www.cpf.gov.sg/member/healthcare-financing/using-your-medisave-savings/using-medisave-for-outpatient-treatments \n
https://www.cpf.gov.sg/member/healthcare-financing/using-your-medisave-savings/using-medisave-for-hospitalisation \n
https://www.cpf.gov.sg/member/healthcare-financing/using-your-medisave-savings/applying-to-use-your-healthcare-plans \n
''')

st.markdown('''**Features:** \n
•	LLM-powered app to understand and respond to user queries in a conversational manner. \n
•	Hospital Ward Class Claim Computation Details: Detailed breakdowns of what each claim covers, including daily hospital charges, surgery, total hospital bill, less: deductible, claimable amount, less: co-insurance, MediShield Life and MediSave pays amounts. \n
•	MediSave Explainer Tool: Allows users to explore the usage of MediSave savings in their healthcare financing, including the eligibility and benefits. \n
''')
