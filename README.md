## root VK bot

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
./venv/bin/pip install -U pip
./venv/bin/pip install -r requirements.txt
```

### Step 3) Running bot

```
sudo nohup $PWD/venv/bin/python $PWD/main.py 1> $PWD/out.txt 2> $PWD/errors.txt &
```
