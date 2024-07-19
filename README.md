# Max搶票機器人
MaxBot是一個免費、開放原始碼的搶票機器人。祝您搶票成功。

MaxBot is a FREE and open source bot program. Good luck getting your expected ticket.

# Download 
(搶票程式下載)

https://github.com/max32002/tixcraft_bot/releases

下載說明:
* 目前有打包的「執行檔」，只有Windows 平台，其他作業系統需要使用原始碼來執行。當然Windows 平台也可以用原始碼執行MaxBot.
* 如果你是要用「原始碼」執行MaxBot, 在透過git clone 或在github按下載原始碼的 zip檔，你的python 版本可以使用3.7 / 3.8 / 3.9 / 3.10 這4個版號。
* 如果有辦法的話，建議使用原始碼來執行MaxBot，執行上的「效率」與「相容性」的問題會較少。

# Demo 
(示範影片)

https://github.com/max32002/tixcraft_bot/blob/master/demo_video.md

# How to Use 
(如何使用教學)

* tixcraft / indievox / ticketmaster: https://max-everyday.com/2018/03/tixcraft-bot/
* kktix: https://max-everyday.com/2018/12/kktix-bot/
* FamiTicket: https://max-everyday.com/2019/01/maxbot-famiticket/
* ibon: https://max-everyday.com/2023/01/ibon-bot/
* cityline: https://max-everyday.com/2019/03/cityline-bot/
* urbtix: https://max-everyday.com/2019/02/urbtix-bot/
* hkticketing / galaxymacau: https://max-everyday.com/2023/01/hkticketing-bot/

# How to Execute Source Code 
(透過原始碼的執行方法)

透過原始碼執行MaxBot教學影片：
https://youtu.be/HpVG91j0lbI

使用原始碼的解法，第一步是先取得原始碼後，開啟 Terminal 視窗來下指令，應該是4行指令就可以了。

請參看看文章: 如何用虛擬主機搶拓元的門票，這篇文章是以虛擬主機來示範，在 Windows / macOS / Linux 平台裡的 python 操作方式幾乎相同。

詳細的文字說明: 
https://max-everyday.com/2023/11/buy-ticket-by-vm/

### Step 1: 取得source code:

<code>git clone https://github.com/max32002/tixcraft_bot.git</code>

### Step 2: 進入 clone 的資料夾: tixcraft_bot:

<code>cd tixcraft_bot </code>

### Step 3: 安裝第三方套件:

<code>python3 -m pip install -r pip-req.txt</code>

### Step 4: 執行設定介面主桯式:

<code>python3 settings.py</code>

如果不使用設定介面，直接執行主程式:

<code>python3 chrome_tixcraft.py</code>

如果不使用設定介面，直接執行主程式並套用特定的設定檔:

<code>python3 chrome_tixcraft.py --input settings.json</code>

如果遇到MaxBot 改版, 請重新操作上面4個步驟一次, 即可取得新的版本.

如果MaxBot 沒改版, 第二次要再執行的話, 使用 Step 2 + Step 4, 這2行指令, 就可以執行 MaxBot.

如果你是 ARM CPU 應該會在 Step 3 就顯示錯誤訊息,  解法:
https://github.com/max32002/tixcraft_bot/issues/82#issuecomment-1878986084

不管是 macOS 還是 Windows 預設都是沒有 git 這個指令，如果 Step 1 執行後,  沒有檔案被下載, 請先安裝 git 到你的作業系統。或是使用github 網頁裡的 Download 功能把python 腳本下載。

如果你選擇下載 github 上的 zip 檔, 在 Step 2 進入目錄的指令可能會遇到問題, 因為「直接解壓縮」後的目錄名稱並不是 tixcraft_bot 而是 tixcraft_bot-master, 你在進入的資料夾名稱, 需要調整為你實際解壓縮後的目錄名稱。

透過瀏覽器下載 github 上的 zip 檔, 在 Windows / macOS / Linux 平台, 預設的路徑在「下載」(~/Download) 的資料夾, 你在執行的 Terminal 視窗的路徑, 與你解壓縮的路徑可能不同, 直接執行上面的指令, 會無法進入到預期的資料夾內。

### Q: 取得source code後跑出來fatal: destination path 'tixcraft_bot' already exists and is not an empty directory.想問是什麼意思?

A: 執行 git clone 2次, 重覆取得 source code, 才會有這個問題, 如果 tixcraft_bot 目錄已經存在, 直接 cd tixcraft_bot 就可以了。
如果你想把已下載的刪除, 可以直把把 tixcraft_bot 目錄刪掉即可。
如果你想更新 source code, 可以重新下載, 或是先 cd tixcraft_bot 目錄後, 再執行 git pull , 可以更新 source code 為新的版本。


