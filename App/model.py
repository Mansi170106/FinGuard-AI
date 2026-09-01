import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Load dataset
df = pd.read_csv("Data/transactions.csv")

# Features used for risk detection
features = [
    "amount",
    "hour",
    "customer_age",
    "previous_transactions",
    "distance_from_home",
    "device_changed",
    "new_merchant",
    "international"
]

X = df[features]
y = df["is_risky"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Create model
model = RandomForestClassifier(
    n_estimators=150,
    max_depth=10,
    random_state=42,
    class_weight="balanced"
)

# Train
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)

print("FinGuard-AI Risk Detection Model")
print("---------------------------------")

print(classification_report(y_test, predictions))

print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))


def predict_risk(
    amount,
    hour,
    customer_age,
    previous_transactions,
    distance_from_home,
    device_changed,
    new_merchant,
    international
):
    """Predict transaction risk."""

    transaction = pd.DataFrame([{
        "amount": amount,
        "hour": hour,
        "customer_age": customer_age,
        "previous_transactions": previous_transactions,
        "distance_from_home": distance_from_home,
        "device_changed": device_changed,
        "new_merchant": new_merchant,
        "international": international
    }])

    prediction = model.predict(transaction)[0]

    probability = model.predict_proba(transaction)[0][1]

    if prediction == 1:
        risk_label = "HIGH RISK"
    else:
        risk_label = "LOW RISK"

    return risk_label, probability
import joblib

joblib.dump(model, "App/risk_model.pkl")

print("Model saved successfully!")