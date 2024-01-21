#P and T test for All Lipids

from scipy.stats import ttest_ind
from openpyxl import Workbook
import pandas as pd

wb1 = Workbook()

SEWF = 4
EEWF = 8

SWBF = 12
EWBF = 16

SEBF = 20
EEBF = 24


avgFoldEWF = {}
tTestEWF = {}
pTestEWF = {}

avgFoldWBF = {}
tTestWBF = {}
pTestWBF = {}


invalidFoldChange = []

for metaName in total:
    
    temp = total.get(metaName)
    
    EWF = temp[SEWF:EEWF]
    WBF = temp[SWBF:EWBF]
    EBF = temp[SEBF:EEBF]
    
    avgEWF = sum(EWF)/len(EWF)
    avgEBF = sum(EBF)/len(EBF)
    
    if avgEBF>0:
        avg=avgEWF/avgEBF
    else:
        invalidFoldChange.append(metaName)
    

    t_statistic, p_value = ttest_ind(EWF, EBF)
    
    tTestEWF.update({metaName:t_statistic})
    pTestEWF.update({metaName:p_value})
    avgFoldEWF.update({metaName:avg})
    

    
    
    t_statistic, p_value = ttest_ind(WBF, EBF)
    
    avgWBF = sum(WBF)/len(WBF)
    if avgEBF>0:
        avg=avgWBF/avgEBF
    else:
        invalidFoldChange.append(metaName)
    
    tTestWBF.update({metaName:t_statistic})
    pTestWBF.update({metaName:p_value})
    avgFoldWBF.update({metaName:avg})
    
    
   
        


# Convert dictionary to DataFrame
df = pd.DataFrame(list(tTestEWF.items()), columns=['MetaName', 'Value'])

# Write DataFrame to Excel
writer = pd.ExcelWriter('totalTTestEBF.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)

# Define worksheet and cell formats
workbook = writer.book
worksheet = writer.sheets['Sheet1']
cell_format = workbook.add_format({'align': 'left'})

# Set column widths
worksheet.set_column('A:A', 30, cell_format)
worksheet.set_column('B:B', 20, cell_format)

# Save and close Excel file
writer.save()

# Convert dictionary to DataFrame
df = pd.DataFrame(list(pTestEWF.items()), columns=['MetaName', 'Value'])

# Write DataFrame to Excel
writer = pd.ExcelWriter('totalPTestEBF.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)

# Define worksheet and cell formats
workbook = writer.book
worksheet = writer.sheets['Sheet1']
cell_format = workbook.add_format({'align': 'left'})

# Set column widths
worksheet.set_column('A:A', 30, cell_format)
worksheet.set_column('B:B', 20, cell_format)

# Save and close Excel file
writer.save()


# Convert dictionary to DataFrame
df = pd.DataFrame(list(avgFoldEWF.items()), columns=['MetaName', 'Value'])

# Write DataFrame to Excel
writer = pd.ExcelWriter('totalAvgFoldEBF.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)

# Define worksheet and cell formats
workbook = writer.book
worksheet = writer.sheets['Sheet1']
cell_format = workbook.add_format({'align': 'left'})

# Set column widths
worksheet.set_column('A:A', 30, cell_format)
worksheet.set_column('B:B', 20, cell_format)

# Save and close Excel file
writer.save()



# Convert dictionary to DataFrame
df = pd.DataFrame(list(tTestWBF.items()), columns=['MetaName', 'Value'])

# Write DataFrame to Excel
writer = pd.ExcelWriter('totalTTestWBF.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)

# Define worksheet and cell formats
workbook = writer.book
worksheet = writer.sheets['Sheet1']
cell_format = workbook.add_format({'align': 'left'})

# Set column widths
worksheet.set_column('A:A', 30, cell_format)
worksheet.set_column('B:B', 20, cell_format)

# Save and close Excel file
writer.save()

# Convert dictionary to DataFrame
df = pd.DataFrame(list(pTestWBF.items()), columns=['MetaName', 'Value'])

# Write DataFrame to Excel
writer = pd.ExcelWriter('totalPTestWBF.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)

# Define worksheet and cell formats
workbook = writer.book
worksheet = writer.sheets['Sheet1']
cell_format = workbook.add_format({'align': 'left'})

# Set column widths
worksheet.set_column('A:A', 30, cell_format)
worksheet.set_column('B:B', 20, cell_format)

# Save and close Excel file
writer.save()


# Convert dictionary to DataFrame
df = pd.DataFrame(list(avgFoldWBF.items()), columns=['MetaName', 'Value'])

# Write DataFrame to Excel
writer = pd.ExcelWriter('totalAvgFoldWBF.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)

# Define worksheet and cell formats
workbook = writer.book
worksheet = writer.sheets['Sheet1']
cell_format = workbook.add_format({'align': 'left'})

# Set column widths
worksheet.set_column('A:A', 30, cell_format)
worksheet.set_column('B:B', 20, cell_format)

# Save and close Excel file
writer.save()
