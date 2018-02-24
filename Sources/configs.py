headers1 ={
'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0" ,
'Accept':"application/json, text/javascript, */*; q=0.01",
'Accept-Language':"zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4",
'Accept-Encoding':"gzip, deflate, br",
'Referer':"https://mp.dayu.com/dashboard/stat/video?spm=a2s0i.db_index.menu.10.50b11bb77JFIka",
'Cookie':"USER_TMP=2RBJmJ5O04WKeJnAeA2lXw.oJ-FY99olXzsAGFeBeF22QDED2VX3uCtnFW6SDsc9fKuSG9GIL3_MD0EVzvbXeCob09r1_0zJSL_MKQeRzyi1RnhUng0Jp_V2dbUnQt9h6GSOgx6dlm5FoWs8y6L0CJ03SK8d1c9wN-w8VETyV6_d66aZ_pp0fvEIsjx-gdSUv983yStFdy0ciOtraD1Do68wzAuJMUU6BhZZa3nSox6KmwXv88T_OxKH9wDhfH9m49F2ZqQ26EXaoWoe6AaMMSCY1GGDyJcbe4ErugByyk750dxOGeEmj3x7nJhxfDPCacHps7EZy_RG1E2Gg851Z7ZfytG4HvvAUrpbQsk9CIpGANO1QYP2RaE1Pn9iWJ2EWiK-Kr8jW_YX0gJoWoF4RYfyvNg13QYjzBOGqz5GPt-5ozSHYMtUiqsfgrweC5UmGkA6W4mTu_sV2Fc7rmypF2fmLu3oUqIrplSjDhKrJrTNYlPlAxS2xDEAFGQZ9s1Bi98J6lEwO8GD5bO0bZ7T2B3bZIjXPvYIMPVCfaP5KJampWkEU7g231aGoXtczC_UhpoFN_cK1ifX2ZYXkmldFitHNczXw_MfecGXtiG44DM7zS7WzhCdgFpFVbZ8djOkNWPPIwJ3Wq52v9RdEPev_kRsCSfrKczOLWLEcExBwD3nBUo1EQENyJSzrS2vNNk2nNzU5H_myW4E3ae4SitDAzTonJopuZeC4oa-sTKuCjWwcpoxxUGaw23nTlYMZryZT3xPEJyn41ixD2mb-ENShqjMkycBjK6toCSTYAwdCVe8JtA0-Y5l5NGWDB6AgpHSy_taSA1P16pDeSh0bhHPUFrJ6_nxXARif_669Tu61VJwuRd0ZpEP1JvhHABam0NrN94JtxIsv6GHjpQoecX_aaj-CXQrZIg7YvKgAHQQFCa5Qayy9X6c40K6B4a_Ns_II0vnOXiD18ImXJPyv69ijDWBTs4n181YxFq3R1Tl4jYFKYoAec9UTG26ojW1fdHeGuSG7nLjOjY__VINVonGr3kF7NKkQmYlHgxzzEpT-6od4Xt29ZnWV774ICjkbt83iqn0O_UysDL8p9d5FTxEudc-0kVc6uAi5It--F7LDESuJ_kVn3HgTh-LF6oXc5_4KQLcgLtVOYC2YJAob5yt0xrS5dG3XISBw2iPCUM2eVqKE45Si1rkYKV_mlC9djrcWQIBgx1ptC6glULedHWQOoKPTjAandj8JE3MXv34UkzQpIDyZOEX8ajSyvzbjCv8nsxpas9aSsnzhx2LWy5HdtaGRfr_qSwlbhe0K0S3e0q-45XE01Qa4l0TGmg5B_OROVGUpTewtul8D4YLNU_o73YeOugkUT0LJjvt-QnN0iS1C8zBv6-3zFIa1WA9G-9vNRlTO0ZI-atniHlwZXTHIQslJx_EgR4HKW47nQVWeB1ay_tmrwj7b9SHDlS5cnS5Kd8fRgchOA6AIUtS-cfZkJagzogaOvQScz9TEQ7U9GbMceel6UBLhKGFta-Tn8_TcNX2Qp1kBi5_p_To8vjr-aK.1504238215854.86400000.NyEDdpm_QXPoVsPvf1EY4C_otoC-Nnor2FbfADA1iOg; cna=2aJNEViXkj4CAdOh+MmT1FK7; isg=Ajc3yVgPIqY3N6YqoxXfh_KUxi1BVAo3IySy2Inw44aZOEp6mM_nrWVeZK6d",
'Connection':"keep-alive",
'Host':'mp.dayu.com',
}

headers2 = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
    'Connection':'keep-alive'
}


address = '北京市海淀区上地十街10号'
my_ak = '4BNYmGY6bFkg2knNx7tbKGqZDGA9cG0c'
baidu_api_url = 'http://api.map.baidu.com/geocoder/v2/?address='+ address + '&output=json&ak=' + my_ak +'&callback=showLocation'
