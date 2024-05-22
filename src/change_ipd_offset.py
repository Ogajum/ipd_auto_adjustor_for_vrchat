import sys
import json

settings_path = "./data/settings.json"
with open(settings_path, mode='rt', encoding='utf-8') as f:
    settings = json.load(f)
    vrsettings_path = settings["vrsetting_path"]

args = sys.argv
ipd_offset = float(args[1])

with open(vrsettings_path,mode='rt',encoding='utf-8') as f:
    data = json.load(f)

data["steamvr"]["ipdOffset" ] = ipd_offset

with open(vrsettings_path,mode='wt',encoding='utf-8') as f:
    json.dump(data,f,indent=3)
