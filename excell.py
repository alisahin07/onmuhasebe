from openpyxl import Workbook
wb = Workbook ()
ws = wb. active

testdata = [[ 'Name', 'City'] ,['Manish', 'Melbourne'], ['Rama', 'Bangalore'], ['Sam', 'London'] ]
for data in testdata:
    ws.append (data)
wb.save ("demoexcel.xlsx")
