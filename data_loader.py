import请求
导入json

def load_football_data():
    """
从 football-data.org 获取免费的英超历史数据
    """
    # 这是一个公开的API端点，获取2023-2024赛季英超数据
    url = "https://api.football-data.org/v4/competitions/PL/matches"
    
headers = {
        # 注意：这是演示用的Token，如果失效你需要去官网申请一个免费的
        'X-Auth-Token': 'YOUR_API_TOKEN_HERE' 
    }
    
    print("正在连接 API 获取数据...")
    
    try:
        response = requests.get(url, headers=headers)
        如果 response.status_code == 200:
            data = response.json()
            print(f"成功获取 {len(data.get('matches', []))} 场比赛数据！")
            return data['matches']
        else:
            print(f"获取失败，状态码: {response.status_code}")
            return []
    except Exception as e:
        print(f"发生错误: {e}")
        return []

if __name__ == "__main__":
    matches = load_football_data()
    如果匹配：
        print("第一场比赛示例:", matches[0]['homeTeam']['name'], "vs", matches[0]['awayTeam']['name'])
