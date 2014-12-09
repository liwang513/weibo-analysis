#encoding=utf-8
from weibo import APIClient
from re import split
import urllib,httplib
import webbrowser
import codecs
 
APP_KEY = '1371841863' #youre app key 
APP_SECRET = '48268c18e397b5fbdb286d78c5274af2' #youre app secret  
 # callback url, your must set this URL in your "my application->appInfos-> advanced  info"
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'
ACCOUNT = 'antv.isionantsphere@gmail.com'#your email address
PASSWORD = '*******'     #your pw
 
#for getting the authorize url
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
#print url

#for getting the code contained in the callback url
def get_code():
    conn = httplib.HTTPSConnection('api.weibo.com')
    postdata = urllib.urlencode({'client_id':APP_KEY,'response_type':'code','redirect_uri':CALLBACK_URL,'action':'submit','userId':ACCOUNT,'passwd':PASSWORD,'isLoginSina':0,'from':'','regCallback':'','state':'','ticket':'','withOfficalFlag':0})
    conn.request('POST','/oauth2/authorize',postdata,{'Referer':url,'Content-Type': 'application/x-www-form-urlencoded'})
    res = conn.getresponse()
    #print 'headers===========',res.getheaders()
    #print 'msg===========',res.msg
    #print 'status===========',res.status    
    #print 'reason===========',res.reason
    #print 'version===========',res.version
    location = res.getheader('location')
    #print location
    code = location.split('=')[1]
    conn.close()
    #print code
    return code

#webbrowser.open_new(url)
#raw_input()
code = get_code()
r = client.request_access_token(code)
access_token = r.access_token    # The token return by sina
expires_in = r.expires_in 
 
#print "access_token=" ,access_token, "expires_in=" ,expires_in
 
#save the access token
client.set_access_token(access_token, expires_in)
 
def weibo_1000_content(name):
    weibo_box = []
    for num in range(1,11):
        Json_text = client.statuses.user_timeline.get(screen_name=name, count=100, page=num)
        inner_text = list(Json_text.viewvalues())[5]
        for item in inner_text:
            for key in list(item.viewkeys()):
                if (key == 'text'):
                    weibo_box.append(item[key])
    return str(weibo_box).decode('unicode-escape')



