# 내 첫번째 코드. 주차 요금을 바로 계산함. 마지막에 한꺼번에 계산해야 정확한 값이 나옴.
def solution(fees, records):
    default_time, default_charge, unit_time, unit_charge = fees
    car_times = {}
    car_fees = {}
    for record in records:
        time, number, state = record.split()
        hh, mm = map(int, time.split(":"))
        minutes = hh*60 + mm
        if state == "OUT":
            parked_time = minutes - car_times[number]
            fee = default_charge + max(0, (parked_time - default_time + unit_time - 1)//unit_time * unit_charge)
            car_fees[number] = car_fees.get(number, 0) + fee
            del car_times[number]
        else:
            car_times[number] = minutes

    if car_times:
        for car in car_times:
            minutes = 23 * 60 + 59
            parked_time = minutes - car_times[car]
            fee = default_charge + max(0, (parked_time - default_time + unit_time - 1)//unit_time * unit_charge)
            car_fees[car] = car_fees.get(car, 0) + fee

    ret = [car_fees[key] for key in sorted(car_fees)]
    return ret

# 수정한 코드.
def solution(fees, records):
    """
    fees를 기본시간, 기본요금, 단위시간, 단위요금으로 언패킹.
    car_times: 입차시간을 담을 딕셔너리
    car_fees: 1) 기존의 주차시간, 2) 주차요금 을 담을 딕셔너리

    첫번째 순회에서는 records에 명시된 데이터대로 입차시간, 출차시간을 계산한 뒤 car_fees에 담는다.
    두번째 순회에서는 출차시간이 명시되어있지 않은 차들의 주차시간을 계산하여 car_fees에 추가한다.
    세번째 순회에서 car_fees에 담긴 각 차들의 총 주차시간을 계산한뒤, 주차요금을 저장한다.
    마지막으로 차 번호 순서대로 오름차순 정렬한 뒤 해당 차의 주차요금을 반환한다.
    """
    default_time, default_charge, unit_time, unit_charge = fees
    car_times = {}
    car_fees = {}
    for record in records:
        time, number, state = record.split()
        hh, mm = map(int, time.split(":"))
        minutes = hh*60 + mm
        if state == "OUT":
            parked_time = minutes - car_times[number]
            car_fees[number] = car_fees.get(number, 0) + parked_time
            del car_times[number]
        else:
            car_times[number] = minutes

    for car in car_times:
        minutes = 23 * 60 + 59
        parked_time = minutes - car_times[car]
        car_fees[car] = car_fees.get(car, 0) + parked_time

    for car in car_fees:
        fee = default_charge + max(0, ((car_fees[car]-default_time + unit_time-1)//unit_time * unit_charge))
        car_fees[car] = fee

    ret = [car_fees[key] for key in sorted(car_fees)]
    return ret