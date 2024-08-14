import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
# Data for YOLOv8 Pretrained Models
pretrained_models = ['yolov8n', 'yolov8s', 'yolov8m', 'yolov8l', 'yolov8x', 'yolov8x10', 'yolov8x13', 'yolov8x16', 'yolov8x19']
# pretrained_map50 = [0.956, 0.975, 0.959, 0.974,0.975,0.989, 0.975, 0.969, 0.988]
pretrained_detection_times = [2.9, 10.5, 7.2, 20.6,29.3, 16.3, 16.7, 15.3, 16.2]


# Create the bar chart
fig, ax1 = plt.subplots(figsize=(8, 4))
sns.barplot(x=pretrained_detection_times, y=pretrained_models, color='red', alpha=0.2)

# # Set the y-axis limit for the primary y-axis
# ax1.set_ylim(0, 31.0)

# # Add more ticks to the primary y-axis
# ax1.set_yticks(np.arange(0, 30.0, 5))

# # Add precision values on top of the bars
# for i, (model, value) in enumerate(zip(models, precision)):
#     ax1.text(i, value + 0.01, f'{value:.3f}', ha='center', va='bottom')



# Add grid lines with opacity
ax1.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.5) # Grid lines for the primary y-axis

# Remove the top and right spines
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Set the labels and title
ax1.set_xlabel('Detection Time (ms)')
ax1.set_ylabel('Models')
plt.title('Comparison of Various YOLO Models and Detection Time (ms)')

# Customize x-axis tick positions and labels
# plt.xticks(rotation=45, ha='right')  # Rotate labels for better visibility

# Adjust layout to prevent clipping of labels
plt.tight_layout()

# Show the plot
plt.show()