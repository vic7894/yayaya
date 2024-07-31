#前往購物網站https://www.goopi.co/products/"商品名稱"
#輸入商品名稱後，自動前往該商品頁面，直到該商品出現為止
#自動選擇尺寸加入購物車，並前往結帳頁面
#自動填寫姓名、電話、地址等資訊，並選擇付款方式
#自動填寫信用卡資訊，並完成付款
#計算執行時間
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options



def go_to_product_and_add_to_cart(product_name):
    start = time.time()
    user_data_dir = 'C:\\Users\\10007212\\AppData\\Local\\Google\\Chrome\\User Data'
    chrome_options = Options()
    chrome_options.add_argument(f"user-data-dir={user_data_dir}")
    chrome_options.add_argument("--disable-animations")
    chrome_options.add_argument("--disable-background-networking")
    chrome_options.add_argument("--disable-backgrounding-occluded-windows")
    chrome_options.add_argument("--disable-bookmark-reordering")
    chrome_options.add_argument("--disable-boot-animation")
    chrome_options.add_argument("--disable-breakpad")
    chrome_options.add_argument("--disable-canvas-aa")
    chrome_options.add_argument("--disable-client-side-phishing-detection")
    chrome_options.add_argument("--disable-cloud-import")
    chrome_options.add_argument("--disable-component-cloud-policy")
    chrome_options.add_argument("--disable-component-update")
    chrome_options.add_argument("--disable-composited-antialiasing")
    chrome_options.add_argument("--disable-default-apps")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-device-discovery-notifications")
    chrome_options.add_argument("--disable-dinosaur-easter-egg")
    chrome_options.add_argument("--disable-domain-reliability")
    chrome_options.add_argument("--disable-features=IsolateOrigins,site-per-process,TranslateUI,PrivacySandboxSettings4")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--disable-login-animations")
    chrome_options.add_argument("--disable-login-screen-apps")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-print-preview")
    chrome_options.add_argument("--disable-renderer-backgrounding")
    chrome_options.add_argument("--disable-session-crashed-bubble")
    chrome_options.add_argument("--disable-smooth-scrolling")
    chrome_options.add_argument("--disable-suggestions-ui")
    chrome_options.add_argument("--disable-sync")
    chrome_options.add_argument("--disable-translate")
    chrome_options.add_argument("--hide-crash-restore-bubble")
    chrome_options.add_argument("--lang=zh-TW")
    chrome_options.add_argument("--no-default-browser-check")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--no-pings")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--no-service-autorun")
    chrome_options.add_argument("--password-store=basic")
    chrome_options.add_experimental_option('detach', True)

    driver = webdriver.Chrome(options=chrome_options)  # 或使用其他瀏覽器
    product_url = f"https://www.goopi.co/"
    
    while True:
        driver.get(product_url)
        
        # 檢查商品是否存在，如果不存在則立即刷新
        if not driver.find_elements(By.XPATH, f"//a[contains(@class, 'quick-cart-item js-quick-cart-item') and .//div[contains(@class, 'title') and contains(text(), '{product_name}')]]"):
            print("商品未出現，重新加載。")
            continue
        else:
        # 使用 WebDriverWait 和 expected_conditions 來等待元素出現
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, f"//a[contains(@class, 'quick-cart-item js-quick-cart-item') and .//div[contains(@class, 'title') and contains(text(), '{product_name}')]]"))).click()
            break
    
    # 選擇尺寸，這裡假設我們選擇第一個尺寸
    # 定位到 <select> 元素
    select_element = driver.find_element(By.CLASS_NAME, "js-selectpicker")
    select = Select(select_element)
    # 選擇尺寸，這裡以選擇 "2號" 為例
    select.select_by_visible_text("1號")
    
    # 加入購物車
    # wait = WebDriverWait(driver, 10)  # 等待最多10秒
    # add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="#btn-variable-buy-now"]')))
    # add_to_cart_button.click()
    buy_now_button = driver.find_element(By.CLASS_NAME, "btn-buy-now")
    buy_now_button.click()
    
    # # 前往結帳頁面，這裡假設結帳頁面的按鈕ID為"checkout-button"
    checkout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn-checkout[data-e2e-id='checkout_button']"))
    )
    checkout_button.click()

    # 在這裡可以繼續添加填寫結帳資訊的代碼
    # 注意：自動填寫個人資訊和付款資訊涉及隱私和安全問題，請確保遵守相關法律法規和網站政策。
    end = time.time()
    print(f"執行時間：{end - start} 秒")

# 使用範例
# product='“br-m3g”-softbox-basic-pants-bone'
product='T1-END.93 - “Nessie” Logo Tee'
go_to_product_and_add_to_cart(product)


