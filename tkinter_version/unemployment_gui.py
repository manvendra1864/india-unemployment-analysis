import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import calendar
from tkinter import Tk, Button, Label, Frame, messagebox

# Loading the dataset
file_path = 'dataset/unemployment_india.csv'
try:
    unemployment = pd.read_csv(file_path)
    unemployment.columns = [
        'State', 'Date', 'Frequency', 'Estimated Unemployment Rate',
        'Estimated Employed', 'Estimated Labour Participation Rate', 'Area'
    ]
    unemployment['Date'] = pd.to_datetime(unemployment['Date'], dayfirst=True)
    unemployment['MonthNumber'] = unemployment['Date'].dt.month
    unemployment['MonthNumber'] = unemployment['MonthNumber'].fillna(0).astype(int)
    unemployment['MonthName'] = unemployment['MonthNumber'].apply(lambda x: calendar.month_abbr[x] if x > 0 else "Unknown")
except FileNotFoundError:
    messagebox.showerror("Error", f"File '{file_path}' not found.")
    exit()

# Defining visualization functions
def show_box_plot():
    fig = px.box(
        unemployment,
        x='State',
        y='Estimated Unemployment Rate',
        color='State',
        title='Unemployment Rate by State',
        template='plotly',
        color_discrete_sequence=px.colors.qualitative.Plotly
    )
    fig.show()

def show_bar_plot():
    state_avg = unemployment.groupby('State')['Estimated Unemployment Rate'].mean().reset_index()
    fig = px.bar(
        state_avg,
        x='State',
        y='Estimated Unemployment Rate',
        color='State',
        title='State Wise Average Employment Rate',
        color_discrete_sequence=px.colors.qualitative.Plotly
    )
    fig.show()

def show_heatmap():
    try:
        heatmap_data = unemployment[['Estimated Unemployment Rate', 'Estimated Employed', 'Estimated Labour Participation Rate']].corr()
        fig = px.imshow(
            heatmap_data,
            text_auto=True,
            color_continuous_scale='Viridis',
            title='Correlation Heatmap'
        )
        fig.show()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate heatmap: {str(e)}")

def show_scatter_matrix():
    fig = px.scatter_matrix(
        unemployment,
        dimensions=['Estimated Unemployment Rate', 'Estimated Employed', 'Estimated Labour Participation Rate'],
        color='Area',
        title='Scatter Matrix of Key Metrics',
        color_discrete_sequence=px.colors.qualitative.Plotly
    )
    fig.show()

def show_area_unemployment():
    fig = px.bar(
        unemployment,
        x='Area',
        y='Estimated Unemployment Rate',
        animation_frame='MonthName',
        color='Area',
        title='Monthly Unemployment Rate by Area',
        height=600,
        color_discrete_sequence=px.colors.qualitative.Plotly
    )
    fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1500 
    fig.show()

def show_sunburst_chart():
    unempDF = unemployment.groupby(['Area', 'State'])['Estimated Unemployment Rate'].mean().reset_index()
    fig = px.sunburst(
        unempDF,
        path=['Area', 'State'],
        values='Estimated Unemployment Rate',
        title='Unemployment Rate by Area and State',
        height=600,
        color_discrete_sequence=px.colors.qualitative.Plotly
    )
    fig.show()

def show_lockdown_impact_scatter_geo():
    try:
        state_coords = {
            "Andhra Pradesh": [15.9129, 79.7400],
            "Arunachal Pradesh": [28.2180, 94.7278],
            "Assam": [26.2006, 92.9376],
            "Bihar": [25.0961, 85.3131],
            "Chhattisgarh": [21.2787, 81.8661],
            "Goa": [15.2993, 74.1240],
            "Gujarat": [22.2587, 71.1924],
            "Haryana": [29.0588, 76.0856],
            "Himachal Pradesh": [31.1048, 77.1734],
            "Jharkhand": [23.6102, 85.2799],
            "Karnataka": [15.3173, 75.7139],
            "Kerala": [10.8505, 76.2711],
            "Madhya Pradesh": [22.9734, 78.6569],
            "Maharashtra": [19.7515, 75.7139],
            "Manipur": [24.6637, 93.9063],
            "Meghalaya": [25.4670, 91.3662],
            "Mizoram": [23.1645, 92.9376],
            "Nagaland": [26.1584, 94.5624],
            "Odisha": [20.9517, 85.0985],
            "Punjab": [31.1471, 75.3412],
            "Rajasthan": [27.0238, 74.2179],
            "Sikkim": [27.5330, 88.5122],
            "Tamil Nadu": [11.1271, 78.6569],
            "Telangana": [18.1124, 79.0193],
            "Tripura": [23.9408, 91.9882],
            "Uttar Pradesh": [26.8467, 80.9462],
            "Uttarakhand": [30.0668, 79.0193],
            "West Bengal": [22.9868, 87.8550],
            "Delhi": [28.7041, 77.1025],
            "Jammu and Kashmir": [33.7782, 76.5762],
            "Ladakh": [34.1526, 77.5771],
        }
        coords_df = pd.DataFrame.from_dict(state_coords, orient='index', columns=['latitude', 'longitude']).reset_index()
        coords_df.rename(columns={'index': 'State'}, inplace=True)
        unemployment_with_coords = unemployment.merge(coords_df, on="State", how="left")
        fig = px.scatter_geo(
            unemployment_with_coords,
            lat='latitude',
            lon='longitude',
            color="Area",
            hover_name="State",
            size="Estimated Unemployment Rate",
            animation_frame="MonthName",
            scope='asia',
            title='Lockdown Impact throughout India'
        )
        fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1200
        fig.update_geos(
            lataxis_range=[5, 35],
            lonaxis_range=[65, 100],
            oceancolor="#6dd5ed",
            showocean=True
        )
        fig.show()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate lockdown impact scatter geo: {str(e)}")

