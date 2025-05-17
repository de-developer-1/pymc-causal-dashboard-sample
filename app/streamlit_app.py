
import streamlit as st
import pandas as pd
import pymc as pm
import arviz as az
import matplotlib.pyplot as plt

st.title("ベイズ推定によるキャンペーン効果可視化")

uploaded_file = st.file_uploader("CSVデータをアップロード（group, converted列）", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
else:
    data = pd.read_csv("data/campaign_data.csv")

with st.expander("データサンプル"):
    st.dataframe(data.head())

control = data[data['group'] == 'control']['converted'].values
treatment = data[data['group'] == 'treatment']['converted'].values

with pm.Model() as model:
    alpha = beta = 1
    p_c = pm.Beta('p_control', alpha, beta)
    p_t = pm.Beta('p_treatment', alpha, beta)
    obs_c = pm.Bernoulli('obs_control', p=p_c, observed=control)
    obs_t = pm.Bernoulli('obs_treatment', p=p_t, observed=treatment)
    diff = pm.Deterministic('difference', p_t - p_c)
    trace = pm.sample(2000, return_inferencedata=True, progressbar=False)

st.subheader("推定されたコンバージョン率の分布")
fig, ax = plt.subplots()
az.plot_posterior(trace, var_names=['p_control', 'p_treatment'], ax=ax)
st.pyplot(fig)

st.subheader("uplift (介入 - 対照) の分布")
fig2, ax2 = plt.subplots()
az.plot_posterior(trace, var_names=['difference'], ref_val=0, ax=ax2)
st.pyplot(fig2)

st.markdown("---")
summary_df = az.summary(trace, var_names=["p_control", "p_treatment", "difference"])
st.dataframe(summary_df)
