echo "Cloning Repo, Please Wait..."
git clone -b master https://github.com/Nancy-Robot/Nancy-Model-Bot.git /Nancy-Model-Bot
cd /Nancy-Model-Bot
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot, Please Wait..."
python3 bot.py
