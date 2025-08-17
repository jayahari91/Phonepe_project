import pandas as pd
import json
import os
import pymysql
import mysql.connector


path=r"D:\Phonepe\pulse-master\data\aggregated\transaction\country\india\state\\"
Agg_state_list=os.listdir(path)
print(Agg_state_list)

clm={'State':[], 'Year':[],'Quater':[],'Transacion_type':[], 'Transacion_count':[], 'Transacion_amount':[]}

for st in Agg_state_list:
    st_1=path+st+"/"
    Agg_yr=os.listdir(st_1)
    for yr in Agg_yr:
        yr_1=st_1+yr+"/"
        Agg_yr_list=os.listdir(yr_1)
        for file in Agg_yr_list:
            file_1=yr_1+file
            Data=open(file_1,'r')
            D=json.load(Data)
            for z in D['data']['transactionData']:
              Name=z['name']
              count=z['paymentInstruments'][0]['count']
              amount=z['paymentInstruments'][0]['amount']
              clm['Transacion_type'].append(Name)
              clm['Transacion_count'].append(count)
              clm['Transacion_amount'].append(amount)
              clm['State'].append(st)
              clm['Year'].append(yr)
              clm['Quater'].append(int(file.strip('.json')))

Agg_Trans=pd.DataFrame(clm)
#Agg_user
Path2=r"D:\Phonepe\pulse-master\data\aggregated\user\country\india\state\\"
Agg_user_list=os.listdir(Path2)

clm2={'States':[], 'Years':[],'Quarter':[],'Brands':[], 'Transaction_count':[], 'Percentage':[]}

for st in Agg_user_list:
    st_2=Path2+st+"/"
    Agg_yr=os.listdir(st_2)
    for yr in Agg_yr:
        yr_2=st_2+yr+"/"
        Agg_yr_list=os.listdir(yr_2)
        for file in Agg_yr_list:
            file_2=yr_2+file
            Data2=open(file_2,"r")
            E=json.load(Data2)

            try:
                for z in E['data']['usersByDevice']:
                    brands=z['brand']
                    count=z['count']
                    percentage=z['percentage']
                    clm2['Brands'].append(brands)
                    clm2['Transaction_count'].append(count)
                    clm2['Percentage'].append(percentage)
                    clm2['States'].append(st)
                    clm2['Years'].append(yr)
                    clm2['Quarter'].append(int(file.strip('.json')))

            except:
                pass

Agg_user=pd.DataFrame(clm2)

# Aggregate insurance

Path3=r"D:\Phonepe\pulse-master\data\aggregated\insurance\country\india\state\\"
Agg_insur_list=os.listdir(Path3)

clm3= {"States":[], "Years":[], "Quarter":[], "Insurance_type":[], "Insurance_count":[],"Insurance_amount":[] }

for st in Agg_insur_list:
    st_3=Path3+st+"/"
    Agg_yr=os.listdir(st_3)
    for yr in Agg_yr:
        yr_3=st_3+yr+"/"
        Agg_yr_list=os.listdir(yr_3)
        for file in Agg_yr_list:
            file_3=yr_3+file
            Data3=open(file_3,"r")
            F=json.load(Data3)

            
            for i in F["data"]["transactionData"]:
                Name = i["name"]
                count = i["paymentInstruments"][0]["count"]
                amount = i["paymentInstruments"][0]["amount"]
                clm3["Insurance_type"].append(Name)
                clm3["Insurance_count"].append(count)
                clm3["Insurance_amount"].append(amount)
                clm3["States"].append(st)
                clm3["Years"].append(yr)
                clm3["Quarter"].append(int(file.strip(".json")))

Agg_insur=pd.DataFrame(clm3)
# #Map Transaction

Path4=r"D:\Phonepe\pulse-master\data\map\transaction\hover\country\india\state\\"
Map_tran_list=os.listdir(Path4)

clm4={'States':[], 'Years':[],'Quarter':[],'District':[], 'Transaction_count':[], 'Transaction_amount':[]}

for st in Map_tran_list:
    st_4=Path4+st+"/"
    Map_yr=os.listdir(st_4)
    for yr in Map_yr:
        yr_4=st_4+yr+"/"
        Map_yr_list=os.listdir(yr_4)
        for file in Map_yr_list:
            file_4=yr_4+file
            Data4=open(file_4,"r")
            J=json.load(Data4)
            
            for z in J['data']['hoverDataList']:
              Name=z['name']
              count=z['metric'][0]['count']
              amount=z['metric'][0]['amount']
              clm4['District'].append(Name)
              clm4['Transaction_count'].append(count)
              clm4['Transaction_amount'].append(amount)
              clm4['States'].append(st)
              clm4['Years'].append(yr)
              clm4['Quarter'].append(int(file.strip('.json')))  

