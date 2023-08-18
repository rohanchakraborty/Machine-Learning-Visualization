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

