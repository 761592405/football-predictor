import pandas as pd
import os

def load_matches(filepath="matches.csv"):
    """加载历史比赛数据"""
    if not os.path.exists(filepath):
        print(f"❌ 找不到文件: {filepath}")
        return None
    
    df = pd.read_csv(filepath)
    print(f"✅ 成功加载 {len(df)} 场比赛数据")
    return df

def get_team_stats(df, team_name):
    """获取某支球队的历史统计数据"""
    # 主队身份的比赛
    home_matches = df[df['home_team'] == team_name]
    # 客队身份的比赛
    away_matches = df[df['away_team'] == team_name]
    
    # 主队胜率
    home_wins = len(home_matches[home_matches['home_goals'] > home_matches['away_goals']])
    home_total = len(home_matches)
    
    # 客队胜率
    away_wins = len(away_matches[away_matches['away_goals'] > away_matches['home_goals']])
    away_total = len(away_matches)
    
    print(f"\n📊 {team_name} 数据统计:")
    print(f"  主场: {home_total}场 | 胜{home_wins}场 | 胜率 {home_wins/home_total*100:.1f}%" if home_total else "  主场: 无数据")
    print(f"  客场: {away_total}场 | 胜{away_wins}场 | 胜率 {away_wins/away_total*100:.1f}%" if away_total else "  客场: 无数据")
    
    return df

# 测试代码
if __name__ == "__main__":
    data = load_matches()
    if data is not None:
        print(data.head())  # 打印前5行
        get_team_stats(data, "Manchester United")
        get_team_stats(data, "Chelsea")