Map_trans=pd.DataFrame(clm4)
#Map users

Path5=r"D:\Phonepe\pulse-master\data\map\user\hover\country\india\state\\"
Map_user_list=os.listdir(Path5)

clm5={"States":[], "Years":[], "Quarter":[], "District":[], "RegisteredUser":[], "AppOpens":[]}
for st in Map_user_list:
    st_5=Path5+st+"/"
    Map_yr=os.listdir(st_5)
    for yr in Map_yr:
        yr_5=st_5+yr+"/"
        Map_yr_list=os.listdir(yr_5)
        for file in Map_yr_list:
            file_5=yr_5+file
            Data5=open(file_5,"r")
            K=json.load(Data5)

            for i in K["data"]["hoverData"].items():
                district = i[0]
                registereduser = i[1]["registeredUsers"]
                appopens = i[1]["appOpens"]
                clm5["District"].append(district)
                clm5["RegisteredUser"].append(registereduser)
                clm5["AppOpens"].append(appopens)
                clm5["States"].append(st)
                clm5["Years"].append(yr)
                clm5["Quarter"].append(int(file.strip(".json")))



Map_users=pd.DataFrame(clm5)
#Map Insurence

Path6=r"D:\Phonepe\pulse-master\data\map\insurance\hover\country\india\state\\"
Map_insur_list=os.listdir(Path6)

clm6= {"States":[], "Years":[], "Quarter":[], "District":[], "Transaction_count":[],"Transaction_amount":[] }

for st in Agg_insur_list:
    st_6=Path6+st+"/"
    Agg_yr=os.listdir(st_6)
    for yr in Agg_yr:
        yr_6=st_6+yr+"/"
        Agg_yr_list=os.listdir(yr_6)
        for file in Agg_yr_list:
            file_6=yr_6+file
            Data6=open(file_6,"r")
            G=json.load(Data6)

            
            for i in G["data"]["hoverDataList"]:
                    name = i["name"]
                    count = i["metric"][0]["count"]
                    amount = i["metric"][0]["amount"]
                    clm6["District"].append(name)
                    clm6["Transaction_count"].append(count)
                    clm6["Transaction_amount"].append(amount)
                    clm6["States"].append(st)
                    clm6["Years"].append(yr)
                    clm6["Quarter"].append(int(file.strip(".json")))

Map_insur=pd.DataFrame(clm6)
# #Top Transaction

Path7=r"D:\Phonepe\pulse-master\data\top\transaction\country\india\state\\"
Top_tran_list=os.listdir(Path7)

clm7={"States":[], "Years":[], "Quarter":[], "Pincodes":[], "Transaction_count":[], "Transaction_amount":[]}

for st in Top_tran_list:
    st_7=Path7+st+"/"
    Top_yr=os.listdir(st_7)
    for yr in Top_yr:
        yr_7=st_7+yr+"/"
        Top_yr_list=os.listdir(yr_7)
        for file in Top_yr_list:
            file_7=yr_7+file
            Data7=open(file_7,"r")
            H=json.load(Data7)
            
            for i in H["data"]["pincodes"]:
                entityName = i["entityName"]
                count = i["metric"]["count"]
                amount = i["metric"]["amount"]
                clm7["Pincodes"].append(entityName)
                clm7["Transaction_count"].append(count)
                clm7["Transaction_amount"].append(amount)
                clm7["States"].append(st)
                clm7["Years"].append(yr)
                clm7["Quarter"].append(int(file.strip(".json")))  

Top_trans=pd.DataFrame(clm7)
#Top users

Path8=r"D:\Phonepe\pulse-master\data\top\user\country\india\state\\"
Top_user_list=os.listdir(Path8)

clm8={"States":[], "Years":[], "Quarter":[], "Pincodes":[], "RegisteredUser":[]}

for st in Top_user_list:
    st_8=Path8+st+"/"
    Map_yr=os.listdir(st_8)
    for yr in Map_yr:
        yr_8=st_8+yr+"/"
        Map_yr_list=os.listdir(yr_8)
        for file in Map_yr_list:
            file_8=yr_8+file
            Data8=open(file_8,"r")
            S=json.load(Data8)

            for i in S["data"]["pincodes"]:
                name = i["name"]
                registeredusers = i["registeredUsers"]
                clm8["Pincodes"].append(name)
                clm8["RegisteredUser"].append(registeredusers)
                clm8["States"].append(st)
                clm8["Years"].append(yr)
                clm8["Quarter"].append(int(file.strip(".json")))


Top_users=pd.DataFrame(clm8)
#Top Insurence

Path9=r"D:\Phonepe\pulse-master\data\top\insurance\country\india\state\\"
Top_insur_list=os.listdir(Path9)

