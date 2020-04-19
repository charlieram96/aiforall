# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WsSeniorprojectItem(scrapy.Item):
  Product = scrapy.Field()
  Price = scrapy.Field()
  Low_Price = scrapy.Field()
  High_Price = scrapy.Field()
  #product_sale_price_cents = scrapy.Field()
  Rating = scrapy.Field()
  Rating_Count = scrapy.Field()
  Five_Stars = scrapy.Field()
  Four_Stars = scrapy.Field()
  Three_Stars = scrapy.Field()
  Two_Stars = scrapy.Field()
  One_Star = scrapy.Field()
  Category = scrapy.Field()
  Sales_Rank = scrapy.Field() 
  Rank_Category = scrapy.Field()
  Answered_Questions = scrapy.Field()
  #Prime = scrapy.Field()
  Description_Main = scrapy.Field()
  Description_Product = scrapy.Field()
  Dimensions = scrapy.Field()
  Dimensions_Length = scrapy.Field()
  Dimensions_Width = scrapy.Field()
  Dimensions_Height = scrapy.Field()
  ASIN_Number = scrapy.Field()
  First_Listed = scrapy.Field()
  First_Listed_Formatted = scrapy.Field()
  Days_Since_First_Listed = scrapy.Field()
  Fit_As_Expected = scrapy.Field()

  #product_availability = scrapy.Field()
  #urls = scrapy.Field()
  # 