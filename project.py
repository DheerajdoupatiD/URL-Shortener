class URLShortener:
    def _init_(self):
        self.counter = 0
        self.url_mapping = {}

    def shorten_url(self, url):
        self.counter += 1
        short_code = str(self.counter)
        self.url_mapping[short_code] = url
        return f"short.url/{short_code}"  # Replace 'short.url/' with your domain

    def expand_url(self, short_code):
        if short_code in self.url_mapping:
            return self.url_mapping[short_code]
        else:
            return "URL not found."

# Example usage
url_shortener = URLShortener()

original_url = "https://mail.google.com/mail/u/0/?tab=rm&ogbl#starred/FMfcgzGsmrGgJwcsbspstTGxZCmSNFMW"
shortened_url = url_shortener.shorten_url(original_url)
print("Shortened URL:", shortened_url)

expanded_url = url_shortener.expand_url(shortened_url.split('/')[-1])
print("Expanded URL:",expanded_url)
