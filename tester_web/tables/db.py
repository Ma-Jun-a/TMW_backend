# import cx_Oracle
# def get_seal(**kwargs):
#     connection = cx_Oracle.connect(TICKET_BASE, DB_PWD, DB_ADDR,encoding = "UTF-8", nencoding = "UTF-8")
#     cursor = connection.cursor()
#     agency_code = kwargs['agency_code']
#     admdiv_code = kwargs['admdiv_code']
#     try:
#         sql = "SELECT T.SEALID,T.SEALNAME,T.SEALHASH FROM FT_AGENCY_SEAL_DETAIL T WHERE T.AGENCY_CODE='{agency_code}' AND ADMDIV_CODE='{admdiv_code}'".format(agency_code=agency_code,admdiv_code=admdiv_code)
#         cursor.execute(sql)
#         re = cursor.fetchall()
#         cursor.close()
#         connection.commit()
#         connection.close()
#         if re is not []:
#             return re
#         else:
#             raise ('没有获取到单位的印章信息')
#     except Exception as e:
#         print(e)
