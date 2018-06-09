# 用scrapy来爬取实验楼用户的所有开源项目

## 爬取内容
用xpath方法,  爬取更方便
取name, 用xpath的属性方法./a[@attr="xxx"]这样取的， 去掉换行和空格用 re_first('\n\s*(.*)')
取时间和name一样， 用xpath属性方法即可实现

## 实验楼开源地址
实验楼 ['https://github.com/shiyanlou?page=2&tab=repositories']
页数用{}来代替, start_urls方法必须写@property把他变成属性

``` python
  @property
  def start_urls(self):
    url_temp = 'https://github.com/shiyanlou?page={}&tab=repositories'
    urls =  (url_temp.format(i) for i in range(1, 5))
    return urls
```

## 爬虫结果是
``` python
  [{'name': XXX, 'update_time': XXX}]
```
