from json import load,dump
from enum import Enum

template_path = "./data/template.bat"
settings_path = "./data/settings.json"
userbody_data_path = "./data/userbody.json"

#classes
class CalcMode(Enum):
    EYEHEIGHT_BASE = 0
    IPD_BASE = 1

#open files
with open(template_path,mode='rt',encoding='utf-8') as change_ipd_file:
    template = change_ipd_file.read()

with open(settings_path, mode='rt', encoding='utf-8') as change_ipd_file:
    settings = load(change_ipd_file)
    
with open(userbody_data_path, mode='rt', encoding='utf-8') as change_ipd_file:
    userbody = load(change_ipd_file)

#ask info
#need
user_eye_height = 0.0
avatar_eye_height = 0.0
user_ipd = 1.0
avatar_ipd = 1.0
file_name = "proxy"

print("数字を入力し、モードを選択してください\n0.EyeHeight(簡易)モード\n1.ipdモード\n> ",end="")
input_mode = int(input())
if input_mode == 0:
    mode = CalcMode.EYEHEIGHT_BASE
elif input_mode == 1:
    mode = CalcMode.IPD_BASE

if mode == CalcMode.EYEHEIGHT_BASE:
    measure_flg = False
    if userbody["eyeheight_valid"]:
        print("保存された身体データを使いますか[y/n] \n> ",end="")
        if str(input()) == "n":
            measure_flg = True
        else:
            user_eye_height = userbody["eyeheight"]
    else:
        measure_flg = True
    if measure_flg:
        print("自分の目の高さ(身長-0.1m程度)を入力してください(m) \n> ",end="")
        user_eye_height = float(input())
        userbody["eyeheight_valid"] = True
        userbody["eyeheight"] = user_eye_height
    print("使用するアバターの目の高さを入力してください(m) \n> ",end="")
    avatar_eye_height = float(input())
    
elif mode == CalcMode.IPD_BASE:
    measure_flg = False
    if userbody["eyeheight_valid"]:
        print("保存された目の高さを使いますか[y/n] \n> ",end="")
        if str(input()) == "n":
            measure_flg = True
        else:
            user_eye_height = userbody["eyeheight"]
    else:
        measure_flg = True
    if measure_flg:
        print("自分の目の高さ(身長-0.1m程度)を入力してください(m) \n> ",end="")
        user_eye_height = float(input())
        userbody["eyeheight_valid"] = True
        userbody["eyeheight"] = user_eye_height
    
    print("使用するアバターの目の高さを入力してください(m) \n> ",end="")
    avatar_eye_height = float(input())  
    
    if userbody["ipd_valid"]:
        print("保存されたipd(瞳孔間距離)を使いますか[y/n] \n> ",end="")
        if str(input()) == "n":
            measure_flg = True
        else:
            user_ipd = userbody["ipd"]
    else:
        measure_flg = True
    if measure_flg:
        print("自分のipd(瞳孔間距離)を入力してください(mm) \n> ",end="")
        user_ipd = float(input())/1000
        userbody["ipd_valid"] = True
        userbody["ipd"] = user_ipd
    print("使用するアバターのipdを入力してください(mm) \n> ",end="")
    avatar_ipd = float(input())/1000

print("保存するファイル名を入力してください > ",end="")
file_name = str(input())

#calc
ipd_offset = ((user_eye_height/user_ipd)/(avatar_eye_height/avatar_ipd) - 1)*settings["base_ipd"]

#save data
with open(userbody_data_path,mode='wt',encoding='utf-8') as userbody_file:
    dump(userbody,userbody_file,indent=3)

with open(rf"{file_name}.bat",mode='wt',encoding='utf-8') as change_ipd_file:
    change_ipd_file.write(template + str(ipd_offset))
    
#print success
print(f"{file_name}.batの作成が完了しました。\nEnterキーで終了します…",end="")
input()
    