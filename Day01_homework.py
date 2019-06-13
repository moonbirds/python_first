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

