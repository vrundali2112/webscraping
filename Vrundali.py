import urllib
import urllib.request 
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt
import csv

filename = "Internpro19.csv"
f= open(filename,"a")
headers = "COLLEGE NAME , LOCATION , CONTACT , EMAIL , WEBSITE , TPO_NAME , TPO_CONTACT \n" 
f.write(headers)
 
college_id = [4649,4653,5003,5006,5007,5008,5009,5010,5103,5104,5105,5106,5107,5108,5109,5121,5124,5125,5139,5151,5160,5161,5162,5164,
              5167,5168,5169,5170,5171,5172,5173,5176,5177,5179,5181,5182,5183,5184,5220,5221,5222,5223,5224,5225,5226,5227,5228,5229,
              5230,5231,5232,5235,5237,5238,5239,5240,5241,5243,5245,5246,5247,5248,5249,5250,5251,5252,5253,5254,5256,5257,5258,5259,
              5260,5261,5263,5322,5330,5331,5354,5356,5357,5358,5360,5361,5362,5363,5365,5366,5367,5368,5369,5370,5371,5372,5373,5374,
              5375,5376,5385,5387,5389,5390,5395,5396,5399,5401,5402,5404,5408,5409,5411,5413,5414,5415,5417,5418,5419,5420,5423,5431,
              5433,5434,5449,6004,6006,6005,6007,6010,6011,6013,6014,6015,6016,6017,6018,6019,6020,6023,6028,6138,6139,6141,6144,6145,
              6146,6147,6148,6149,6151,6155,6156,6160,6175,6176,6177,6178,6179,6182,6183,6184,6185,6187,6206,6207,6214,6215,6217,6219,
              6220,6222,6223,6225,6250,6259,6265,6266,6267,6268,6269,6270,6271,6272,6273,6274,6275,6276,6277,6278,6281,6282,6283,6284,
              6285,6289,6288,6293,6298,6303,6302,6304,6305,6307,6308,6310,6311,6312,6313,6315,6317,6318,6319,6320,6321,6322,6323,6324,
              6325,6326,6402,6403,6404,6405,6406,6407,6408,6409,6410,6414,6415,6416,6417,6418,6419,6420,6421,6422,6423,6425,6427,6428,
              6429,6430,6431,6432,6433,6434,6435,6436,6437,6439,6441,6442,6443,6444,6445,6446,6447,6448,6449,6451,6452,6455,6456,6457,
              6458,6462,6463,6464,6465,6466,6467,6469,6470,6471,6472,6473,6474,6475,6476,6526,6544,6545,6602,6609,6618,6620,6621,6622,
              6625,6634,6640,6643,6649,6712,6713,6714,6715,6716,6720,6721,6722,6723,6724,6725,6728,6729,6731,6732,6754,6755,6756,6757,
              6758,6759,6760,6762,6766,6767,6768,6769,6770,6771,6772,6780,6781,6782,6786,6787,6794,6795,6796,6797,6802,6800,6799,6808,
              6809,6810,6811,6815,6814,6816,6817,6822,6824,6828,6830,6834,6839,6878,6881,6888,6901]
print(len(college_id))
url = "http://dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode={}"
for i in range(0,353):
    url_1 = url.format(college_id[i])
    html = urllib.request.urlopen(url_1).read()
    soup = BeautifulSoup(html,'lxml')
    table = soup.find('div',id = 'ContentTable1')
    college_name = soup.find('span',id = 'ctl00_ContentPlaceHolder1_lblInstituteNameEnglish')
    co = college_name.text
    location = soup.find('span',id = 'ctl00_ContentPlaceHolder1_lblRegion')
    lo = location.text
    contact_number = soup.find('span',id = 'ctl00_ContentPlaceHolder1_lblResidentialPhoneNo')
    cn = contact_number.text
    email = soup.find('span',id = 'ctl00_ContentPlaceHolder1_lblEMailAddress')
    ee = email.text
    website_link = soup.find('span',id = 'ctl00_ContentPlaceHolder1_lblWebAddress')
    wl = website_link.text
    tpo_name = soup.find('span',id = 'ctl00_ContentPlaceHolder1_lblRegistrarNameEnglish')
    tn = tpo_name.text
    tpo_no = soup.find('span',id = 'ctl00_ContentPlaceHolder1_lblOfficePhoneNo')
    tc = tpo_no.text
    print("college: ",college_name.text)
    print("contact: ",contact_number.text)
    print("location: ",location.text)
    print("email: ",email.text)
    print("website: ",website_link.text)  
    print("TPO name: ",tpo_name.text)
    print("tpo contact: ",tpo_no.text)
    
    f.write(co.replace(",","|") +","+ lo +"," + cn + "," + ee.replace(",","|") + "," +wl+ "," + tn + "," + tc +"\n")