clm9= {"States":[], "Years":[], "Quarter":[], "Pincodes":[], "Transaction_count":[], "Transaction_amount":[]}

for st in Top_insur_list:
    st_9=Path9+st+"/"
    Agg_yr=os.listdir(st_9)
    for yr in Agg_yr:
        yr_9=st_9+yr+"/"
        Agg_yr_list=os.listdir(yr_9)
        for file in Agg_yr_list:
            file_9=yr_9+file
            Data9=open(file_9,"r")
            P=json.load(Data9)

            
            for i in P["data"]["pincodes"]:
                entityName = i["entityName"]
                count = i["metric"]["count"]
                amount = i["metric"]["amount"]
                clm9["Pincodes"].append(entityName)
                clm9["Transaction_count"].append(count)
                clm9["Transaction_amount"].append(amount)
                clm9["States"].append(st)
                clm9["Years"].append(yr)
                clm9["Quarter"].append(int(file.strip(".json")))


Top_insur=pd.DataFrame(clm9)
#print(Top_insur)

# MySQL connection
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='12345'
)

cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS phonepe_data")
cursor.execute("USE phonepe_data")

#  Create table
# -------------------------------
# TABLE 1: agg_trans
# -------------------------------
table_1='''
    CREATE TABLE IF NOT EXISTS Agg_transaction (
        State VARCHAR(50),
        Year INT,
        Quater INT,
        TransactionType VARCHAR(50),
        TransactionCount BIGINT,
        TransactionAmount DOUBLE
    )
'''
cursor.execute(table_1)
connection.commit()

# 4. Insert all rows from DataFrame
insert_table1 = """
    INSERT INTO Agg_transaction
    (State, Year, Quater, TransactionType, TransactionCount, TransactionAmount)
    VALUES (%s, %s, %s, %s, %s, %s)
"""

for _, row in Agg_Trans.iterrows():
    cursor.execute(insert_table1, (
        row['State'],
        row['Year'],
        row['Quater'],
        row['Transacion_type'],
        row['Transacion_count'],
        row['Transacion_amount']
    ))

connection.commit()

print(f"Inserted {len(Agg_Trans)} rows top into agg_transaction successfully.")

# -------------------------------
# TABLE 2: agg_user
# -------------------------------

table2 = '''
    CREATE TABLE IF NOT EXISTS aggregated_user (
        States VARCHAR(50),
        Years INT,
        Quarter INT,
        Brands VARCHAR(50),
        Transaction_count BIGINT,
        Percentage FLOAT
    )
'''
cursor.execute(table2)
connection.commit()

insert_table2 = """
    INSERT INTO aggregated_user
    (States, Years, Quarter, Brands, Transaction_count, Percentage)
    VALUES (%s, %s, %s, %s, %s, %s)
"""
for _, row in Agg_user.iterrows():
    cursor.execute(insert_table2, (
        row["States"],
        row["Years"],
        row["Quarter"],
        row["Brands"],
        row["Transaction_count"],
        row["Percentage"]
    ))

connection.commit()
print(f"Inserted {len(Agg_user)} rows in to agg_user successfully.")
# -------------------------------
# TABLE 3: agg_insur
# -------------------------------

table3 = '''
    CREATE TABLE IF NOT EXISTS aggregated_insurance (
        States VARCHAR(50),
        Years INT,
        Quarter INT,
        Insurance_type VARCHAR(50),
        Insurance_count BIGINT,
        Insurance_amount BIGINT
    )
'''
cursor.execute(table3)
connection.commit()

insert_table3 = """
    INSERT INTO aggregated_insurance
    (States, Years, Quarter, Insurance_type, Insurance_count, Insurance_amount)
    VALUES (%s, %s, %s, %s, %s, %s)
"""
for _, row in Agg_insur.iterrows():
    cursor.execute(insert_table3, (
        row["States"],
        row["Years"],
        row["Quarter"],
        row["Insurance_type"],
        row["Insurance_count"],
        row["Insurance_amount"]
    ))

connection.commit()
print(f"Inserted {len(Agg_insur)} rows top into agg_insurance successfully.")

# -------------------------------
# TABLE 4: map_trans
# -------------------------------
table4 = '''
    CREATE TABLE IF NOT EXISTS map_trans (
        States VARCHAR(50),
        Years INT,
        Quarter INT,
        District VARCHAR(50),
        Transaction_count BIGINT,
        Transaction_amount FLOAT
    )
'''
cursor.execute(table4)
connection.commit()

insert_table4 = """
    INSERT INTO map_trans
    (States, Years, Quarter, District, Transaction_count, Transaction_amount)
    VALUES (%s, %s, %s, %s, %s, %s)
"""

for _, row in Map_trans.iterrows():
    cursor.execute(insert_table4, (
        row['States'],
        row['Years'],
        row['Quarter'],
        row['District'],
        row['Transaction_count'],
        row['Transaction_amount']
    ))
