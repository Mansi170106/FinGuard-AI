import pandas as pd
import random

random.seed(42)

transactions = []

for i in range(5000):

    amount = round(random.uniform(100, 50000), 2)
    hour = random.randint(0, 23)

    customer_age = random.randint(18, 70)

    previous_transactions = random.randint(1, 50)

    distance_from_home = round(random.uniform(0, 1000), 2)

    device_changed = random.choice([0, 0, 0, 1])

    new_merchant = random.choice([0, 0, 0, 1])

    international = random.choice([0, 0, 0, 0, 1])

    transactions.append({
        "transaction_id": f"TXN{i+1:05d}",
        "amount": amount,
        "hour": hour,
        "customer_age": customer_age,
        "previous_transactions": previous_transactions,
        "distance_from_home": distance_from_home,
        "device_changed": device_changed,
        "new_merchant": new_merchant,
        "international": international
    })


df = pd.DataFrame(transactions)


# Create realistic synthetic risk patterns
risk_score = (
    (df["amount"] > 30000).astype(int) * 2
    + (df["hour"] < 5).astype(int) * 2
    + (df["distance_from_home"] > 500).astype(int) * 2
    + df["device_changed"]
    + df["new_merchant"]
    + df["international"]
)


# Add some randomness so the model doesn't get a perfect score
noise = [random.choice([0, 0, 0, 1, -1]) for _ in range(len(df))]

risk_score = risk_score + noise


df["is_risky"] = (risk_score >= 4).astype(int)


df.to_csv("Data/transactions.csv", index=False)

print("FinGuard-AI transaction dataset created successfully!")
print(f"Total transactions: {len(df)}")
print(f"Risky transactions: {df['is_risky'].sum()}")
print(f"Normal transactions: {(df['is_risky'] == 0).sum()}")