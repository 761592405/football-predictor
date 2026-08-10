import math

def poisson_probability(actual, mean):
    """
    计算泊松分布概率：P(X=k) = (lambda^k * e^-lambda) / k!
    """
    return (mean**actual * math.exp(-mean)) / math.factorial(actual)

def predict_match(home_avg_goals, away_avg_goals):
    """
    根据两队的期望进球数，预测胜平负概率
    """
    最大进球数 = 10  # 假设单场进球不超过10个
    
    主队胜率 = 0.0
    平局概率 = 0.0
    客队胜率 = 0.0
    
    # 遍历所有可能的比分组合 (0-0 到 10-10)
    for h in range(max_goals):
        对于 一个 在 范围内(最大进球数):
            # 计算该比分出现的概率
            概率 = 泊松概率(h, 主队场均进球数) * 泊松概率(客队场均进球数)
            
            如果 h > a：
                主队胜率 += 概率
            elif h == a:
                平局概率 += 概率
            else:
                客队胜率 += 概率
                
    返回 {
        "主队胜": 四舍五入(主队胜概率 * 100, 2),
        "平局": 四舍五入(平局概率 * 100, 2),
        "客胜": 四舍五入(客胜概率 * 100, 2)
    }
