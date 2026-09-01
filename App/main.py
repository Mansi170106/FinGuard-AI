from model import predict_risk


print("=" * 55)
print("              FINGUARD-AI")
print("        AI TRANSACTION RISK ENGINE")
print("=" * 55)

print("\nEnter transaction details:\n")

amount = float(input("Transaction amount (₹): "))
hour = int(input("Transaction hour (0-23): "))
customer_age = int(input("Customer age: "))
previous_transactions = int(input("Previous transactions: "))
distance_from_home = float(
    input("Distance from usual location (km): ")
)

device_changed = int(
    input("New device detected? (1 = Yes, 0 = No): ")
)

new_merchant = int(
    input("New merchant? (1 = Yes, 0 = No): ")
)

international = int(
    input("International transaction? (1 = Yes, 0 = No): ")
)


risk_label, probability = predict_risk(
    amount,
    hour,
    customer_age,
    previous_transactions,
    distance_from_home,
    device_changed,
    new_merchant,
    international
)


# -----------------------------------------
# Generate explanations
# -----------------------------------------

risk_factors = []

if amount > 30000:
    risk_factors.append("High transaction amount")

if hour < 5:
    risk_factors.append("Unusual transaction time")

if distance_from_home > 500:
    risk_factors.append("Large distance from usual location")

if device_changed == 1:
    risk_factors.append("New device detected")

if new_merchant == 1:
    risk_factors.append("New merchant")

if international == 1:
    risk_factors.append("International transaction")


# -----------------------------------------
# Display result
# -----------------------------------------

print("\n" + "=" * 55)
print("                 RISK ANALYSIS")
print("=" * 55)

print(f"\nRisk Level: {risk_label}")
print(f"Risk Probability: {probability * 100:.2f}%")


if risk_factors:

    print("\nRisk Factors Detected:")

    for factor in risk_factors:
        print(f"  ⚠ {factor}")

else:

    print("\nRisk Factors Detected:")
    print("  ✓ No major risk signals detected")


# -----------------------------------------
# Recommendation
# -----------------------------------------

print("\nRecommended Action:")

if risk_label == "HIGH RISK":

    print("  🔴 Request additional verification")

elif probability >= 0.30:

    print("  🟡 Monitor transaction")

else:

    print("  🟢 Allow transaction")


print("\n" + "=" * 55)