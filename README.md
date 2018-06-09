# github_spider
github shiyanlou scrapy

# 用scrapy来爬取实验楼用户的所有开源项目

## 爬取内容
用xpath方法,  爬取更方便
取name, 用xpath的属性方法./a[@attr="xxx"]这样取的， 去掉换行和空格用 re_first('\n\s*(.*)')
取时间和name一样， 用xpath属性方法即可实现
