import streamlit as st
import numpy as np
import pickle
import joblib

feature_name = ['CreditScore','Geography','Gender','Age','Tenure',
                'Balance','NumOfProducts','HasCrCard','IsActiveMember','EstimatedSalary']



path = "Deployment\model_1.pkl"

def load_model(path):
    with open(path, "rb") as mod:
        model = pickle.load(mod)
    return model


with open('Deployment\cat_dict.json', "rb") as fp:
    cat_dict = pickle.load(fp)


def get_value(feature_name, value, my_dict = cat_dict):
    feature_dict = my_dict[feature_name]
    Encodedvalue = feature_dict[value]
    return Encodedvalue


def get_feature_dic(feature_name, dic = cat_dict):
    return dic[feature_name]

def main():
    # Bank Churn Prediction App
    st.title("Bank Churn Prediction")
    activities = ["Introduction", "Predictions", "About"]
    choice = st.sidebar.selectbox("Select Activity", activities)
    
    st.sidebar.markdown(
            """ Developed by Team Vispy    
                Email me @ : kareemsikiru@gmail.com
                """)

    if choice == "Introduction":
        html_temp_home1 = """<div style="background-color:#00CCFF;padding:10px">
                                            <h4 style="color:white;text-align:center;">
                                            Predicting Bank Churn Rate Using Machine Learning Model
                                            </h4>
                                            </div>
                                            </br>"""
        st.markdown(html_temp_home1, unsafe_allow_html=True)
    
        st.write("""
            Studies shows that accquiring new coustomers can cost five times retaining existing customers. Customer churn refers to 
            the phenomenon when a customer leaves a company or an organization,in our case a bank. Thus tracking of bank 
            customer churn rate through prediction will help in reducing marketing costs, lead to increase in capital ,expanding total customers and a lot more.
             """)
        st.write("""
                 
                 
                 """)
        
        
    elif choice == "Predictions":
        st.subheader("Bank Churn Prediction")
        
        creditscore_code = st.number_input("Enter Credit Score")
        
        geography_class = st.selectbox("Select Geography", tuple(get_feature_dic("Geography").keys()))
        geography_code = get_value(feature_name="Geography",value=geography_class)
        
        gender_class = st.radio("Select Gender", tuple(get_feature_dic("Gender").keys()))
        gender_code = get_value(feature_name = "Gender", value = gender_class)
        
        age_code = st.number_input("Enter Age")
        
        tenure_code = st.number_input("Specify Tenure ")
        
        balance_code = st.number_input("Enter Balance")
        
        num_of_product_code = st.number_input("How many products purchased ?")
        
        
        hascrcard_class = st.radio("Does the customer has credit card ?", tuple(get_feature_dic("HasCrCard").keys()))
        hascrcard_code = get_value(feature_name = "HasCrCard", value = hascrcard_class)
        
        
        isactive_class = st.radio("Is the customer an active member ?", tuple(get_feature_dic("HasCrCard").keys()))
        isactive_code = get_value(feature_name = "IsActiveMember", value = isactive_class)
        
        estimatedsalary_code = st.number_input("Enter estimated salary ?")
        


        
        feature_values = [creditscore_code, geography_code, age_code, gender_code,
        tenure_code, balance_code, num_of_product_code, hascrcard_code, isactive_code, estimatedsalary_code]
        
        

        Result = ['CreditScore','Geography','Gender','Age','Tenure',
                'Balance','NumOfProducts','HasCrCard','IsActiveMember','EstimatedSalary']
        
        single_sample = np.array(feature_values).reshape(1,-1)
        single_sample = [feature_values]
        
        if st.button("Predict"):
            preds = load_model(path).predict(single_sample)
                
            if preds == 0:
                st.write("No, There is a very low probability that the customer will churn")
                        
            elif preds == 1:
                st.write("Yes, There is high probability that the customer will churn")
                    
            else:
                st.write("Invalid")
                
                
    elif choice == "About":
        st.subheader("About this app")
        html_temp_about1= """<div style="background-color:#4073FF;padding:10px">
                                    <h4 style="color:white;text-align:center;">
                                    Definition : </h4>
                                    </div>
                                    </br>"""
        st.markdown(html_temp_about1, unsafe_allow_html=True)

        html_temp4 = """
                                        <div style="background-color:#4073FF;padding:10px">
                                        <h4 style="color:white;text-align:center;">This application is developed by team vispy for the purpose of predicting the rate of churn by the customers.</h4>
                                        <h4 style="color:white;text-align:center;">Thanks for Visiting</h4>
                                        </div>
                                        <br></br>
                                        <br></br>"""

        st.markdown(html_temp4, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
