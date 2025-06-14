# Quantium starter repo
This repo contains everything you need to get started on the program! Good luck!

## Task 2: Data Cleaning 🧹

In this task, the raw sales data was cleaned to focus only on `Pink Morsels`. The steps included:

- Filtering data for the product "Pink Morsels"
- Converting dates to datetime format
- Ensuring the data was sorted by date
- Removing unnecessary columns or entries

The cleaned dataset was saved as `formatted_sales_data.csv`.

---

## Task 3: Sales Visualisation Using Dash 📊

This task involved creating a simple interactive dashboard using **Dash** to visualize the impact of a price change in Pink Morsels.

The line chart below shows how sales varied over time. A noticeable jump in sales is visible around the start of 2021 — indicating the price change.

### 📈 Output – Sales Line Chart

![Sales Line Chart](newplot.png)

The dashboard was implemented in `dash_app.py`.

## ✅ Task 4: Final Dash App with Callback and CSS

### Objective
Create an interactive Dash app to display sales data with region filtering using a dropdown, and apply custom styles using CSS.

### Features
- 📊 Line chart of daily sales per region.
- 🔽 Dropdown to filter data by region.
- 🎨 CSS styling via `assets/styles.css`.

### Files
- `dash_app.py`: Contains the full Dash app with callbacks.
- `assets/styles.css`: Custom styling for the app.
- `data/`: Folder containing 3 CSV datasets.
- `formatted_sales_data.csv`: Cleaned and merged data used by the app.

### How to Run
```bash
python dash_app.py

## ✅ Task 5: Dash App Testing

### Objective
To verify the Dash app is functioning correctly using the Dash testing framework with pytest.

### Test Coverage
- ✅ Header is present.
- ✅ Graph is rendered.
- ✅ Region picker dropdown is available.

### File
- `test_dash_app.py`: Contains 3 test functions.
- Tested using `pytest` and `dash[testing]`.

### How to Run
```bash
pip install -r requirements.txt
pytest test_dash_app.py
