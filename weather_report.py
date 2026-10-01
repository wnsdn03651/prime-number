# =========================================================
# GitHub Repository: https://github.com/wnsdn03651/창의적공학설계
# =========================================================

import random

def get_location():
    location = input("날씨를 확인할 지역을 입력하세요 (기본: 포항): ").strip()
    if not location:
        location = "포항"  # 기본 지역: 포항으로 설정
    return location

def generate_weather_data(days=3):
    """최소 2일 이상의 날씨 데이터를 생성하는 함수"""
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

def display_weather_report(location, weather_data):
    """날씨 리포트를 깔끔한 포맷으로 출력하는 함수"""[cite: 1]
    print("\n" + "=" * 45)
    print(f"       [ {location} 지역 날씨 리포트 ]")
    print("=" * 45)
    
    for item in weather_data:
        print(f"📅 {item['day']} 날씨")
        print(f"  · 기상 상태: {item['condition']}")
        print(f"  · 기온: 최저 {item['low']}°C / 최고 {item['high']}°C")
        print(f"  · 습도: {item['humidity']}%")
        print("-" * 45)

def main():
    location = get_location()
    weather_data = generate_weather_data(days=3)  # 3일치 날씨 리포트
    display_weather_report(location, weather_data)

if __name__ == "__main__":
    main()
