import pandas as pd

# Load the dataset
df = pd.read_csv('IBM_HR_Attrition.csv')

# Analyze the dataset structure and features
print(df.head())
print(df.info())

# Preprocessing steps
# Handle missing values
df.dropna(inplace=True)

# Encode categorical variables
df = pd.get_dummies(df, columns=['BusinessTravel', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus', 'Over18', 'OverTime'], drop_first=True)

# Scale numerical features (if necessary)
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# df[['Age', 'MonthlyIncome']] = scaler.fit_transform(df[['Age', 'MonthlyIncome']])

# Separate features and target variable
X = df.drop('Attrition', axis=1)
y = df['Attrition']
