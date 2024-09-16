def members_count (membership:str):
    sqlite_lib.connect('ecomm.db')
    count = sqlite_lib.run_query_select(f'SELECT COUNT ("Customer ID")'
                                        f'FROM "E-commerce Customer Behavior - Sheet1"'
                                        f'WHERE "Membership Type" = "{membership}" ')
    sqlite_lib.close()
    return count[0][0]

print(members_count('Gold'))
