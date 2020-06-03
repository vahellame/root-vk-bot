## root bot

### Step 1) Requirements

- Linux / macOS
- Python 3.x

### Step 2) Install

View and edit `main.py`.

Run in your console:

```
sudo apt update && sudo apt -y dist-upgrade
sudo apt install -y git python3-venv
git clone https://github.com/vahellame/root-vk-bot.git
cd root-vk-bot
python3 -m venv venv
./venv/bin/pip install -U pip setuptools wheel
./venv/bin/pip install -r requirments.txt
```

### Step 3) Running bot

```
nohup ./venv/bin/python main.py 1> output_nohup.txt 2> errors_nohup.txt &
```
