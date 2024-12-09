import openai
import random
import csv
import os


api_key = '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'
# 設定 OpenAI API 金鑰
school_lists = [
    "台北市立建國高級中學", "台北市立中山高級中學", "台北市立松山高級中學", "台北市立大同高級中學", 
    "台北市立光明高級中學", "私立薇閣高級中學", "台北市立西松高級中學", "台北市立南港高級中學",
    "台北市立景美高級中學", "台北市立大直高級中學", "台北市立中正高級中學", "台北市立大理高級中學",
    "台北市立和平高級中學", "台北市立華岡高級中學", "台北市立第一女子高級中學", "台北市立實踐高級中學",
    "台北市立大安高級中學", "新北市立板橋高級中學", "新北市立新店高級中學", "新北市立三峽高級中學",
    "新北市立三重高級中學", "新北市立中和高級中學", "新北市立新莊高級中學", "新北市立新北高級中學",
    "新北市立新莊高中", "新北市立淡水高級中學", "新北市立鶯歌高級中學", "新北市立中和高級中學",
    "新北市立泰山高級中學", "新北市立土城高級中學", "新北市立瑞芳高級中學", "新北市立林口高級中學",
    "新北市立樹林高級中學", "新北市立金山高級中學", "新北市立三芝高級中學", "新北市立深坑高級中學",
    "新北市立五股高級中學",
]

# Function to handle retries with OpenAI API
def safe_openai_request(request_function, *args, **kwargs):
    retries = 3
    for attempt in range(retries):
        try:
            return request_function(*args, **kwargs)
        except openai.error.OpenAIError as e:
            if '500' in str(e):  # Server error, retry
                print(f"Server error (500), retrying... (Attempt {attempt + 1}/{retries})")
                time.sleep(5)
            else:
                raise e
    raise Exception("Max retries reached, request failed.")

# Function to generate student names
def generate_student_name_batch(n):
    prompt = f"請生成{n}個台灣人的名字"
    response = safe_openai_request(openai.Completion.create, 
                                   model="text-davinci-003", 
                                   prompt=prompt, 
                                   max_tokens=300, 
                                   n=1, 
                                   stop=None)
    names = response['choices'][0]['text'].strip().split("\n")
    return names

# Function to generate student phone numbers
def generate_student_tel_batch(n):
    prompt = f"請生成{n}個10位數的手機號碼，格式：09xx-xxx-xxx"
    response = safe_openai_request(openai.Completion.create, 
                                   model="text-davinci-003", 
                                   prompt=prompt, 
                                   max_tokens=300, 
                                   n=1, 
                                   stop=None)
    tel_numbers = response['choices'][0]['text'].strip().split("\n")
    return tel_numbers

# Function to generate student addresses
def generate_student_address_batch(n):
    prompt = f"請生成{n}個台北的地址"
    response = safe_openai_request(openai.Completion.create, 
                                   model="text-davinci-003", 
                                   prompt=prompt, 
                                   max_tokens=500, 
                                   n=1, 
                                   stop=None)
    addresses = response['choices'][0]['text'].strip().split("\n")
    return addresses

# Function to generate student data in batches
def generate_data_with_delay(total_students=2000, batch_size=100):
    data = []
    num_batches = total_students // batch_size
    
    for batch in range(num_batches):
        print(f"Generating batch {batch + 1}/{num_batches}...")
        
        # Generate student information in batches
        names = generate_student_name_batch(batch_size)
        tels = generate_student_tel_batch(batch_size)
        addresses = generate_student_address_batch(batch_size)

        init_student_num_1 = 168
        init_student_num_2 = 346
        init_student_num_3 = 360

        for i in range(batch_size):
            if i < batch_size // 3:
                student_id_prefix = 's_2021'
                init_student_num_1 += 1
                stu_num = init_student_num_1
            elif i < 2 * batch_size // 3:
                student_id_prefix = 's_2022'
                init_student_num_2 += 1
                stu_num = init_student_num_2
            else:
                student_id_prefix = 's_2023'
                init_student_num_3 += 1
                stu_num = init_student_num_3

            student_id = f"{student_id_prefix}{str(stu_num).zfill(4)}"
            student_name = names[i]
            school = random.choice(school_lists)
            grade = random.choice(["一年級", "二年級", "三年級"])
            tel = tels[i]
            address = addresses[i]
            status = random.choice([""] * 9 + ["已離開"])

            data.append([student_id, student_name, school, grade, tel, address, status])

        # Add a delay between batches to avoid rate limiting
        time.sleep(5)  # Wait 5 seconds between each batch

    return data

# Save the generated data to a CSV file
def save_to_csv(data, filename="students_data.csv"):
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['student_id', 'student_name', 'school', 'grade', 'tel', 'address', 'status'])
        writer.writerows(data)
    print(f"Data saved to {filename}")

# Main function to generate and save data
if __name__ == "__main__":
    student_data = generate_data_with_delay(total_students=2000, batch_size=100)
    save_to_csv(student_data, 'students_data.csv')