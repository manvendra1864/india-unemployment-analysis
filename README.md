# Unemployment Analysis – India

This project analyzes unemployment trends in India using Python and visualizes the insights through a user-friendly interface. It includes multiple graphs and charts that reflect unemployment rates across states, urban/rural areas, and pre/post-lockdown periods.

> 🚧 A web-based version of this project using **`Streamlit`** is under development and will replace the GUI version for broader accessibility and interactivity.

---

## 🔍 Project Features

- 📉 **State-Wise Average Unemployment:** Visualize the average unemployment rate across all states using an intuitive bar chart.

- 📊 **Unemployment Distribution by State:** Analyze the spread and variability of unemployment rates using a detailed box plot.

- 🔥 **Correlation Heatmap:** Identify relationships between key economic indicators through a visually engaging heatmap.

- ✳️ **Scatter Matrix of Metrics:** Explore correlations and interdependencies among multiple metrics with an interactive scatter matrix.

- 🏘️ **Monthly Rural vs Urban Unemployment Trends:** Track monthly unemployment changes in rural and urban areas using an animated bar chart.

- 🌞 **Sunburst Chart of Area and State Unemployment:** Visualize hierarchical unemployment data by region and state with a multi-level sunburst chart.

- 🗺️ **Geospatial Lockdown Impact Analysis:** Examine the geographic impact of lockdowns on unemployment through a scatter geo plot.

- 🔄 **Pre vs Post-Lockdown Unemployment Comparison:** Compare unemployment rates before and after lockdown periods using percentage change visualizations.

- 🚦 **Lockdown Impact on Employment:** Display the state-wise severity of lockdown impact on employment using color-coded indicators and emoji-based classifications for quick interpretation.

---

## ⚙️ Tech Stack

- **Language**: Python 3.7+
- **Libraries**:
  - `numpy`, `pandas`
  - `matplotlib`, `seaborn`, `plotly`
  - `tkinter` (GUI – desktop)
- **Tools**:
  - Jupyter Notebook
  - Coming soon: Streamlit for web deployment

---

## 📁 File Structure

```plaintext
india-unemployment-analysis/
├── tkinter_version/
│   ├── unemployment_gui.py
│   ├── requirements.txt
├── notebooks/
│   └── Unemployment Analysis.ipynb
├── dataset/
│   └── unemployment_india.csv
├── README.md
```
---

## 🚀 Installation & Usage

### Prerequisites

Ensure you have the following installed:

- **Python**: Version 3.7 or higher
- **Required Libraries**:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `plotly`

---

### 📦 Step 1: Clone the Repository

```bash
git clone https://github.com/manvendra1864/india-unemployment-analysis.git
cd india-unemployment-analysis
```

### 📁 Step 2: Install Required Dependencies
Navigate to the Tkinter version:

```bash
cd tkinter_version
```

Then install all required libraries:

```bash
pip install -r requirements.txt
```

### ▶️ Step 3: Run the GUI Application
```bash
python unemployment_gui.py
```
This will launch a window with buttons to display various visualizations of unemployment trends in India.

---

### 📓 (Optional) Use the Jupyter Notebook
Navigate to the `notebooks` folder and open the Jupyter notebook:

```bash
cd ../notebooks
jupyter notebook
```
Then open Unemployment Analysis.ipynb in your browser to explore the analysis code and plots interactively.

---
---