import base64
import hashlib
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class ImageScraper:
    def __init__(self, save_folder='more_thylacine/'):
        self.save_folder = save_folder
        self.existing_urls = set()
        self.counter = 0
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.options.add_argument('window-size=1200x600')
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

    def scroll_to_end(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        print('scroll done')

    def download_images(self, query, max_scrolls=10):
        self.driver.get('https://www.google.com/imghp')
        search_box = self.driver.find_element(By.NAME, 'q')
        search_box.send_keys(query)
        search_box.submit()

        for _ in range(max_scrolls):
            try:
                self.scroll_to_end()
                image_elements = self.driver.find_elements(By.CLASS_NAME, 'rg_i')
                for image in image_elements:
                    url = image.get_attribute('src')
                    if url is not None and url not in self.existing_urls:
                        self.existing_urls.add(url)
                        if url.startswith('data:image/jpeg;base64,'):
                            # The URL is a Base64-encoded image
                            data = url[len('data:image/jpeg;base64,'):]
                            img_data = base64.b64decode(data)
                            filename = self.save_folder + hashlib.md5(img_data).hexdigest() + '.jpeg'
                            try:
                                with open(filename, 'wb') as f:
                                    f.write(img_data)
                                    self.counter += 1
                            except Exception as e:
                                print(f'Error downloading {url}: {e}')
                        else:
                            # The URL is a direct URL to an image file
                            filename = self.save_folder + hashlib.md5(url.encode('utf-8')).hexdigest() + '.jpeg'
                            try:
                                with open(filename, 'wb') as f:
                                    f.write(requests.get(url).content)
                                    self.counter += 1
                            except Exception as e:
                                print(f'Error downloading {url}: {e}')
            except Exception as e:
                print(f'Error scrolling: {e}')
                break
        print(f'Downloaded {self.counter} images')
        self.driver.quit()


        
# scraper = ImageScraper(save_folder='test/')
# scraper.download_images('thylacine', max_scrolls=2)
