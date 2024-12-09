import random
import pandas as pd
import csv

# 讀取CSV檔案
class_data = pd.read_csv('class.csv')
student_data = pd.read_csv('student.csv')

# 獲取不重複的課程名稱列表
class_type = class_data['class_name'].drop_duplicates().tolist()

# 生成隨機選課資料
take = []  # 用來儲存 student_id 和 class_id

# 遍歷學生資料，使用 iterrows() 來遍歷每一行
for _, student_row in student_data.iterrows():
    # 檢查學生是否仍在學
    if student_row['status'] != '已離開':
        # 根據學生的年級選擇課程
        if student_row['grade'] == '三年級':
            # 篩選出 '高三' 的課程，並隨機選擇
            available_classes = class_data[class_data['class_name'].str.startswith('高三')]
            class_id = random.choice(available_classes['class_id'].tolist())
        elif student_row['grade'] == '二年級':
            # 篩選出 '高二' 的課程，並隨機選擇
            available_classes = class_data[class_data['class_name'].str.startswith('高二')]
            class_id = random.choice(available_classes['class_id'].tolist())
        else:
            # 篩選出 '高一' 的課程，並隨機選擇
            available_classes = class_data[class_data['class_name'].str.startswith('高一')]
            class_id = random.choice(available_classes['class_id'].tolist())

        # 把學生ID與課程ID加入選課清單
        take.append([student_row['student_id'], class_id])

# 寫入 'take.csv' 檔案
with open('take.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["student_id", "class_id"])  # 寫入表頭
    writer.writerows(take)  # 寫入學生選課資料

print("Data has been written to 'take.csv'")
