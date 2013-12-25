# pydouban
A simple python libary for douban.com that contains some basic functions 

#Install
``` 
git clone https://github.com/tianyu0915/pydouban.git
cd pydouban && python setup.py install 

or

pip install pydouban

easy_install pydouban

```

# Usage
```
from pydouban.client  import DoubanClient
client = DoubanClient('your account','your password')
if client.login():
    url,title  = client.get_topics()[0]
    client.reply_topic(url,content='hello world')

```

