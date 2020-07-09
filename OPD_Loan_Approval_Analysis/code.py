# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)
bank = pd.DataFrame(bank_data)
#Step 1
print("Step 1............................................................")

categorical_var = bank.select_dtypes(include = 'object')

print("categorical_var :",categorical_var.shape) 
numerical_var=bank.select_dtypes(include = 'number')
print("numerical_var :",numerical_var.shape) 
#Step 2
print("Step 2............................................................")

banks=bank.drop(['Loan_ID'],axis=1)

print("banks : ",banks.isnull().sum())

bank_mode=banks.mode()
print(bank_mode)

banks = banks.fillna(bank_mode)  #,inplace=True)

# df['Gender'].fillna(df['Gender'].mode()[0],inplace=True)
#banks.isnull()

print("banks.shape  : ",banks.shape)
print("banks.isnull().sum().values.sum() : ",banks.isnull().sum())

#Step3
print("Step 3..............................................................")
avg_loan_amount = pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount',aggfunc=np.mean)

print("avg_loan_amount ",avg_loan_amount)

#Step 4
print("Step 4...............................................................")

loan_approved_se = banks['Loan_Status'].value_counts()['Y']

print("loan_approved_se  :",loan_approved_se)

loan_approved_nse = banks['Loan_Status'].value_counts()['N']
print("loan_approved_nse  :",loan_approved_nse)


percentage_se = (55.9968 * 100 / 614)

print("percentage_se :",percentage_se)

percentage_nse = (366.0064 * 100 / 614)

print("percentage_nse :",percentage_nse)

#Step 5

print("Step 5..............................................................")


big_loan_term = 554

print(big_loan_term)

# = banks.groupby('ApplicantIncome')['Credit_History'].agg(np.mean)


loan_groupby = banks.groupby({'Loan_Status':['ApplicantIncome','Credit_History']})


mean_values=banks.groupby(['Loan_Status']).mean()

print("mean_value",mean_values)

#Code starts here



