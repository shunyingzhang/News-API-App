import body as body
import requests
from send_email import send_email

api_key = 'yourAPIkey'

url = 'https://newsapi.org/v2/everything?'\
      'q=tesla&from=2023-02-02'\
      '&sortBy=publishedAt'\
      "&apiKey=786c6e38035d49b885fb8a379272e0fc" \
      "&language=en"


request = requests.get(url)
content = request.json()
message = "Subject: Today's news" + '\n'
for article in content['articles'][:20]:
      if article:
            message = message + article['title'] + '\n' \
                      + article['description'] + '\n' \
                      + article['url'] + 2 * '\n'

message = message.encode('utf-8')
send_email(message)