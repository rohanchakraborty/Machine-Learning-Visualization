[![Continuous Integration](https://github.com/rohanchakraborty/Machine-Learning-Visualization/actions/workflows/main.yml/badge.svg)](https://github.com/rohanchakraborty/Machine-Learning-Visualization/actions/workflows/main.yml)

# cvplot

cvplot is a Python library for visualizing cross-validation results.

## Installation

You can install cvplot using pip:

```bash
pip install cvplot
```

## Usage

To use cvplot, simply import the functions from the library:

```python
from cvplot.plotgridsearch import plotGridSearch
from cvplot.tablegridsearch import tableGridSearch
```
Then, you can call these functions with the appropriate arguments to visualize your cross-validation results.

# Example Usage

Here's an example of how you can use cvplot to visualize cross-validation results for a machine learning model:

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from cvplot.plotgridsearch import plotGridSearch
from cvplot.tablegridsearch import tableGridSearch

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Define the parameter grid for RandomForestClassifier
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}

# Create a RandomForestClassifier
rf_clf = RandomForestClassifier()

# Perform grid search
grid_search = GridSearchCV(rf_clf, param_grid, cv=3)
grid_search.fit(X, y)

# Visualize the grid search results
plotGridSearch(grid_search)

# Display the grid search results in a table
tableGridSearch(grid_search)

```

## Author

This project was created by Rohan Chakraborty