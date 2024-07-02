
#this code is owned by ayush agarwal.

from requests_html import HTMLSession
import speechtext
#https://www.google.com/search?q=weather+ranchi
#user agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36
# span id = "wob_tm"
# span id = "wob_t" for symbol under class div of class="vk_bk wob-unit"
def weather():
  s = HTMLSession()
  query = "ranchi"
  url =f'https://www.google.com/search?q=weather+ranchi'
  r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'})
  temp = r.html.find('span#wob_tm' , first= True).text
  #print(temp)
  unit = r.html.find('div.vk_bk.wob-unit span.wob_t' , first= True).text
  #print(unit)
  desc = r.html.find('span#wob_dc' , first= True).text
  #print(desc)
  return temp + " " + unit + " " + desc

