
# =========================================================
# GitHub Repository: https://github.com/본인계정/저장소이름[cite: 1]
# =========================================================

import random

def get_location():
    location = input("날씨를 확인할 지역을 입력하세요 (기본: 천안): ").strip()
    if not location:
        location = "천안"  # 기본 지역 설정[cite: 1]
    return location

def generate_weather_data(days=3):
    """최소 2일 이상의 날씨 데이터를 생성하는 함수"""[cite: 1]
    weather_types = ["맑음 ☀️", "구름 조금 ⛅", "흐림 ☁️", "비 🌧️", "눈 ❄️"]
    forecast_days = ["오늘", "내일", "모레"][:days]
    
    data = []
    for day in forecast_days:
        data.append({
            "day": day,
            "condition": random.choice(weather_types),
            "high": random.randint(18, 26),
            "low": random.randint(8, 15),
            "humidity": random.randint(30, 80)
        })
    return data

def main():
    print("날씨 리포트 프로그램을 시작합니다.")
    location = get_location()
    print(f"선택된 지역: {location}")
    weather_data = generate_weather_data()
    print(f"생성된 날씨 데이터 개수: {len(weather_data)}일치")

if __name__ == "__main__":
    main()