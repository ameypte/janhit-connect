import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load numerical data into a DataFrame
data = pd.read_csv('data.csv')

# Select only specific columns as features
selected_features = ['People in Ward', 'Festive Season', 'Construction']  # List of column names you want to include
X = data[selected_features]

# Select the target variable
y = data['Electricity Usage']

# Initialize and train Random Forest model using 100% of the data
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
rf_regressor.fit(X, y)

# Take input from the user
ward_no = int(input("Enter Ward No: "))
people_in_ward = int(input("Enter People in Ward: "))
season = input("Enter Season (Spring/Summer/Fall): ")
construction = input("Enter Construction (True/False): ")

# Make predictions using user input
input_data = pd.DataFrame({
    'People in Ward': [people_in_ward],
    'Season': [season],
    'Construction': [construction]
})

# Encode categorical variables
input_data['Season'] = input_data['Season'].map({'Spring': 0, 'Summer': 1, 'Fall': 2})
input_data['Construction'] = input_data['Construction'].map({'True': 1, 'False': 0})

# Predict water utilization
predicted_utilization = rf_regressor.predict(input_data)[0]

print("Predicted Water Utilization:", predicted_utilization)
