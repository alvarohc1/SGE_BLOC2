import dict_to_db as d_t_db
import pandas as pd

def csv_to_dict():
    df = pd.read_csv("/home/isard/SGE_DAMM/SGE_BLOC2/bloc2_AlvaroHuamani/send_data_to_db/Clientes.csv")
    d  = df.to_dict(orient='list')
    return d

data = csv_to_dict()

for i in range(1):
    d_t_db.send_data_to_db(i, data)