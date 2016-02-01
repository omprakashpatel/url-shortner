# url-shortner
URL Shortner With Python, Flask, Mongodb

# URL shortner API
http://localhost:8000/shortner
METHOD: POST
DATA: url => url, for shortning

# Redirect Short URL to Original Long URL
[short_url]
METHOD: GET

# Short URL details
[short_url]/desc
ex: http://localhost:8000/[short_string]/desc
method: GET


# Search Key in URL
http://localhost:8000/search?word=[keyword]
Method: GET
Arguments: 'word'
