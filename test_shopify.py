'''

@author: yung_messiah

'''
import shopify_atc

''' Unit tests for the shopify ATC bot.
    
    Tests different websites to check if bot is fully functional ''' 
class TestShopifyATC(object):
    
    # TO RUN IN TERMINAL USE pytest -q test_shopify.py WHEN IN THE FILE'S DIRECTORY
    def test_kith_one_size(self):
        assert shopify_atc.run("https://kith.com/products/7-moncler-fragment"
        + "-hiroshi-fujiwara-zaino-olive") == True
    
    def test_kith_num_size(self):
        assert shopify_atc.run("https://kith.com/collections/footwear/products/nike-air"
        + "-max-97-pure-platinum-university-red") == True
        
    def test_kith_letter_size(self):
        assert shopify_atc.run("https://kith.com/collections/kith/products/kith-undershirt"
        + "-3-pack-off-white-light-pink-cinder") == True
        
    def test_kong_one_size(self):
        assert shopify_atc.run("https://www.kongonline.co.uk/collections/new-arrivals/products/"
        + "niketechmanbagblack?variant=12179057606764") == True
    
    def test_kong_num_size(self):
        assert shopify_atc.run("https://www.kongonline.co.uk/collections/new-arrivals/products/"
        + "adidasbusentizcoreblackcoreblackwhite?variant=12178507169900") == True

    
    def test_kong_letter_size(self):
        assert shopify_atc.run("https://www.kongonline.co.uk/collections/polar/products/"
        + "polarstrokelogoteegreen?variant=12146453938284") == True
        
    def test_suede_one_size(self):
        assert shopify_atc.run("https://suede-store.com/collections/under-100-00/products/herschel"
        + "-lawson-select-backpack-664160031") == True
        
    def test_suede_num_size(self):
        assert shopify_atc.run("https://suede-store.com/collections/mens/products/nike-air-max-1"
        + "-beach-camo-875844-204") == True
        
    def test_suede_letter_size(self):
        assert shopify_atc.run("https://suede-store.com/collections/mens/products/adidas-originals"
        + "-og-adibreak-track-pants-cz0679") == True
        
    def test_urban_industry_one_size(self):
        assert shopify_atc.run("https://www.urbanindustry.co.uk/products/eastpak-bust-backpack-mp"
        + "-red") == True
        
    def test_urban_industry_num_size(self):
        assert shopify_atc.run("https://www.urbanindustry.co.uk/products/nike-air-max-98-shoes-wolf"
        + "-grey-dark-grey-total-crimson") == True
        
    def test_urban_industry_letter_size(self):
        assert shopify_atc.run("https://www.urbanindustry.co.uk/products/carhartt-wip-chase-pullover"
        + "-hoody-lakers-gold") == True
        assert True
        
    def test_nrml_one_size(self):
        assert shopify_atc.run("https://nrml.ca/products/hannesbackpackblk") == True
        
    def test_nrml_num_size(self):
        assert shopify_atc.run("https://nrml.ca/collections/recently-added/products/rs"
        + "-replicant-ozweego-f34237") == True
        
    def test_nrml_letter_size(self):
        assert shopify_atc.run("https://nrml.ca/products/maynard-camo-jacket") == True
        
    def test_blends_one_size(self):
        assert shopify_atc.run("https://www.blendsus.com//products/jansport-x-mark-gonzales"
        + "-the-gonz-super-fx-black-red-white") == True
        
    def test_blends_num_size(self):
        assert shopify_atc.run("https://www.blendsus.com/collections/mens-footwear/products/puma"
        + "-thunder-electric-white-black-mandarine-red") == True
        
    def test_blends_letter_size(self):
        assert shopify_atc.run("https://www.blendsus.com/collections/mens-apparel/products/vans"
        + "-vault-x-john-van-hamersveld-crazy-world-ss-tshirt-black") == True
        
    def test_rock_city_one_size(self):
        assert shopify_atc.run("https://rockcitykicks.com/products/puma-x-xo-backpack-puma-black"
        + "-acid-wash?variant=5601180844063") == True
        
    def test_rock_city_num_size(self):
        assert shopify_atc.run("https://rockcitykicks.com/products/wmns-nike-air-skylon-ii"
        + "-white-black-clear-emerald") == True
        
    def test_rock_city_letter_size(self):
        assert shopify_atc.run("https://rockcitykicks.com/products/born-x-raised-snooty-fox"
        + "-t-shirt-white") == True
