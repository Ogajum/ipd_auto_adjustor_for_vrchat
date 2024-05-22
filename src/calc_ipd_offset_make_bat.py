from json import load
template_path = "./data/template.bat"
settings_path = "./data/settings.json"

with open(template_path,mode='rt',encoding='utf-8') as f:
    template = f.read()

with open(settings_path, mode='rt', encoding='utf-8') as f:
    settings = load(f)

print("自分の目の高さ(身長-0.1m程度)を入力してください(m) > ",end="")
real_eye_height = float(input())
print("使用するアバターの目の高さを入力してください(m) > ",end="")
avatar_eye_height = float(input())
print("保存するファイル名を入力してください > ",end="")
file_name = str(input())

ipd_offset = (real_eye_height/avatar_eye_height - 1)*settings["base_ipd"]
        
with open(rf"{file_name}.bat",mode='wt',encoding='utf-8') as f:
    f.write(template + str(ipd_offset))
    