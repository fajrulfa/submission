import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


day_df = pd.read_csv('all_data.csv')

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
def plot_monthly_usage(data):
    monthly_usage_df = data.resample(rule='M', on='dteday').agg({
        "cnt": "mean"
    })
    monthly_usage_df.index = monthly_usage_df.index.strftime('%B %Y')

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(monthly_usage_df.index, monthly_usage_df["cnt"], marker='o', linewidth=2, color="blue")
    ax.set_title("Average Bicycle Use per Month (2011-2012)", loc="center", fontsize=20)
    ax.set_xticklabels(monthly_usage_df.index, rotation=75, fontsize=8)
    ax.set_yticklabels(ax.get_yticks(), fontsize=10)
    ax.set_xlabel("Month", fontsize=12)
    ax.set_ylabel("Average Bicycle Use", fontsize=12)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig)

def plot_weekly_usage(data):
    weekly_df = data.groupby(data['dteday'].dt.strftime('%A'))['cnt'].mean().reindex(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(weekly_df.index, weekly_df.values, marker='o', color='blue')
    ax.set_title("Average Bicycle Use per Day in a Week (2011-2012)", loc="center", fontsize=15)
    ax.set_xticklabels(weekly_df.index, rotation=45)
    ax.set_xlabel("Days of the Week", fontsize=12)
    ax.set_ylabel("Average Bicycle Use", fontsize=12)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig)

# Call the function in your Streamlit app
st.header('Bicycle Use Dashboard :sparkles:')
st.subheader('A.Graph bicycle use per month')
plot_monthly_usage(day_df)
st.subheader('A.Graph bicycle use per day in a week')
plot_weekly_usage(day_df)
