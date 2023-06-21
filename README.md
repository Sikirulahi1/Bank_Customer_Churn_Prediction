# Team-Vispy-Premier-Project

# Bank_Customer_Churn_Prediction

## Definition
Customer churn refers to the phenomenon where customers discontinue their relationship with a company or service provider. In the context of the banking industry, customer churn occurs when customers close their accounts or switch to a different bank.

## Objective
The goal of this project is to predict customer churn in the banking industry.
In this project, we aim to build machine learning models that can accurately predict customer churn based on various customer attributes.

## Team Members
- Abdulkareem Sikirulahi Opeyemi - (Group Lead)
- Eke Mong Eke - (Assistant Group Lead)
- Carolyne Jebiwott Samoei - (Query Analyst)
- Kayode Blessing Adebayo 	
- Oyelola Emmanuel Akinsola 	
- Ejiroghene Vivian Okpirikhre	
- Newton Kimathi		
- Ibrahim Abdulsalam Abdullahi 	
- Chukwuebuka Ohaji		
- Akinbode Afolabi	
- Chukwuebuka Ohaji	
- Newton Kimathi	
- Ganiyu Zainab Ayomide 	
- Olamileye Clement Duduyemi	


## Flow of Project:
Data Sourcing --> Data Preprocessing --> Model Training --> Model Evaluation --> Deployment

## Source of Data:
https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset

## Feature Description
- CustomerId: Unique ID which is assigned to each customer
- Surname: Last name of the customer
- CreditScore: It defines the credit history of the customer.
- Geography: A customer’s location
- Gender: It defines the Gender of the customer
- Age: Age of the customer
- Tenure: Number of years for which the customer has been with the bank
- NumOfProducts: It refers to the number of products that a customer has purchased through the bank.
- Balance: Account balance
- HasCrCard: It is a categorical variable that decides whether the customer has a credit card or not.
- EstimatedSalary: Estimated salary
- isActiveMember: It is a categorical variable that decides whether the customer is an active member of the bank or not ( Active member in the sense, using bank products regularly, making transactions, etc )
- Exited: It is a categorical variable that decides whether the customer left the bank within six months or not. It can take two values 0=No ( Customer did not leave the bank ) 1=Yes ( Customer left the bank )

## Data Preprocessing:
- RowNumber, CustomerId and Surname were dropped because they were unique for every customer and don't add value to our target variable.
- 
- Using SMOTE (Synthetic Minority Over-sampling Technique) to address class imbalance in target variable.

## Modelling
We built different algorithms, such as

- Logistic Regression,
- KNeighbors
- Decision Tree
- Random Forest,
- XGBoost and
- Support Vector Machines,
- And compared their metrics.

## Model selected for the project:
XGBoost

## Model Deployment:
Streamlit was used to deploy the model

## Dashboard link (tableau)
https://public.tableau.com/app/profile/emmanuel.oyelola/viz/HamoyeCapstoneProjectBankCustomerChurnDashboard2/Dashboard22

## Colab link (Preprocessing and Modelling)
https://colab.research.google.com/drive/1XOcz9J_l4P11J3pv3zedMSNty7zMusvs?usp=sharing#scrollTo=77e10b35

## Link to the slides
https://docs.google.com/presentation/d/1RHnJjVI3iAGAuNhn4FreS-Ihi64oA1yBdSt6daC59ds/edit#slide=id.p20

## Folders present in the project:

- Data - Contains the dataset
- Deployment - the python motebooks for the app deploymnet
- EDA - Contains the analysis of the dataset
- Model_Training - Contains the python notebooks feature Engineering and Modelling




 


