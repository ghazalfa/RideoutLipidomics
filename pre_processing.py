import csv
from openpyxl import load_workbook 
from openpyxl import Workbook

wb = load_workbook(filename = '/Users/ghazalfallahpour/Desktop/20221004_FlyBrain_Lipids_Summary.xlsx')
wb1 = Workbook()


    
sheet = wb.worksheets[2]


# Define the start and end rows
start_row = 2
end_row = 1350

start_col = 4
end_col = 29


total = {}




for row in sheet.iter_rows(min_row=start_row, max_row=end_row):

    for cell in row[start_col-1:end_col]:
        
        
        if  cell.col_idx==4:
            if 'w/o' in cell.value:
                state = False
            elif 'Unknown' in cell.value:
                state = False
            elif 'RIKEN' in cell.value:
                state = False
            else:
                state = True
                
            if state == True:
                 metaName = cell.value
                 if total.get(metaName) == None:
                     #updating metabolite name to each dictionary
                     total.update({metaName: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]})
                     
        if state == True:
            
            if cell.col_idx>5:
                
                    #this gets tge list for that specific metabolite name
                    allValues = total[metaName]
                    
                    #this gets the list for that specific genotype
                    specificValue = allValues[cell.col_idx-6]
                    specificValue = specificValue + cell.value
                    allValues[cell.col_idx-6]=specificValue
                    total.update({metaName:allValues})
                    
wb = load_workbook(filename = '/Users/ghazalfallahpour/Desktop/20221004_FlyBrain_Lipids_Summary.xlsx')

wb.sheetnames
sheet = wb.active
sheet = wb.active

# Define the start and end rows
start_row = 2
end_row = 4200

start_col = 4
end_col = 29


totalNeg = {}


for row in sheet.iter_rows(min_row=start_row, max_row=end_row):

    for cell in row[start_col-1:end_col]:
        
        
        if  cell.col_idx==4:
            if 'w/o' in cell.value:
                state = False
            elif 'Unknown' in cell.value:
                state = False
            elif 'RIKEN' in cell.value:
                state = False
            else:
                state = True
                
            if state == True:
                 metaName = cell.value
                 if totalNeg.get(metaName) == None:
                     #updating metabolite name to each dictionary
                     totalNeg.update({metaName: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]})
                     
        if state == True:
            
            if cell.col_idx>5:
                
                    #this gets tge list for that specific metabolite name
                    allValues = totalNeg[metaName]
                    
                    #this gets the list for that specific genotype
                    specificValue = allValues[cell.col_idx-6]
                    specificValue = specificValue + cell.value
                    allValues[cell.col_idx-6]=specificValue
                    totalNeg.update({metaName:allValues})
                 
for metaName in totalNeg:
    counter = 0
    sum = 0
    sumAvg = 0
    if total.get(metaName) == None:
        total.update({metaName: totalNeg[metaName]})
    else:
        while counter <24 :
            sum = total[metaName][counter]+totalNeg[metaName][counter]
            sumAvg = sum/2
            total[metaName][counter] = sumAvg
            counter +=1
            
        
        
        
        
        
        
