from dao.aircompany_plane_table import AircompanyPlane
from global_var import db


def add_company_plane_info(company_name, plane_id):
    company_plane = AircompanyPlane.query.filter_by(air_company_name=company_name,
                                                    plane_id=plane_id).first()
    if not company_plane:
        company_plane = AircompanyPlane(
            air_company_name=company_name,
            plane_id=plane_id
        )
        db.session.add(company_plane)
    else:
        return False
    db.session.commit()
    return True