f.close()



filename = "Internpro19.csv"
f= open(filename,"w")
headers = "COLLEGE NAME , LOCATION , CONTACT , EMAIL , WEBSITE , TPO_NAME , TPO_CONTACT \n" 
f.write(headers)


college_id = [1002,1006,1007,1008,1009,1010,1011,1012,1015,1101,1105,1107,1108,1114,1116,1117,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,
              1129,1130,1139,1140,1141,1142,1144,1147,1148,1151,1152,1153,1168,1180,1182,1244,1245,1246,1247,1249,1250,1251,1265,1266,1267,1268,
              1269,1275,1276,1277,1278,2008,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2113,2114,2116,2126,2127,2128,2129,2130,2131,
              2132,2133,2134,2135,2136,2137,2138,2141,2145,2146,2168,2171,2172,2174,2175,2176,2178,2179,2180,2181,2182,2183,2184,2185,2186,2187,
              2189,2190,2192,2193,2194,2195,2197,2198,2224,2250,2252,2254,2256,2255,2277,2278,2279,2280,2283,2284,2285,2287,2289,2290,2291,2292,
              2293,2294,2226,2298,2508,2513,2515,2516,2517,2522,2525,2526,2528,2529,2533,2534,2540,2573,3007,3008,3009,3010,3011,3013,3023,3025,
              3027,3028,3032,3033,3040,3143,3148,3154,3175,3173,3174,3181,3183,3185,3188,3189,3191,3192,3193,3194,3197,3198,3202,3206,3207,3209,
              3210,3215,3216,3217,3218,3219,3220,3221,3222,3224,3255,3256,3257,3258,3262,3263,3264,3270,3268,3267,3272,3274,3275,3277,3280,3281,
              3283,3284,3285,3286,3306,3421,3436,3449,3462,3463,3465,3466,3467,3503,3036,3021,3012,3184,3014,3147,3199,3035,3201,3196,3187,3233,
              3203,3204,3190,3208,3190,3214,3176,3182,3146,3212,3145,3144,3353,3036,3021,3012,3184,3014,3147,3199,3035,3201,3196,3187,3233,3203,
              3204,3190,3208,3190,3214,3176,3182,3146,3212,3145,3144,3353,4004,4005,4008,4009,4010,4011,4012,4013,4015,4116,4117,4118,4123,4133,
              4134,4135,4136,4137,4138,4139,4141,4142,4143,4144,4145,4146,4147,4151,4163,4165,4167,4171,4172,4174,4175,4175,4177,4178,4179,4180,
              4184,4185,4186,4187,4188,4189,4190,4192,4193,4194,4195,4196,4197,4222,4223,4224,42256,4227,4229,4230,4231,4232,4233.4234,4235,4236,
              4237,4238,4239,4240,4241,4242,4243,4245,4246,4247,4248,4249,4250,4251,4252,4253,4254,4255,4258,4285,4301,4302,4303,4304,4305,4319,
              4597,4598,4601,4602,4604,4605,4608,4609,4610,4611,4612,4613,4639,4642,4645,4648]
print(len(college_id))

