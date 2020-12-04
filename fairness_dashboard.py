import time

import numpy as np
import pandas as pd
from sklearn.datasets import fetch_openml

RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

import streamlit as st

from sections.intro import intro_component

st.title("Study of Equalized Odds using Fairlearn")

st.markdown("""
This is a dashboard I created while reading [Equality of Opportunity in Supervised Learning](https://arxiv.org/abs/1610.02413).

I am not sure there is a way to access the code the authors used to produce their plots/results, however, after some googling I found the [Fairlearn](https://fairlearn.github.io/v0.5.0/index.html#) package, which seemingly aims to _empowers developers of artificial intelligence (AI) systems to assess their system's fairness and mitigate any observed unfairness issues_. Reading their documentation they seem to implement, among others, the methodology described by the paper above.

I thought it would be good to play around with this tool to assimilate the theoretical concepts introduced by the paper, so what you find below is a minimal overview of the practical use of this methodology, compared to another standard definition of fairness called _Demographic Parity_ (also implemented in Fairlearn)
""")

intro = st.beta_expander("Intro")
intro_component(intro)

