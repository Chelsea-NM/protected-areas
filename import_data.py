from .models import WdpaOecm
import csv

def import_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            WdpaOecm.objects.create(
        wdpaid=row['WDPAID'],
        wdpa_pid=row['WDPA_PID'],
        name=row['NAME'],  
        desig_eng=row['DESIG_ENG'],
        desig_type=row['DESIG_TYPE'],
        marine=row['MARINE'],
        status=row['STATUS'],
        status_yr=row['STATUS_YR'],
        gov_type=row['GOV_TYPE'],
        own_type=row['OWN_TYPE'],
        mang_auth=row['MANG_AUTH'],
        sub_loc=row['SUB_LOC'],
        parent_iso3=row['PARENT_ISO3'],
    )

if __name__ == '__main__':
    csv_file_path = 'csv-data/WDOECM_Public_ZAF.csv' 
    import_data(csv_file_path)
