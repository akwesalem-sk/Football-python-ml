import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load data
df = pd.read_csv("results.csv")

# Convert team names to numbers
le = LabelEncoder()
df["home_team"] = le.fit_transform(df["home_team"])
df["away_team"] = le.transform(df["away_team"])

# Features and target
X = df[["home_team", "away_team"]]
y = df["result"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Check accuracy
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Predict a specific match
home = le.transform(["Arsenal"])[0]
away = le.transform(["Chelsea"])[0]

prediction = model.predict([[home, away]])
print(f"\nPrediction: {prediction[0]}")
print("H = Home Win, A = Away Win, D = Draw")