url = "http://dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode={}"
for i in range(0,379):
    url_1 = url.format(college_id[i])
    html = urllib.request.urlopen(url_1).read()
    soup = BeautifulSoup(html,'lxml')
    table = soup.find('div',id = 'ContentTable1')
    college_name = soup.find('span',id = 'ctl00_ContentPlaceHolder1_lblInstituteNameEnglish')
    co = college_name.text
    location = soup.find('span',id = 'ctl00_ContentPlaceHolder1_lblRegion')
    lo = location.text
    contact_number = soup.find('span',id = 'ctl00_ContentPlaceHolder1_lblResidentialPhoneNo')
    cn = contact_number.text
    email = soup.find('span',id = 'ctl00_ContentPlaceHolder1_lblEMailAddress')
    ee = email.text
    website_link = soup.find('span',id = 'ctl00_ContentPlaceHolder1_lblWebAddress')
    wl = website_link.text
    tpo_name = soup.find('span',id = 'ctl00_ContentPlaceHolder1_lblRegistrarNameEnglish')
    tn = tpo_name.text
    tpo_no = soup.find('span',id = 'ctl00_ContentPlaceHolder1_lblOfficePhoneNo')
    tc = tpo_no.text
    print("college: ",college_name.text)
    print("contact: ",contact_number.text)
    print("location: ",location.text)
    print("email: ",email.text)
    print("website: ",website_link.text)  
    print("TPO name: ",tpo_name.text)
    print("tpo contact: ",tpo_no.text)
    
    f.write(co.replace(",","|") +","+ lo +"," + cn + "," + ee.replace(",","|") + "," +wl+ "," + tn + "," + tc +"\n")
f.close()


            

