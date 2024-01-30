from scipy.stats import ttest_ind
from openpyxl import Workbook
import pandas as pd

# Constants for column indices
SEWF, EEWF = 4, 8
SWBF, EWBF = 12, 16
SEBF, EEBF = 20, 24

# Dictionaries to store calculated values
avgFoldEWF, tTestEWF, pTestEWF = {}, {}, {}
avgFoldWBF, tTestWBF, pTestWBF = {}, {}, {}

# List to store metabolites with invalid fold changes
invalidFoldChange = []

# Loop through metabolites in the 'total' dictionary
for metaName in total:
    
    temp = total.get(metaName)
    
    # Extract sublists for EWF, WBF, and EBF
    EWF, WBF, EBF = temp[SEWF:EEWF], temp[SWBF:EWBF], temp[SEBF:EEBF]
    
    # Calculate average fold change for EWF and EBF
    avgEWF, avgEBF = sum(EWF) / len(EWF), sum(EBF) / len(EBF)
    
    # Calculate fold change and handle division by zero case
    if avgEBF > 0:
        avg_fold = avgEWF / avgEBF
    else:
        invalidFoldChange.append(metaName)
    
    # Perform t-test for EWF vs EBF
    t_statistic, p_value = ttest_ind(EWF, EBF)
    
    # Update dictionaries with calculated values
    tTestEWF.update({metaName: t_statistic})
    pTestEWF.update({metaName: p_value})
    avgFoldEWF.update({metaName: avg_fold})
    
    # Perform t-test for WBF vs EBF
    t_statistic, p_value = ttest_ind(WBF, EBF)
    
    # Calculate average fold change for WBF and handle division by zero case
    avgWBF = sum(WBF) / len(WBF)
    if avgEBF > 0:
        avg_fold = avgWBF / avgEBF
    else:
        invalidFoldChange.append(metaName)
    
    # Update dictionaries with calculated values for WBF
    tTestWBF.update({metaName: t_statistic})
    pTestWBF.update({metaName: p_value})
    avgFoldWBF.update({metaName: avg_fold})

# Convert dictionaries to DataFrames
df_tTestEWF = pd.DataFrame(list(tTestEWF.items()), columns=['MetaName', 'Value'])
df_pTestEWF = pd.DataFrame(list(pTestEWF.items()), columns=['MetaName', 'Value'])
df_avgFoldEWF = pd.DataFrame(list(avgFoldEWF.items()), columns=['MetaName', 'Value'])

df_tTestWBF = pd.DataFrame(list(tTestWBF.items()), columns=['MetaName', 'Value'])
df_pTestWBF = pd.DataFrame(list(pTestWBF.items()), columns=['MetaName', 'Value'])
df_avgFoldWBF = pd.DataFrame(list(avgFoldWBF.items()), columns=['MetaName', 'Value'])

# Function to save DataFrame to Excel
def save_to_excel(df, filename):
    writer = pd.ExcelWriter(filename, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)

    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    cell_format = workbook.add_format({'align': 'left'})

    worksheet.set_column('A:A', 30, cell_format)
    worksheet.set_column('B:B', 20, cell_format)

    writer.save()

# Save DataFrames to Excel files
save_to_excel(df_tTestEWF, 'totalTTestEBF.xlsx')
save_to_excel(df_pTestEWF, 'totalPTestEBF.xlsx')
save_to_excel(df_avgFoldEWF, 'totalAvgFoldEBF.xlsx')

save_to_excel(df_tTestWBF, 'totalTTestWBF.xlsx')
save_to_excel(df_pTestWBF, 'totalPTestWBF.xlsx')
save_to_excel(df_avgFoldWBF, 'totalAvgFoldWBF.xlsx')

