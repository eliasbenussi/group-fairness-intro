# Group fairness with Fairlearn

This repository explores concepts of group fairness in ML I encountered while reading the paper [Equality of Opportunity in Supervised Learning](https://arxiv.org/abs/1610.02413). Since I aimed for this to be a nice and easy interactive intro, the code is stored in a Jupyter notebook (called `fairlearn_overview.ipynb`).


I am not sure there is a way to access the code the authors used to produce their plots and results, however, after some googling I found the [Fairlearn](https://fairlearn.github.io/v0.5.0/index.html#) package, which seemingly aims to _empowers developers of artificial intelligence (AI) systems to assess their system's fairness and mitigate any observed unfairness issues_. Reading their documentation they seem to implement, among others, the methodology described by the paper above.

I thought it would be good to play around with this tool to assimilate the theoretical concepts introduced by the paper, so what you find in the notebook is a minimal overview of the practical use of this methodology, compared to another standard definition of fairness called _Demographic Parity_ (also implemented in Fairlearn)

### Getting Started

Since the code is in Jupyter notebooks, you will need to be able to access it. If you don't know what a Jupyter notebook is, I encourage you to use vanilla Jupyter. Go to https://jupyter.org/ to find out how to install it and to learn more about it.

With that out of the way, you will need to install the code dependencies. I include a `requirements.txt` that you can install executing `pip install -r requirements.txt` or `conda install --yes --file requirements.txt` depending on what package manager you prefer.

### Methodologies comparison

In the `methodologies_comparison.ipynb` notebook you can find a comparison of two possible methodologies to achieve equalized odds as described in the intro notebook. The comparison is done using 3 datasets, which can be downloaded from [OpenML](https://www.openml.org/)
