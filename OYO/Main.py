import streamlit as st
import pymongo
import io
import os



# Save File Function

def save_uploaded_file(uploadedfile):
    with open(os.path.join("C:/test", uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success("File Saved".format(uploadedfile.name))


"""Run this function to display the Streamlit app"""
#st.info(__doc__)
#st.markdown(STYLE, unsafe_allow_html=True)
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


    uploaded_file = st.file_uploader("Upload FIle", type=['pdf','csv'])
    #print(uploaded_file)

    if uploaded_file is not  None:
        st.write(" file uploaded")
        file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
        st.write(file_details)
        # save_uploaded_file( uploaded_file.name )
        with open( uploaded_file.name, 'r' ) as csvfile:
            content = csvfile.read().splitlines()
            for row in content :
                row_data: row.split(",")
                print(row_data[0])



