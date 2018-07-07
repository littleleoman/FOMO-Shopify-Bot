'''

@author: yung_messiah

'''
import requests
import bs4
# import random
# import webbrowser

''' Retrieves sizes for item in stock.

    @param url: The url passed by the user pointing to the item he/she wants ''' 
def get_sizes(url):
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    #url = "https://kith.com/collections/footwear/products/nkaq0996-001"
    
    raw_HTML = requests.get(url, headers=headers)
    page = bs4.BeautifulSoup(raw_HTML.text, 'lxml')
    
    print(page.title.string)
    
    for size in page.select('option'):
        size = size.getText().split(' ')
        get_size_variant(page, size[0])
        
''' Retrieves the id associated to the item size (required to create a link). 

    @param page: Page information retrieved through requests
    @param size: Size of the item to be searched for '''
def get_size_variant(page, size):
    scripts = page.find_all("script")
    # 10 is the index for the correct script (IN CASE OF ERRORS CHECK INDEX AGAIN)
    script = scripts[10].getText()
    print("SIZE = " + size)
    
    ''' split it in this manner to store items of script separated by a new line '''
    script = script.split(';')
    ''' retrieve only the line containing size information '''
    script = script[3]
    ''' split in this manner so that each size is a different list item '''
    script = script.split('{\"id\":')
    ''' remove unwanted information in beginning of list '''
    script.remove(script[0])
    script.remove(script[0])
      
    for item in script:
        if ('public_title\":\"' + str(size)) in item:
            data = item
            data = data.split(',')
            
            retrieved_id = data[0]
            print_link(size, str(retrieved_id))
            break


''' Prints a correctly formated link which takes user straight to purchase.

    @param size: Size of the given item
    @param retrieved_id: Id associated to the item size  '''
def print_link(size, retrieved_id):
    print('[' + size + '] \t' + '\thttps://kith.com/cart/' + retrieved_id + ':1')

''' Kickstarts the entire script.

    @param url: The url pointing to the item which the user wants to buy '''
def run(url):
    get_sizes(url)
    
run("https://kith.com/collections/kith/products/kith-undershirt-3-pack-off-white-light-pink-cinder")
    
# def find_variant_script(size):  
#     ''' Loops through all the scripts on page to find correct script containing size data 
#             We uncomment the code below if we get errors in the future retrieving data from 
#             the page
#     '''
# #     for number, script in enumerate(scripts):
# #         if "variant" in script.getText():
# #             print(number, script)
# 
#     ''' Code below is responsible for running code test to see that correct data is being retrieved '''
# #   id For size 7 :2611882196999  
#     URL = input("Paste the url:")
#     headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
#     raw_HTML = requests.get(URL, headers = headers)
#     page = bs4.BeautifulSoup(raw_HTML.text, 'lxml')
#     scripts = page.find_all("script")
#     script = scripts[10].getText()
#      
#     print(page.title.string)
#     
#     ''' split it in this manner to store items of script separated by a new line '''
#     script = script.split(';')
#     ''' retrieve only the line containing size information '''
#     script = script[3]
#     ''' split in this manner so that each size is a different list item '''
#     script = script.split('{\"id\":')
#     ''' remove unwanted information in beginning of list '''
#     script.remove(script[0])
#     script.remove(script[0])
#     print(script)
#      
#      
#     for item in script:
#         if ('public_title\":\"' + str(size)) in item:
#             print("This is the item! " + item)
#             data = item
#             data = data.split(',')
#             
#             print(data)
#             retrieved_id = data[0]
#             print('[ ' + size + ' ] - ' + 'https://kith.com/cart/' + str(retrieved_id))
#             break