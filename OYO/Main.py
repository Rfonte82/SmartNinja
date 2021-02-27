import streamlit as st
import pandas as pd
#import pymongo
import io
import openpyxl
import Datamongo


# Save File Function

#def save_uploaded_file(uploadedfile):
#    with open(os.path.join("C:/test", uploadedfile.name), "wb") as f:
#        f.write(uploadedfile.getbuffer())
#    return st.success("File Saved".format(uploadedfile.name))


"""Run this function to display the Streamlit app"""
#st.info(__doc__)
#st.markdown(STYLE, unsafe_allow_html=True)
navigation=st.sidebar.radio("Go to",["Contactos","EFatura","Criar Documento",])
if navigation =="EFatura":
    # List Declaration
    efatura_header = ['Setor', 'Comerciante', 'Tipo', 'Situação', 'Nº Fatura', 'Código Controlo', 'Data Emissão','IVA', 'Valor Total', 'Registado por Comerciante', 'Registado por Consumidor']
    db_header = ['Num Interno','Data Documento','Pais','NIF','Entidade', 'Valor IVA', 'Total', 'Tipo Despesa', 'Data Limite Pagamento', 'Ref Bancária', 'Mapa Despesa', 'Data Limite Pagamento' , 'Comentários',]
    uploaded_file = st.file_uploader("Upload FIle", type=['pdf','csv' , 'xlsx'])
    #print(uploaded_file) # Debug file name
    if uploaded_file is not  None:
        #st.write(" Sucess file uploaded")
        try:
            df1 = pd.read_csv(uploaded_file)
        except Exception as e:
            print(e)
            # Excel file
            df1 = pd.read_excel(uploaded_file) # Read uploaded file


    try:
        st.write(df1)
        #st.write(len(df))
        # Save dataframe on db2021
        b_save = st.button('Start Game')

        if  b_save ==True:

            df2 = pd.read_excel('C:/test/db/db2021.xlsx')  # Read Destination File

            # Create a Pandas Excel writer using XlsxWriter as the engine.
            writer = pd.ExcelWriter('C:/test/db/db2021.xlsx', engine='openpyxl')

            i=1
            for i in range(len(df1)):
                df1_data = (df1.at[i, efatura_details[4]])  # Data from Uploaded File
                for i in range(len(df2)):
                    df2_data = (df2.at[i, db_header[1]])  # Data from database
                    if   df1_data == df2_data:
                        break
                # initialize list of lists
                df3_data = [int(sizedf2+1),'1','2','3','4','5','6','7','8','9','10','11','12'] # Create Dataframe Strucure
                df3 = pd.DataFrame(df3_data)
                df3.to_excel(writer, sheet_name='Sheet1')
            writer.save()

            #
            #    df.loc[[i]].to_excel('C:/test/db/db2022.xlsx',
            #                       index=False,
            #                       header=False,
            #                       mode='a')
    except Exception as e:
        print(e)
        i = 0
        #st.write("Please Upload File")
        st.info("Please Upload File")





