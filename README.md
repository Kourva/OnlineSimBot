<div align="center">
    <h3><b>𑁍 OnlineSim Bot 𑁍</b></h3>
  <p>∞ Virtual Number bot for Telegram which uses OnlineSim's free virtual numbers ∞</p>
</div>

# 𖣠 About OnlineSim Bot
This telegram bot fetches virtual numbers and countries from [OnlineSim](https://onlinesim.io). Then filters numbers based on **active** and **online** numbers, and selects a random number and sends it to user.<br>
Users also can **re-new** number or **check number's profile** in Telegram to make sure there is no account registered on that number!<br>
Bot will send last 5 messages for each number in each request. So use number and click on **inbox** inline button to get last 5 messages.<br><br>
⿻ Here is list of commands:
+ `/start` | `/restart` -> **Starts the bot**
+ `/help` | `/usage` -> **Shows help message**
+ `/number` -> **Sends random virtual number**
<br>

# ⚝ Installation
1. **Clone repository**:
    ```bash
    git clone https://github.com/Kourva/OnlineSimBot
    ```
2. **Navigate to OnlineSimBot**:
    ```bash
    cd OnlineSimBot
    ```
3. **Activate Virtual Environment**:
    ```bash
    virtualenv venv && source venv/bin/activate
    ```
4. **Install requirements**:
    ```bash
    pip install -r requirements.txt
    ```
<br>

# 🕸 Configuration
Open `src/token.txt` and put your bot's token in that file. Get token from [bot father](https://t.me/botfather)
> Example token: **1234567890:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa**
+ **Lanuch the bot**:
    After configuring the token, simply run `main.py` to launch your bot: 
    ```bash
    python main.py
    ```
<br>

# 𖡎 Using Proxychains with TOR proxy
You can use this bot with **TOR as proxy** using `proxychains` to bypass Telegram filtering (You need to start the **tor** on terminal before using proxychains):
```bash
proxychains -q python main.py
```
Also you can re-new you identity and IP address using `kill` command:
```bash
sudo pkill -HUP tor
```
