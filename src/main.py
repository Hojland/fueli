%load_ext autoreload
%autoreload 2
import pandas as pd 
import numpy as np
import matplotlib

import settings

DATASET_NAME = "../data/drive_magnetic_sens.csv"

def first_3d_viz(df: pd.DataFrame):
    from mpl_toolkits import mplot3d

    import numpy as np
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")

    #z_line = np.linspace(0, 15, 1000)
    #x_line = np.cos(z_line)
    #y_line = np.sin(z_line)
    #ax.plot3D(x_line, y_line, z_line, 'gray')

    #ax.scatter3D(df['X'], df['Y'], df['Z'], cmap='hsv')
    ax.plot3D(df['X'], df['Y'], df['Z'], color='orange', marker='o', linestyle='solid', linewidth=2, markersize=3)
    matplotlib.interactive(True)
    plt.show()

def interactive_3d_viz(df: pd.DataFrame):
    import plotly
    import plotly.graph_objs as go

    # Configure Plotly to be rendered inline in the notebook.
    plotly.offline.init_notebook_mode()

    trace_1 = go.Scatter3d(
        x=df['X'], y=df['Y'], z=df['Z'],
        marker=dict(
            size=4,
            color=df['micro_tesla'],
            colorscale='Viridis')
            )
    
    trace_2 = go.Scatter3d(
        x=df['X'], y=df['Y'], z=df['Z'],
        mode='lines',
        name='lines')

    fig = go.Figure(data=[trace_1, trace_2]
    )
    plotly.offline.iplot(plot_figure)

def main():
    df = pd.read_csv(DATASET_NAME, delimiter=';', decimal=',')
    df['DateTime'] = pd.to_datetime("2021-01-01" + df['DateTime'], format='%Y-%m-%d%H.%M.%S')
    df['micro_tesla'] = df['Magnitude']

    import plotly.express as px
    fig = px.line_3d(df, x="X", y="Y", z="Z", color='micro_tesla')
    fig

if __name__ == "__main__":
    main()