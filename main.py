import medical_data_visualizer
from test_module import test_draw_cat_plot, test_draw_heat_map

# Generate plots
medical_data_visualizer.draw_cat_plot()
medical_data_visualizer.draw_heat_map()

# Run tests
test_draw_cat_plot()
test_draw_heat_map()

print("All tests passed successfully!")