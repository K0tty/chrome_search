# モジュール読み込み
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# WEBブラウザの起動とChromedriverとChromeのバージョン調整
driver = webdriver.Chrome(ChromeDriverManager().install())

# 特定のURLへ移動
driver.get('http://www.google.com/') 
time.sleep(2)

# ページ上の要素の取得
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('ChromeDriver')
search_box.submit()

with open('index.html', 'w', encoding='utf-8') as f:
  f.write(res.text)
