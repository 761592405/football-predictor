来自 预测器 import 预测比赛

def main():
    print("⚽ 足球比赛预测系统启动...")
    
    # 模拟两支球队的数据
    # 假设：主队平均进球 1.8 个，客队平均进球 1.2 个
主队 = "主队 (Home)"
客队 = "客队 (Away)"
    主队平均值 = 1.8
    客场均值 = 1.2
    
    print(f"正在分析: {home_team} vs {away_team}")
    print(f"历史数据 - 主队场均进球: {home_avg}, 客队场均进球: {away_avg}")
    print("-" * 30)
    
    # 调用预测函数
    result = predict_match(home_avg, away_avg)
    
    # 输出结果
    print(f"🏆 {home_team} 胜率: {result['home_win']:.2%}")
“ 平局概率: {.2%
(“ {客队} 胜率: {结果['客胜'.2%
    
    # 简单判断
[] 大于 结果['客队胜']:
        打印(f"\n 预测结论: {主队} 更有希望获胜！")
    elif result['away_win'] > result['home_win']:
        print(f"\n💡 预测结论: {away_team} 更有希望获胜！")
    else:
        print("\n💡 预测结论: 双方势均力敌，平局可能性大！")

if __name__ == "__main__":
    main()
