from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
'''d=((1,2,3,4),(11,12,13,14),(21,22,23,24),(31,32,33,34))
for i in d:
    sheet.append(i)'''
data=(('Name','Age','DOB','Location'),('Karthik',22,1999,'Bangalore'),('Rajesh',23,1998,'Chittoor'),('Sanju',19,2001,'Bangalore'))
for i in data:
    sheet.append(i)
for i in sheet.iter_rows(min_row=1,min_col=1,max_row=4,max_col=4):
    for j in i:
        print(j.value,sep=' ',end=' ')
    print()
wb.save('c:\\Users\\178342\\Documents\\xsheet2.xlsx')
