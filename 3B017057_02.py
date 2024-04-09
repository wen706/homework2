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
    for i in data:
        if i["student_id"]==student_id:
            if course_name != "" and course_score!="":
                i["courses"].append({"name": course_name, "score": float(course_score)})
                return "=>課程已成功新增。"
            raise ValueError( "=>其它例外: 課程名稱或分數不可空白.")
    raise ValueError( "=>發生錯誤: 學號 {} 找不到.".format(student_id))


def calculate_average_score(student_data:dict)->float:
    """"""
    print(student_data)
    student_score=[float(x['score']) for x in student_data["courses"] ]
    return sum(student_score)/len(student_score)


if os.path.isfile("students.json"):
    jsonFile = open("./students.json",'r',encoding="utf8")
    jsondata = json.load(jsonFile)
    jsonFile.close
    while 1 :
        print("""***************選單***************
1. 查詢指定學號成績
2. 新增指定學號的課程名稱與分數
3. 顯示指定學號的各科平均分數
4. 離開
**********************************""")
        comm=input("請選擇操作項目：")
        try:
            if comm == '1':
                student_data = json.dumps(get_student_info(jsondata,input("請輸入學號: ")), indent=2, ensure_ascii=False)
                print(student_data)
            elif comm == '2':
                print(add_course(jsondata,input("請輸入學號: "),input("請輸入要新增課程的名稱: "),input("請輸入要新增課程的分數: ")))
            elif comm == '3':
                student_data = get_student_info(jsondata,input("請輸入學號: "))
                print(calculate_average_score(student_data))
            elif comm == '4':
                break
            else:
                raise ValueError("=>請輸入有效的選項。")
        except ValueError as error:
            print(error)