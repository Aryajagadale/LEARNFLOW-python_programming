#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install pyshorteners')


# In[6]:


import pyshorteners

def shorten_url(url):
    # Initialize the Shortener object
    shortener = pyshorteners.Shortener()

    # Shorten the URL
    shortened_url = shortener.tinyurl.short(url)
    
    return shortened_url

# Prompt user to input URL
url = input("Enter the URL to shorten: ")

# Shorten the URL
shortened_url = shorten_url(url)
print("Shortened URL:", shortened_url)


# In[ ]:




