
# =========================================================
# GitHub Repository: https://github.com/본인계정/저장소이름[cite: 1]
# =========================================================

def get_location():
    location = input("날씨를 확인할 지역을 입력하세요 (기본: 천안): ").strip()
    if not location:
        location = "천안"  # 기본 지역 설정[cite: 1]
    return location

def main():
    print("날씨 리포트 프로그램을 시작합니다.")
    location = get_location()
    print(f"선택된 지역: {location}")

if __name__ == "__main__":
    main()