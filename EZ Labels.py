# EZ Labels for the Zebra Printer by Haseeb Durrani

# Output XLS file name and location
out_xls_file = 'Desktop/STF_8.26.16.xls'

# The following variables must be entered by user to generate slide labels specific to the study
study_name = "STF" # What is the study name?
conditions = 4 # How many conditions are being tested?
donors = ["068825", "09A825", "G900825", "G35F825"] # List of Donors - Include date (MDD) if same donor is used for multiple experiments
doses = ["000", "020", "040", "080"] # List of doses

tpoints = ["00","12","24","36","48"]

slides_per_dose = 3 # How many slides per dose?
alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# WARNING: DO NOT CHANGE ANYTHING BELOW UNLESS YOU KNOW WHAT YOU ARE DOING!!!!
# One line of code: Slide Naming needs to be adjusted based on Slide Naming Scheme

import xlwt
from collections import OrderedDict
import numpy as np

book = xlwt.Workbook(encoding="utf-8")

sheet1 = book.add_sheet("Sheet 1")

style = xlwt.easyxf("font: bold 1; align: horiz center")

sheet1.write(0, 0, "Study Name", style)
sheet1.write(0, 1, "Time Point", style)
sheet1.write(0, 2, "Condition", style)
sheet1.write(0, 3, "Donor ID", style)
sheet1.write(0, 4, "Dose", style)
sheet1.write(0, 5, "Slide Label", style)
sheet1.write(0, 6, "Slide # in Case", style)


prots = range(1, conditions + 1)
    
xrow = 1
c = 1 

for t in tpoints:

    for protocol_number in prots: 

        slide_number = 1
    
        for donor in donors:
    
            for dose in doses:

                for s in range(0, slides_per_dose):
            
                    sheet1.write(xrow, 0, str(study_name), style)
                    sheet1.write(xrow, 1, "T" + t, style)
                    sheet1.write(xrow, 2, "C" + str(protocol_number), style)
                    sheet1.write(xrow, 3, str(donor), style)
                    sheet1.write(xrow, 4, str(dose), style)
                    # The slide label text (below) needs to be adjusted any time there is a change in the slide naming scheme (Example: "C" for Con A # instead of "P" for Protocol #)
                    slide_label = study_name + "." + str(donor) + "C" + str(protocol_number) + "-" + str(t) + "." + str(dose) + alpha[s]
    
                    sheet1.write(xrow, 5, slide_label, style)
                    
                    
                    sheet1.write(xrow, 6, slide_number, style)
                            
                    xrow += 1
                    slide_number += 1

sheet1.col(0).width = 256 * (15)
sheet1.col(1).width = 256 * (15)
sheet1.col(2).width = 256 * (15)
sheet1.col(3).width = 256 * (15)
sheet1.col(4).width = 256 * (15)
sheet1.col(5).width = 256 * (30)
sheet1.col(6).width = 256 * (30)
sheet1.col(7).width = 256 * (30)
sheet1.col(8).width = 256 * (15)


book.save(out_xls_file)