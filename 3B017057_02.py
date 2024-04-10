import os
import json


def get_student_info(data:dict, student_id:str)->dict:
    """返回該學生的個人資料字典"""
    for student_data in data:
        if student_data["student_id"]==student_id:
            return student_data
    raise ValueError( "=>發生錯誤: 學號 {} 找不到.".format(student_id))


def add_course(data:dict, student_id:str, course_name:str, course_score:str)->str:
    """為指定學生添加一門課程及其分數"""
    if course_name != "" and course_score!="":
        for i in data:
            if i["student_id"]==student_id:
                i["courses"].append({"name": course_name, "score": float(course_score)})
                return "=>課程已成功新增。"
        raise ValueError( "=>發生錯誤: 學號 {} 找不到.".format(student_id))
    raise ValueError( "=>其它例外: 課程名稱或分數不可空白.")


def calculate_average_score(student_data:dict)->float:
    """算平均,student_data{"courses":[{"score"},...]}"""
    student_score=[float(x['score']) for x in student_data["courses"] ]
    if len(student_score)==0:
        return 0.0
    return sum(student_score)/len(student_score)


if os.path.isfile("students.json"):
    jsonFile = open("./students.json",'r',encoding="utf8")
    json_data = json.load(jsonFile)
    jsonFile.close()
    while True :
        print("""***************選單***************
1. 查詢指定學號成績
2. 新增指定學號的課程名稱與分數
3. 顯示指定學號的各科平均分數
4. 離開
**********************************""")
        comm=input("請選擇操作項目：")
        try:
            if comm == '1':
                student_id = input("請輸入學號: ")
                student_data = get_student_info(json_data, student_id)
                print(json.dumps(student_data, indent=2, ensure_ascii=False))
            elif comm == '2':
                student_id = input("請輸入學號: ")
                course_name = input("請輸入要新增課程的名稱: ")
                course_score = input("請輸入要新增課程的分數: ")
                print(add_course(json_data, student_id, course_name, course_score))
            elif comm == '3':
                student_id = input("請輸入學號: ")
                student_data = get_student_info(json_data, student_id)
                print("=>各科平均分數: {:.2f}".format(calculate_average_score(student_data)))
            elif comm == '4':
                print("=>程式結束。\n")
                break
            else:
                raise ValueError("=>請輸入有效的選項。")
        except ValueError as error:
            print(error)