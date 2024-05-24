# ipd_auto_adjustor_for_vrchat
VRChatでアバターの大きさに合わせてSteamVRのipdOffsetを変更するためのセットアップツールのプロトタイプです。
SteamVR,pythonがインストールされたWindowsで動作します

calc_ipd_offset_make_bat.batから適切なipdOffsetを計算し、対応するipdOffset出力用のbatファイルを新しく生成します。

生成されたbatファイルを実行すると C:\Program Files (x86)\Steam\config\steamvr.vrsettings が書き換えられ、SteamVRの描画が変化します。
reset.batを実行すると C:\Program Files (x86)\Steam\config\steamvr.vrsettings をデフォルトの設定に戻します。