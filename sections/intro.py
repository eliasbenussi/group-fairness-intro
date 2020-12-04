import numpy as np
import pandas as pd
from sklearn.datasets import fetch_openml

RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

import streamlit as st

def intro_component(component):
    component.markdown(
        """
        ### Fairness metrics

        When working on fairness, before we can start _fairifying_ models we need to establish
        fairness metrics to optimise. Here we consider two definitions _Demographic Parity_ and
        _Equalized Odds_.

        **Demographic Parity**: is defined as:

        $$Pr(\hat{Y}=1 | A=1) = Pr(\hat{Y}=1 | A=0)$$

        **Equalized Odds**: is defined as:

        $$Pr(\hat{Y}=1 | A=1, Y=y) = Pr(\hat{Y}=1 | A=0, Y=y)$$

        Since in both cases we won't get perfect equality a good way to assess fairness is to look at the difference between the terms, and this is exactly what is done in `fairnlearn`:

        For _Demographic Parity_ we have:
        ```
        demographic_parity_difference = |Pr(Y_pred=1 | A=1) - Pr(Y_pred=1 | A=0)|
        ```

        For _Equalized Odds_ we have:

        $$
        equalized\_odds\_difference = max(
            |Pr(\hat{Y}=1 | A=1, Y=0) - Pr(\hat{Y}=1 | A=0, Y=0)|,
            |Pr(\hat{Y}=1 | A=1, Y=1) - Pr(\hat{Y}=1 | A=0, Y=1)|
        )
        $$
        """
    )

    component.markdown(
        """
        Let's see how this works in practice. We use the Adult dataset ADD LINK to evaluate the
        unfairness of a vanilla decision tree classifier, and we then see how we can mitigate the
        model's according to the two metrics using `fairlearn`.
        """
    )
