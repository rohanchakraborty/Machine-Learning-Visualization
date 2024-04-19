import pytest
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV
from plotGridSearch import plotGridSearch
from tableGridSearch import tableGridSearch
from sklearn.ensemble import RandomForestClassifier  # Add this import

@pytest.fixture
def iris_data():
    # Load the iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target
    return X, y

def test_plotGridSearch(iris_data):
    X, y = iris_data
    # Define the parameter grid for RandomForestClassifier
    param_grid = {
        'n_estimators': [50, 100],
        'max_depth': [None, 10],
        'min_samples_split': [2, 5]
    }
    # Create a RandomForestClassifier
    rf_clf = RandomForestClassifier()
    # Perform grid search
    grid_search = GridSearchCV(rf_clf, param_grid, cv=2)
    grid_search.fit(X, y)
    # Call plotGridSearch and ensure it runs without errors
    plotGridSearch(grid_search)
    assert True
    
def test_tableGridSearch(iris_data):
    X, y = iris_data
    # Define the parameter grid for RandomForestClassifier
    param_grid = {
        'n_estimators': [50, 100],
        'max_depth': [None, 10],
        'min_samples_split': [2, 5]
    }
    # Create a RandomForestClassifier
    rf_clf = RandomForestClassifier()
    # Perform grid search
    grid_search = GridSearchCV(rf_clf, param_grid, cv=2)
    grid_search.fit(X, y)
    # Call tableGridSearch and ensure it runs without errors
    tableGridSearch(grid_search, all_columns=True, all_ranks=True, save=False)
