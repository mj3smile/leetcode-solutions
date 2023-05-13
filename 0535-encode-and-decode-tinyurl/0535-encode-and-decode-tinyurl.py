class Codec:
    def __init__(self):
        self.index = dict()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        baseUrl = 'https://tinyurl.com/'
        shortUrl = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        while baseUrl + shortUrl in self.index:
            shortUrl = ''.join(random.choices(string.ascii_letters + string.digits, k=N))
        self.index[baseUrl + shortUrl] = longUrl
        return baseUrl + shortUrl
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.index[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))