# pydouban

#Install
``` 
git clone https://github.com/tianyu0915/pydouban.git
cd pydouban && python setup.py install 
```

# Useage
```
from pydouban.client  import DoubanClient
client = DoubanClient('your account','your password')
url,title  = client.get_topics()[0]
client.reply_topic(url,content='hello world')

```

