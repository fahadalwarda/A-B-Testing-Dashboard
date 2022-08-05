from multiprocessing import shared_memory
import numpy as np
import streamlit as st

import scipy.stats as stats
import matplotlib.pyplot as plt
import statistics

x = np.linspace(- 3,  3, 100)
y = stats.norm.pdf(x, 0,1)



def pvalue(z):
    pvalue= stats.norm.sf(abs(z))
    return pvalue

def prob(z):
    shade=stats.norm.ppf(1-z/2)
    return shade

st.title('A/B Testing')
alpha = st.sidebar.radio('Significance level % (Alpha)', options = [0.01,0.05,0.1])
zscore = st.sidebar.slider('Zscore', min_value=-3.0, max_value=3.0, value=0.0, step=0.01)
st.sidebar.subheader('P-value')
pvalue=st.sidebar.write( np.round_(pvalue(zscore),3))

fig = plt.figure(figsize=(14,6))
ax1 = fig.add_subplot()
ax1.plot(x, stats.norm.pdf(x,0,1))
ax1.set_xticks((-2.58,-1.96,-1.64,0,1.64,1.96,2.58))
ax1.plot([0,0],[0,0.4], color='black', linestyle='dashed')
ax1.plot([1.96,1.96],[0,0.055], color='grey', linestyle='dashed')
ax1.plot([-1.96,-1.96],[0,0.055], color='grey', linestyle='dashed')
ax1.plot([1.64,1.64],[0,0.1], color='grey', linestyle='dashed')
ax1.plot([-1.64,-1.64],[0,0.1], color='grey', linestyle='dashed')
ax1.plot([2.58,2.58],[0,0.01], color='grey', linestyle='dashed')
ax1.plot([-2.58,-2.58],[0,0.01], color='grey', linestyle='dashed')
ax1.fill_between(np.linspace(prob(alpha),  3, 100), stats.norm.pdf(np.linspace(prob(alpha),  3, 100), 0,1 ))
ax1.fill_between(np.linspace(-3,  -1*prob(alpha), 100), stats.norm.pdf(np.linspace(-3,  -1*prob(alpha), 100), 0,1 ))
ax1.scatter(zscore,0, marker="D", color='red')
ax1.spines['bottom'].set_position(('outward', -15))
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.set_title('Standard Normal Distribution')
ax1.set_xlabel('Z score')

ax2 = ax1.twiny()
ax2.set_xticks([0.242,0.445,0.555,1.1, 1.65,1.755,1.965, 2.2])
ax2.set_xticklabels((0.005,0.025,0.05,0.5,0.05,0.025,0.005,0.0001))
ax2.xaxis.set_ticks_position('bottom') 
ax2.xaxis.set_label_position('bottom') 
ax2.spines['bottom'].set_position(('outward', 20))
ax2.set_xlabel('Significance level (Alpha)')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.get_yaxis().set_visible(False)

ax3 = ax1.twiny()
ax3.set_xticks([0.242,0.445,0.555,1.1, 1.65,1.755,1.965, 2.2])
ax3.set_xticklabels((99,95,90,0,90,95,99,99.9999))
ax3.xaxis.set_ticks_position('bottom') 
ax3.xaxis.set_label_position('bottom') 
ax3.spines['bottom'].set_position(('outward', 60))
ax3.set_xlabel('Confidence level %')
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.spines['left'].set_visible(False)
ax3.get_yaxis().set_visible(False)

st.pyplot(fig)
