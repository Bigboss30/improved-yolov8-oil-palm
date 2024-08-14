# Sample data
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Sample data
models = ['YOLOv8n', 'YOLOv8s', 'YOLOv8m', 'YOLOv8l', 'YOLOv8x']
map5095 = [0.709, 0.756,0.75,0.763,0.761]

# Create the bar chart
fig, ax1 = plt.subplots(figsize=(8, 4))
sns.barplot(x=models, y=map5095, color='purple', alpha=0.2)

# Set the y-axis limit for the primary y-axis
ax1.set_ylim(0, 1.0)

# Add more ticks to the primary y-axis
ax1.set_yticks(np.arange(0, 1.0, 0.1))

# # Add precision values on top of the bars
# for i, (model, value) in enumerate(zip(models, precision)):
#     ax1.text(i, value + 0.01, f'{value:.3f}', ha='center', va='bottom')

# Create the secondary y-axis for the trend line
ax2 = ax1.twinx()

# Set the y-axis limit for the primary y-axis
ax2.set_ylim(0.65, 0.8)

# Add the trend line
ax2.plot(models, map5095, color='black', marker='o', linewidth=2)

# Add grid lines with opacity
ax1.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.5) # Grid lines for the primary y-axis
ax2.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.5)

# Remove the top and right spines
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

# Set the labels and title
ax1.set_xlabel('Models')
ax1.set_ylabel('mAP@0.50:0.95')
ax2.set_ylabel('Trend')
plt.title('mAP@0.50:0.95 Comparison of Various YOLO Models with Trend Line')

# Show the plot
plt.show()
