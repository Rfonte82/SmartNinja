import streamlit as st
import pandas as pd
import pymongo
import io
import openpyxl


# Save File Function

def save_uploaded_file(uploadedfile):
    with open(os.path.join("C:/test", uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success("File Saved".format(uploadedfile.name))


"""Run this function to display the Streamlit app"""
#st.info(__doc__)
#st.markdown(STYLE, unsafe_allow_html=True)
global df
navigation=st.sidebar.radio("Go to",["Dashboard","Upload Invoice","Create Expense Doc", "Create Km File"])
if navigation == "Upload Invoice" :
    #@st.cache
    # upload de faturas
   # caching.clear_cache()
    invoice_data = st.date_input("Invoice Data")
    invoice_overdue = st.date_input("Overdue Data")
    # validate overdue data
    # Invoice number
    invoice_number = st.text_input("Invoice Number")
    # Invoice Details
    invoice_details = {"Invoice Data": invoice_data,"Overdue Data":invoice_overdue,"Invoice Number":invoice_number }
    # Debug Invoice Details
    #st.write(invoice_details)


    uploaded_file = st.file_uploader("Upload FIle", type=['pdf','csv' , 'xlsx'])
    #print(uploaded_file)

    if uploaded_file is not  None:
        st.write(" Sucess file uploaded")
        try:
            df = pd.read_csv(uploaded_file)
        except Exception as e:
            print(e)
            df =pd.read_excel(uploaded_file)

    try:
        st.write(df)
    except Exception as e:
        print(e)
        st.write("Please Upload File")



