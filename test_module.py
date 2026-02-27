import medical_data_visualizer
import matplotlib

def test_draw_cat_plot():
    fig = medical_data_visualizer.draw_cat_plot()
    assert isinstance(fig, matplotlib.figure.Figure), "draw_cat_plot must return a matplotlib Figure"

def test_draw_heat_map():
    fig = medical_data_visualizer.draw_heat_map()
    assert isinstance(fig, matplotlib.figure.Figure), "draw_heat_map must return a matplotlib Figure"