def show_percentage_change_bar_chart():
    try:
        df47 = unemployment[(unemployment['MonthNumber'] >= 4) & (unemployment['MonthNumber'] <= 7)]
        df14 = unemployment[(unemployment['MonthNumber'] >= 1) & (unemployment['MonthNumber'] <= 4)]
        df47g = df47.groupby('State')['Estimated Unemployment Rate'].mean().reset_index()
        df14g = df14.groupby('State')['Estimated Unemployment Rate'].mean().reset_index()
        df47g['Unemployment Rate before lockdown'] = df14g['Estimated Unemployment Rate']
        df47g.columns = ['State', 'Unemployment Rate After Lockdown', 'Unemployment Rate Before Lockdown']
        df47g['% Change in Unemployment'] = round(
            (df47g['Unemployment Rate After Lockdown'] - df47g['Unemployment Rate Before Lockdown']) /
            df47g['Unemployment Rate Before Lockdown'] * 100, 2
        )
        fig = px.bar(
            df47g,
            x='State',
            y='% Change in Unemployment',
            color='% Change in Unemployment',
            title='% Change in Unemployment After Lockdown'
        )
        fig.show()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate percentage change bar chart: {str(e)}")

def show_lockdown_impact_on_employment():
    try:
        df47 = unemployment[(unemployment['MonthNumber'] >= 4) & (unemployment['MonthNumber'] <= 7)]
        df14 = unemployment[(unemployment['MonthNumber'] >= 1) & (unemployment['MonthNumber'] <= 4)]
        df47g = df47.groupby('State')['Estimated Unemployment Rate'].mean().reset_index()
        df14g = df14.groupby('State')['Estimated Unemployment Rate'].mean().reset_index()
        df47g['Unemployment Rate Before Lockdown'] = df14g['Estimated Unemployment Rate']
        df47g.columns = ['State', 'Unemployment Rate After Lockdown', 'Unemployment Rate Before Lockdown']
        df47g['% Change in Unemployment'] = round(
            (df47g['Unemployment Rate After Lockdown'] - df47g['Unemployment Rate Before Lockdown']) /
            df47g['Unemployment Rate Before Lockdown'] * 100, 2
        )
        df47g['Impact Status'] = df47g['% Change in Unemployment'].apply(
            lambda x: 'Low Impact' if x <= 10 else
                      'Moderate Impact' if x <= 20 else
                      'High Impact' if x <= 30 else
                      'Severe Impact'
        )
        fig = px.bar(
            df47g,
            y='State',
            x='% Change in Unemployment',
            color='Impact Status',
            title='Lockdown Impact on Employment in India',
            color_discrete_map={
                'Low Impact': 'green',
                'Moderate Impact': 'yellow',
                'High Impact': 'orange',
                'Severe Impact': 'red'
            }
        )
        fig.show()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate lockdown impact graph: {str(e)}")

# Function to apply hover effects on buttons
def on_enter(e):
    e.widget['background'] = '#4a4f6d'  # Lighter shade for hover

def on_leave(e):
    e.widget['background'] = '#3a3f5c'  # Original button color

# Create the GUI
def create_gui():
    root = Tk()
    root.title("Unemployment Analysis")
    root.geometry("500x600")  # Set the window size
    root.configure(bg="#2e2e2e")  # Set dark background color

    # Header Frame
    header_frame = Frame(root, bg="#2e2e2e", pady=10)
    header_frame.pack(fill="x")

    header_label = Label(
        header_frame,
        text="Unemployment Analysis – India",
        font=("Segoe UI", 18, "bold"),
        fg="white",
        bg="#2e2e2e"
    )
    header_label.pack()

    # Button Frame
    button_frame = Frame(root, pady=20, bg="#2e2e2e")
    button_frame.pack(fill="both", expand=True)

    # Updated button style with increased width
    button_style = {
        "font": ("Segoe UI", 12, "bold"),
        "bg": "#3a3f5c",  # Dark blue button color
        "fg": "white",
        "relief": "flat",
        "bd": 0,
        "width": 40,  # Increased width to accommodate longer button names
        "height": 2
    }

    buttons = [
        ("Unemployment Rate by State", show_box_plot),
        ("State-Wise Average Unemployment", show_bar_plot),
        ("Correlation Heatmap", show_heatmap),
        ("Scatter Matrix of Metrics", show_scatter_matrix),
        ("Monthly Area Unemployment", show_area_unemployment),
        ("Unemployment Rate by Area and State", show_sunburst_chart),
        ("Lockdown Impact Scatter Geo", show_lockdown_impact_scatter_geo),
        ("Percentage Change in Unemployment", show_percentage_change_bar_chart),
        ("Lockdown Impact on Employment in India", show_lockdown_impact_on_employment),  # New button
    ]

    for text, command in buttons:
        btn = Button(button_frame, text=text, command=command, **button_style)
        btn.pack(pady=5)
        btn.bind("<Enter>", on_enter)  # Add hover effect
        btn.bind("<Leave>", on_leave)

    # Exit Button
    exit_button = Button(
        root,
        text="Exit",
        command=root.quit,
        font=("Segoe UI", 12, "bold"),
        bg="#FF4C4C",  # Red exit button
        fg="white",
        relief="flat",
        bd=0,
        width=30,
        height=2
    )
    exit_button.pack(pady=20)
    exit_button.bind("<Enter>", lambda e: e.widget.config(bg="#FF6666"))  # Lighter red on hover
    exit_button.bind("<Leave>", lambda e: e.widget.config(bg="#FF4C4C"))  # Original red

    root.mainloop()

# Run the GUI
if __name__ == "__main__":
    create_gui()