import datetime
from django.core.cache import cache
from collections import Counter
from .models import style

def get_ranking(gender):
    end_date = datetime.datetime.today()                  
    start_date = end_date + datetime.timedelta(days=-7) 
    
    style_list = [
        style for style in style.objects.filter(created_at__range=(
        start_date, end_date)) if style.gender == gender
    ]
    
    list_cnt = []
    for a in style_list:
        list_cnt.append(str(a.top+a.top_color+a.bottom+a.bottom_color))
    cnt = Counter(list_cnt)
    rank = str(cnt.most_common(1))
    
    strip = "[""]"")""("
    wow = rank.strip(strip)
    sp = wow.replace('\'','').split(',')
    
    for b in style_list:
        if str(b.top+b.top_color+b.bottom+b.bottom_color) == sp[0]:
            res = {
                'gender':b.gender,
                'top':b.top,
                'top_color':b.top_color,
                'bottom':b.bottom,
                'bottom_color':b.bottom_color,
                'count': sp[1].replace(' ','')
                }           
            return res  
    return ('except')
