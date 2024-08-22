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



def go_to_product_and_add_to_cart(product_name,product_type='type1',product_size='1號'):
    
    # user_data_dir = 'C:\\Users\\10007212\\AppData\\Local\\Google\\Chrome\\User Data'
    chrome_options = Options()
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
    login_url = f"https://www.goopi.co/users/sign_in"
    product_url = f"https://www.goopi.co/categories/goopimade-goopi-孤僻"
    login_action="pass"
    
    if  not login_action=="pass":
        # 開啟登入網頁
        driver.get(login_url)
        print("請手動登入...")

        # 等待用戶手動登入完成並確認登入成功
        try:
            WebDriverWait(driver, 300).until(EC.url_contains("https://www.goopi.co/?type=signin&platform=facebook"))
            print("登入成功")
        except Exception as e:
            print("登入失敗或超時:", e)
            driver.quit()
            exit()
        
    # 尋找商品
    while True:

        driver.get(product_url)
        product_xpath=f"//a[contains(@class, 'quick-cart-item js-quick-cart-item') and .//div[contains(@class, 'title') and contains(text(), '{product_name}')]]/div[1]/div[1]/div"
        # 檢查商品是否存在，如果不存在則立即刷新
        try: 
            product_element=driver.find_element(By.XPATH, product_xpath)
            # product_element.click()
            driver.execute_script("arguments[0].click();", product_element)
            break
        except:
            print("商品未出現，重新加載。")
            continue
    
    # 選擇購買類型
    if product_type=='type1':

        try:
            select_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".selectpicker.js-selectpicker.form-control.form-control-sm.form-control-inline.ng-pristine.ng-untouched.ng-valid.ng-scope.ng-not-empty"))
            )
            # 使用Select類來與<select>元素互動
            select = Select(select_element)

            # 選擇尺寸，這裡以選擇 "1號" 為例
            select.select_by_visible_text(product_size)
        except:
            print("無法選擇尺寸。")
        try:
            # 定位到"立即購買"按鈕
            buy_now_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-buy-now.btn-purchase-action.btn-custom.ladda-button.form-control-inline.js-btn-main-buy-now.js-btn-show.js-btn-scroll"))
            )
            # 點擊"立即購買"按鈕
            buy_now_button.click()
        except:
            print("無法點擊立即購買按鈕。") 



    # 定位到"前往結帳"按鈕
    checkout_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-success.btn-block.btn-checkout[data-e2e-id='checkout_button']"))
    )
    # 點擊"前往結帳"按鈕
    checkout_button.click()

    # 在這裡可以繼續添加填寫結帳資訊的代碼

    insert_html_and_click_script = """
    // 找到目標<label>元素
    var targetLabel = document.querySelector('label[for="order-delivery-location-code"]');

    // 建立要新增的HTML內容
    var newContent = `
    <div class="margin-bottom-small">
        <div class="row">
        <span class="col-xs-12 col-sm-4">已選擇門市店號:</span>
        <span class="col-xs-12 col-sm-8" name="order[delivery_data][location_code]" ng-non-bindable="" translate="no">187079</span>
        </div>
        <div class="row">
        <span class="col-xs-12 col-sm-4">已選擇門市名稱:</span>
        <span class="col-xs-12 col-sm-8" name="order[delivery_data][location_name]" ng-non-bindable="" translate="no">權美門市</span>
        </div>
        <div class="row">
        <span class="col-xs-12 col-sm-4">門市地址:</span>
        <span class="col-xs-12 col-sm-8" name="order[delivery_data][store_address]" ng-non-bindable="">台中市西區美村路一段736號</span>
        </div>
    </div>
    `;

    // 將新的HTML內容插入到目標<label>元素後面一格
    targetLabel.insertAdjacentHTML('afterend', newContent);

    // 找到 收件人資料與顧客資料相同
    var targetCheckbox = document.querySelector('input[data-e2e-id="order-delivery-recipient-is-customer_checkbox"]');

    // 模擬勾選目標<input>元素
    targetCheckbox.click();

    // 找到 我同意網站服務條款及隱私權政策
    var targetButton = document.querySelector('input[data-e2e-id="checkout-policy_checkbox"]');

    // 模擬點擊目標<input>元素
targetButton.click();
    """
    #執行js填寫收件資訊
    driver.execute_script(insert_html_and_click_script)
    #送出訂單
    checkout_script = """
    // 找到 提交訂單
    var targetButton = document.querySelector('button[data-e2e-id="place-order_button"]');

    // 模擬點擊目標按鈕
    targetButton.click();
    """
    #執行js提交訂單
    # driver.execute_script(checkout_script)
    


# 使用範例

product='“LM-S01” G-Lightweight Utility Shorts - L-Gray'
# product='“BR-M3G” SOFTBOX Basic Pants - Shadow'
product_type='type1' #type1:有size type2:無size(包包類)
product_size='1號'
go_to_product_and_add_to_cart(product,product_type,product_size)