college_id = [1002,1006,1007,1008,1009,1010,1011,1012,1015,1101,1105,1107,1108,1114,1116,1117,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,
              1129,1130,1139,1140,1141,1142,1144,1147,1148,1151,1152,1153,1168,1180,1182,1244,1245,1246,1247,1249,1250,1251,1265,1266,1267,1268,
              1269,1275,1276,1277,1278,2008,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2113,2114,2116,2126,2127,2128,2129,2130,2131,
              2132,2133,2134,2135,2136,2137,2138,2141,2145,2146,2168,2171,2172,2174,2175,2176,2178,2179,2180,2181,2182,2183,2184,2185,2186,2187,
              2189,2190,2192,2193,2194,2195,2197,2198,2224,2250,2252,2254,2256,2255,2277,2278,2279,2280,2283,2284,2285,2287,2289,2290,2291,2292,
              2293,2294,2226,2298,2508,2513,2515,2516,2517,2522,2525,2526,2528,2529,2533,2534,2540,2573,3007,3008,3009,3010,3011,3013,3023,3025,
              3027,3028,3032,3033,3040,3143,3148,3154,3175,3173,3174,3181,3183,3185,3188,3189,3191,3192,3193,3194,3197,3198,3202,3206,3207,3209,
              3210,3215,3216,3217,3218,3219,3220,3221,3222,3224,3255,3256,3257,3258,3262,3263,3264,3270,3268,3267,3272,3274,3275,3277,3280,3281,
              3283,3284,3285,3286,3306,3421,3436,3449,3462,3463,3465,3466,3467,3503,3036,3021,3012,3184,3014,3147,3199,3035,3201,3196,3187,3233,
              3203,3204,3190,3208,3190,3214,3176,3182,3146,3212,3145,3144,3353,3036,3021,3012,3184,3014,3147,3199,3035,3201,3196,3187,3233,3203,
              3204,3190,3208,3190,3214,3176,3182,3146,3212,3145,3144,3353,4004,4005,4008,4009,4010,4011,4012,4013,4015,4116,4117,4118,4123,4133,
              4134,4135,4136,4137,4138,4139,4141,4142,4143,4144,4145,4146,4147,4151,4163,4165,4167,4171,4172,4174,4175,4175,4177,4178,4179,4180,
              4184,4185,4186,4187,4188,4189,4190,4192,4193,4194,4195,4196,4197,4222,4223,4224,42256,4227,4229,4230,4231,4232,4233.4234,4235,4236,
              4237,4238,4239,4240,4241,4242,4243,4245,4246,4247,4248,4249,4250,4251,4252,4253,4254,4255,4258,4285,4301,4302,4303,4304,4305,4319,
              4597,4598,4601,4602,4604,4605,4608,4609,4610,4611,4612,4613,4639,4642,4645,4648,4649,4653,5003,5006,5007,5008,5009,5010,5103,5104,5105,5106,5107,5108,5109,5121,5124,5125,5139,5151,5160,5161,5162,5164,
              5167,5168,5169,5170,5171,5172,5173,5176,5177,5179,5181,5182,5183,5184,5220,5221,5222,5223,5224,5225,5226,5227,5228,5229,
              5230,5231,5232,5235,5237,5238,5239,5240,5241,5243,5245,5246,5247,5248,5249,5250,5251,5252,5253,5254,5256,5257,5258,5259,
              5260,5261,5263,5322,5330,5331,5354,5356,5357,5358,5360,5361,5362,5363,5365,5366,5367,5368,5369,5370,5371,5372,5373,5374,
              5375,5376,5385,5387,5389,5390,5395,5396,5399,5401,5402,5404,5408,5409,5411,5413,5414,5415,5417,5418,5419,5420,5423,5431,
              5433,5434,5449,6004,6006,6005,6007,6010,6011,6013,6014,6015,6016,6017,6018,6019,6020,6023,6028,6138,6139,6141,6144,6145,
              6146,6147,6148,6149,6151,6155,6156,6160,6175,6176,6177,6178,6179,6182,6183,6184,6185,6187,6206,6207,6214,6215,6217,6219,
              6220,6222,6223,6225,6250,6259,6265,6266,6267,6268,6269,6270,6271,6272,6273,6274,6275,6276,6277,6278,6281,6282,6283,6284,
              6285,6289,6288,6293,6298,6303,6302,6304,6305,6307,6308,6310,6311,6312,6313,6315,6317,6318,6319,6320,6321,6322,6323,6324,
              6325,6326,6402,6403,6404,6405,6406,6407,6408,6409,6410,6414,6415,6416,6417,6418,6419,6420,6421,6422,6423,6425,6427,6428,
              6429,6430,6431,6432,6433,6434,6435,6436,6437,6439,6441,6442,6443,6444,6445,6446,6447,6448,6449,6451,6452,6455,6456,6457,
              6458,6462,6463,6464,6465,6466,6467,6469,6470,6471,6472,6473,6474,6475,6476,6526,6544,6545,6602,6609,6618,6620,6621,6622,
              6625,6634,6640,6643,6649,6712,6713,6714,6715,6716,6720,6721,6722,6723,6724,6725,6728,6729,6731,6732,6754,6755,6756,6757,
              6758,6759,6760,6762,6766,6767,6768,6769,6770,6771,6772,6780,6781,6782,6786,6787,6794,6795,6796,6797,6802,6800,6799,6808,
              6809,6810,6811,6815,6814,6816,6817,6822,6824,6828,6830,6834,6839,6878,6881,6888,6901]
print(len(college_id))
url = "http://dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode={}"
g=0
a=0
u=0
o=0
for i in range(0,732):
    url_1 = url.format(college_id[i])
    html = urllib.request.urlopen(url_1).read()
    soup = BeautifulSoup(html,'lxml')
    table = soup.find('div',id = 'ContentTable1')
    status = soup.find('span',id = 'ctl00_ContentPlaceHolder1_lblStatus1')
    s = status.text
    if s=="Government":
        g=g+1
    elif s=="Un-Aided":
        u=u+1
    elif s=="Government-Aided":
        a=a+1
    else:
        o=o+1
print(g,u,a,o)

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

recipe = ["Government",
          "Unaided",
          "Government-aided",
          "other"]
        

data = [ 'g','u','a','o' ]

wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, **kw)

ax.set_title("Break up of Engineering colleges in India by Status")

plt.show()


















