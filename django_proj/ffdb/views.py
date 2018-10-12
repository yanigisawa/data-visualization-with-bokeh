from django.shortcuts import render
from django.http import HttpResponse
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import ColumnDataSource
from bokeh.layouts import column
import pandas as pd
from ffdb.models import PlayerStat


def index_single(req):

    df = pd.DataFrame(list(PlayerStat.objects.filter(player_name='Jamaal Charles', year=2013).values()))

    p = figure(plot_width=800, plot_height=250, title="Jamaal Charles - 2013")
    p.line('week', 'fpts', color='navy', alpha=0.5, source=df)

    script, div = components(p)
    return render(req, 'ffdb/bokeh_plot.html', {'script': script, 'div': div} )

def index(req):
    # SqlLite doesn't support SELECT DISTINCT
    # django.db.utils.NotSupportedError: DISTINCT ON fields is not supported by this database backend
    player_name = 'Jamaal Charles'
    years = PlayerStat.objects.filter(player_name=player_name).values('year').distinct()
    graphs = []
    x_range, y_range= (1, 16), (0, 55)

    for y in years:
        df = pd.DataFrame(list(PlayerStat.objects.filter(player_name=player_name, year=y['year']).values()))

        if graphs:
            x_range, y_range = graphs[0].x_range, graphs[0].y_range

        f = figure(plot_width=800, plot_height=250,
            title=f'{player_name} - {y["year"]}', y_range=y_range, x_range=x_range)
        f.line('week', 'fpts', color='navy', alpha=0.5, source=df)
        graphs.append(f)

    p = column(graphs)

    script, div = components(p)
    return render(req, 'ffdb/bokeh_plot.html', {'script': script, 'div': div} )
