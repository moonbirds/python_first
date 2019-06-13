"""Capital Assets Pricing Model
    资本资产定价模型"""
Rf=float(input('市场无风险收益率为：'))#e.g. 0.3
Rm=float(input('市场预期收益率为：'))#e.g 0.8
beta=float(input('该产品的市场相关系数为：'))#e.g 1.2
Rp=Rf+beta*(Rm-Rf)
print('该产品的预期收益为：%.2f' % Rp)


"""Black_Shole Options Princing Model
    BSM期权价格定价模型"""
import math
s=float(input('股票的现在价格为：'))#e.g 100
k=float(input('股票的未来价格为：'))#e.g 120
r=float(input('现在的市场利率为（年化利率）：'))#e.g 0.05
T=float(input('到期时间为(年化时间）：'))#e.g 2 yrs
sigma = float(input('市场波动率：'))#e.g 0.5
d_1=(math.log(s/k))/(sigma*math.sqrt(T))+0.5*sigma*math.sqrt(T)
d_2=(math.log(s/k))/(sigma*math.sqrt(T))-0.5*sigma*math.sqrt(T)#d_1,d_2为模型计算因子

from scipy.stats import norm
c=s*norm.cdf(d_1)-k*math.exp(-r*T)*norm.cdf(d_2)
print('该股票的看涨期权的价格为：%.2f'% c) #C为看涨期权的价格
p=k*math.exp(-r*T)*norm.cdf(-d_2)-s*norm.cdf(-d_1)
print('该股票的看跌期权的价格为：%.2f'% p) #p为看跌期权的价格


"""分支结构的练习"""
"""GPA转换英国本科学位算法"""
y2=float(input('第二年的平均成绩：'))
y3=float(input('第三年的平均成绩：'))
score=y2*0.4+y3*0.6#最终的加权平均分数
if score < 40:
    grade = 'No degree'#未能毕业
elif score < 50:
    grade = '3 class degree'
elif score < 60:
    grade = '2.2 class degree'
elif score < 70:
    grade = '2.1 class degree'
else:
    grade = '1 class degree'
print(grade)


"""人民币，美元，英镑，港币之间汇率换算"""
value=float(input('货币总量：'))
currency=input('货币种类为：')
if currency == 'CNY' or currency == '人民币':
    print('%.2f CNY= %.2f USD=%.2f GBP=%.2f HKD'% (value,value*0.1445,value*0.1140,value*1.1312))
elif  currency == 'USD' or currency == '美元':
    print('%.2f USD=%.2f CNY=%.2f GBP=%.2f HKD'%(value,value*6.9211,value*0.7887,value*7.8293))
elif  currency == 'GBP' or currency == '英镑':
    print('%.2f GBP=%.2f CNY=%.2f USD=%.2f HKD'%(value,value*8.7753,value*1.2679,value*9.9268))
elif  currency == 'HKD' or currency == '港币':
    print('%.2f HKD=%.2f CNY=%.2f USD=%.2f GBP'%(value,value*0.8840,value*0.1277,value*0.1007))
else:
    print('请输入有效货币单位')

