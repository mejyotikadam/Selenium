from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains  import ActionChains
def download():
    urllib.urlretrieve(m, "images/imgOUI_"+unique_filename+".png")
    im = Image.open("images/imgOUI_"+unique_filename+".png")
    out = im.resize((int(ExtractResize), int(ExtractResize2)))
    out.save("images/ImgComplete_"+unique_filename+".png")

def main():
    co = webdriver.ChromeOptions()
    co.add_argument("--user-data-dir=C:\Users\Marshall\AppData\Local\Google\Chrome\User Data\Default")
    browser = webdriver.Chrome(chrome_options = co) 
    browser.get("http://*/")
    browser.find_element_by_id('SubmitButton').click()
    #----------Move iframe-------
    try:
        wait(browser, 20).until(EC.frame_to_be_available_and_switch_to_it(browser.find_element_by_xpath('//iframe[contains(@src, "google.com/recaptcha")]')))
    except:
        print("error")

    [...]
    while True:

        [...]
        link = wait(browser, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//img[contains(@src, "https://www.google.com/recaptcha/api2/payload?")]')))
        listLink = [] 
        for k in link:
            m = k.get_attribute('src')
            if m in listLink:
                print("Already added")
            else:
            listLink.insert(0, m)
            test = k.value_of_css_property("height") 
            test2 = k.value_of_css_property("width")
            ExtractResize = test.replace('px', '')
            ExtractResize2 = test2.replace('px', '')

            unique_filename = str(uuid.uuid4())
            download() 

            dim = wait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@style, "width")]'))).get_attribute('style')
            int1, int2 = re.findall(r'\d+', dim)
            subprocess.check_call("cut.py", shell=True) #Here, i want execute my other script python

if __name__ == "__main__":
   main()