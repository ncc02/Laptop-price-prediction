from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import os 

# Khởi tạo trình duyệt
s = Service('driver_chrome/chromedriver.exe')
driver = webdriver.Chrome(service=s)
_path = '02 - Dự đoán giá laptop/raw data/test/'
driver.get("https://www.chotot.com/mua-ban-laptop")
time.sleep(0.5)

# Click button để tắt modal thông báo đăng tin trong trang 
try:
    close_button = driver.find_element(By.CSS_SELECTOR,'.aw__s1k4y3yn')
    if close_button.is_displayed(): 
        close_button.click()
        time.sleep(0.5)
except NoSuchElementException:
    pass

# Đọc tất cả các dòng trong file links.txt
links = []
with open(_path + 'links.txt', 'r') as file:
    links = file.readlines()

# Hàm get value 
def find_value_by_itemprop(driver, itemprop):
    try:
        element = driver.find_element(By.CSS_SELECTOR, f'span.AdParam_adParamValue__IfaYa[itemprop="{itemprop}"]')
        return element.text
    except:
        return None

list_laptop = []

# Lặp qua các link trong file links.txt
link_start = 0
link_end = 10
for link in links[link_start:link_end]:

    # Truy cập đến sản phẩm tương ứng với link 
    driver.get(link.strip()) 

    # Lấy dữ liệu các đặc tính của sản phẩm
    ProductName = None 
    try:
        ProductName = driver.find_element(By.CSS_SELECTOR, '.AdDecription_adTitle__AG9r4').text
    except:
        pass
    Price = None 
    try:
        Price = driver.find_element(By.CSS_SELECTOR, 'span[itemprop="price"]').text
    except:
        pass
    PcBrand = find_value_by_itemprop(driver,'pc_brand') 
    PcModel = find_value_by_itemprop(driver,'pc_model') 
    EltCondition = find_value_by_itemprop(driver,'elt_condition') 
    EltWarranty = find_value_by_itemprop(driver,'elt_warranty') 
    LaptopScreenSize = find_value_by_itemprop(driver,'laptop_screen_size') 
    PcCpu = find_value_by_itemprop(driver,'pc_cpu') 
    PcRam = find_value_by_itemprop(driver,'pc_ram') 
    PcVga = find_value_by_itemprop(driver,'pc_vga') 
    PcDriveCapacity = find_value_by_itemprop(driver,'pc_drive_capacity') 
    EltOrigin = find_value_by_itemprop(driver,'elt_origin') 
    PcDriveType = find_value_by_itemprop(driver,'pc_drive_type') 
    Address = None 
    try:
        Address = driver.find_element(By.CSS_SELECTOR, '.media-body.media-middle.AdParam_address__5wp1F > span').text
    except:
        pass
    NameShop = None 
    try:
        NameShop = driver.find_element(By.CSS_SELECTOR, '.SellerProfile_nameDiv__sjPxP > b').text
    except:
        pass
    # Tìm thấy link của shop hoặc cá nhân rồi click vào để đi đến đó 
    try:
        link_shop = driver.find_element(By.CSS_SELECTOR, '.SellerProfile_inforWrapper__KXg71 > a')
        driver.get(link_shop.get_attribute('href'))
    except:
        pass
    # Cửa hàng 
    ShopRating = None 
    try:
        ShopRating = driver.find_element(By.CSS_SELECTOR, '.flex.items-center.justify-center.gap-3 > .text-2xl.font-bold').text
    except:
        pass

    Comments = None 
    try:
        Comments = driver.find_element(By.CSS_SELECTOR, '.flex.items-center.gap-2.px-3 .text-darkblue-2').text
    except:
        pass
    # Cá nhân (Nếu không phải cửa hàng thì là cá nhân)
    if(ShopRating == None):
        try:
            ShopRating = driver.find_element(By.CSS_SELECTOR, '.ratingInfo.r8rxioc .rymcx98').text
        except:
            pass
    if(Comments == None): 
        try:
            Comments = driver.find_element(By.CSS_SELECTOR, '.ratingInfo.r8rxioc > a').text
        except:
            pass
    list_laptop.append([ProductName,Price,PcBrand,PcModel,EltCondition,EltWarranty,LaptopScreenSize,PcCpu,PcRam,PcVga,PcDriveCapacity,EltOrigin,PcDriveType,Address,NameShop,ShopRating,Comments])

# Đóng trình duyệt
driver.quit()

# Ghi thông tin các laptop vào file laptop.csv (test/official)
df_laptop = pd.DataFrame(list_laptop, columns=['ProductName', 'Price', 'PcBrand', 'PcModel', 'EltCondition', 'EltWarranty', 'LaptopScreenSize', 'PcCpu', 'PcRam', 'PcVga', 'PcDriveCapacity', 'EltOrigin', 'PcDriveType', 'Address','NameShop','ShopRating','Comments'])
import os.path
import pandas as pd

if os.path.isfile(_path + 'laptop.csv'):
    df_laptop = pd.read_csv(_path + 'laptop.csv')
else:
    df_laptop = pd.DataFrame(columns=['ProductName', 'Price', 'PcBrand', 'PcModel', 'EltCondition', 'EltWarranty', 'LaptopScreenSize', 'PcCpu', 'PcRam', 'PcVga', 'PcDriveCapacity', 'EltOrigin', 'PcDriveType', 'Address','NameShop','ShopRating','Comments'])
df_new = pd.DataFrame(list_laptop, columns=['ProductName', 'Price', 'PcBrand', 'PcModel', 'EltCondition', 'EltWarranty', 'LaptopScreenSize', 'PcCpu', 'PcRam', 'PcVga', 'PcDriveCapacity', 'EltOrigin', 'PcDriveType', 'Address','NameShop','ShopRating','Comments'])
if not os.path.isfile(_path + 'laptop.csv') or df_laptop.columns.to_list() != df_new.columns.to_list():
    df_new.to_csv(_path + 'laptop.csv', index=False, mode='a', header=True, encoding='utf-8-sig')
else:
    df_new.to_csv(_path + 'laptop.csv', index=False, mode='a', header=False, encoding='utf-8-sig')

