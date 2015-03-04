import urllib, http.cookiejar, re, html.parser

HEADERS = {'User-Agent':
'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0'}

class VKError(Exception):
    pass

def vk_login(email, password):
    cookie = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    urllib.request.install_opener(opener)
    ip_h = re.findall('ip_h=(.+?)\&',
                      urllib.parse.quote_from_bytes(urllib.request.urlopen("http://vk.com").read()))
    data = {"act":"login",
            "ip_h":ip_h,
            "_origin":"http://vk.com",
            "email":email,
            "pass":password}
    sendData = urllib.parse.urlencode(data)
    req = urllib.request.Request("http://login.vk.com", urllib.parse.unquote_to_bytes(sendData), HEADERS)
    urllib.request.urlopen(req)
    print ('Getting user ID')
    page = urllib.request.urlopen("http://vk.com/friends").read()
    try:
        userid = re.findall('write[0-9]+',
                            urllib.parse.quote_from_bytes(page))
        print (userid)
    except Exception:
        raise VKError("Login failed!")
    return userid

vk_login('loginnnnn', 'paasssssss')

