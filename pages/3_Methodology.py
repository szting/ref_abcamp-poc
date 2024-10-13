import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Methodology Page")

st.markdown('''**Detailed Flowchart Description For Hospital Ward Class Planning Simulator:** \n
1.	User Submits Query: User enters a query in the Streamlit app and the query is sent to the BaseCallbackHandler. \n
2.	BaseCallbackHandler Receives Query: The handler receives and processes the incoming query and routed directly to the Information Retrieval Agent. \n
3.	Information Retrieval Agent Processing: This agent analyses the query using PDFSearchTool and generates a response based on its analysis for Customer Service Agent to process. \n
4.	Customer Service Agent Processing: This agent analyses the query using FileReadTool and prepare the output which is a well-structured response ready for display. \n
5.	Output to User: Display the final response to the user in the Streamlit app and await further interactions. Users can provide feedback on the response, which can loop back for further queries and back to 1. \n
''')

st.image("ward-class-flowchart.jpg")

st.markdown('''**Detailed Flowchart Description For MediSave Explainer:** \n
1.	User Submits Query: User enters a query in the Streamlit app and the query is sent to the BaseCallbackHandler. \n
2.	BaseCallbackHandler Receives Query: The handler receives and processes the incoming query and routed directly to the Researcher Agent. \n
3.	Researcher Agent Processing: This agent analyses the query using ScrapeWebsiteTool and generates a response based on its analysis for Customer Service Agent to process.\n
4.	Customer Service Agent Processing: This agent analyses the query using FileReadTool and prepare the output which is a well-structured response ready for display. \n
5.	Output to User: Display the final response to the user in the Streamlit app and await further interactions. Users can provide feedback on the response, which can loop back for further queries and back to 1.
''')

st.image("medisave-flowchart.jpg")
