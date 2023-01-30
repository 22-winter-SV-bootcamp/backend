class Sort:
    def get_bot():
        with open('images/sort/bottom.txt') as f:
            bot = f.read().splitlines()
        return bot
    def get_top():
        with open('images/sort/top.txt') as g:
            top = g.read().splitlines()
        return top
