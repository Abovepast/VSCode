from urllib import request
url='https://zhihu.com/hot/'
headers={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9,ru;q=0.8,en;q=0.7',
    'Cookie':'_zap=01fc13eb-044e-46cd-a02b-6872318ca641; d_c0=AGATrrNPVRePTjxsMbYYHe8QZuKzsrFEKI0=|1693642138; YD00517437729195%3AWM_TID=72oiRugv0z5AVEAUBBfQ3GcyAIGr17Xp; l_n_c=1; l_cap_id="NzI0Y2I0M2M2MjYxNDQ1ZmFlYmI4MjlkZWUzOGJlODM=|1694618673|1dc65233802f7dfc7aeb1456833fdde6000087b0"; r_cap_id="ZGRmOGI3YWMyMzliNGY5Y2IwOTEwZTE5YmQyNTNlMjc=|1694618673|5426ddaa560f690265a3984f5d67c1a4e8bc7f10"; cap_id="NmZkYzg4ODNkNTBjNGM2ZTkzMTZhM2U3NDI2OTZjZWE=|1694618673|983ba287ef9348a06d6fc01d3a6b3ad98486ac4b"; n_c=1; _xsrf=OmJlHrjH2wAn3pXHOieIPRVXLLsZwEy8; captcha_session_v2=2|1:0|10:1694618680|18:captcha_session_v2|88:a1k1enptRnhXTkhtMFNrQUwwaDdWOHFTLzFxWTdNdUNYOVd1RStkV0hZRVRwMW5nWWI1NWdRUi83ZVZwYXRKbA==|af3b9ec7b76c947b98a054511cf73f2bca84d099a8d364ce4d7b5c43ccaaba0f; SESSIONID=YYlkDmwaqZrUIAuSRL1VF8XSiUYDAwXdA4uhHdLSHSL; JOID=UloUC0vLfBXuckC2UMJexmXGB-FGkCZwjTYvwji6JGSyMwHBAPKiFYNwQbxR2Yds1oCRfqJihrax5HHDcKiv4ok=; osd=UVsRAE_IfRDldkO3VclaxWTDDOVFkSN7iTUuxzO-J2W3OAXCAfepEYBxRLdV2oZp3YSSf6dpgrWw4XrHc6mq6Y0=; __snaker__id=AxQ7ychw98GEjulO; gdxidpyhxdE=iV9C40QEwrnaxqRnPEp2mlq4%5CURxSj4OJeVs%2B%2FfMPXbbRkOawGS4w8pnlc1Mkt2YxtOycTf6Ef%5CnXfXPmQhcebPDla%2F9bcXrMLbr05uLWhlAn%2BI%5CmssMNKk7%2FDJ9%5C%5C00Ig%2F4rCVDG8sQNad74A%2BdDUP5nwgBLjCGAjo%2Br3Ykl%2FGBLC8O%3A1694619582361; YD00517437729195%3AWM_NI=BTwwVkc2BGd5%2Fpb2m7X7Sc6TLvg%2B%2BEqfIzA8OV05J7lnIuSO5S27aoTbTEuGBBnvRwXn2%2Bz0pzGED1wW1nXeRxuhqzoB9OK9q0qcOc5QQICIEnlXvRaz8EloTRdIm2TMaGY%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eeb0e56ebabdfe85bb62a8968fa2c54a968a8e87c8679a8dbfb5d7438c89acaeea2af0fea7c3b92a828cb998d561a1ee8ea8e73fedb0aed3f03d9ce99d84b56090aaa9ccaa4fb3ba879bc4348d8a00d6c93db0b28796d245f78dfed8e46598be9ca6f84d829ea297d17d9cb2feccf93cb4a689a6c73bb589ff8fdb6f92a8bb89f472ad9ef7b0ca33b3f0bf84ce69f78f9faac24387b2a4b9f55aa3a6f8a6ef65988eacaaf03a9893afa8dc37e2a3; z_c0=2|1:0|10:1694618722|4:z_c0|92:Mi4xaFI3bUN3QUFBQUFBWUJPdXMwOVZGeVlBQUFCZ0FsVk5ZaUx2WlFCaGZYbWlMV1ZTTmVwdFkzT2hybDNQNDBJS09n|2629f0c64379290dc8d9a239fdf118b55b443f07ba9c8a23a7bf59c948444fc8; KLBRSID=031b5396d5ab406499e2ac6fe1bb1a43|1694618722|1694618673',
    'Referer':'https://www.zhihu.com/signin?next=%2F',
    'Sec-Ch-Ua':'"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':'"Windows"',
    'Sec-Fetch-Dest':'document',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-Site':'same-origin',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
req=request.Request(url=url,headers=headers)
response=request.urlopen(req)
print(response.read().decode('gbk'))