script_full_path=$(dirname "$0")
git pull
python  "$script_full_path/index.py" &
iceweasel 127.0.0.1:8080  &
#@midori -p -e Fullscreen -a http://127.0.0.1:8080
