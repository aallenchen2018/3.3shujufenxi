import requests
 
headers={
    'cookie': '_zap=a88bf5a2-74ed-4d29-a258-836b0aab1d8b; d_c0="ADCiFEZyFA-PTrrMIMJ4mtmPOhbxVW5G6U8=|1551850171"; q_c1=0bbe9a11243141798e2a43ac69b7e206|1551850172000|1551850172000; tgw_l7_route=73af20938a97f63d9b695ad561c4c10c; _xsrf=JlAOX5PcobaxYjmbLF0LgpptkXHMpkEv; capsion_ticket="2|1:0|10:1552013105|14:capsion_ticket|44:ZmI5NmE0NGI4MjBmNDIxYmE3NTNiNTc4YTBmNzA1ZGU=|9c4576760f0c35f0297eb4effff90ba25fd66b59ce4ef67e537b0863f9ea8032"; z_c0="2|1:0|10:1552013125|4:z_c0|92:Mi4xb3VKNEFnQUFBQUFBTUtJVVJuSVVEeVlBQUFCZ0FsVk5SU1Z2WFFCR2ZpSzhReFFkVjlrYnpvV3JXQkhxZXcwSDNn|7c37024c43933963497f83c7170af53a0889ad36c01ba2637f45fe04aab251a3"; unlock_ticket="ABBK0nceTgkmAAAAYAJVTU3egVyu-W47-ocRCuRe04-qaRSyFRpx7A=="; tst=r',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

}




url='https://www.zhihu.com'
r=requests.get(url,allow_redirects=False,headers=headers)

print(r.text)