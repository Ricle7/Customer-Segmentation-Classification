import streamlit as st
import numpy as np

# import ml package
import joblib
import os

attribute_info = """
                 - Profession: Healthcare, Engineer, Lawyer, Entertainment, Artist,
                                Executive, Doctor, Homemaker, Marketing
                 - Work Experience: 0-14
                 - Gender: Male and Female
                 - Age: 18-89
                 - Married: 1. Yes, 0. No
                 - Graduation: 1. Yes, 0. No
                 - Family size: 0-9
                 - Var_1: Cat_1, Cat_2, Cat_3, Cat_4, Cat_5, 
                                 Cat_6, Cat_7
                 - Spending Score: Low, Average, High
                
                 """


grad = {'Yes':1, 'No':0}
gen = {'m':1, 'f':0}
marr = {'Yes':1, 'No':0}
Artist ={'Yes':1, 'No':0}
Engineer ={'Yes':1, 'No':0}
Lawyer ={'Yes':1, 'No':0}
Entertainment ={'Yes':1, 'No':0}
Executive ={'Yes':1, 'No':0}
Doctor ={'Yes':1, 'No':0}
Homemaker ={'Yes':1, 'No':0}
Marketing ={'Yes':1, 'No':0}
Healthcare ={'Yes':1, 'No':0}
high = {'Yes':1, 'No':0}
average = {'Yes':1, 'No':0}
low = {'Yes':1, 'No':0}
cat1 = {'Yes':1, 'No':0}
cat2 = {'Yes':1, 'No':0}
cat3 = {'Yes':1, 'No':0}
cat4 = {'Yes':1, 'No':0}
cat5 = {'Yes':1, 'No':0}
cat6 = {'Yes':1, 'No':0}
cat7 = {'Yes':1, 'No':0}


def get_value(val, my_dict):
   for key, value in my_dict.items():
       if val == key:
           return value

            
def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file), 'rb'))
    return loaded_model

