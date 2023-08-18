import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plotGridSearch(clf):
    # Create a DataFrame from cross-validation results and sort by rank and fit time
    cv_results = pd.DataFrame(clf.cv_results_).sort_values(by=['rank_test_score', 'mean_fit_time'])

    # Get parameter names
    parameters = cv_results['params'][0].keys()

    # Calculate the number of rows and columns for subplot layout
    rows = -(-len(parameters) // 2)
    columns = min(len(parameters), 2)

    # Create a subplot figure
    fig = make_subplots(rows=rows, cols=columns)

    row = 1
    column = 1

    # Iterate over each parameter
    for parameter in parameters:
        # Add scatter plot for mean test score
        fig.add_trace(go.Scatter(
            x=cv_results['param_' + parameter],
            y=cv_results['mean_test_score'],
            mode='markers',
            marker=dict(size=cv_results['mean_fit_time'],
                        color='SteelBlue'),
            name='Mean test score'
        ), row=row, col=column)

        # Add scatter plot for best estimator
        rank_1 = cv_results[cv_results['rank_test_score'] == 1]
        fig.add_trace(go.Scatter(
            x=rank_1['param_' + parameter],
            y=rank_1['mean_test_score'],
            mode='markers',
            marker=dict(size=rank_1['mean_fit_time'],
                        color='Crimson'),
            name='Best estimators'
        ), row=row, col=column)

        # Update axis titles
        fig.update_xaxes(title_text=parameter, row=row, col=column)
        fig.update_yaxes(title_text='Score', row=row, col=column)

        # Increment row and column indexes
        column += 1
        if column > columns:
            column = 1
            row += 1

    # Configure layout
    fig.update_layout(
        legend=dict(traceorder='reversed'),
        width=columns * 360 + 100,
        height=rows * 360,
        title='Best score: {:.6f} with {}'.format(cv_results['mean_test_score'].iloc[0], str(cv_results['params'].iloc[0])),
        hovermode='closest'
    )

    # Show the plot
    fig.show()
