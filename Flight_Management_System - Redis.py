#!/usr/bin/env python
# coding: utf-8

# In[1]:


import redis
r = redis.Redis(host='localhost',port='6379')


# ## Make a list of Flight Coordinates using geoadd() 

# In[2]:


r.geoadd("Flight Coordinates",-96.1679447,19.1922834,"pos_1")
r.geoadd("Flight Coordinates",19.7935705,50.0898965,"pos_2")
r.geoadd("Flight Coordinates",-123.4112839,48.4373686,"pos_3")
r.geoadd("Flight Coordinates",-86.3630197,13.0851139,"pos_4")
r.geoadd("Flight Coordinates",-72.0645776,-13.3379818,"pos_5")
r.geoadd("Flight Coordinates",34.1114621,3.0062022,"pos_6")
r.geoadd("Flight Coordinates",103.9344076,16.0332128,"pos_7")
r.geoadd("Flight Coordinates",36.2090012,49.854824,"pos_8")
r.geoadd("Flight Coordinates",36.8458837,-1.2816645,"pos_9")
r.geoadd("Flight Coordinates",18.7971435,50.6283477,"pos_10")
r.geoadd("Flight Coordinates",71.3099509,29.8626871,"pos_11")
r.geoadd("Flight Coordinates",141.2777515,38.5796262,"pos_12")
r.geoadd("Flight Coordinates",15.379192,46.791555,"pos_13")
r.geoadd("Flight Coordinates",-8.9978149,38.9458437,"pos_14")
r.geoadd("Flight Coordinates",113.930475,22.533012,"pos_15")
r.geoadd("Flight Coordinates",-77.0852258,38.9374808,"pos_16")
r.geoadd("Flight Coordinates",-8.6867786,40.1721605,"pos_17")
r.geoadd("Flight Coordinates",10.4494906,11.7775345,"pos_18")
r.geoadd("Flight Coordinates",18.7293002,50.969668,"pos_19")
r.geoadd("Flight Coordinates",24.4154907,60.0557978,"pos_20")
r.geoadd("Flight Coordinates",116.664056,28.695534,"pos_21")
r.geoadd("Flight Coordinates",15.4122128,51.0350353,"pos_22")
r.geoadd("Flight Coordinates",-64.182416,-31.372506,"pos_23")
r.geoadd("Flight Coordinates",23.0102888,40.4168034,"pos_24")
r.geoadd("Flight Coordinates",109.428608,24.326292,"pos_25")
r.geoadd("Flight Coordinates",110.947552,34.423878,"pos_26")
r.geoadd("Flight Coordinates",114.6204667,-3.2690585,"pos_27")
r.geoadd("Flight Coordinates",-75.6033497,6.1307505,"pos_28")
r.geoadd("Flight Coordinates",21.7513868,39.3525635,"pos_29")
r.geoadd("Flight Coordinates",-8.7386338,39.764261,"pos_30")
r.geoadd("Flight Coordinates",120.6947522,-8.6577711,"pos_31")
r.geoadd("Flight Coordinates",6.6372501,52.3323097,"pos_32")
r.geoadd("Flight Coordinates",108.5671,-7.1311,"pos_33")
r.geoadd("Flight Coordinates",-61.344385,15.38447,"pos_34")
r.geoadd("Flight Coordinates",-50.534262,-29.6216078,"pos_35")
r.geoadd("Flight Coordinates",29.85391,-30.85775,"pos_36")
r.geoadd("Flight Coordinates",-76.240381,8.788161,"pos_37")
r.geoadd("Flight Coordinates",-171.5877457,-13.8875282,"pos_38")
r.geoadd("Flight Coordinates",-77.6929792,-9.2623446,"pos_39")
r.geoadd("Flight Coordinates",139.7750031,36.7003816,"pos_40")
r.geoadd("Flight Coordinates",2.368326,48.7823921,"pos_41")
r.geoadd("Flight Coordinates",103.46083,52.86917,"pos_42")
r.geoadd("Flight Coordinates",-40.2509918,-15.2475119,"pos_43")
r.geoadd("Flight Coordinates",69.079674,34.496651,"pos_44")
r.geoadd("Flight Coordinates",113.829667,22.720595,"pos_45")
r.geoadd("Flight Coordinates",8.6023254,8.943208,"pos_46")
r.geoadd("Flight Coordinates",-9.3872558,38.7080654,"pos_47")
r.geoadd("Flight Coordinates",96.06085,5.255183,"pos_48")
r.geoadd("Flight Coordinates",117.3616476,39.3433574,"pos_49")
r.geoadd("Flight Coordinates",123.0902,-8.4793,"pos_50")


# In[3]:


for i in dir(r):
    if i.startswith('geo'):
        print(i)


# ## Make a list of Aiports using geoadd()

# In[4]:


r.geoadd("Airport",55.35964257431236,25.246723864900527,"Dubai")
r.geoadd("Airport",88.44483366180721,22.653396616182025,"Kolkata")
r.geoadd("Airport",2.4371427867420805,48.96178249488121,"Paris")
r.geoadd("Airport",72.86270898110179,19.090521468885544,"Mumbai")
r.geoadd("Airport",-73.7774419816457,40.65329457638332,"New York")
r.geoadd("Airport",55.97379226624302,37.412427896024774,"Moscow")
r.geoadd("Airport",52.364155015199636,13.509105013029252,"Berlin")
r.geoadd("Airport",144.84320876328124,-37.670236331901954,"Melbourne")
r.geoadd("Airport",8.579918752111869,50.04176379866092,"Frankfurt")
r.geoadd("Airport",77.0998505085893,28.557029355781793,"Delhi")


# ## Calculate Distance Between 2 Airports

# In[5]:


Airport_list = ['Dubai','Kolkata','Paris','Mumbai','New York','Moscow','Berlin','Melbourne','Frankfurt','Delhi']

for x in Airport_list:
    for y in Airport_list:
        if(x != y):
            print('The Distance Between {} and {} -> {}'.format(x,y,r.geodist('Airport',x,y,unit='km')))
        else:
            pass


# In[6]:


coor_pos1 = r.geopos('Flight Coordinates','pos_1')
print(coor_pos1)
coor_airport = r.geopos('Airport','Dubai')
print(coor_airport)


# # Combining Flight Coordinates & Airport Keys 

# In[18]:


r.zunionstore('result',('Flight Coordinates','Airport'),aggregate="MIN")


# # Calculation of Distance Between Flight's(pos_1) & Dubai

# In[19]:


r.geodist('result',"Dubai","pos_1",unit='km')


# # Calculation of Distance Between Flight(pos_2) & Kolkata

# In[20]:


r.geodist('result',"Kolkata","pos_2",unit='km')


# # As we see from above, position of Flights are closer to Kolkata than Dubai (km)

# In[ ]:




