import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from PIL import ImageTk
import datetime
'''
window1 = tk.Tk()
window1.title("咖啡廳推薦")
window1.geometry("500x300")
cafe_v1 = tk.IntVar()
#plug_lable = tk.Lable(window1, text = "有無插座", font = ("微軟正黑體",20))

#plug_btn1 = tk.Checkbutton(window1, text = "有", variable = cafe_v1, 
# onvalue = 1,offvalue = 0,command = selection).pack()
#plug_btn2 = tk.Checkbutton(window1, text = "無", variable = cafe_v2,
# onvalue = 1,offvalue = 0,command = selection).pack()
plug_btn1 = tk.Radiobutton(window1, text = "有", variable = cafe_v1,value = 1).pack()
plug_btn2 = tk.Radiobutton(window1, text = "無", variable = cafe_v1,value = 2).pack()
plug_btn3 = tk.Radiobutton(window1, text = "皆可", variable = cafe_v1,value = 3).pack()

def selection():
  if (cafe_v1 == 1):
    print("yes")

window1.mainloop()
'''
def change_window(frame):
    frame.tkraise()

class cafeteria(tk.Frame):
  def __init__(self):
    tk.Frame.__init__(self)
    self.grid()
    self.createWidgets()
  
  def createWidgets(self):
    f1 = tkFont.Font(family = "微軟正黑體")
    
    #選擇咖啡廳條件
    self.welcome_label = tk.Label(self,text = "請選擇您想要的條件", font = f1)
    self.welcome_label.grid(row = 0 , column = 0 , sticky = tk.NE + tk.SW)
    
    #有無插座
    self.plug_var = tk.IntVar()
    self.plug_label = tk.Label(self, text = "有無插座",font = f1)
    self.plug_btn1 = tk.Radiobutton(self, text = "有", variable = self.plug_var, value = 1, font = f1) 
    self.plug_btn2 = tk.Radiobutton(self, text = "無", variable = self.plug_var, value = 0, font = f1) 
    self.plug_btn3 = tk.Radiobutton(self, text = "皆可",variable = self.plug_var, value = 2, font = f1) 
    self.plug_label.grid(row = 4, column = 0, sticky = tk.NE + tk.SW)
    self.plug_btn1.grid(row = 4, column = 1, sticky = tk.NE + tk.SW)
    self.plug_btn2.grid(row = 4, column = 2, sticky = tk.NE + tk.SW)
    self.plug_btn3.grid(row = 4, column = 3, sticky = tk.NE + tk.SW)

    #有無wifi
    self.wifi_var = tk.IntVar()
    self.wifi_label = tk.Label(self, text = "有無Wifi",font = f1)
    self.wifi_btn1 = tk.Radiobutton(self, text = "有", variable = self.wifi_var, value = 1, font = f1)
    self.wifi_btn2 = tk.Radiobutton(self, text = "無", variable = self.wifi_var, value = 0, font = f1)
    self.wifi_btn3 = tk.Radiobutton(self, text = "皆可", variable = self.wifi_var, value = 2, font = f1)
    self.wifi_label.grid(row = 5, column = 0, sticky = tk.NE + tk.SW)
    self.wifi_btn1.grid(row = 5, column = 1, sticky = tk.NE + tk.SW)
    self.wifi_btn2.grid(row = 5, column = 2, sticky = tk.NE + tk.SW)
    self.wifi_btn3.grid(row = 5, column = 3, sticky = tk.NE + tk.SW)  

    #有無寵物
    self.pet_var = tk.IntVar()
    self.pet_label = tk.Label(self, text = "有無寵物",font = f1)
    self.pet_btn1 = tk.Radiobutton(self, text = "有", variable = self.pet_var, value = 1, font = f1)
    self.pet_btn2 = tk.Radiobutton(self, text = "無", variable = self.pet_var, value = 0, font = f1)
    self.pet_btn3 = tk.Radiobutton(self, text = "皆可", variable = self.pet_var, value = 2, font = f1)
    self.pet_label.grid(row = 6, column = 0, sticky = tk.NE + tk.SW)
    self.pet_btn1.grid(row = 6, column = 1, sticky = tk.NE + tk.SW)
    self.pet_btn2.grid(row = 6, column = 2, sticky = tk.NE + tk.SW)
    self.pet_btn3.grid(row = 6, column = 3, sticky = tk.NE + tk.SW)

    #是否限時
    self.limit_var = tk.IntVar()
    self.limit_label = tk.Label(self, text = "是否限時",font = f1)
    self.limit_btn1 = tk.Radiobutton(self, text = "有", variable = self.limit_var, value = 1, font = f1)
    self.limit_btn2 = tk.Radiobutton(self, text = "無", variable = self.limit_var, value = 0, font = f1)
    self.limit_btn3 = tk.Radiobutton(self, text = "皆可", variable = self.limit_var, value = 2, font = f1)
    self.limit_label.grid(row = 7, column = 0, sticky = tk.NE + tk.SW)
    self.limit_btn1.grid(row = 7, column = 1, sticky = tk.NE + tk.SW)
    self.limit_btn2.grid(row = 7, column = 2, sticky = tk.NE + tk.SW)
    self.limit_btn3.grid(row = 7, column = 3, sticky = tk.NE + tk.SW)

    #選擇所在地區
    self.place_label = tk.Label(self, text = "地區", font = f1)
    self.place_btn = ttk.Combobox(self, values = ["基隆","宜蘭","台北","新北市","桃園","新竹","苗栗","台中","彰化",
        "南投","雲林","嘉義","台南","高雄","屏東","台東","花蓮","金門","馬祖","澎湖"])
    self.place_btn.current(2)
    self.place_label.grid(row = 1, column = 0, sticky = tk.NE + tk.SW)
    self.place_btn.grid(row = 1, column = 1, columnspan = 3,sticky = tk.NE + tk.SW)

    #選擇咖啡廳風格
    self.type_label = tk.Label(self, text = "風格", font = f1)
    self.type_btn = ttk.Combobox(self, values = ["老宅風","文青風","工業風","網美風","不限"])
    self.type_btn.current(4)
    self.type_label.grid(row = 2, column = 0, sticky = tk.NE + tk.SW)
    self.type_btn.grid(row = 2,column = 1, columnspan = 3,sticky = tk.NE + tk.SW) 

    #選擇想去的時間
    self.gotime_label = tk.Label(self, text = "想去的時間", font = f1)
    self.time_btn = ttk.Combobox(self, values = ["7:00","8:00","9:00","10:00","11:00","12:00","13:00","14:00",
              "15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00","24:00"])
    self.time_btn.current(0)
    self.gotime_label.grid(row = 3, column = 0, sticky = tk.NE + tk.SW)
    self.time_btn.grid(row = 3, column = 1, columnspan = 3,sticky = tk.NE + tk.SW)

    #送出
    self.confirm_btn = tk.Button(self,text = "確認", command = self.clickConfirmBtn, font = f1)
    self.confirm_btn.grid(row = 8, column = 1,sticky = tk.NE + tk.SW)
    
    lb_btn_list = [self.place_label,self.place_btn,self.type_label,self.type_btn,self.gotime_label,self.time_btn,
    self.plug_label,self.plug_btn1,self.plug_btn2,self.plug_btn3,self.wifi_label,self.wifi_btn1,self.wifi_btn2,
    self.wifi_btn3,self.pet_label,self.pet_btn1,self.pet_btn2,self.pet_btn3,self.limit_label,self.limit_btn1,self.limit_btn2,self.limit_btn3]
    
    #按鈕根據視窗調整大小
    row_number = 0
    column_number = 0
    for lb_btn in lb_btn_list:
      self.rowconfigure(row_number,weight = 1)
      self.columnconfigure(column_number,weight = 1)
      row_number += 1
      column_number += 1

  
  def clickPlugBtn(self):
    if self.plug_var > 0: 
      return True
  def clickWifiBtn(self):
    if self.wifi_var > 0:
      return True
  def clickPetBtn(self):
    if self.pet_var > 0:
      return True
  def clickLimitBtn(self):
    if self.limit_var > 0:
      return True
  def clickPlaceBtn(self):
    return self.place_btn.get()
  def clickTypeBtn(self):
    return self.type_btn.get()
  def clickTimeBtn(self):
   return (datetime.today().strftime('%A') + self.time_btn.get())
  def clickConfirmBtn(self):
    print(self.place_btn.get()+self.type_btn.get()+self.time_btn.get())


cafe = cafeteria()
cafe.master.title("咖啡廳推薦")
cafe.mainloop()
