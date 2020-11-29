from dao.flight_table import Flight
from global_var import db


def add_flight_info(flight_id, start_time, arrive_time, first_class_price, business_class_price,
                    economy_class_price, num_remain_seat, num_remain_first_class,
                    num_remain_business_class, num_remain_economy_class, air_line_id, airport_id, plane_id,
                    company_name):
    flight = Flight.query.filter_by(id=flight_id).first()
    if not flight:
        flight = Flight(
            air_company_name=company_name,
            id=flight_id,
            start_time=start_time,
            arrive_time=arrive_time,
            first_class_price=first_class_price,
            business_class_price=business_class_price,
            economy_class_price=economy_class_price,
            num_remain_seat=num_remain_seat,
            num_remain_first_class=num_remain_first_class,
            num_remain_business_class=num_remain_business_class,
            num_remain_economy_class=num_remain_economy_class,
            air_line_id=air_line_id,
            airport_id=airport_id,
            plane_id=plane_id
        )

        db.session.add(flight)
    else:
        return False
    db.session.commit()
    return True
