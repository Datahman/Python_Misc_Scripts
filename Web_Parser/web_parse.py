# -*- coding: utf-8 -*-

# A basic web parser using BeautifulSoup to extract data from SSL- secured websites. 
# Data stored using Pandas data frame.
# Class strings are ignored using Regular expressions.
import bs4
from bs4 import BeautifulSoup
import urllib2, ssl
import requests
import csv
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8') # Set default encode to utf-8. 
import pandas as pd
from collections import defaultdict
import numpy as np
from datetime import datetime
startime = datetime.now()
def Web_Parser():
    
    

    URL = 'https://www.civilservicejobs.service.gov.uk/csr/index.cgi?SID=cGFnZWFjdGlvbj1zZWFyY2hieWNvbnRleHRpZCZwYWdlY2xhc3M9Sm9icyZrZXk9ZmFpciZ1c2Vyc2VhcmNoY29udGV4dD0yNzE5MjUwOSZyZXFzaWc9MTQ3Njg5NzQ1Mi01NTk1YmQ3ZmViZDE2NmQyYjNhOWVlMjQ4NGZhZGM2M2I5MTY4OWUx'
    response = requests.get(URL, verify = './civil.crt') # Use cookie stored within civil.crt to validate the 'GET' call.
    
    # Create empty lists to store valid/invalid links. 
    invalid_links = []
    valid_links = []
    reference_list = []
    p = pd.DataFrame(columns = ['Reference No.',
                                'Salary',
                                'Role Type',
                                'Band Type',
                                'Term',
                                'Hours',
                                'Location',
                                'Description'
                                        ])
  
    try:
        if response.status_code== 200:
            soup = BeautifulSoup(response.text,'lxml')
            output = soup.prettify()
            
            for link in soup.find_all('a'):
                valid_links.append(link.get('href'))
            valid_links = valid_links[5:20] # 5:20
            #print valid_links
            
            for each_link in valid_links:
                
                
                try:
                    
                    
                    response_each_link = requests.get(each_link, verify = './civil.crt')
                    soup_all = bs4.BeautifulSoup(response_each_link.content)
                    counter = 0
                    try:
                            
                        #for div_attributes in soup_all.find_all('div',{'class':'vac_display_field_value'}): # TO DO : Print Salary, descrption, Location, Name. Done
                            counter += 1
                            all_class_divs= soup_all.find_all(class_="vac_display_field_value")

            
                            
                            if len(all_class_divs) ==0:
                                pass
                            else:
                                #print all_class_divs
                                #print (len(all_class_divs),all_class_divs, counter)
                                
                                ref_values=str(all_class_divs[0]) 
                                
                                ref_values = ref_values.replace('<div class="vac_display_field_value">','').replace('</div>','')
                                ref_values= int(ref_values)
                            
                                reference_list.append(ref_values)
                                
                                
                            
                                #other_value = (all_class_divs[1:10])
                                # Order of lists: Salary [1], Role [2], Band type [3], Term [4], Hours [9], 
                                # Location [11], Descrption[12]

                                
                                
                                dict_for_all = {'Salary':"1",'Role':"2",'Band Type':"3",'Term':"4",'Hours':"9",'Location':"11",'Descrption':"12"}
                                salary_values = str(all_class_divs[1])

                                salary_values = salary_values.replace('<div class="vac_display_field_value">','').replace('</div>','')
                                salary_values = re.sub(r'[Â£\+]' ,'',salary_values)
                                #regex = r"^\D\£\d{2}\,\d{3} \- \D\£\d{2}\,\d{3}"
                                #salary_values = re.search(regex,salary_values)
                                #salary_values = salary_values.group(0)
                                
                                #role_values = str(all_class_divs[2])
                                #print role_values
                                
                                
                                
                                #print salary_values
                                
                                                                                

                                
                                list_num = [2,3,4,9,11,12]
                                for i in list_num:
                                    
                                    if i ==2:
                                        
                                        role_values = str(all_class_divs[i]).replace('<div class="vac_display_field_value">','').replace('</div>','')
                                        
                                    
                                    if i ==3:
                                        band_type = str(all_class_divs[i]).replace('<div class="vac_display_field_value">','').replace('</div>','')
                                        
                                    if i ==4:
                                        term_values = str(all_class_divs[i]).replace('<div class="vac_display_field_value">','').replace('</div>','')
                                        
                                    if i ==7:
                                        hours_values = str(all_class_divs[i]).replace('<div class="vac_display_field_value">','').replace('</div>','')
                                        
                                    if i ==11:
                                        Location_ = str(all_class_divs[i]).replace('<div class="vac_display_field_value">','').replace('</div>','')
                                        
                                    if i ==12:
                                        Descrption_ = str(all_class_divs[i]).replace('<div class="vac_display_field_value">','').replace('</div>','')
                                        
                                        
                                         
                                        
                                        p = p.append({'Reference No.':ref_values,
                                                'Salary':salary_values,
                                                'Role Type':role_values,
                                                'Band Type':band_type,
                                                'Term':term_values,
                                                #'Hours':hours_values,
                                                'Location':Location_,
                                                'Description':Descrption_,}, ignore_index=True)
                            #print (soup_all, counter, str("######################"))
                        

                        
                    except Exception as e:
                        print (str(e))
                        
                        
                except Exception as e:
                    print(str(e))
                
        p.to_csv("data.csv")
        print ("Success")
    except Exception as e:
        print(str(e))
    
Web_Parser()
print datetime.now()- startime

# TO DO: ADD all features to the pandas column. Done
