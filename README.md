# kiwawa

LINE／Discord 訊息同步機器人。一個機器人只能服務一組 LINE 群組／Discord 文字頻道，已知不支援 LINE 貼圖、跨平台標記（@）。

## 使用教學

### 一鍵部署
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

若部署失敗請fork此repo並連結到Heroku來實現同步。亦可直接使用git下載及上傳

請確定resources裡面兩個自動執行的程式（`l2d.py`是Line to Discord，`d2l.py`是Discord to Line）都已被開啟，並且請到設定的Config Vars設定環境變數

總共有 6 個環境變數要設定： 
```
LINEBOT_SECRET
LINEBOT_ACCESS_TOKEN
LOTIFY_TOKEN
DISCORDBOT_TOKEN
DISCORD_WEBHOOK
MESSAGE_CHANNEL_ID(可選)
```

### LINE bot

至[Line Developers](https://developers.line.biz/console/) => 新增或選取Provider => Create a new channel => Message API。設定環境變數 `LINEBOT_SECRET` 及 `LINEBOT_ACCESS_TOKEN`。
> * Secret在Basic settings，Channel access token (long-lived)在Messaging API
> * Messaging API 底下的 Webhook 請設為 `https://(你的heroku網址)/callback`

### LINE Notify

https://notify-bot.line.me/my/ => 發行權杖 => 設定環境變數 `LOTIFY_TOKEN`。

> * 記得換成電腦板模式
> 權杖名稱是顯示在 `【 】` 中的文字，建議越短越好避免洗版

### Discord bot

https://discord.com/developers/applications => `New Application` => `Bot` => `Add Bot` => 往下拉設定權限 => Username 下方複製 token => 設定環境變數 `DISCORDBOT_TOKEN`

> 記得開啟Bot設定底下的REQUIRES OAUTH2 CODE GRANT和MESSAGE CONTENT INTENT

### Discord webhook

Discord 伺服器 => `伺服器設定` => `整合` => `建立 Webhook` => `複製 Webhook 網址` => 設定環境變數 `DISCORD_WEBHOOK`

> Webhook頭像和名稱不用特別設定，會自動換成發送訊息者的名稱及頭像

### Discord channel

Discord 伺服器 => 伺服器頻道 => 右鍵頻道 => `複製ID`(需至設定 => 進階 => 開啟開發者模式) => 設定環境變數 `MESSAGE_CHANNEL_ID`

## 小提醒

* Line有新訊息會叫醒機器人，但Discord不會。因此機器人在Discord離線時打開heroku網址即可喚醒他（若Discord未來改用Webhook即可被動式接受訊息）
* 當然，請邀請Line Notify和機器人到你的群組。Line機器人ID在Messaging API分頁下，請先加入好友再拉進去
* 邀請Discord機器人時請給足權限，如果懶得選的話直接給管理員權限也不是不行

## Author

- CA-Lee

## Contributor

- MirrorShih
- BWsix(VFLC)
- Edit Mr.
