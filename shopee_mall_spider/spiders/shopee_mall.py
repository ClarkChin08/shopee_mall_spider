# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.selector import Selector
import math
import datetime

class ShopeeMallSpider(scrapy.Spider):
	name = 'shopee_mall'
	
	start_urls = [
		'https://shopee.com.my/api/v2/brand_lists/get',
		# 'https://shopee.co.id/api/v2/brand_lists/get',
		# 'https://shopee.tw/api/v2/brand_lists/get',
		# 'https://shopee.vn/api/v2/brand_lists/get',
		# 'https://shopee.co.th/api/v2/brand_lists/get',
		# 'https://shopee.ph/api/v2/brand_lists/get',
		# 'https://shopee.sg/api/v2/brand_lists/get',
	]
	

	
	def parse(self, response):
		data = json.loads(response.text).get('data')
		shopids = []
		for k, item in data.items():
			shopid = item.get('shopid')
			item['crawl_country'] = 'shopee_'+response.url.split('/')[2].replace('.', '_')
			item['crawl_data_type'] = 'brands'
			item['crawl_date'] = datetime.datetime.now().timestamp()
			yield item
			if shopid not in shopids:
				shopids.append(shopid)
				username = item.get('username')
				tmp = response.url.split('/')
				prefix = tmp[0]+"//"+tmp[2]
				url = f'{prefix}/api/v2/shop/get?username='+username
				yield scrapy.Request(url, callback=self.parse_shop_info, meta={'username':username})
#                
				
				
				
				
	def parse_shop_info(self, response):
		item = json.loads(response.text).get("data")
		
		tmp = response.url.split('/')
		prefix = tmp[0]+"//"+tmp[2]
		shopid = item.get('shopid')
		username = item.get('account').get('username')
		item_count = item.get('item_count')
		page_count = math.ceil(item_count/30)
		for i in range(0,page_count+1):
			url = f'{prefix}/api/v2/search_items/?by=pop&limit=30&match_id={shopid}&newest={i*30}&order=desc&page_type=shop&version=2'
			yield scrapy.Request(url, callback=self.parse_shop_item, meta={'username': username, 'page':i})

		item['crawl_country'] = 'shopee_'+response.url.split('/')[2].replace('.', '_')
		item['crawl_data_type'] = 'shop_info'
		item['crawl_date'] = datetime.datetime.now().timestamp()
		yield item
					
			
	def parse_shop_item(self, response):
		tmp = response.url.split('/')
		prefix = tmp[0]+"//"+tmp[2]
		items = json.loads(response.text).get('items')
		for item in items:
			itemid = item.get('itemid')
			shopid = item.get('shopid')
			url = f'{prefix}/api/v2/item/get?itemid={itemid}&shopid={shopid}'
			yield scrapy.Request(url, callback=self.parse_item)

			# item['crawl_country'] = 'shopee.'+response.url.split('/')[2]
			# item['crawl_data_type'] = 'item_info'
			# item['crawl_date'] = datetime.datetime.now().timestamp()
			# yield item
	
	def parse_item(self, response):
		item = json.loads(response.text).get('item')

		item['crawl_country'] = 'shopee_'+response.url.split('/')[2].replace('.', '_')
		item['crawl_data_type'] = 'item_info'
		item['crawl_date'] = datetime.datetime.now().timestamp()
		yield item

