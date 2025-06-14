# test_dash_app.py

import pytest
from dash import Dash
from dash_app import app  # assuming your app is in dash_app.py

@pytest.fixture
def dash_duo_app(dash_duo):
    dash_duo.start_server(app)
    return dash_duo

def test_header_is_present(dash_duo_app):
    assert dash_duo_app.find_element("h1").text == "🛍️ Pink Morsel Sales Dashboard"

def test_graph_is_present(dash_duo_app):
    graph = dash_duo_app.find_element("#sales-line-chart")
    assert graph is not None

def test_region_picker_is_present(dash_duo_app):
    radio_items = dash_duo_app.find_elements("input[type='radio']")
    assert len(radio_items) == 5  # all, north, east, south, west
