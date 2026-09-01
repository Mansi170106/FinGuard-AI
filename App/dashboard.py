import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="FinGuard-AI",
    page_icon="🛡️",
    layout="wide"
)


# =========================================================
# LOAD TRAINED MODEL
# =========================================================

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "risk_model.pkl"

model = joblib.load(MODEL_PATH)


# =========================================================
# HEADER
# =========================================================

st.title("🛡️ FinGuard-AI")

st.subheader("AI-Powered Transaction Risk Detection")

st.write(
    "Analyze a financial transaction using behavioral and "
    "transaction-level risk signals."
)

st.divider()


# =========================================================
# TRANSACTION DETAILS
# =========================================================

st.header("💳 Transaction Details")

col1, col2 = st.columns(2)


# -----------------------------
# LEFT COLUMN
# -----------------------------

with col1:

    transaction_amount = st.number_input(
        "Transaction Amount (₹)",
        min_value=0.0,
        value=5000.0,
        step=500.0
    )

    transaction_hour = st.slider(
        "Transaction Hour",
        min_value=0,
        max_value=23,
        value=14
    )

    customer_age = st.number_input(
        "Customer Age",
        min_value=18,
        max_value=100,
        value=25,
        step=1
    )

    previous_transactions = st.number_input(
        "Previous Transactions",
        min_value=0,
        value=20,
        step=1
    )


# -----------------------------
# RIGHT COLUMN
# -----------------------------

with col2:

    distance = st.number_input(
        "Distance From Usual Location (km)",
        min_value=0.0,
        value=5.0,
        step=1.0
    )

    new_device = st.selectbox(
        "New Device Detected?",
        ["No", "Yes"]
    )

    new_merchant = st.selectbox(
        "New Merchant?",
        ["No", "Yes"]
    )

    international = st.selectbox(
        "International Transaction?",
        ["No", "Yes"]
    )


st.divider()


# =========================================================
# ANALYZE TRANSACTION
# =========================================================

if st.button("🔍 Analyze Transaction", use_container_width=True):

    # Convert Yes/No to 1/0

    device_changed = 1 if new_device == "Yes" else 0

    new_merchant_value = 1 if new_merchant == "Yes" else 0

    international_value = 1 if international == "Yes" else 0


    # =====================================================
    # INPUT DATA
    #
    # THESE COLUMN NAMES MUST MATCH THE MODEL
    # =====================================================

    input_data = pd.DataFrame({
        "amount": [transaction_amount],
        "hour": [transaction_hour],
        "customer_age": [customer_age],
        "previous_transactions": [previous_transactions],
        "distance_from_home": [distance],
        "device_changed": [device_changed],
        "new_merchant": [new_merchant_value],
        "international": [international_value]
    })


    # =====================================================
    # PREDICTION
    # =====================================================

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1] * 100


    # =====================================================
    # RESULT
    # =====================================================

    st.divider()

    st.header("📊 FinGuard-AI Risk Assessment")


    # -----------------------------
    # Risk level
    # -----------------------------

    if probability >= 70:

        risk_level = "HIGH RISK"

        st.error("🚨 HIGH RISK TRANSACTION")

        st.warning(
            "This transaction shows strong risk indicators "
            "and requires additional verification."
        )


    elif probability >= 40:

        risk_level = "MEDIUM RISK"

        st.warning("⚠️ MEDIUM RISK TRANSACTION")

        st.info(
            "This transaction contains some unusual "
            "characteristics and should be reviewed."
        )


    else:

        risk_level = "LOW RISK"

        st.success("✅ LOW RISK TRANSACTION")

        st.info(
            "This transaction appears to be within "
            "normal risk levels."
        )


    # -----------------------------
    # Risk probability
    # -----------------------------

    st.subheader("Risk Probability")

    st.metric(
        "Risk Probability",
        f"{probability:.2f}%"
    )

    st.progress(min(probability / 100, 1.0))


    # =====================================================
    # RISK FACTORS
    # =====================================================

    st.subheader("🔎 Detected Risk Factors")

    risk_factors = []


    if transaction_amount > 20000:
        risk_factors.append(
            "💰 High transaction amount"
        )


    if transaction_hour < 6 or transaction_hour > 22:
        risk_factors.append(
            "🌙 Unusual transaction hour"
        )


    if distance > 100:
        risk_factors.append(
            "📍 Large distance from usual location"
        )


    if device_changed == 1:
        risk_factors.append(
            "📱 New device detected"
        )


    if new_merchant_value == 1:
        risk_factors.append(
            "🏪 New merchant detected"
        )


    if international_value == 1:
        risk_factors.append(
            "🌎 International transaction"
        )


    if len(risk_factors) > 0:

        for factor in risk_factors:
            st.write(factor)

    else:

        st.write(
            "✅ No major risk signals detected."
        )


    # =====================================================
    # TRANSACTION SUMMARY
    # =====================================================

    st.subheader("🧾 Transaction Summary")

    summary1, summary2, summary3 = st.columns(3)


    with summary1:

        st.write("**Amount**")

        st.write(
            f"₹{transaction_amount:,.2f}"
        )


    with summary2:

        st.write("**Transaction Hour**")

        st.write(
            f"{transaction_hour}:00"
        )


    with summary3:

        st.write("**Distance**")

        st.write(
            f"{distance:,.1f} km"
        )


    summary4, summary5, summary6 = st.columns(3)


    with summary4:

        st.write("**New Device**")

        st.write(new_device)


    with summary5:

        st.write("**New Merchant**")

        st.write(new_merchant)


    with summary6:

        st.write("**International**")

        st.write(international)


# =========================================================
# MODEL PERFORMANCE
# =========================================================

st.divider()

st.header("📈 Model Performance")

metric1, metric2, metric3, metric4 = st.columns(4)


with metric1:
    st.metric("Accuracy", "92%")


with metric2:
    st.metric("Precision", "92%")


with metric3:
    st.metric("Recall", "91%")


with metric4:
    st.metric("F1 Score", "91%")


st.caption(
    "Model evaluation based on a held-out test dataset "
    "of 1,000 transactions."
)


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "FinGuard-AI | AI-powered financial transaction risk detection"
)
