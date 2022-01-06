<div align="center">
  <img src="https://avatars.githubusercontent.com/u/93623406?s=400&u=5ef153fb995fc34a84bc4a66fbc504a4b2d66c10&v=4"><br>
</div>

# Kern-Rowduction: undersampling by graph kernelization

[![PyPI Latest Release](https://img.shields.io/pypi/v/kern-rowduction.svg)](https://pypi.org/project/kern-rowduction/)
[![Package Status](https://img.shields.io/pypi/status/kern-rowduction.svg)](https://pypi.org/project/kern-rowduction/)
[![Build Status](https://app.travis-ci.com/Kern-Rowduction/Kern-Rowduction.svg?branch=main)](https://app.travis-ci.com/Kern-Rowduction/Kern-Rowduction)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/kern-rowduction/kern-rowduction/blob/main/LICENSE)


## What is it ?

**Kern-Rowduction** is a ready-to-use package to increase the quality of your data by deleting near-duplicates in your data set. This is possible by converting your data set into an oriented graph and extract its quasi-kernel which will represent your reduced data. Using the reduced data instead of your original data will improve the computational & statistical performance of your machine learning algorithm.

## Why use it ?

The Kern-Rowduction package has namely the following goals :
  - Increase the quality of a data set
  - Reduce datasets and computational time / cost
  - Undersample imbalanced datasets and over represented cohort
  - Improve statistics and predictive models' performances
  
Below some use cases of the Kern-Rowduction package :

  - Rebalance the population of 0 and 1 in a binary classification on a imbalanced population with a too large number of 0 by example
  - Undersample over-represented classes for multi classification
  - Reduce the influence of given ranges of values in the case of a regression
  - Reduce the size of datasets without losing its 'significant' values in order to improve computational time / cost
  - Improve feature engineering and machine learning models in general 

## Installation

The source code is currently hosted on GitHub at:
https://github.com/kern-rowduction/kern-rowduction

Binary installers for the latest released version are available at the [Python Package Index (PyPI)](https://pypi.org/project/kern-rowduction) :

```sh
pip install kern_rowduction
```

## Dependencies

- [Numpy](https://www.numpy.org)
- [Pandas](https://pandas.pydata.org/docs/)
- [Networkx](https://networkx.org/documentation/stable/index.html)
- [tqdm](https://tqdm.github.io/)

## Documentation

The official documentation is hosted on Github: https://kern-rowduction.github.io/Kern-Rowduction/

## Sample Usage

Below an example of usage where a given simple DataFrame is 'rowductioned':

```python
import kern_rowduction as krd
import pandas as pd

df = pd.DataFrame(
  {
  'A': [20 ,21, 6, 5, 6, 91],
  'B': [11, 12, 1, 14, 113, 1],
  'C': [51, 50, 2, 21, 40, 95],
  'D': [63, 65, 54, 12, 70, 98],
  'Label': [0, 0, 1, 1, 1, 0]
  },
  index = ['0', '1', '2','3','4','5'])

rowductioned_df = krd.rowduct(df,rowduction_target=[0,1],\
  epsilon=0.5,label_col='Label',rowduction_method='separately',remove_isolated_points=False)
```

## Getting Help

If you have usage questions or you found bugs, the best place to go to is here, by creating an issue. 
For other reasons, you can send an email to kern.rowduction@gmail.com.

## Contributing to Kern-Rowduction

All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome.
Most development discussions take place on GitHub in this repo or by email between the contributors.

In order to :
  - test the code : execute ```make test``` in the root folder.
  - lint the code : execute ```make lint``` in the root folder.
  - update the Sphinx documentation : execute ```make html``` in the docs folder.

Feel free to ask questions or to make suggestions, you're welcome !

## License

Copyright (c) 2021, Kern-Rowduction. Work released under [MIT](LICENSE) License.

Initial authors : 
  - Hichem Boughattas : hichem.boughattas@protonmail.com  
  - Hamza Bouanani : h.bouanani97@gmail.com