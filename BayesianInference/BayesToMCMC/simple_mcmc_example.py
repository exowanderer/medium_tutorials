def metropolis_hasting_iterator(curr_state, verbose=False):
    proposal = np.random.normal(curr_state, 0.5)
    l_curr = np.exp(-curr_state**2 / 2) / np.sqrt(2 * np.pi)
    l_prop = np.exp(-proposal**2 / 2) / np.sqrt(2 * np.pi)
    accept_prob = l_prop / l_curr
    accept_thresh = np.random.uniform(0,1)

    if verbose:
        print(
            proposal,
            l_prop,
            accept_prob,
            accept_thresh,
            accept_prob > accept_thresh
        )

    if accept_prob > accept_thresh:
        return proposal

    return curr_state

def mcmc(initial_state=0, n_samples=1, verbose=False):
    chain = []
    curr_state = initial_state
    for _ in range(n_samples):
        curr_state = metropolis_hasting_iterator(
            curr_state,
            verbose=verbose
        )
        chain.append(curr_state)

    return chain

def plot_chain(chain):

    title = 'Example MCMC Chain with Standard Normal Likelihood'

    fig = px.line(y=chain, title=title)

    fig.update_layout({
        'plot_bgcolor': 'rgba(0,0,0,0)',
        'paper_bgcolor': 'rgba(0,0,0,0)',
    })

    fig.add_trace(
        go.Violin(
            y=chain,
            side='positive',
            xaxis="x2",
            yaxis="y2",
            showlegend=False
        )
    )

    width=1600
    height=800
    margins={'l':20, 'r':20, 't':50, 'b':20}

    layout = {
        'showlegend': False,
        'xaxis': {'domain': [0, 0.88]},
        'xaxis2': {'domain': [0.9, 1]},
        'yaxis2': {
            'anchor': 'x2',
        },
        "margin": margins,
        "width": width,
        "height": height

    }
    fig.update_layout(layout)
    fig.update_traces(line_color='orange', line_width=5)

    fig.show()

if __name__ == '__main__':
    import numpy as np
    from plotly import express as px
    from plotly import graph_objs as go

    np.random.seed(42)
    initial_state = 5.0
    n_samples = 1000

    chain = mcmc(
        initial_state=initial_state,
        n_samples=n_samples,
        verbose=False
    )

    plot_chain(chain)
