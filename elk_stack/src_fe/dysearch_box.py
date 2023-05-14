import requests
from ast import literal_eval
from loguru import logger
from bokeh.layouts import layout
from bokeh.io import curdoc
from bokeh.models.widgets import Select, TextInput


def get_suggestions(query):
    dictToSend = {"query": f"{query}"}
    res = requests.post("http://jupyterlab:5000/predict", json=dictToSend)
    suggestions = literal_eval(res.json()[0]["autocompletions"])
    logger.info(f"update autocomplete options with new suggestions: {suggestions}")
    return (suggestions)


def update(attr, old, new):
    logger.info(f"getting autocompletions for query: {autocomp.value_input}")
    new_completions = get_suggestions(autocomp.value)
    suggestions.options = new_completions


autocomp = TextInput(value='', title="Autocomplete Search Box")
suggestions = Select(title="New suggestions", value='', options=['abc', 'pqr'])
autocomp.on_change('value_input', update)
layout = layout([[autocomp, suggestions]])

curdoc().add_root(layout)
