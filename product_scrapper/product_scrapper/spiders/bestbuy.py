from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from product_scrapper.items import ProductItem

def complete_url(string):
    """Return complete url"""
    return "http://www.bestbuy.ca/" + string
    
def get_until_para(title):
    new_title = ''
    desc = ''
    
    splitted_text = title.split('(')
    new_title = splitted_text[0]
    desc = splitted_text[1]
    new_desc = desc.replace(')', "")
    
    return (new_title, new_desc)
        
    

class BestBuy(BaseSpider):
    name = "bestbuy"
    allowed_domains = ["bestbuy.ca"]
    

    
    def start_requests(self):
        
        #Laptop Computers and Macbooks
        
        #Laptops
        for i in range(1,4):
            yield Request("http://www.bestbuy.ca/en-CA/category/laptops/36711.aspx?type=product&page=%d" % i, meta={'category': 1, 'subcategory': 1}, callback=self.parse)
        
        #Ultrabooks
        yield Request("http://www.bestbuy.ca/en-CA/category/ultrabooks/31678.aspx?path=fe884ba670fbf11da7209f60d231ea97en01", meta={'category': 1 , 'subcategory': 2}, callback=self.parse)
    
    
        #Chromebooks
        yield Request("http://www.bestbuy.ca/en-CA/category/chromebooks/33933.aspx?path=718c5ddc1b8a59855669b35ab04b2a20en01", meta={'category': 1 , 'subcategory': 3}, callback=self.parse)
    
    
        #Gaming Laptops
        yield Request("http://www.bestbuy.ca/en-CA/category/gaming-laptops/36712.aspx?path=373f19819022a3682214f3ab1eb3179fen01", meta={'category': 1 , 'subcategory': 4}, callback=self.parse)
        
        #Macbook Pro
        yield Request("http://www.bestbuy.ca/en-CA/category/apple-macbook-pro/26225.aspx?path=4f49cf0de6e8d56ebed17b05a782d681en01", meta={'category': 4 , 'subcategory': 5}, callback=self.parse)
        
        #Macbook Air
        yield Request("http://www.bestbuy.ca/en-CA/category/apple-macbook-air/26224.aspx?path=e9d37841b35fb793b85b302bb46e2d67en01", meta={'category': 4 , 'subcategory': 6}, callback=self.parse)
        
        #Tablets
        
        #Apple IPAD
        for i in range(1,3):
            yield Request("http://www.bestbuy.ca/en-CA/category/apple-ipads/29059.aspx?type=product&page=%d" % i, meta={'category': 2 , 'subcategory': 7}, callback=self.parse)
        
        #Android Tablets
        for i in range(1,4):
            yield Request("http://www.bestbuy.ca/en-CA/category/android-tablets/20356.aspx?type=product&page=%d" % i, meta={'category': 2 , 'subcategory': 8}, callback=self.parse)
        
        #Windows Tablets
        yield Request("http://www.bestbuy.ca/en-CA/category/windows-8-tablets/31040.aspx?path=b9391d439de4616a2eb60e2567176d38en01", meta={'category': 2 , 'subcategory': 9}, callback=self.parse)
        
        #Desktop Computers
        
        #Desktop Computers
        for i in range(1,3):
            yield Request("http://www.bestbuy.ca/en-CA/category/everyday-computing/20217.aspx?type=product&page=%d" % i, meta={'category': 3 , 'subcategory': 10}, callback=self.parse)
        
        #Gaming Desktops
        for i in range(1,3):
            yield Request("http://www.bestbuy.ca/en-CA/category/performance-gaming-computers/30441.aspx?type=product&page=%d" % i, meta={'category': 3 , 'subcategory': 11}, callback=self.parse)
        
        #All-in One Computers
        yield Request("http://www.bestbuy.ca/en-CA/category/all-in-one-computers/26199.aspx?path=08f4922b80475c7e9a815b5e7748711cen01", meta={'category': 3 , 'subcategory': 12}, callback=self.parse)
        
        #Mini Pcs
        yield Request("http://www.bestbuy.ca/en-CA/category/mini-pcs/30482.aspx?path=eb6575e4b24c25409b3cd4a09bc9fc63en01", meta={'category': 3 , 'subcategory': 13}, callback=self.parse)
        
        yield Request("http://www.bestbuy.ca/en-CA/category/barebone-pcs/32291.aspx?path=d7e1172d289e796672964200f960fc0fen01", meta={'category': 3 , 'subcategory': 13}, callback=self.parse)
        
        #Refurbished Desktop Computers
        yield Request("http://www.bestbuy.ca/en-CA/category/barebone-pcs/32291.aspx?path=d7e1172d289e796672964200f960fc0fen01", meta={'category': 3 , 'subcategory': 14}, callback=self.parse)
        
        #IMac
        yield Request("http://www.bestbuy.ca/en-CA/category/apple-imac/22154.aspx?path=1eae01f35d1328a6eeac74d0238fc125en01", meta={'category': 3 , 'subcategory': 15}, callback=self.parse)
        
        #MacPro
        yield Request("http://www.bestbuy.ca/en-CA/category/apple-mac-pro/26656.aspx?path=21b7c3cf1d7b766b50839bfbf4c6c809en01", meta={'category': 3 , 'subcategory': 16}, callback=self.parse)
        
        #MacMini
        yield Request("http://www.bestbuy.ca/en-CA/category/apple-mac-mini/26226.aspx?path=e8185772ee051fec3ab848ebca54b494en01", meta={'category': 3 , 'subcategory': 17}, callback=self.parse)
        
        
        
        
        
        
        
        
        
        
        
        
    
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//div[@id="ctl00_CP_ctl00_ctl00_ProductSearchResultListing_SearchProductListing"]')
        
        urls = []

        for site in sites:
            urls = site.select("//div[contains(@class,'prod-image')]/*[1]/@href").extract()
            
        for url in urls:
            yield Request(complete_url(url), meta= {'category': response.meta["category"], 'subcategory': response.meta["subcategory"]}, callback=self.parse_detail_page)
           
            
    def parse_detail_page(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//div[@id="page"]')
        items = []
        
        for site in sites:
            item = ProductItem()
            title = site.select('//*[@id="ctl00_CP_ctl00_PD_lblProductTitle"]/text()').extract()
            price = site.select('(//*[@class="amount"])[1]/text()').extract()
            img = site.select('(//*[@id="ctl00_CP_ctl00_PD_PI_IP"])[1]/@src').extract()
               
                 
            item['title'], item['description'] = get_until_para(title[0])
            item["url"] = response.url
            item["img"] = complete_url(img[0])
            item["price"] = price[0]
            item["category"] = response.meta["category"]
            item["subcategory"] = response.meta["subcategory"]
            
            items.append(item)

            
        return items

            
            
       
