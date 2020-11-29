from dao.aircompany_plane_table import AircompanyPlane
from global_var import db


def delete_company_plane_info(company_plane_id):
    company_plane = AircompanyPlane.query.filter_by(id=company_plane_id).first()
    if company_plane:
        db.session.delete(company_plane)
    else:
        return False
    db.session.commit()
    return True

