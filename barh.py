import matplotlib.pyplot as plt

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [20, 35, 30, 25]

# Creating a horizontal bar plot
plt.barh(categories, values, color='skyblue')
plt.xlabel('Values')
plt.ylabel('Categories')
plt.title('Horizontal Bar Plot')
plt.show()
