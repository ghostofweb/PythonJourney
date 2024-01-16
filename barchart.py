import matplotlib.pyplot as plt

def display_bar_chart(data):
    categories = list(data.keys())
    values = list(data.values())

    plt.bar(categories, values, color='skyblue')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Bar Chart Example')
    plt.show()

def display_pie_chart(data):
    categories = list(data.keys())
    values = list(data.values())

    plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightgreen', 'lightskyblue'])
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Pie Chart Example')
    plt.show()

# Example data
bar_chart_data = {'Category A': 30, 'Category B': 45, 'Category C': 25}
pie_chart_data = {'Category X': 20, 'Category Y': 40, 'Category Z': 40}

# Display Bar Chart
display_bar_chart(bar_chart_data)

# Display Pie Chart
display_pie_chart(pie_chart_data)
