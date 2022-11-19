import eyaletler
import requests
import os
import time
import json
import pandas    as pd
import csv
#Transaction Search   URL -- 'https://api.yelp.com/v3/transactions/{transaction_type}/search'
#Autocomplete         URL -- 'https://api.yelp.com/v3/autocomplete'

#Categories           URL -- 'https://api.yelp.com/v3/categories'
#Categories Alias     URL -- 'https://api.yelp.com/v3/categories/{alias}'
def CompanyAndPhone(xx):
     text=''
     for x in xx:
         text=x['name']+';'+x['phone']
         yazdir(text)




def yazdir(yazi):
    file1 = open(dosya_yolu, "a")
    # \n is placed to indicate EOL (End of Line)
    file1.write("  \n")
    file1.writelines(yazi)
    file1.close()  # to change file access modes
    print(yazi)


def sil(dosyaa):
    if os.path.exists(dosyaa):  # FENER_KOLONLARI_OLUSTUR.sql dosyasi siliniyor
        os.remove(dosyaa)
    else:
        print("The file does not exist")


def convert_excell():
    for x in eyaletler.eyalet():
        try:
            PARAMETERS = {'location': x

                          }
            response = requests.get(url=BUSINESS_PATH,
                                    params=PARAMETERS,
                                    headers=HEADERS)
            time.sleep(1)
            # Convert response to a JSON String
            business_data = response.json()
            time.sleep(1)
            print(business_data['businesses'])
            print(len(business_data['businesses']))
            CompanyAndPhone(business_data['businesses'])
        except:
            print("An exception occurred")






# Import the modules


# Define a business ID
#category_alias = 'hotdogs'

# Define API Key, Search Type, and header
MY_API_KEY = 'ZOZfxsbgPRb8UGMmlrElq_sVx1G-SdsH0mu6zuGvrlGmo2t5fRuzEdHgcCwJA5ySNssn7Ws6vS44gDq9IVUg5yOzjJ1a8wm14CNYL4tljMoqs0zLWaJyG2MO_c9vY3Yx'
BUSINESS_PATH = 'https://api.yelp.com/v3/transactions/delivery/search'
HEADERS = {'Authorization': 'bearer %s' % MY_API_KEY}

# Define the Parameters of the search

dosya_yolu = r"C:\Users\Ali\Desktop\OnMuhasebe\test.txt"
sil(dosya_yolu)
convert_excell()
# Make a Request to the API, and return results


# print the data
#print(json.dumps(business_data, indent = 3))

# Define Phone Parameter - Phone Search - MUST START WITH "+" and the COUNTRY CODE
#PARAMETERS = {'phone': '+18584340001'}

# Define Parameters - Transaction Type
#PARAMETERS = {'location':'San Diego'}

# Define Paramters -  Autocomplete
#PARAMETERS = {'text': 'good food',
#              'latitude': 32.715736,
#              'longitude': -117.161087}