def run_ml_appp():
    st.subheader("ML Section")
    with st.expander("Attribute Info"):
        st.markdown(attribute_info)

    st.subheader("Input Your Data")
    gender = st.radio('Gender', ['m','f'])
    married = st.selectbox('Married', ['No','Yes'])
    age = st.number_input("Age",18,89)
    graduated = st.selectbox('Graduated', ['No','Yes'])
    work_experience = st.number_input("Work Experience",0,14)
    family = st.number_input("Family size",0,9)
    


    
    with st.expander("Profession Options"):
        #Options for Profession
        Profession_Artist = st.selectbox('Artist',['No','Yes'])
        Profession_Engineer = st.selectbox('Engineer',['No','Yes'])
        Profession_Lawyer = st.selectbox('Lawyer',['No','Yes'])
        Profession_Entertainment = st.selectbox('Entertainment',['No','Yes'])
        Profession_Executive = st.selectbox('Executive',['No','Yes'])
        Profession_Doctor = st.selectbox('Doctor',['No','Yes'])
        Profession_Homemaker = st.selectbox('Homemaker',['No','Yes'])
        Profession_Marketing = st.selectbox('Marketing',['No','Yes'])
        Profession_Healthcare = st.selectbox('Healthcare',['No','Yes'])
        
        # Profession_Artist = st.radio('Artist',['No','Yes'])
        # Profession_Engineer = st.radio('Engineer',['No','Yes'])
        # Profession_Lawyer = st.radio('Lawyer',['No','Yes'])
        # Profession_Entertainment = st.radio('Entertainment',['No','Yes'])
        # Profession_Executive = st.radio('Executive',['No','Yes'])
        # Profession_Doctor = st.radio('Doctor',['No','Yes'])
        # Profession_Homemaker = st.radio('Homemaker',['No','Yes'])
        # Profession_Marketing = st.radio('Marketing',['No','Yes'])
        # Profession_Healthcare = st.radio('Healthcare',['No','No'])
    
    # Other options
    with st.expander("Var 1 Options"):
        cat1 = st.selectbox('Cat_1',['No','Yes'])
        cat2 = st.selectbox('Cat_2',['No','Yes'])
        cat3 = st.selectbox('Cat_3',['No','Yes'])
        cat4 = st.selectbox('Cat_4',['No','Yes'])
        cat5 = st.selectbox('Cat_5',['No','Yes'])
        cat6 = st.selectbox('Cat_6',['No','Yes'])
        cat7 = st.selectbox('Cat_7',['No','Yes'])
    
    with st.expander("Spending Score Option"):
        spending_average = st.selectbox('Spending_Score_Average',['No','Yes'])
        spending_high = st.selectbox('Spending_Score_High',['No','Yes'])
        spending_low = st.selectbox('Spending_Score_Low',['No','Yes'])
    

    with st.expander("Your Selected Options"):
        result = {
            'Healthcare':Profession_Healthcare,
            'Engineer': Profession_Engineer,
            'Lawyer':Profession_Lawyer,
            'Entertainment':Profession_Entertainment,
            'Artist':Profession_Artist,
            'Executive':Profession_Executive,
            'Doctor':Profession_Doctor,
            'Homemaker':Profession_Homemaker,
            'Marketing':Profession_Marketing,
            'Graduated':graduated,
            'Married':married,
            'Gender':gender,
            'Age':age,
            'Work Experience':work_experience,
            'Family Size':family,
            'Cat 1':cat1,
            'Cat 2':cat2,
            'Cat 3':cat3,
            'Cat 4':cat4,
            'Cat 5':cat5,
            'Cat 6':cat6,
            'Cat 7':cat7,
            'Spend Score High': spending_high,
            'Spend Score Average': spending_average,
            'Spend Score Low': spending_low,
           
        }
    
    encoded_result = []
    for i in result.values():
        if type(i) == int:
            encoded_result.append(i)
        elif i in ['Yes','No']:
            res = get_value(i, grad)
            encoded_result.append(res)
        elif i in ['Yes','No']:
            res = get_value(i, marr)
            encoded_result.append(res)
        elif i in ['m','f']:
            res = get_value(i, gen)
            encoded_result.append(res)
        elif i in ['Yes','No']:
            res = get_value(i, Artist)
            encoded_result.append(res)
        elif i in ['Yes','No']:
            res = get_value(i, Engineer)
            encoded_result.append(res)
        elif i in ['Yes','No']:
            res = get_value(i, Lawyer)
            encoded_result.append(res)
        elif i in ['Yes','No']:
            res = get_value(i, Healthcare)
            encoded_result.append(res)
        elif i in ['Yes','No']:
            res = get_value(i, Entertainment)
            encoded_result.append(res)
        elif i in ['Yes','No']:
            res = get_value(i, Doctor)
            encoded_result.append(res)
        elif i in ['Yes','No']:
            res = get_value(i, Marketing)
            encoded_result.append(res)
        elif i in ['Yes','No']:
            res = get_value(i, Homemaker)
            encoded_result.append(res)
        elif i in ['Yes','No']:
            res = get_value(i, Executive)
            encoded_result.append(res)
        elif i in ['Yes','No']:
            res = get_value(i, high)
            encoded_result.append(res)
        elif i in ['Yes','No']:
            res = get_value(i, average)
            encoded_result.append(res)
        elif i in ['Yes','No']:
            res = get_value(i, low)
            encoded_result.append(res)
        elif i in ['Yes','No']:
            res = get_value(i, cat1)
            encoded_result.append(res)
        elif i in ['Yes','No']:
            res = get_value(i, cat2)
            encoded_result.append(res)
        elif i in ['Yes','No']:
            res = get_value(i, cat3)
            encoded_result.append(res)
        elif i in ['Yes','No']:
            res = get_value(i, cat4)
            encoded_result.append(res)
        elif i in ['Yes','No']:
            res = get_value(i, cat5)
            encoded_result.append(res)
        elif i in ['Yes','No']:
            res = get_value(i, cat6)
            encoded_result.append(res)
        elif i in ['Yes','No']:
            res = get_value(i, cat7)
            encoded_result.append(res)
  
    # prediction section
    st.subheader('Prediction Result')
    single_array = np.array(encoded_result).reshape(1, -1)
    #st.write(single_array)

    model = load_model("best_model_svm.pkl")
    prediction = model.predict(single_array)
    

    #st.write(prediction)

    if prediction == 0:
        st.success("Congratulations, the predicted segment is Segment A!")
    elif prediction == 1:
        st.success("Congratulations, the predicted segment is Segment B!")
    elif prediction == 2:
        st.success("Congratulations, the predicted segment is Segment C!")
    elif prediction == 3:
        st.success("Congratulations, the predicted segment is Segment D!")
    else:
        st.warning("The predicted segment is unknown. Please check the input data.")
    
if __name__ == "__main__":
    run_ml_appp()
