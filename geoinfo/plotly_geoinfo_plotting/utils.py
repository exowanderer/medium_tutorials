import plotly.io as pio
import plotly.graph_objs as go
import numpy as np

def make_globe_plot_per_continent(
        df, locations_col, data_col, text_col=None, title='', type='choropleth',
        lakecolor='rgb(0,191,255)', showlakes=True, log_plot=False, width=800, height=800):
    '''
        Docstring
    '''
    # https://towardsdatascience.com/geographical-plotting-of-maps-with-plotly-4b5a5c95f02a
    if log_plot:
        data = dict(
            type=type,
            locations=df[locations_col],
            z=np.log10(df[data_col]),
            text=df[text_col] if text_col is not None else None
        )
    else:
        data = dict(
            type=type,
            locations=df[locations_col],
            z=df[data_col],
            text=df[text_col] if text_col is not None else None
        )


    layout = dict(
        title=title,
        geo=dict(
            projection={'type':'orthographic'},
            showlakes=showlakes,
            lakecolor=lakecolor
        ),
        width=width,
        height=height
    )


    fig = go.Figure(
        data=[data],
        layout=layout
    )

    fig.show()

