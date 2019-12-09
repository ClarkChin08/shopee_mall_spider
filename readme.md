## Brief introduction

#### Purpose

​		Crawl data of shopee mall, the location include: Indonesia, Vietnam, Thailand, Philippines, Malaysia, Singpore. There are some unkown error about Taiwan and I don't have much energy to solve it  at the moment, maybe it will be solve in the future.

#### Data

**brands**: the information of brand 

![image-20191209205056017](C:\Users\hxx\iCloudDrive\Github\shopee_mall_spider\doc\typora-user-images\image-20191209205056017.png)

**shops**: the information of shops

![image-20191209205338174](C:\Users\hxx\iCloudDrive\Github\shopee_mall_spider\doc\typora-user-images\image-20191209205338174.png)

![image-20191209205421443](C:\Users\hxx\iCloudDrive\Github\shopee_mall_spider\doc\typora-user-images\image-20191209205421443.png)

**items**: the information of item

![image-20191209205527182](C:\Users\hxx\iCloudDrive\Github\shopee_mall_spider\doc\typora-user-images\image-20191209205527182.png)

![image-20191209205633825](C:\Users\hxx\iCloudDrive\Github\shopee_mall_spider\doc\typora-user-images\image-20191209205633825.png)

![image-20191209205718388](C:\Users\hxx\iCloudDrive\Github\shopee_mall_spider\doc\typora-user-images\image-20191209205718388.png)

#### requirement

**python3**+: scrapy, pymongo, fake_useragent, requests

**MongoDB**

**Notes**:

I have tried to use a proxy to avoid IP blocking, but  Shopee does not limit the IP request.