# Simplified `plotGridSearch` Algorithm Explanation

The `plotGridSearch` algorithm visualizes cross-validation results using Plotly. It creates scatter plots to showcase how different parameters influence the mean test score. Below, we provide a breakdown of the steps involved, along with a complexity analysis.

## Steps Undertaken

1. **Data Preparation**:
   - Create a DataFrame from cross-validation results (`clf.cv_results_`).
   - Sort the DataFrame based on rank and mean fit time.

2. **Layout Configuration**:
   - Calculate the required number of rows and columns for the subplot layout.

3. **Figure Creation**:
   - Create a subplot figure using `make_subplots` from Plotly.

4. **Iteration Over Parameters**:
   - Iterate over each parameter in `parameters`.

     a. **Scatter Plot for Mean Test Score**:
        - Add a scatter plot trace for mean test score using `mean_test_score` data.
        - Configure marker properties such as size and color.

     b. **Scatter Plot for Best Estimators**:
        - Add a scatter plot trace for the best estimator using `rank_1` data.
        - Configure marker properties.

     c. **Axis Titles**:
        - Update x-axis and y-axis titles based on the current parameter.

     d. **Linearity Check**:
        - Check if the parameter values show linear behavior using Pearson's correlation coefficient (r).
        - If linearity is below a threshold (r < 0.86), update the x-axis to be logarithmic.

     e. **Subplot Layout Management**:
        - Increment the row and column indexes for subplot layout.

5. **Figure Layout Configuration**:
   - Configure the overall layout of the figure, including legend order, size, title, and hover mode.

6. **Display Plot**:
   - Display the finalized figure using `fig.show()`.

## Complexity Analysis

**Time Complexity**:

- DataFrame operations (sorting, indexing): O(n log n)
- Loop over parameters: O(len(parameters))
- Plotly figure creation and updates: O(len(parameters))
- Linearity check: O(len(parameters))
- `fig.show()`: Rendering time, not considered in complexity analysis.

Overall Time Complexity: O(n log n) + O(len(parameters))

**Space Complexity**:

- `cv_results`, `rank_1`: O(n)
- `fig` and other local variables: O(1)

Overall Space Complexity: O(n)
# Complexity Analysis of `tableGridSearch` Function

The `tableGridSearch` function is analyzed for its time and space complexity. This function is designed to display cross-validation results in a tabular format while providing options to manipulate the display.

## Steps Undertaken

1. **Data Preparation and Sorting**:
   - A DataFrame is created from cross-validation results (`clf.cv_results_`).
   - The DataFrame is sorted based on rank and mean fit time.

2. **Column Reordering**:
   - Column order is rearranged to prioritize `rank_test_score`, `mean_test_score`, and `std_test_score` columns.

3. **CSV Saving** (Optional):
   - If `save` is True, the DataFrame is saved to a CSV file. This involves iterating over the DataFrame rows and writing to a CSV file.

4. **Column Dropping** (Optional):
   - Unless `all_columns` is True, specific columns are dropped from the DataFrame. Columns dropped include `params`, `std_*`, and `split*` columns.

5. **Row Filtering** (Optional):
   - Unless `all_ranks` is True, only rows with a rank equal to 1 are retained in the DataFrame. The `rank_test_score` column is dropped from the DataFrame.

6. **Display the DataFrame**:
   - The DataFrame is displayed using the `display` function.

## Complexity Analysis

**Time Complexity**:

- DataFrame operations (sorting): O(n log n)
- Column reordering: O(n), where n is the number of columns in the DataFrame.
- CSV saving (if enabled): O(n)
- DataFrame dropping and filtering (based on `all_columns` and `all_ranks`): O(n)

Overall Time Complexity: O(n log n) + O(n) + O(n) + O(n)

**Space Complexity**:

- `cv_results`: O(n), where n is the number of cross-validation results.
- `columns`: O(m), where m is the number of columns in the DataFrame.
- Style modifications: O(1)

Overall Space Complexity: O(n)


