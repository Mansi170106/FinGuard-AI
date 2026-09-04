# 🛡️ FinGuard-AI

## AI-Powered Financial Transaction Risk Detection

FinGuard-AI is a machine-learning-based financial transaction risk detection system designed to identify potentially suspicious transactions using transaction and behavioral indicators.

The system uses a Random Forest classification model and an interactive Streamlit dashboard to analyze transactions and estimate their risk probability.

---

## 🚨 Problem Statement

Financial fraud and suspicious transactions can cause significant financial losses and reduce customer trust.

FinGuard-AI explores how machine learning can help identify potentially risky transactions by analyzing transaction and behavioral signals.

---

## 💡 Solution

FinGuard-AI uses the following transaction and behavioral features for risk detection:

- Transaction amount
- Transaction hour
- Customer age
- Distance from usual location
- Device change detection

These features are processed by a Random Forest classifier to estimate the probability that a transaction is risky.

---

## ✨ Key Features

- 🤖 Machine-learning-based risk detection
- 📊 Risk probability estimation
- 🚨 LOW / MEDIUM / HIGH risk classification
- 🔎 Risk-factor identification
- 🖥️ Interactive Streamlit dashboard
- 📈 Model performance metrics
- 💳 Real-time transaction analysis

---

## 🏗️ System Architecture

```text
User Transaction
       │
       ▼
Streamlit Dashboard
       │
       ▼
Transaction Features
       │
       ▼
Random Forest Model
       │
       ▼
Risk Probability
       │
       ▼
Risk Classification
       │
       ▼
Risk Factors + Alert
