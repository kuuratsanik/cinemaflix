#walid.saad

import yts as yts
import kickass as kickass
import tpb as tpb
import nyaa as nyaa
import limetorrents as lime
from t411 import T411 as t411
import cpabsien as cpabsien
import strike as strike
from eztv import eztv
from operator import attrgetter
import re

def search(query,provider,sort=None,seeds=0,max=0):
    results=[]
    sorts=['seeds','size']
    if(provider=="kickass"):
         results=kickass.search(query)
    if(provider=="yts"):
         results=yts.search(query)
    if(provider=="thepiratebay"):
         results=tpb.search(query)
    if(provider=="limetorrents"):
         results=lime.search(query)
    if(provider=="cpabsien"):
         results=cpabsien.search(query)
    if(provider=="t411"):
         results=t411().search(query)
    if(provider=="strike"):
         results=strike.search(query)
    if(provider=="nyaa"):
         results=nyaa.search(query)
    if(provider=="eztv"):
        x=re.compile("(([a-zA-Z]+\s*)+)(\s[0-9]+\s[0-9]+)$")
        m=x.match(query)
        if m:
            show=m.group(1)
            season=m.group(3).strip().split(' ')[0]
            episode=m.group(3).strip().split(' ')[1]
            results=eztv().search(show,season,episode)
        else:
            results=[]
    filtered_results=[x for x in sort_results(results,sort) if x.seeds>=seeds] if sort in sorts else [x for x in results if x.seeds>=seeds]
    final_results=filtered_results[:max]
    return final_results
    
def sort_results(torrent_list,criteria):
    return sorted(torrent_list,key=attrgetter(criteria),reverse=True)