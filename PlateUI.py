from tkinter import *



window = Tk()
window.title('Check Plate')

plateImg = PhotoImage(file="D:\\Projects\\OpenCV_3_License_Plate_Recognition_Python-master\\Plates\\imgPlate.png")


plate_label = Label(window, text='PLATE', pady=20, padx=20)
plate_label.grid(row=0, column=1)

plateImg_label = Label(window, image=plateImg, padx = 20, pady=20)
plateImg_label.grid(row=0, column=5)

numPlate = "MCLRNF1"
# numPlate_label = Label(window, text = numPlate, font=('bold', 25))
# numPlate_label.grid(row=1, column=5)

correctNumPlate_Text = StringVar()
correctNumPlate_Text.set(numPlate)
correctNumPlate = Entry(window, textvariable=correctNumPlate_Text, font = ('bold', 14))
correctNumPlate_Label = Label(window, text='Plate Number', font=('bold', 14))
correctNumPlate_Label.grid(row=2, column=0)
correctNumPlate.grid(row=2, column=5)


window.mainloop()
