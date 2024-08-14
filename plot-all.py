# ตัวอย่างข้อมูล (กรุณาแทนที่ด้วยข้อมูลของคุณเอง)
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    'Model': ['yolov8n', 'yolov8s', 'yolov8m', 'yolov8l', 'yolov8x'],
    'Precision': [0.827, 0.924, 0.917, 0.922, 0.918],
    'Recall': [0.93, 0.927, 0.918, 0.952, 0.964],
    'F1-score': [0.875, 0.925, 0.918, 0.937, 0.940],
    'mAP50': [0.956, 0.975, 0.959, 0.974, 0.975],
    'mAP50-95': [0.709, 0.756, 0.75, 0.763, 0.761]
}
# data = {
#     'Model': ['yolov8x10', 'yolov8x13', 'yolov8x16', 'yolov8x19'],
#     'Precision': [ 0.956, 0.92, 0.94, 0.966],
#     'Recall': [ 0.964, 0.931, 0.909, 0.968],
#     'F1-score': [0.960, 0.925, 0.924, 0.967],
#     'mAP50': [0.989, 0.975, 0.969, 0.988],
#     'mAP50-95': [0.763, 0.755, 0.757, 0.773]
# }
# สร้าง DataFrame
df = pd.DataFrame(data)

# ตั้งค่าความกว้างของแท่ง
bar_width = 0.15
index = np.arange(len(df['Model']))

# สร้างกราฟ
fig, ax = plt.subplots(figsize=(10, 4))

# วาดกราฟแท่งสำหรับแต่ละค่าโดยใช้สีแบบพาสเทล
pastel_colors = ['#FFB6C1', '#ADD8E6', '#90EE90', '#FFD700', '#FFA07A']

# Plot bars
bar1 = ax.bar(index, df['Recall'], bar_width, label='Recall', color=pastel_colors[0])
bar2 = ax.bar(index + bar_width, df['Precision'], bar_width, label='Precision', color=pastel_colors[1])
bar3 = ax.bar(index + 2 * bar_width, df['F1-score'], bar_width, label='F1-score', color=pastel_colors[2])
bar4 = ax.bar(index + 3 * bar_width, df['mAP50'], bar_width, label='mAP50', color=pastel_colors[3])
bar5 = ax.bar(index + 4 * bar_width, df['mAP50-95'], bar_width, label='mAP50-95', color=pastel_colors[4])

# เพิ่มป้ายกำกับในแต่ละแท่ง
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2.0, height, f'{height:.2f}', ha='center', va='bottom', fontsize=8, color='black')

add_labels(bar1)
add_labels(bar2)
add_labels(bar3)
add_labels(bar4)
add_labels(bar5)

# ตั้งค่าแกน x
ax.set_xlabel('Models', fontsize=14)
ax.set_ylabel('Metric Values', fontsize=14)  # แกน y แสดงค่าต่างๆ
ax.set_title('YOLOv8 Model Performance Metrics', fontsize=16)
ax.set_xticks(index + 1.5 * bar_width)
ax.set_xticklabels(df['Model'], fontsize=12)

# กำหนดขอบเขตของแกน y
ax.set_ylim(0.5, 1)

# เพิ่มตำนาน (legend)
ax.legend(fontsize=8, loc='best')

# เพิ่มกริด
ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.7)

# แสดงกราฟ
plt.tight_layout()
plt.show()


# import pandas as pd

# # Given data
# data = {
#     'Model': ['yolov8n', 'yolov8s', 'yolov8m', 'yolov8l', 'yolov8x', 'yolov8x10', 'yolov8x13', 'yolov8x16', 'yolov8x19'],
#     'Precision': [0.827, 0.924, 0.917, 0.922, 0.918, 0.956, 0.92, 0.94, 0.966],
#     'Recall': [0.93, 0.927, 0.918, 0.952, 0.964, 0.964, 0.931, 0.909, 0.968],
#     'mAP50': [0.956, 0.975, 0.959, 0.974, 0.975, 0.989, 0.975, 0.969, 0.988],
#     'mAP50-95': [0.709, 0.756, 0.75, 0.763, 0.761, 0.763, 0.755, 0.757, 0.773]
# }
# # 'F1-score': [0.875, 0.925, 0.918, 0.937, 0.940, 0.960, 0.925, 0.924, 0.967]
# # Calculate F1-score
# f1_scores = []
# for i in range(len(data['Model'])):
#     precision = data['Precision'][i]
#     recall = data['Recall'][i]
#     f1_score = 2 * (precision * recall) / (precision + recall)
#     f1_scores.append(f1_score)

# # Add F1-score to the data
# data['F1-score'] = f1_scores

# # Convert to DataFrame
# df = pd.DataFrame(data)

# # Display the updated DataFrame
# print(df)