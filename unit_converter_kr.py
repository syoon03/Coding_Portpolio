# 단위 변환 계수 정의

LENGTH_UNITS = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000,
    "in": 0.0254,
    "ft": 0.3048,
    "yd": 0.9144,
    "mi": 1609.344,
}  # 기준 단위: m

WEIGHT_UNITS = {
    "mg": 0.001,
    "g": 1,
    "kg": 1000,
    "t": 1_000_000,
    "oz": 28.350,
    "lb": 453.592,
}  # 기준 단위: g

TIME_UNITS = {
    "ms": 0.001,
    "s": 1,
    "min": 60,
    "h": 3600,
    "day": 86400,
    "week": 604800,
}  # 기준 단위: s

AREA_UNITS = {
    "mm2": 0.000001,
    "cm2": 0.0001,
    "m2": 1,
    "km2": 1_000_000,
    "평": 3.306,
    "ha": 10000,
    "acre": 4046.86,
}  # 기준 단위: m2

VOLUME_UNITS = {
    "mL": 1,
    "L": 1000,
    "cm3": 1,
    "m3": 1_000_000,
    "cup": 236.5625,   # 1/16 gal
    "pt": 473.125,      # 1/2 qt
    "qt": 946.25,        # 1/4 gal
    "gal": 3785,
}  # 기준 단위: mL

SPEED_UNITS = {
    "m/s": 1,
    "km/h": 1 / 3.6,
    "mph": 1.609 / 3.6,
    "knot": 1.852 / 3.6,
}  # 기준 단위: m/s

DATA_UNITS = {
    "bit": 1,
    "Byte": 8,
    "KB": 8 * 1000,
    "MB": 8 * 1000 ** 2,
    "GB": 8 * 1000 ** 3,
    "TB": 8 * 1000 ** 4,
    "PB": 8 * 1000 ** 5,
}  # 기준 단위: bit

CATEGORIES = {
    "1": ("길이", LENGTH_UNITS),
    "2": ("무게", WEIGHT_UNITS),
    "3": ("온도", None),  # 온도는 별도 함수로 처리
    "4": ("시간", TIME_UNITS),
    "5": ("넓이", AREA_UNITS),
    "6": ("부피", VOLUME_UNITS),
    "7": ("속도", SPEED_UNITS),
    "8": ("데이터", DATA_UNITS),
}


def convert_by_factor(value: float, from_unit: str, to_unit: str, units: dict) -> float:
    """기준 단위 배율을 이용한 일반 변환 (온도 제외 전 분류 공통)"""
    base_value = value * units[from_unit]   # 입력값 -> 기준 단위
    return base_value / units[to_unit]       # 기준 단위 -> 목표 단위


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """온도는 배율이 아니라 offset이 있어서 별도 처리"""
    # 1단계: 무엇이 들어오든 섭씨(C)로 통일
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9
    else:  # "K"
        celsius = value - 273.15

    # 2단계: 섭씨에서 원하는 단위로 변환
    if to_unit == "C":
        return celsius
    elif to_unit == "F":
        return celsius * 9 / 5 + 32
    else:  # "K"
        return celsius + 273.15


def choose_unit(prompt: str, units: dict) -> str:
    unit_list = list(units.keys())
    display = "/".join(f"{i + 1}.{u}" for i, u in enumerate(unit_list))
    while True:
        choice = input(f"{prompt}[{display}]: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(unit_list):
            return unit_list[int(choice) - 1]
        for u in unit_list:
            if choice.lower() == u.lower():
                return u
        print("잘못된 입력입니다. 목록에 있는 번호나 단위명을 입력해주세요.\n")


def choose_temp_unit(prompt: str) -> str:
    temp_map = {"1": "C", "2": "F", "3": "K"}
    while True:
        choice = input(f"{prompt}[1.°C/2.°F/3.K]: ").strip()
        if choice in temp_map:
            return temp_map[choice]
        if choice.upper() in ("C", "F", "K"):
            return choice.upper()
        print("잘못된 입력입니다. 1~3 중에서 선택해주세요.\n")


def run_conversion(category_key: str) -> None:
    name, units = CATEGORIES[category_key]

    try:
        value = float(input("숫자를 입력해주세요: "))
    except ValueError:
        print("숫자만 입력할 수 있습니다.\n")
        return

    if category_key == "3":  # 온도
        from_unit = choose_temp_unit("원래 단위를 선택해주세요")
        to_unit = choose_temp_unit("변환할 단위를 선택해주세요")
        result = convert_temperature(value, from_unit, to_unit)
        label = {"C": "°C", "F": "°F", "K": "K"}
        print(f"\n결과: {value}{label[from_unit]} = {result:.4f}{label[to_unit]}\n")
    else:
        from_unit = choose_unit("원래 단위를 선택해주세요", units)
        to_unit = choose_unit("변환할 단위를 선택해주세요", units)
        result = convert_by_factor(value, from_unit, to_unit, units)
        print(f"\n결과: {value}{from_unit} = {result:.6g}{to_unit}\n")


def main() -> None:
    print("=" * 40)
    print(" 단위 변환기 ")
    print("=" * 40)

    while True:
        print("\n변환할 단위의 분류를 골라주세요")
        for key, (name, _) in CATEGORIES.items():
            print(f"  {key}. {name}")
        print("  0. 종료")

        category = input("\n선택: ").strip()

        if category == "0":
            print("프로그램을 종료합니다.")
            break

        if category not in CATEGORIES:
            print("1~8 중에서 선택해주세요.\n")
            continue

        run_conversion(category)


if __name__ == "__main__":
    main()