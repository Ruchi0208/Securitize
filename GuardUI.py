import mysql.connector
import VisitorCheck_In
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="vishal2098",
#     database="CRIMINAL"
# )
# mycursor = mydb.cursor()


# def ShowPlateAndNumber(NumPlate):
#     window = Tk()
#     window.title('Check Plate')
#     # window.geometry('1000x1000')
#
#     plate_label = Label(window, text='PLATE', pady=20, font=('bold', 14))
#     plate_label.grid(row=0, column=0, sticky=E)
#
#
#     correctNumPlate_Text = StringVar()
#     l = [n + ' ' for n in NumPlate]
#     numPlate = ''
#     for c in l:
#         numPlate += c
#     correctNumPlate_Text.set(numPlate)
#     correctNumPlate = Entry(window, textvariable=correctNumPlate_Text, font='25')
#
#     correctNumPlate_Label = Label(window, text='NUMBER - PLATE', font=('bold', 14), pady=50)
#     correctNumPlate_Label.grid(row=4, column=0, sticky=E)
#     correctNumPlate.grid(row=4, column=3, sticky=EW)
#
#     return window, correctNumPlate_Text


def UIScreen(NumPlate):
    VisitorCheck_In.checkIn(NumPlate)
#     window, correctNumPlate_Text = ShowPlateAndNumber(NumPlate)
#     plateImg = PhotoImage(file="D:\\Projects\\OpenCV_3_License_Plate_Recognition_Python-master\\Plates\\imgPlate.png")
#     plateImg_label = Label(window, image=plateImg, pady=50, height=150)
#     plateImg_label.grid(row=0, column=3, sticky=E)
#
#     # Buttons
#     criminalCheck = Button(window, text='Check Theft', font=('bold', 20), bg='orange', command=lambda: CheckTheft(correctNumPlate_Text))
#     criminalCheck.grid(row=5, column=3, sticky=EW)
#
#     window.mainloop()
#
# def CheckTheft(correctNumPlate_Text):
#     NumPlate = correctNumPlate_Text.get()
#     numPlate = ''
#     for c in NumPlate:
#         if c != ' ':
#             numPlate += c
#     checkQuerry = f"SELECT * FROM CRIMINALS WHERE NUMBER_PLATE = '{numPlate}'"
#     mycursor.execute(checkQuerry)
#
#     myresult = mycursor.fetchall()
#     if len(myresult) == 0:
#         result = "Not found in theft record"
#         MessageBox.showinfo('Theft Status :', result)
#     else:
#         for row in myresult:
#             MessageBox.showinfo('Theft Status :', row)
# mydb.commit()