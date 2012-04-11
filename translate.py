#! /usr/bin/env python

# -*- coding: utf-8 -*-

"""This script allow users to translate a string 

from one language to another with Google translate"""



import sys

import re

import urllib

import urllib2

import json

import pytils


def print_params(data):

  """print parameters from list"""

  for val in data:

    if isinstance(val, basestring):

      print ("\t " + val)



def main():

  """

  Usage:

    first arg - string to translate

    second arg - source lang

    third arg - target lang  

  Example:

    translate.py 'text to translate' en ru

    translate.py 'text to translate' ru en

  """

  #print 'DDE (C) 2011'

  url = "http://translate.google.com/translate_a/t?%s"

  list_of_params = {'client' : 't', 

                    'hl' : 'en', 

                    'multires' : '1', }   

  #if len(sys.argv) >1:
  if len(sys.argv)<5:
      print (main.__doc__)
      return 0
  if len(sys.argv)>=5:
    txt='';
    for x in range(4,len(sys.argv)):
      txt+=str(sys.argv[x]) +' '
    #print (txt)
    #return
    
    sourcelang=sys.argv[2]
    if sourcelang=='ru':
      try:
        buff=pytils.translit.detranslify(txt.encode('utf8'))
        #print buff
        #return
      except:
        pass#print 'lib exception'
      else:
        txt=buff.encode('utf8')
    
    list_of_params.update({'text' : txt,

                           'sl' : sourcelang, 

                           'tl' : sys.argv[3] })


  request = urllib2.Request(url % urllib.urlencode(list_of_params), 

    headers={ 'User-Agent': 'Mozilla/5.0', 'Accept-Charset': 'utf-8' })

  res = urllib2.urlopen(request).read()



  fixed_json = re.sub(r',{2,}', ',', res).replace(',]', ']')  

  data = json.loads(fixed_json)

    

  #simple translation
  for l in data[0]:
    print( "%s / %s / %s" % (l[0], l[1], 

              l[2] or l[3]))

    

  #abbreviation

  if not isinstance(data[1], basestring):

      print (data[1][0][0])

      print_params(data[1][0][1])

      

  #interjection  

  try:

      if not isinstance(data[1][1], basestring):

        print (data[1][1][0])

        print_params(data[1][1][1])

  except Exception:

      print ("no interjection" )

  #else:

   # print (main.__doc__)

    

if __name__ == '__main__':

  main()

