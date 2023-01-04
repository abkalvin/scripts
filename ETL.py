import psycopg2
import csv
import collections
import xlsxwriter
import pandas as pd

conn = psycopg2.connect(
    host="wally-datateam.c0gbuyodkzl0.us-east-2.rds.amazonaws.com",
    database="wally",
    user="postgres",
    password="aINK0$RfGOv9BdPn1Azfjq6ckr$NfRcjevRd#Y$BODN$wxrcrHetOd8agp3N3FuX")
cur = conn.cursor()
curs = conn.cursor()
cur.execute('select distinct "orgId" from wallycore')
res = cur.fetchall()
res.pop(1)
res.pop(18)

for first in res:
    last = "_site_wise_audit_info"
    table = str(first[0])+last
    dou = '"'+table+'"'
    curs.execute("Select category_counts from "+dou)
    ress = curs.fetchall()
    r = []
    re =[]
    for i in ress:
        for n in i:
            re.append(n)

    counter = collections.Counter()
#     # list(re)
#     # print(type(re))
    for d in re:
        counter.update(d)
    result = tuple(counter.items())
#     # with open('C:\\Users\FleetStudio-14\Documents\Rule_count2.xlsx', 'w') as output:
#     #     writer = csv.writer(output)
#     #     writer.writerow(["Rule_number", "Count"])
#     #     for key, value in result.items():
#     #         writer.writerow([key, value])
    df = pd.DataFrame(result)


    if not df.empty:

        df.columns = ['Rule_number', 'Count']
        final_df = df.sort_values(by='Count')
        #print(final_df)
    firstpath= "C:\\Users\FleetStudio-14\Documents\\"
    secondpath= table
    thirdpath = ".xlsx"
    finalpath=firstpath+secondpath+thirdpath
    writer = pd.ExcelWriter("C:\\Users\FleetStudio-14\Documents\\kalvin.xlsx", engine='xlsxwriter')
    final_df.to_excel(writer, sheet_name=table, index=False)
    writer.save()