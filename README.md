## 1. Cào dữ liệu
### 1.1 Driver chrome

* Nhóm đã chuẩn bị 2 driver (Window/Mac) cho chrome phiên bản 102 ở đường link: https://drive.google.com/drive/folders/1PlrHcI6emL2XKbWdVk95xBuq8A5nNI7B?usp=sharing , download về thư mục `./driver_chrome/`
* Driver chrome hiện đã giải nén là giành cho Window.
* Nếu là MacOS thì giải nén file: `./driver_chrome/chromedriver_mac64.zip`
* Nếu thầy đang sử dụng chrome phiên bản khác 102 thì vào link sau để tải driver tương ứng với phiên bản chrome đang dùng: `https://chromedriver.chromium.org/downloads`
* NOTE: lưu ý không tải và sử dụng chrome phiên bản 103 (bản mới nhất tính tới thời điểm hiện tại), vì có 1 số issue liên quan đến Selenium. Link issue: `https://github.com/SeleniumHQ/selenium/issues/10799`

### 1.2 Cài đặt package

Cài đặt các package cần thiết
```
pip install -r requirements.txt
```

### 1.3 Cào dữ liệu
Chạy lệnh sau để cào dữ liệu:
```
cd crawler
python crawl_links.py
python crawl_data.py
```

## 2. Chạy file notebook (Cần cài đặt pandas, numpy, scikit-learn, eli5)
* Lưu ý:
    - Chỉ chạy code notebook ở phần 3 trở về sau

#   L a p t o p - p r i c e - p r e d i c t i o n  
 