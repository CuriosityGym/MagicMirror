script_full_path=$(dirname "$0")
git pull
pip install -r requirements.txt
python  "$script_full_path/index.py" &
sleep 30
iceweasel 127.0.0.1:8080  &

