from dao.plane_table import Plane
from typing import *


def get_plane_info(plane_id):
    plane = Plane.query.filter_by(id=plane_id).first()
    result: Dict[str] = {
        'plane_id': plane.id,
        'num_seat': plane.num_seat,
        'num_first_class_seat': plane.num_first_class_seat,
        'num_business_class_seat': plane.num_business_class_seat,
        'num_economy_class_seat':plane.num_economy_class_seat
    }
    return result