PS:
* 請先確定你的python 執行環境下已安裝 selenium 及相關的套件，請參考 pip-req.txt 檔案內容。
* 透過 python3 執行 settings.py 就可以有 GUI 的設定介面。
* 如果你是使用 macOS 並且執行環境沒有 python3，請 python 官方網站([https://www.python.org/downloads/](https://www.python.org/downloads/))來安裝 python3.
* 如果你是使用 Firefox, ChromeDriver 的元件是叫 geckodriver，下載點在：https://github.com/mozilla/geckodriver/releases ，與 ChromeDriver 的處理方式是一樣，如果是 mac 電腦，要在元件按右鍵開啟，做一次授權的動作，mac 有2個版本，-macos.tar.gz 與 -macos-aarch64.tar.gz ，如果是 intel CPU 的版本，請服用前面沒有 aarch64 的版本。

PS：搶票程式可以多開chrome瀏覽器，如果你電腦效能高。

PS：「掛機模式」的選項，指人不需要在電腦前，驗證碼會猜到對為止。

### Q: 是只有使用虛擬主機才要用程式碼執行搶票機器人嗎？

A: 除了 Window 有打包的執行檔之外, macOS / Linux 只能使用原始碼來執行, 當然 Windows 也可以用原始碼來執行.

# File Description
(檔案說明)
* chrome_tixcraft.py : 搶票機器人主程式, 用來自動化網頁的操作。
* config_launcher.py : 設定檔管理, 方便對多個設定檔案搶票。
* kktix_status.py : kktix 售票狀態監控，可以在有票時提發出提醒。
* settings.py : 編輯 settings.json 的 GUI 介面。提供圖片OCR功能給chrome擴充功能。支援定時啟用/停用MaxBot。

# Introduce the Implement 
(實作方法)

https://stackoverflow.max-everyday.com/2018/03/selenium-chrome-webdriver/

# Execute Suggestion 
(搶票建議)

please run this source code with high performance hardware computer and high speed + stable network.

門票的「限量」是很殘酷的，建議不要用破舊的電腦或連線不穩的手機網路來搶票，因為只要比別人慢個 0.1 秒，票可能就沒了。為了要搶到限量的票真心建議去一下網咖或找一個網路連線穩定且快的地方並使用硬體不差的電腦來搶票。

# TODO about Cpatcha 
(關於驗證碼)

目前自動輸入驗證碼用的元件是:

https://github.com/sml2h3/ddddocr

附註：
* macOS 新的電腦 arm 系列, 暫時沒有提供自動輸入驗證碼功能, 使用上的限制和 ddddocr 相同. 暫時的解法是透過Rosetta來模擬 Intel CPU 環境. 請參考: https://github.com/max32002/tixcraft_bot/issues/82
* macOS 舊款intel CPU 的電腦裡的 python 版本要降到低於等於 3.9版 或 3.10版, 例如:
https://www.python.org/downloads/release/python-31011/
* 猜測驗證碼時比較容易出錯的是字英 f 和 t，還有 q 和 g, v 和 u 還有 w.

想自動輸入驗證碼，可以參考看看：實作基於CNN的台鐵訂票驗證碼辨識以及透過模仿及資料增強的訓練集產生器 (Simple captcha solver based on CNN and a training set generator by imitating the style of captcha and data augmentation)

https://github.com/JasonLiTW/simple-railway-captcha-solver

# Common Problems
(搶票常見問題整理)

詳全文：https://max-everyday.com/2023/02/common-problem-when-you-buy-ticket/

## 整理大家在搶票時常遇到的問題：
* 使用搶票程式有違法嗎？
* 沒講清楚成功後的報酬
* 買到太多票
* 如何處理多的票？
* 使用搶票程式會讓自己的帳號被鎖住嗎？
* 如何恢復拓元的「購票權限」？
* 網頁刷新速度有推薦幾秒刷新一次嗎？
* 拓元的搶票，要多少的網路頻寬才夠？
* 使用VPN/代理伺服器(Proxy)來搶票會有用嗎？
* 同一個IP短時間重試被系統視為惡意程式而封鎖怎麼辦？
* Firefox和chrome搶票上有差距嗎？我看大家基本上都用chrome 很少用Firefox.
* 為什麼要設計搶票的機制？
* 為什麼網頁會有驗證碼？
* 你的硬體設備該不該升級？
* 想組一台新的電腦，是不是可以給我一些建議呢？

# Extension Privacy 
(MaxBot Plus擴充功能隱私權政策)

## 產品如何收集、使用及分享使用者資料

* 擴充取得會取得特定網頁內容, 並且自動輸入張數。
* 擴充功能會移除特定網頁內容裡已售完的網頁區塊。
* 擴充功能會取得特定網址資訊, 並置換為下一個新的網址。
* 擴充取得會取得特定網頁內容, 判斷為需要重新整理時, 自動刷新頁面。

## 使用者資料的所有分享對象。

* 擴充功能沒有分享使用者資料。

## 擴充功能主要功能：

* 特定的訂票網頁內容, 並且自動輸入張數。
* 移除特定的訂票網頁內容裡已售完的網頁區塊。
* 特定的訂票網址, 自動置換為下一步的新網址。
* 當訂票網頁內容已經無票或沒有符合的關鍵字時, 自動刷新網頁。
* 特定網頁支援驗證碼功能, 需要同時開啟 MaxBot 主程式。

# Supporting the Project 
(贊助Max)

如果這個項目對您有幫助，不妨請作者我喝杯咖啡 ：）

## 目前支援的贊助方式：
* 台灣的ATM匯款: 中國信託 (代碼：822) 帳號：071512949756
* 7-11 ATM的無卡存款
* 街口支付： 901643378
* 悠遊付
* PayPal： weng.32002@gmail.com
* 支付寶: 13717075071

詳細的圖文贊助教學如下： https://max-everyday.com/about/#donate
