import bitly_api

BITLY_GENERIC_ACCESS_TOKEN = "ENTER TOKEN"

def main():
    bitly = bitly_api.Connection(access_token=BITLY_GENERIC_ACCESS_TOKEN)
    print("Enter URL :")
    full_link = input()
    short_url = bitly.shorten(full_link)
    print("Mini URL = %s" % short_url['url'])

if __name__ == '__main__':
    main()