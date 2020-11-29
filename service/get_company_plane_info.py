from dao.aircompany_plane_table import AircompanyPlane
from typing import *


def get_company_plane_info(company_name):
    company_plane_infos = AircompanyPlane.query.filter_by(air_company_name=company_name).all()
    results: List[Dict[str]] = [
        {
            'company_plane_id': company_plane_info.id,
            'company_name': company_plane_info.air_company_name,
            'plane_id': company_plane_info.plane_id,
        } for company_plane_info in company_plane_infos
    ]
    return results
