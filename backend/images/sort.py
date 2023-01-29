class Sort:
    def get_bot():
        with open('images/sort/bottom.txt') as f:
            bot = f.read().splitlines()
        return bot
    def get_top():
        with open('images/sort/top.txt') as g:
            top = g.read().splitlines()
        return top

def ai_sort(dict,top,bot):
    bot_list = []
    top_list = []
    for key in dict:
        if key in bot:
            bot_list.append(key)
        if key in top:
            top_list.append(key)
            
    large_top = top_list[0]                             # 항상 0번째 인덱스값이 가장 높은 컨피던스를 가짐
    large_bot = bot_list[0]                           
    # ai 인식 못했을때                               
    if not top_list and bot_list: 
        large_top = top[top.index('t-shirts')] 
        large_bot = bot_list[0]
        
    if top_list and not bot_list:
        large_top = top_list[0]
        large_bot = bot[bot.index('slacks')]
    
    if not top_list and not bot_list:
        large_top = top[top.index('t-shirts')] 
        large_bot = bot[bot.index('slacks')]
    
    return large_top,large_bot