connection.commit()
print(f"Inserted {len(Map_trans)} rows into map_trans successfully.")

# -------------------------------
# TABLE 5: map_user
# -------------------------------
table5 = '''
    CREATE TABLE IF NOT EXISTS map_user (
        States VARCHAR(50),
        Years INT,
        Quarter INT,
        District VARCHAR(50),
        RegisteredUser BIGINT,
        AppOpens BIGINT
    )
'''
cursor.execute(table5)
connection.commit()

insert_table5 = """
    INSERT INTO map_user
    (States, Years, Quarter, District, RegisteredUser, AppOpens)
    VALUES (%s, %s, %s, %s, %s, %s)
"""

for _, row in Map_users.iterrows():
    cursor.execute(insert_table5, (
        row['States'],
        row['Years'],
        row['Quarter'],
        row['District'],
        row['RegisteredUser'],
        row['AppOpens']
    ))
connection.commit()
print(f"Inserted {len(Map_users)} rows into map_user successfully.")

# -------------------------------
# TABLE 6: map_insurance
# -------------------------------
table6 = '''
    CREATE TABLE IF NOT EXISTS map_insurance (
        States VARCHAR(50),
        Years INT,
        Quarter INT,
        District VARCHAR(50),
        Transaction_count BIGINT,
        Transaction_amount FLOAT
    )
'''
cursor.execute(table6)
connection.commit()

insert_table6 = """
    INSERT INTO map_insurance
    (States, Years, Quarter, District, Transaction_count, Transaction_amount)
    VALUES (%s, %s, %s, %s, %s, %s)
"""
for _, row in Map_insur.iterrows():
    cursor.execute(insert_table6, (
        row['States'],
        row['Years'],
        row['Quarter'],
        row['District'],
        row['Transaction_count'],
        row['Transaction_amount']
    ))
connection.commit()
print(f"Inserted {len(Map_insur)} rows into map_insurance successfully.")

# -------------------------------
# TABLE 7: top_transaction
# -------------------------------
table7 = '''
    CREATE TABLE IF NOT EXISTS top_transaction (
        States VARCHAR(50),
        Years INT,
        Quarter INT,
        Pincodes INT,
        Transaction_count BIGINT,
        Transaction_amount BIGINT
    )
'''
cursor.execute(table7)
connection.commit()

insert_table7 = """
    INSERT INTO top_transaction
    (States, Years, Quarter, Pincodes, Transaction_count, Transaction_amount)
    VALUES (%s, %s, %s, %s, %s, %s)
"""

for _, row in Top_trans.iterrows():
    cursor.execute(insert_table7, (
        row["States"],
        row["Years"],
        row["Quarter"],
        row["Pincodes"],
        row["Transaction_count"],
        row["Transaction_amount"]
    ))
connection.commit()
print(f"Inserted {len(Top_trans)} rows into top_transaction successfully.")


# -------------------------------
# TABLE 8: top_user
# -------------------------------
table8 = '''
    CREATE TABLE IF NOT EXISTS top_user (
        States VARCHAR(50),
        Years INT,
        Quarter INT,
        Pincodes INT,
        RegisteredUser BIGINT
    )
'''
cursor.execute(table8)
connection.commit()

insert_table8 = """
    INSERT INTO top_user
    (States, Years, Quarter, Pincodes, RegisteredUser)
    VALUES (%s, %s, %s, %s, %s)
"""

for _, row in Top_users.iterrows():
    cursor.execute(insert_table8, (
        row["States"],
        row["Years"],
        row["Quarter"],
        row["Pincodes"],
        row["RegisteredUser"]
    ))
connection.commit()
print(f"Inserted {len(Top_users)} rows into top_user successfully.")


# -------------------------------
# TABLE 9: top_insurance
# -------------------------------
table9 = '''
    CREATE TABLE IF NOT EXISTS top_insurance (
        States VARCHAR(50),
        Years INT,
        Quarter INT,
        Pincodes INT,
        Transaction_count BIGINT,
        Transaction_amount BIGINT
    )
'''
cursor.execute(table9)
connection.commit()

insert_table9 = """
    INSERT INTO top_insurance
    (States, Years, Quarter, Pincodes, Transaction_count, Transaction_amount)
    VALUES (%s, %s, %s, %s, %s, %s)
"""

for _, row in Top_insur.iterrows():
    cursor.execute(insert_table9, (
        row["States"],
        row["Years"],
        row["Quarter"],
        row["Pincodes"],
        row["Transaction_count"],
        row["Transaction_amount"]
    ))
connection.commit()
print(f"Inserted {len(Top_insur)} rows into top_insurance successfully.")

# Close
cursor.close()
connection.close()