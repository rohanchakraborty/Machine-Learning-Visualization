# Import necessary modules
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
#from my_cv_library.plotgridsearch import plotGridSearch
#from my_cv_library.tablegridsearch import tableGridSearch

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
grid_search = GridSearchCV(rf_clf, param_grid, cv=5)
grid_search.fit(X, y)

# Visualize cross-validation results using Plotly
plotGridSearch(grid_search)

# Display cross-validation results in a tabular format
tableGridSearch(grid_search, all_columns=True, all_ranks=True, save=False)
