import numpy as np
from data_loader import load_matches, get_team_stats

def predict_match(home_team, away_team, df):
    """
    根据两队历史数据预测比赛结果
    返回: (预测结果, 置信度, 详情)
    """
    # 获取两队统计
    home_stats = get_team_stats(df, home_team)
    away_stats = get_team_stats(df, away_team)
    
    if home_stats is None or away_stats is None:
        return "无法预测", 0.0, "缺少数据"
    
    home_win_rate = home_stats.get('home_win_rate', 0.33)
    away_win_rate = away_stats.get('away_win_rate', 0.33)
    away_home_rate = away_stats.get('home_win_rate', 0.33)
    
    # 综合评分
    home_power = home_win_rate * 0.6 + (1 - away_home_rate) * 0.4
    away_power = away_win_rate * 0.5 + (1 - home_win_rate) * 0.3
    
    diff = home_power - away_power
    
    if diff > 0.08:
        result = f"🏆 {home_team} 主胜"
        confidence = min(abs(diff) * 3.5, 0.85)
    elif diff < -0.08:
        result = f"✈️ {away_team} 客胜"
        confidence = min(abs(diff) * 3.5, 0.75)
    else:
        result = "🤝 平局"
        confidence = 0.45
    
    details = {
        f"{home_team} 综合实力": round(home_power, 3),
        f"{away_team} 综合实力": round(away_power, 3),
        "分差": round(diff, 3)
    }
    
    return result, round(confidence * 100, 1), details

# ====== 运行测试 ======
if __name__ == "__main__":
    df = load_matches("matches.csv")
    if df is not None:
        print("\n" + "="*50)
        print("⚽ 预测: Manchester United vs Chelsea")
        print("="*50)
        result, conf, details = predict_match("Manchester United", "Chelsea", df)
        print(f"\n📌 预测结果: {result}")
        print(f"📌 置信度:   {conf}%")
        print(f"📌 详细分析: {details}")