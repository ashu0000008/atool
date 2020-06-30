class PriceItem:
    target = ''     #检测对象
    project = ''    #检测项目
    method = ''     #检测方法
    price = 0       #价钱
    custom = ''     #客户

    def __init__(self, target, project, method, price, custom):
        self.target = target
        self.project = project
        self.method = method
        self.price = price
        self.custom = custom

class ResultItem:
    custom = ''  #客户
    month = ''   #月份
    value = 0    #金额
    total = 0    #年度总金额

    def __init__(self, custom, month, value, total):
        self.custom = custom
        self.month = month
        self.value = value
        self.total = total
