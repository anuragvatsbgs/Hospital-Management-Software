from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
import mysql.connector
from kivymd.uix.snackbar import Snackbar
from kivy.metrics import dp
from kivy.utils import platform
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window
#from kivymd.uix.list import ThreeLineAvatarListItem
from kivymd.uix.list import ThreeLineListItem
from kivymd.app import MDApp
import os
from fpdf import FPDF, HTMLMixin
from datetime import datetime
from fpdf import FPDF, HTMLMixin
import re

class PDF(FPDF, HTMLMixin):
    pass
try:
    err=0
    mycon=mysql.connector.connect(host="localhost",port="3306" ,user="root",password="Kumar4285@",database="HOSPITAL",auth_plugin="mysql_native_password")
    mycursor = mycon.cursor()
    #mycursor.execute("")
    #database.commit()
except Exception as e:
    print(e)

class hospitalmanagementsystem(MDApp):
    global screen_manager
    screen_manager = ScreenManager()
    def build(self):
        login=Builder.load_file("log_in.kv")
        signin=Builder.load_file("sign_in.kv")
        about_us=Builder.load_file("about_us.kv")
        faq=Builder.load_file("faq.kv")
        main=Builder.load_file("main.kv")
        help_support=Builder.load_file("help_support.kv")
        pasd=Builder.load_file("password.kv")
        addd=Builder.load_file("add_patient.kv")
        searchh=Builder.load_file("search.kv")
        deletee=Builder.load_file("delete.kv")
        patient_detailss=Builder.load_file("patient_details.kv")
        search_blood=Builder.load_file("search_blood.kv")
        add_donor=Builder.load_file("add_donor.kv")
        update1_patient=Builder.load_file("update1_patient_details.kv")
        donate_bloods=Builder.load_file("donate_blood.kv")
        discharges=Builder.load_file("discharge.kv")
        prep_bills=Builder.load_file("prepare_bill.kv")
        blood_data=Builder.load_file("blood_group_details.kv")
        details_group=Builder.load_file("details_blood.kv")
        detail_update=Builder.load_file("details_update.kv")
        organ_donor_ids=Builder.load_file("organ_donor_id.kv")
        final_pdf=Builder.load_file("final_bill.kv")
        donor_delete_details=Builder.load_file("donor_delete.kv")
        z_name_patients=Builder.load_file("z_patient_name_update.kv")
        z_mobile_patients=Builder.load_file("z_mobile_update.kv")
        z_age_patients=Builder.load_file("z_age_update.kv")
        z_sex_patients=Builder.load_file("z_sex_update.kv")
        z_marital_patients=Builder.load_file("z_marital_update.kv")
        z_blood_patients=Builder.load_file("z_blood_update.kv")
        z_address_patients=Builder.load_file("z_address_update.kv")
        forget=Builder.load_file("forget_password.kv")

        screen_manager.add_widget(login)                        # Add log in screenwith screenmanager
        screen_manager.add_widget(signin)
        screen_manager.add_widget(about_us)
        screen_manager.add_widget(main)                         # Add Main screen with screenmanager
        screen_manager.add_widget(help_support)
        screen_manager.add_widget(faq)
        screen_manager.add_widget(pasd)
        screen_manager.add_widget(addd)
        screen_manager.add_widget(searchh)
        screen_manager.add_widget(deletee)
        screen_manager.add_widget(patient_detailss)
        screen_manager.add_widget(search_blood)
        screen_manager.add_widget(add_donor)
        screen_manager.add_widget(update1_patient)
        screen_manager.add_widget(donate_bloods)
        screen_manager.add_widget(discharges)
        screen_manager.add_widget(prep_bills)
        screen_manager.add_widget(blood_data)
        screen_manager.add_widget(details_group)
        screen_manager.add_widget(detail_update)
        screen_manager.add_widget(organ_donor_ids)
        screen_manager.add_widget(final_pdf)
        screen_manager.add_widget(donor_delete_details)
        screen_manager.add_widget(z_name_patients)
        screen_manager.add_widget(z_mobile_patients)
        screen_manager.add_widget(z_age_patients)
        screen_manager.add_widget(z_sex_patients)
        screen_manager.add_widget(z_marital_patients)
        screen_manager.add_widget(z_blood_patients)
        screen_manager.add_widget(z_address_patients)
        screen_manager.add_widget(forget)
        # Add patient
        self.theme_cls.theme_style_switch_animation = True      # animation=true
        self.theme_cls.primary_palette ="BlueGray"              # Theme color
        screen_manager.transition.duration = .0
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "Password",
                "font_style" : 'H6',
                "font_name" : "Comic",
                "height": dp(60),
                "on_release": lambda x="Settings": self.reset_pasd(),
            },
            {
                "viewclass": "OneLineListItem",
                "text":"FAQ",
                "font_style" : 'H6',
                "font_name" : "Comic",
                "height": dp(60),
                "on_release": lambda x="Settings": self.faq(),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "About Us",
                "font_style" : 'H6',
                "font_name" : "Comic",
                "height": dp(60),
                "on_release": lambda x="Settings": self.about_us(),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Help & Support",
                "font_style" : 'H6',
                "font_name" : "Comic",
                "height": dp(60),
                "on_release": lambda x="Settings": self.help_support(),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Log Out",
                "font_style" : 'H6',
                "font_name" : "Comic",
                "height": dp(60),
                "on_release": lambda x="Log Out": self.log_out(),
            }]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=4,
        )

        return screen_manager                                   # Return screen manager
    def conf_sign_in(self):
        try:
            self.next1=screen_manager.get_screen('SIGNIN').ids.u_name.text
            self.next2=screen_manager.get_screen('SIGNIN').ids.u_hid.text
            self.next5=screen_manager.get_screen('SIGNIN').ids.u_staff_id.text
            self.next3=screen_manager.get_screen('SIGNIN').ids.cretpssd.text
            self.next4=screen_manager.get_screen('SIGNIN').ids.conf_passd.text
            self.next6=screen_manager.get_screen('SIGNIN').ids.aadhar.text
            exeqq="SELECT * FROM USERID WHERE STAFF_ID="+'"'+self.next5+'"'+";"
            mycursor.execute(exeqq)
            myresultta = mycursor.fetchall()
            if self.next1==""or self.next2=="" or self.next3==""or self.next4=="" or self.next5=="" or self.next6=="":
                cancel_btn_username_dialogue = MDFlatButton(text='Retry',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'Error',text = "Please Fill All Details",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
            elif self.next3!=self.next4:
                cancel_btn_username_dialogue = MDFlatButton(text='Retry',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'Error',text = "Password do not match",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
            elif myresultta==[]:
                g1=len(self.next6)
                if g1==12:
                    try:
                        int(self.next6)
                        exeqq="INSERT INTO USERID(STAFF_ID, STAFF_NAME, PASSWORD, HOSPITAL_ID, AADHAR_NUMBER) VALUES("+'"'+self.next5+'","'+self.next1+'","'+self.next3+'","'+self.next2+'" ,"'+self.next6+'"'+");"
                        mycursor.execute(exeqq)
                        mycon.commit()
                        cancel_btn_username_dialogue = MDFlatButton(text='Retry',on_release = self.close_username_dialogue)
                        self.dialog = MDDialog(title = 'Success',text = "Sign Up Successful",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                        self.dialog.open()
                    except:
                        cancel_btn_username_dialogue = MDFlatButton(text='Retry',on_release = self.close_username_dialogue)
                        self.dialog = MDDialog(title = 'Error',text = "Please Enter Aadhar Number in number format",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                        self.dialog.open()
                else:
                    cancel_btn_username_dialogue = MDFlatButton(text='Retry',on_release = self.close_username_dialogue)
                    self.dialog = MDDialog(title = 'Error',text = "Please Enter a Valid Aadhar Number",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                    self.dialog.open()
            else:
                cancel_btn_username_dialogue = MDFlatButton(text='Retry',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'Error',text = "UserId already exits",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def back2_home_in(self):
        self.dialog.dismiss()
    def close_username_dialogue(self,obj):
        self.dialog.dismiss()
    def on_start(self):
        screen_manager.current="LOGIN"
        screen_manager.get_screen('LOGIN').ids.uh_id.text ="BH2121"
        if err==1:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = "Please check your internet connection !",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def log_in(self):
        #screen_manager.current="Main"
        try:
            if screen_manager.get_screen('LOGIN').ids.uh_id.text!="" and screen_manager.get_screen('LOGIN').ids.us_id!="" and screen_manager.get_screen('LOGIN').ids.password_text_field!="":
                n1=screen_manager.get_screen('LOGIN').ids.us_id.text
                n4=screen_manager.get_screen('LOGIN').ids.uh_id.text
                n2="SELECT * FROM USERID WHERE STAFF_ID="+'"'+n1+'"'
                n3= screen_manager.get_screen('LOGIN').ids.password_text_field.text
                mycursor.execute(n2)
                result = mycursor.fetchall()
                if result==[]:
                    cancel_btn_username_dialogue = MDFlatButton(text='Retry',on_release = self.close_username_dialogue)
                    self.dialog = MDDialog(title = 'Error',text = "Please Enter a Valid Staff Id",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                    self.dialog.open()
                elif n4==result[0][3]:
                    fetch_1=result[0]
                    if n1==fetch_1[0]:
                        if n3==fetch_1[2]:
                            screen_manager.current="Main"
                        else:
                            cancel_btn_username_dialogue = MDFlatButton(text='Retry',on_release = self.close_username_dialogue)
                            self.dialog = MDDialog(title = 'Error',text = "Please Enter a Valid Password",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                            self.dialog.open()
                    else:
                        cancel_btn_username_dialogue = MDFlatButton(text='Retry',on_release = self.close_username_dialogue)
                        self.dialog = MDDialog(title = 'Error',text = "Please Enter a Valid Staff ID",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                        self.dialog.open()
                else:
                    cancel_btn_username_dialogue = MDFlatButton(text='Retry',on_release = self.close_username_dialogue)
                    self.dialog = MDDialog(title = 'Error',text = "Please Enter a Valid Hospital ID",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                    self.dialog.open()
            else:
                cancel_btn_username_dialogue = MDFlatButton(text='Retry',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'Error',text = "Please Fill All Details",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def add_success(self):
        try:
            as0=screen_manager.get_screen('ADD').ids.p_id.text
            as1=screen_manager.get_screen('ADD').ids.p_name.text
            as2=screen_manager.get_screen('ADD').ids.p_mobile_no.text
            as3=screen_manager.get_screen('ADD').ids.p_age.text
            as4=screen_manager.get_screen('ADD').ids.p_sex.text
            as5=screen_manager.get_screen('ADD').ids.p_marital.text
            as6=screen_manager.get_screen('ADD').ids.p_blood.text
            as01=screen_manager.get_screen('ADD').ids.P_house.text
            as02=screen_manager.get_screen('ADD').ids.p_street.text
            as03=screen_manager.get_screen('ADD').ids.p_city.text
            as04=screen_manager.get_screen('ADD').ids.p_state.text
            as05=screen_manager.get_screen('ADD').ids.p_country.text
            ns0=as01+'/'+as02+'/'+as03+'/'+as04+'/'+as05
            n01="'"+as0+"'"+","+"'"+as1+"'"+","+"'"+as2+"'"+","+"'"+as3+"'"+","+"'"+as4+"'"+","+"'"+as5+"'"+", "+"'"+as6+"'"+", "+"'"+ns0+"'"
            n02="INSERT INTO PATIENT(PATIENT_ID, PATIENT_NAME, MOBILE_NO, AGE, SEX, MARITAL_STATUS, BLOOD_GROUP, ADDRESS) VALUES("+n01+");"
            mycursor.execute(n02)
            mycon.commit()
            cancel_btn_username_dialogue = MDFlatButton(text='Close',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'Success !',text = "Successfully added on Databases",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def add_donor_success(self):
        try:
            as0=screen_manager.get_screen('ADD_DONOR_DETAILS').ids.d_id.text
            as1=screen_manager.get_screen('ADD_DONOR_DETAILS').ids.d_name.text
            as2=screen_manager.get_screen('ADD_DONOR_DETAILS').ids.d_mobile_no.text
            as3=screen_manager.get_screen('ADD_DONOR_DETAILS').ids.d_age.text
            as4=screen_manager.get_screen('ADD_DONOR_DETAILS').ids.d_sex.text
            as5=screen_manager.get_screen('ADD_DONOR_DETAILS').ids.d_marital.text
            as6=screen_manager.get_screen('ADD_DONOR_DETAILS').ids.d_blood.text
            as01=screen_manager.get_screen('ADD_DONOR_DETAILS').ids.d_house.text
            as02=screen_manager.get_screen('ADD_DONOR_DETAILS').ids.d_street.text
            as03=screen_manager.get_screen('ADD_DONOR_DETAILS').ids.d_city.text
            as04=screen_manager.get_screen('ADD_DONOR_DETAILS').ids.d_state.text
            as05=screen_manager.get_screen('ADD_DONOR_DETAILS').ids.d_country.text
            ns0=as01+'/'+as02+'/'+as03+'/'+as04+'/'+as05
            n01="'"+as0+"'"+","+"'"+as1+"'"+","+"'"+as2+"'"+","+"'"+as3+"'"+","+"'"+as4+"'"+","+"'"+as5+"'"+", "+"'"+as6+"'"+", "+"'"+ns0+"'"
            n02="INSERT INTO DONOR(DONOR_ID, DONOR_NAME, MOBILE_NO, AGE, SEX, MARITAL_STATUS, BLOOD_GROUP, ADDRESS) VALUES("+n01+");"
            mycursor.execute(n02)
            mycon.commit()
            cancel_btn_username_dialogue = MDFlatButton(text='Close',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'Success !',text = "Successfully added on Databases",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def organ_screen(self):
        screen_manager.current="DONATE_ORGAN"
    def screen_organ(self):
        try:
            de1=screen_manager.get_screen('ORGAN_DONOR_ID').ids.p_id.text
            d1="SELECT * FROM DONOR WHERE DONOR_ID ="+ '"'+de1+'"'+";"
            mycursor.execute(d1)
            fetch_1=mycursor.fetchall()
            if screen_manager.get_screen('ORGAN_DONOR_ID').ids.p_id.text!="":
                if fetch_1!=[]:
                    screen_manager.current="DONATE_ORGAN"
                else:
                    cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                    self.dialog = MDDialog(title = 'error !',text = "Donor ID Not Matched",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                    self.dialog.open()
            else:
                cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'Error !',text = "Please Enter Donor ID",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
        except Exception as e:
                cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
    def organ_donor_id_screen(self):
        screen_manager.current="ORGAN_DONOR_ID"
        screen_manager.get_screen('DONATE_ORGAN').ids.o_id.text =""
    def organ_donate(self):
        try:
            if screen_manager.get_screen('DONATE_ORGAN').ids.o_id.text!="":
                a1=screen_manager.get_screen('DONATE_ORGAN').ids.o_id.text
                b1=screen_manager.get_screen('ORGAN_DONOR_ID').ids.p_id.text
                as1=screen_manager.get_screen('DONATE_ORGAN').ids.p_eye.active
                as2=screen_manager.get_screen('DONATE_ORGAN').ids.p_heart.active
                as3=screen_manager.get_screen('DONATE_ORGAN').ids.p_kidney.active
                as4=screen_manager.get_screen('DONATE_ORGAN').ids.p_pancreas.active
                as5=screen_manager.get_screen('DONATE_ORGAN').ids.p_lung.active
                as6=screen_manager.get_screen('DONATE_ORGAN').ids.p_liver.active
                as7=screen_manager.get_screen('DONATE_ORGAN').ids.p_intestine.active
                if as1==as2==as3==as4==as5==as6==as7==False:
                    cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                    self.dialog = MDDialog(title = 'Error !',text = "Please Fill Any Check Box",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                    self.dialog.open()
                else:
                    if as1==True:
                        c="EYE"
                    elif as2==True:
                        c="HEART"
                    elif as3==True:
                        c="KIDNEY"
                    elif as4==True:
                        c="PANCREAS"
                    elif as5==True:
                        c="LUNGS"
                    elif as6==True:
                        c="LIVER"
                    elif as7==True:
                        c="INTESTINE"
                    aaax1=a1
                    d1="INSERT INTO ORGAN3(DONOR_ID, ORGAN_ID,ORGAN_NAME) VALUES('"+b1+"','"+aaax1+"','"+c+"');"
                    mycursor.execute(d1)
                    mycon.commit()
                    cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                    self.dialog = MDDialog(title = 'Sucess !',text = "Added Sucessfully",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                    self.dialog.open()
            else:
                cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'error !',text = "Please Fill All Details",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def sign_in(self):
        screen_manager.current="SIGNIN"
        screen_manager.get_screen('SIGNIN').ids.u_hid.text ="BH2121"
    def back_to_search_blood(self):
        try:
            if screen_manager.current=="BLOOD_DETAILS":
                try:
                    self.items.clear_widgets()
                    screen_manager.get_screen('BLOOD_DETAILS').ids.three_list_viewer.clear_widgets()
                except Exception as e:
                    cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                    self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                    self.dialog.open()
            screen_manager.current="SEARCH_BLOOD"
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        #screen_manager.current="SEARCH_BLOOD"
    def back_to_blood_details(self):
        screen_manager.current="BLOOD_DETAILS"
    def back_to_log_in(self):
        screen_manager.current="LOGIN"
        screen_manager.get_screen('SIGNIN').ids.u_name.text =""
        screen_manager.get_screen('SIGNIN').ids.u_staff_id.text =""
        screen_manager.get_screen('SIGNIN').ids.cretpssd.text =""
        screen_manager.get_screen('SIGNIN').ids.conf_passd.text =""
        screen_manager.get_screen('SIGNIN').ids.aadhar.text =""
    def log_out(self):
        screen_manager.current="LOGIN"
        screen_manager.get_screen('FORGET_SCREEN').ids.s_id.text =""
        screen_manager.get_screen('FORGET_SCREEN').ids.a_id.text =""
        self.menu.dismiss()
    def forgets(self):
        screen_manager.current="FORGET_SCREEN"
    def forget_password(self):
        de1=screen_manager.get_screen('FORGET_SCREEN').ids.s_id.text
        de2=screen_manager.get_screen('FORGET_SCREEN').ids.a_id.text
        d1="SELECT * FROM USERID WHERE STAFF_ID ="+ '"'+de1+'"'+";"
        mycursor.execute(d1)
        fetch_1=mycursor.fetchall()
        if screen_manager.get_screen('FORGET_SCREEN').ids.s_id.text and screen_manager.get_screen('FORGET_SCREEN').ids.a_id.text !="":
            if fetch_1==[]:
                cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'Error !',text = "Staff ID Not Found",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
            else:
                if de2==fetch_1[0][4]:
                    cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                    self.dialog = MDDialog(title = 'This is your password',text = str(fetch_1[0][2]),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                    self.dialog.open()
                else:
                    cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                    self.dialog = MDDialog(title = 'Error !',text = "Aadhar Number Not Matched",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                    self.dialog.open()
        else:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'Error !',text = "Please Fill All Details",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def res_password(self):
        de1=screen_manager.get_screen('RES_SCREEN').ids.c_id.text
        de2=screen_manager.get_screen('RES_SCREEN').ids.c_id1.text
        de3=screen_manager.get_screen('RES_SCREEN').ids.c_id2.text
        de4=screen_manager.get_screen('LOGIN').ids.us_id.text
        d1="SELECT * FROM USERID WHERE STAFF_ID ="+ '"'+de4+'"'+";"
        mycursor.execute(d1)
        fetch_1=mycursor.fetchall()
        if screen_manager.get_screen('RES_SCREEN').ids.c_id.text and screen_manager.get_screen('RES_SCREEN').ids.c_id1.text and screen_manager.get_screen('RES_SCREEN').ids.c_id2.text !="":
            if de1!=fetch_1[0][2]:
                cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'Error !',text = "Current Password Not Matched",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
            else:
                if de2==de3:
                    d2 = f"UPDATE USERID SET PASSWORD = '{de2}' WHERE STAFF_ID = '{de4}';"
                    mycursor.execute(d2)
                    fetch_1=mycursor.fetchall()
                    mycon.commit()
                    cancel_btn_username_dialogue = MDFlatButton(text='Close',on_release = self.close_username_dialogue)
                    self.dialog = MDDialog(title = 'Success !',text = "Password Successfully Updated",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                    self.dialog.open()
                else:
                    cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                    self.dialog = MDDialog(title = 'Error !',text = "Enter New Password Correctly",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                    self.dialog.open()
        else:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'Error !',text = "Please Fill All details",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def dot(self, button):
        self.menu.caller = button
        self.menu.open()
    def about_us(self):
        screen_manager.current="AboutUs"
        self.menu.dismiss()
    def back_to_mainscreen(self):
        screen_manager.current="Main"
        screen_manager.get_screen('ADD').ids.p_id.text =""
        screen_manager.get_screen('ADD').ids.p_name.text =""
        screen_manager.get_screen('ADD').ids.p_mobile_no.text =""
        screen_manager.get_screen('ADD').ids.p_age.text =""
        screen_manager.get_screen('ADD').ids.p_sex.text =""
        screen_manager.get_screen('ADD').ids.p_marital.text =""
        screen_manager.get_screen('ADD').ids.p_blood.text =""
        screen_manager.get_screen('ADD').ids.P_house.text =""
        screen_manager.get_screen('ADD').ids.p_street.text =""
        screen_manager.get_screen('ADD').ids.p_city.text =""
        screen_manager.get_screen('ADD').ids.p_state.text =""
        screen_manager.get_screen('ADD').ids.p_country.text =""
        screen_manager.get_screen('ADD_DONOR_DETAILS').ids.d_id.text =""
        screen_manager.get_screen('ADD_DONOR_DETAILS').ids.d_name.text =""
        screen_manager.get_screen('ADD_DONOR_DETAILS').ids.d_mobile_no.text =""
        screen_manager.get_screen('ADD_DONOR_DETAILS').ids.d_age.text =""
        screen_manager.get_screen('ADD_DONOR_DETAILS').ids.d_sex.text =""
        screen_manager.get_screen('ADD_DONOR_DETAILS').ids.d_marital.text =""
        screen_manager.get_screen('ADD_DONOR_DETAILS').ids.d_blood.text =""
        screen_manager.get_screen('ADD_DONOR_DETAILS').ids.d_house.text =""
        screen_manager.get_screen('ADD_DONOR_DETAILS').ids.d_street.text =""
        screen_manager.get_screen('ADD_DONOR_DETAILS').ids.d_city.text =""
        screen_manager.get_screen('ADD_DONOR_DETAILS').ids.d_state.text =""
        screen_manager.get_screen('ADD_DONOR_DETAILS').ids.d_country.text =""
        screen_manager.get_screen('SEARCH').ids.p_id.text =""
        screen_manager.get_screen('DELETE').ids.s_id.text =""
        screen_manager.get_screen('DISCHARGE').ids.s_id.text =""
        screen_manager.get_screen('ORGAN_DONOR_ID').ids.p_id.text =""
        screen_manager.get_screen('SEARCH_BLOOD').ids.s_id.text =""
        screen_manager.get_screen('DONOR_DELETE').ids.s_id.text =""
        screen_manager.get_screen('UPDATE1_PATIENT_DETAILS').ids.s_id.text =""
    def back_to_searchscreen(self):
        screen_manager.current="SEARCH"
    def back_to_RES_SCREEN_screen(self):
        screen_manager.current="SEARCH_BLOOD"
    def back_to_screen(self):
        screen_manager.current="Main"
        screen_manager.get_screen('RES_SCREEN').ids.c_id.text =""
        screen_manager.get_screen('RES_SCREEN').ids.c_id1.text =""
        screen_manager.get_screen('RES_SCREEN').ids.c_id2.text =""
    def click_mainscreen(self):
        screen_manager.current="Main"
    def help_support(self):
        self.menu.dismiss()
        screen_manager.current="Help_Support"
    def faq(self):
        self.menu.dismiss()
        screen_manager.current="FAQ"
    def reset_pasd(self):
        self.menu.dismiss()
        screen_manager.current="RES_SCREEN"
    def add_patient(self):
        screen_manager.current="ADD"
    def search_patient(self):
        screen_manager.current="SEARCH"
    def delete_patient(self):
        screen_manager.current="DELETE"
    def delete_donor(self):
        screen_manager.current="DONOR_DELETE"
    def update_patient(self):
        screen_manager.current="UPDATE"
    def patient_details(self):
        #screen_manager.current="PATIENT_DETAILS"
        try:
            self.de1=screen_manager.get_screen('SEARCH').ids.p_id.text
            d1="SELECT * FROM PATIENT WHERE PATIENT_ID ="+ '"'+self.de1+'"'+";"
            mycursor.execute(d1)
            fetch_1=mycursor.fetchall()
            if screen_manager.get_screen('SEARCH').ids.p_id.text!="":
                if fetch_1!=[]:
                    fetch_2=fetch_1[0]
                    fetch_3=fetch_2[7]
                    l1=[fetch_3]
                    sp=l1[0].split('/')
                    a1=sp[0]
                    a2=sp[1]
                    a3=sp[2]
                    a4=sp[3]
                    a5=sp[4]
                    screen_manager.get_screen('PATIENT_DETAILS').ids.p_id.text="Patient ID:    "+str(fetch_2[0])
                    screen_manager.get_screen('PATIENT_DETAILS').ids.p_name.text="Patient Name:   "+fetch_2[1]
                    screen_manager.get_screen('PATIENT_DETAILS').ids.p_mobile_no.text="Mobile No:    "+fetch_2[2]
                    screen_manager.get_screen('PATIENT_DETAILS').ids.p_age.text="Age:  "+str(fetch_2[3])
                    screen_manager.get_screen('PATIENT_DETAILS').ids.p_sex.text="Sex:  "+fetch_2[4]
                    screen_manager.get_screen('PATIENT_DETAILS').ids.p_marital.text="Marital Status: "+fetch_2[5]
                    screen_manager.get_screen('PATIENT_DETAILS').ids.p_blood.text="Blood Group:   "+fetch_2[6]
                    screen_manager.get_screen('PATIENT_DETAILS').ids.p_address.text="Address"
                    screen_manager.get_screen('PATIENT_DETAILS').ids.P_house.text="House Number:  "+a1
                    screen_manager.get_screen('PATIENT_DETAILS').ids.p_street.text="Street Number:   "+a2
                    screen_manager.get_screen('PATIENT_DETAILS').ids.p_city.text="City:   "+a3
                    screen_manager.get_screen('PATIENT_DETAILS').ids.p_state.text="State:   "+a4
                    screen_manager.get_screen('PATIENT_DETAILS').ids.p_country.text="Country:   "+a5
                    screen_manager.current="PATIENT_DETAILS"
                else:
                    cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                    self.dialog = MDDialog(title = 'error !',text = "Patient ID Not Matched",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                    self.dialog.open()
            else:
                cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'error !',text = "Please Enter Patient ID",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
        except Exception as e:
                cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'error !',text = "Please Enter Patient ID",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
    def blood_gr_details(self):
        try:
            if screen_manager.get_screen('SEARCH_BLOOD').ids.s_id.text!="":
                u1=screen_manager.get_screen('SEARCH_BLOOD').ids.s_id.text
                r1="SELECT * FROM organ3 WHERE organ_name="+"'"+u1+"';"
                mycursor.execute(r1)
                exe2 = mycursor.fetchall()
                if exe2!=[]:
                    self.exe3=len(exe2)
                    for i in range(self.exe3):
                        exe3=exe2[i]
                        r2="SELECT * FROM donor WHERE DONOR_ID="+"'"+exe3[0]+"';"
                        mycursor.execute(r2)
                        exeqw = mycursor.fetchall()
                        exe4=exeqw[0]
                        self.items =  ThreeLineListItem(text=f"{exe4[1]}",secondary_text=f"Donor ID: {exe4[0]}",tertiary_text=f"Mobile No: {exe4[2]}",on_release=self.myclick)
                        screen_manager.get_screen('BLOOD_DETAILS').ids.three_list_viewer.add_widget(self.items)
                    screen_manager.current="BLOOD_DETAILS"
                else:
                    cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                    self.dialog = MDDialog(title = 'error !',text = "Organ Name Not Matched",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                    self.dialog.open()
            else:
                cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'error !',text = "Please Enter Organ Name",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def myclick(self, ThreeLineListItem):
        try:
            sef1=ThreeLineListItem.secondary_text
            sef2=list(sef1)
            sef3=sef2[10: ]
            sef4="".join(sef3)
            screen_manager.current="BLOOD_DETAILS_SCREEN"
            self.de1=screen_manager.get_screen('SEARCH').ids.p_id.text
            d2="SELECT * FROM DONOR WHERE DONOR_ID ="+ '"'+sef4+'"'+";"
            mycursor.execute(d2)
            fetch_1=mycursor.fetchall()
            fetch_2=fetch_1[0]
            fetch_3=fetch_2[7]
            l1=[fetch_3]
            sp=l1[0].split('/')
            a1=sp[0]
            a2=sp[1]
            a3=sp[2]
            a4=sp[3]
            a5=sp[4]
            screen_manager.get_screen('BLOOD_DETAILS_SCREEN').ids.p_id.text="Donor ID: "+str(fetch_2[0])
            screen_manager.get_screen('BLOOD_DETAILS_SCREEN').ids.p_name.text="Donor Name: "+fetch_2[1]
            screen_manager.get_screen('BLOOD_DETAILS_SCREEN').ids.p_mobile_no.text="Mobile No: "+fetch_2[2]
            screen_manager.get_screen('BLOOD_DETAILS_SCREEN').ids.p_age.text="Age: "+str(fetch_2[3])
            screen_manager.get_screen('BLOOD_DETAILS_SCREEN').ids.p_sex.text="Sex: "+fetch_2[4]
            screen_manager.get_screen('BLOOD_DETAILS_SCREEN').ids.p_marital.text="Marital Status: "+fetch_2[5]
            screen_manager.get_screen('BLOOD_DETAILS_SCREEN').ids.p_blood.text="Blood Group: "+fetch_2[6]
            screen_manager.get_screen('BLOOD_DETAILS_SCREEN').ids.p_address.text="Address"
            screen_manager.get_screen('BLOOD_DETAILS_SCREEN').ids.P_house.text="House Number:  "+a1
            screen_manager.get_screen('BLOOD_DETAILS_SCREEN').ids.p_street.text="Street Number:   "+a2
            screen_manager.get_screen('BLOOD_DETAILS_SCREEN').ids.p_city.text="City:  "+a3
            screen_manager.get_screen('BLOOD_DETAILS_SCREEN').ids.p_state.text="State:   "+a4
            screen_manager.get_screen('BLOOD_DETAILS_SCREEN').ids.p_country.text="Country:   "+a5
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def back1(self):
        try:
            screen_manager.current="BLOOD_DETAILS"
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def update_patient_det(self):
        try:
            if screen_manager.get_screen('UPDATE1_PATIENT_DETAILS').ids.s_id.text!="":
                u1=screen_manager.get_screen('UPDATE1_PATIENT_DETAILS').ids.s_id.text
                r1="SELECT * FROM PATIENT WHERE PATIENT_ID="+'"'+u1+'"'+";"
                mycursor.execute(r1)
                exe2 = mycursor.fetchall()
                if exe2!=[]:
                    self.exe3=len(exe2)
                    for i in range(self.exe3):
                        #exe4=exe2[i]
                        self.items1 =  ThreeLineListItem(text="PATIENT NAME", on_release=self.my_click1)
                        self.items2 =  ThreeLineListItem(text="MOBILE NO", on_release=self.my_click2)
                        self.items3 =  ThreeLineListItem(text="AGE", on_release=self.my_click3)
                        self.items4 =  ThreeLineListItem(text="SEX", on_release=self.my_click4)
                        self.items5 =  ThreeLineListItem(text="MARITAL STATUS", on_release=self.my_click5)
                        self.items6 =  ThreeLineListItem(text="BLOOD GROUP", on_release=self.my_click6)
                        self.items7 =  ThreeLineListItem(text="ADDRESS", on_release=self.my_click7)
                        screen_manager.get_screen('DETAILS_UPDATE').ids.three_list_viewer.add_widget(self.items1)
                        screen_manager.get_screen('DETAILS_UPDATE').ids.three_list_viewer.add_widget(self.items2)
                        screen_manager.get_screen('DETAILS_UPDATE').ids.three_list_viewer.add_widget(self.items3)
                        screen_manager.get_screen('DETAILS_UPDATE').ids.three_list_viewer.add_widget(self.items4)
                        screen_manager.get_screen('DETAILS_UPDATE').ids.three_list_viewer.add_widget(self.items5)
                        screen_manager.get_screen('DETAILS_UPDATE').ids.three_list_viewer.add_widget(self.items6)
                        screen_manager.get_screen('DETAILS_UPDATE').ids.three_list_viewer.add_widget(self.items7)
                    screen_manager.current="DETAILS_UPDATE"
                else:
                    cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                    self.dialog = MDDialog(title = 'error !',text = "Patient ID Not Matched",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                    self.dialog.open()
            else:
                cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'error !',text = "Please Enter Patient ID",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def back_update1(self):
        try:
            screen_manager.current="DETAILS_UPDATE"
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def my_click1(self, ThreeLineListItem):
        screen_manager.current="PATIENT_NAME1"
    def my_click2(self, ThreeLineListItem):
        screen_manager.current="MOBILE1"
    def my_click3(self, ThreeLineListItem):
        screen_manager.current="AGE1"
    def my_click4(self, ThreeLineListItem):
        screen_manager.current="SSS"
    def my_click5(self, ThreeLineListItem):
        screen_manager.current="MARITAL_STATUS1"
    def my_click6(self, ThreeLineListItem):
        screen_manager.current="BLOOD_GROUP"
    def my_click7(self, ThreeLineListItem):
        screen_manager.current="ADDRESS_UPDATE1"
    def my1(self):
        try:
            if screen_manager.get_screen('PATIENT_NAME1').ids.n_id.text !="":
                de1=screen_manager.get_screen('UPDATE1_PATIENT_DETAILS').ids.s_id.text
                de2=screen_manager.get_screen('PATIENT_NAME1').ids.n_id.text
                d1 = f"UPDATE PATIENT SET PATIENT_NAME = '{de2}' WHERE PATIENT_ID = '{de1}';"
                mycursor.execute(d1)
                fetch_1=mycursor.fetchall()
                mycon.commit()
                cancel_btn_username_dialogue = MDFlatButton(text='Close',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'Success !',text = "Successfully Updated",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
            else:
                cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'error !',text = "Please Enter Patient Name",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def my2(self):
        try:
            if screen_manager.get_screen('MOBILE1').ids.n_id.text !="":
                de1=screen_manager.get_screen('UPDATE1_PATIENT_DETAILS').ids.s_id.text
                de2=screen_manager.get_screen('MOBILE1').ids.n_id.text
                d1 = f"UPDATE PATIENT SET MOBILE_NO = '{de2}' WHERE PATIENT_ID = '{de1}';"
                mycursor.execute(d1)
                fetch_1=mycursor.fetchall()
                mycon.commit()
                cancel_btn_username_dialogue = MDFlatButton(text='Close',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'Success !',text = "Successfully Updated",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
            else:
                cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'error !',text = "Please Enter Mobile Number",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def my3(self):
        try:
            if screen_manager.get_screen('AGE1').ids.n_id.text !="":
                de1=screen_manager.get_screen('UPDATE1_PATIENT_DETAILS').ids.s_id.text
                de2=screen_manager.get_screen('AGE1').ids.n_id.text
                d1 = f"UPDATE PATIENT SET AGE = '{de2}' WHERE PATIENT_ID = '{de1}';"
                mycursor.execute(d1)
                fetch_1=mycursor.fetchall()
                mycon.commit()
                cancel_btn_username_dialogue = MDFlatButton(text='Close',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'Success !',text = "Successfully Updated",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
            else:
                cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'error !',text = "Please Enter Patient Age",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def my4(self):
        try:
            if screen_manager.get_screen('SSS').ids.n_id.text !="":
                de1=screen_manager.get_screen('UPDATE1_PATIENT_DETAILS').ids.s_id.text
                de2=screen_manager.get_screen('SSS').ids.n_id.text
                d1 = f"UPDATE PATIENT SET SEX = '{de2}' WHERE PATIENT_ID = '{de1}';"
                mycursor.execute(d1)
                fetch_1=mycursor.fetchall()
                mycon.commit()
                cancel_btn_username_dialogue = MDFlatButton(text='Close',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'Success !',text = "Successfully Updated",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
            else:
                cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'error !',text = "Please Enter Patient Sex",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def my5(self):
        try:
            if screen_manager.get_screen('MARITAL_STATUS1').ids.n_id.text !="":
                de1=screen_manager.get_screen('UPDATE1_PATIENT_DETAILS').ids.s_id.text
                de2=screen_manager.get_screen('MARITAL_STATUS1').ids.n_id.text
                d1 = f"UPDATE PATIENT SET MARITAL_STATUS = '{de2}' WHERE PATIENT_ID = '{de1}';"
                mycursor.execute(d1)
                fetch_1=mycursor.fetchall()
                mycon.commit()
                cancel_btn_username_dialogue = MDFlatButton(text='Close',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'Success !',text = "Successfully Updated",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
            else:
                cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'error !',text = "Please Enter Patient Marital Status",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def my6(self):
        try:
            if screen_manager.get_screen('BLOOD_GROUP').ids.n_id.text !="":
                de1=screen_manager.get_screen('UPDATE1_PATIENT_DETAILS').ids.s_id.text
                de2=screen_manager.get_screen('BLOOD_GROUP').ids.n_id.text
                d1 = f"UPDATE PATIENT SET BLOOD_GROUP = '{de2}' WHERE PATIENT_ID = '{de1}';"
                mycursor.execute(d1)
                fetch_1=mycursor.fetchall()
                mycon.commit()
                cancel_btn_username_dialogue = MDFlatButton(text='Close',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'Success !',text = "Successfully Updated",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
            else:
                cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'error !',text = "Please Enter Patient Blood Group",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def my7(self):
        try:
            if screen_manager.get_screen('ADDRESS_UPDATE1').ids.n_id1.text and screen_manager.get_screen('ADDRESS_UPDATE1').ids.n_id2.text and screen_manager.get_screen('ADDRESS_UPDATE1').ids.n_id3.text and screen_manager.get_screen('ADDRESS_UPDATE1').ids.n_id4.text and screen_manager.get_screen('ADDRESS_UPDATE1').ids.n_id5.text !="":
                de1=screen_manager.get_screen('UPDATE1_PATIENT_DETAILS').ids.s_id.text
                de2=screen_manager.get_screen('ADDRESS_UPDATE1').ids.n_id1.text
                de3=screen_manager.get_screen('ADDRESS_UPDATE1').ids.n_id2.text
                de4=screen_manager.get_screen('ADDRESS_UPDATE1').ids.n_id3.text
                de5=screen_manager.get_screen('ADDRESS_UPDATE1').ids.n_id4.text
                de6=screen_manager.get_screen('ADDRESS_UPDATE1').ids.n_id5.text
                ns0=de2+'/'+de3+'/'+de4+'/'+de5+'/'+de6
                d1 = f"UPDATE PATIENT SET ADDRESS = '{ns0}' WHERE PATIENT_ID = '{de1}';"
                mycursor.execute(d1)
                fetch_1=mycursor.fetchall()
                mycon.commit()
                cancel_btn_username_dialogue = MDFlatButton(text='Close',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'Success !',text = "Successfully Updated",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
            else:
                cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'error !',text = "Please Enter Patient Address",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def delete_patients(self):
            try:
                if screen_manager.get_screen('DELETE').ids.s_id.text !="":
                    de1=screen_manager.get_screen('DELETE').ids.s_id.text
                    r1="SELECT * FROM PATIENT WHERE PATIENT_ID="+'"'+de1+'"'+";"
                    mycursor.execute(r1)
                    exe2 = mycursor.fetchall()
                    if exe2!=[]:
                        d1 = f"DELETE FROM PATIENT WHERE PATIENT_ID = '{de1}';"
                        mycursor.execute(d1)
                        fetch_1=mycursor.fetchall()
                        mycon.commit()
                        cancel_btn_username_dialogue = MDFlatButton(text='Close',on_release = self.close_username_dialogue)
                        self.dialog = MDDialog(title = 'Success !',text = "Successfully Deleted",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                        self.dialog.open()
                    else:
                        cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                        self.dialog = MDDialog(title = 'error !',text = "Patient ID Not Matched",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                        self.dialog.open()
                else:
                    cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                    self.dialog = MDDialog(title = 'error !',text = "Please Enter Patient ID",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                    self.dialog.open()
            except Exception as e:
                cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
    def delete_donor_details(self):
            try:
                if screen_manager.get_screen('DONOR_DELETE').ids.s_id.text !="":
                    de1=screen_manager.get_screen('DONOR_DELETE').ids.s_id.text
                    r1="SELECT * FROM DONOR WHERE DONOR_ID="+de1+";"
                    mycursor.execute(r1)
                    exe2 = mycursor.fetchall()

                    if exe2!=[]:
                        d1 = f"DELETE FROM DONOR WHERE DONOR_ID = '{de1}';"
                        mycursor.execute(d1)
                        fetch_1=mycursor.fetchall()
                        mycon.commit()
                        cancel_btn_username_dialogue = MDFlatButton(text='Close',on_release = self.close_username_dialogue)
                        self.dialog = MDDialog(title = 'Success !',text = "Successfully Deleted",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                        self.dialog.open()
                        d3 = f"DELETE FROM ORGAN3 WHERE DONOR_ID = '{de1}';"
                        mycursor.execute(d3)
                        fetch_12=mycursor.fetchall()
                        mycon.commit()
                    else:
                        cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                        self.dialog = MDDialog(title = 'error !',text = "Donor ID Not Matched",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                        self.dialog.open()
                else:
                    cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                    self.dialog = MDDialog(title = 'error !',text = "Please Enter Donor ID",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                    self.dialog.open()
            except Exception as e:
                cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
    def back_to_update1_patient_details(self):
        try:
            if screen_manager.current=="DETAILS_UPDATE":
                try:
                    #self.items.clear_widgets()
                    screen_manager.get_screen('DETAILS_UPDATE').ids.three_list_viewer.clear_widgets()
                except Exception as e:
                    cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                    self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                    self.dialog.open()
            screen_manager.current="UPDATE1_PATIENT_DETAILS"
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def search_blood_details(self):
        screen_manager.current="SEARCH_BLOOD"
    def blood_details(self):
        screen_manager.current="BLOOD_DETAILS"
    def add_donor_details(self):
        screen_manager.current="ADD_DONOR_DETAILS"
    def update11_patient_details(self):
        screen_manager.current="UPDATE1_PATIENT_DETAILS"
    def update22_patient_details(self):
        screen_manager.current="UPDATE2_PATIENT_DETAILS"
    def donate_blood(self):
        screen_manager.current="DONATE_BLOOD"
    def discharge(self):
        screen_manager.current="DISCHARGE"
    def prepare_bills(self):
        #screen_manager.current="PREPARE_BILL"
        try:
            screen_manager.get_screen('PREPARE_BILL').ids.q_id2.text ="0"
            screen_manager.get_screen('PREPARE_BILL').ids.q_id3.text ="1000"
            screen_manager.get_screen('PREPARE_BILL').ids.q_id4.text ="0"
            if screen_manager.get_screen('DISCHARGE').ids.s_id.text !="":
                de1=screen_manager.get_screen('DISCHARGE').ids.s_id.text
                r1="SELECT * FROM PATIENT WHERE PATIENT_ID="+'"'+de1+'"'+";"
                mycursor.execute(r1)
                exe2 = mycursor.fetchall()
                if exe2!=[]:
                    screen_manager.current="PREPARE_BILL"
                else:
                    cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                    self.dialog = MDDialog(title = 'error !',text = "Patient ID Not Matched",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                    self.dialog.open()
            else:
                cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'error !',text = "Please Enter Patient ID",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def back_to_prepare_bill(self):
        screen_manager.current="PREPARE_BILL"
    def final_pdf(self):
        #screen_manager.current="FINAL_BILL"
        try:
            de1=screen_manager.get_screen('DISCHARGE').ids.s_id.text
            de3=screen_manager.get_screen('PREPARE_BILL').ids.q_id2.text
            de4=screen_manager.get_screen('PREPARE_BILL').ids.q_id3.text
            de5=screen_manager.get_screen('PREPARE_BILL').ids.q_id4.text
            if de5=="" or de3=="" or de4=="":
                cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'error !',text = "All details are Compulsory",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
            else:
                de01="select * from PREPARE_BILL ORDER BY BILL_NO DESC;"
                mycursor.execute(de01)
                de02=mycursor.fetchall()
                if de02!=[]:
                    de03=de02[0]
                    de2=de03[0]
                    self.de2=str(int(de2)+1)
                else:
                    self.de2=str(int(1))
                n01="'"+self.de2+"'"+","+"'"+de4+"'"+","+"'"+de3+"'"+","+"'"+de5+"'"+","+"'"+de1+"'"
                n02="INSERT INTO PREPARE_BILL(BILL_NO, TREATMENT_CHARGES, BED_CHARGES, OTHER_CHARGES, PATIENT_ID) VALUES("+n01+");"
                mycursor.execute(n02)
                mycon.commit()
                self.treat=de4
                self.bed=de3
                self.other=de5
                cancel_btn_username_dialogue = MDFlatButton(text='Close',on_release = self.close_username_dialogue)
                nexxt_scrren = MDFlatButton(text='Next',on_release = self.next_screen)
                self.dialog = MDDialog(title = 'Success !',text = "Bill Confirmation",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue,nexxt_scrren] )
                self.dialog.open()
                self.de1=de1
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def next_screen(self, alpha):
        try:
            self.dialog.dismiss()
            screen_manager.current="FINAL_BILL"
            d1="SELECT * FROM PREPARE_BILL WHERE PATIENT_ID ="+ '"'+self.de1+'"'+";"
            mycursor.execute(d1)
            fetch_1=mycursor.fetchall()
            fetch_2=fetch_1[0]
            d2="SELECT * FROM PATIENT WHERE PATIENT_ID ="+ '"'+self.de1+'"'+";"
            mycursor.execute(d2)
            fetch_12=mycursor.fetchall()
            fetch_21=fetch_12[0]
            screen_manager.get_screen('FINAL_BILL').ids.p_id1.text="Patient ID:    "+str(fetch_21[0])
            self.ppntidd=str(fetch_21[0])
            screen_manager.get_screen('FINAL_BILL').ids.p_id2.text="Patient Name:    "+str(fetch_21[1])
            self.nname_pat=str(fetch_21[1])
            de3=screen_manager.get_screen('PREPARE_BILL').ids.q_id2.text
            de4=screen_manager.get_screen('PREPARE_BILL').ids.q_id3.text
            de5=screen_manager.get_screen('PREPARE_BILL').ids.q_id4.text
            s1=float(de3) + float(de4) + float(de5)
            screen_manager.get_screen('FINAL_BILL').ids.p_id3.text="Bill Number:   --- "
            screen_manager.get_screen('FINAL_BILL').ids.p_id4.text="Bed Charge:    "+str(de3)
            screen_manager.get_screen('FINAL_BILL').ids.p_id5.text="Treatment Charge:    "+str(de4)
            screen_manager.get_screen('FINAL_BILL').ids.p_id6.text="Other Charge:    "+str(de5)
            screen_manager.get_screen('FINAL_BILL').ids.p_id7.text="Total:    "+str(s1)
            self.totall=str(s1)
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def creatte_bille(self):
        try:
            pdf = PDF()
            pdf.set_font_size(16)
            pdf.add_page()
            pdf.set_font('Arial', '', 12)
            pdf.set_fill_color(35, 75, 83)
            pdf.cell(0, 6 ,"", 0, 1, 'L', True)
            pdf.ln(4)
            pdf.set_font("Arial", size = 30)
            pdf.cell(200, 10, txt = "Hospital Management System",ln = 1, align = 'C')
            pdf.set_font('Arial', '', 15)
            pdf.cell(200, 10, txt = "Powered By HMS",ln = 2, align = 'C')
            pdf.set_font('Arial', '', 10)
            pdf.cell(200, 10, txt = "#47, First Floor, Above Bakery, Chikkanayakanahalli, Bangalore-560035",ln = 2 ,align = 'C')
            pdf.set_font('Arial', '', 10)
            pdf.cell(200, 10, txt = "Email: hms@gmail.com" + "                                                                                                                      Mobile: 9878675645",ln = 2, align = 'L')
            pdf.image('images/logo.png', 12, 18, 20)
            pdf.set_font('Arial', '', 12)
            pdf.set_fill_color(35, 75, 83)
            pdf.cell(0, 6, "", 0, 1, 'L', True)
            pdf.ln(6)
            pdf.cell(0, 10, txt = "PATIENT COPY" ,ln = 0, align = 'C')
            no = datetime.now()
            pdf.ln(7)
            pdf.cell(0, 8, txt = "RECEIPT ID: "+str(self.de2), align = 'L')
            pdf.cell(0, 8, txt = "DATE: "+str(no),align = 'R')
            pdf.ln(8)
            pdf.cell(0, 8, txt = "PATIENT DETAILS:", ln = 0, align = 'L')
            l1=self.ppntidd
            pdf.ln(9)
            pdf.cell(0, 8, txt = "PATIENT ID: " + l1, align = 'L')
            l2=self.nname_pat
            pdf.ln(10)
            pdf.cell(0, 8, txt = "PATIENT NAME: " + l2, ln=1,align = 'L')
            pdf.cell(0, 8, txt = "CONSULTANT DOCTOR:  DR SAURAV KUMAR:   (MBBS) ", ln=2,align = 'L')
            pdf.set_font('Arial', '', 12)
            pdf.set_fill_color(35, 75, 83)
            pdf.cell(0, 5, "", 0, 1, 'L', True)
            pdf.ln(11)
            pdf.cell(0, 1, txt = "PAYMENT DETAILS:", align = 'L')
            pdf.ln(15)
            pdf.set_fill_color(225, 225, 255)
            data = [
                ("S NO.", "SERVICE NAME", "SERVICE CHARGE", "STATUS"),
                ("1", "TREATMENT CHARGE",str(self.treat), "----"),
                ("2", "BED CHARGE", str(self.bed) , "----"),
                ("3", "OTHER CHARGE", str(self.other), "----"),
                ("", "TOTAL", str(self.totall), "PAID"),
                ]
            pdf.write_html(
                f"""<table border="1"><thead><tr>
                <th width="16%">{data[0][0]}</th>
                <th width="28%">{data[0][1]}</th>
                <th width="28%">{data[0][2]}</th>
                <th width="28%">{data[0][3]}</th>
            </tr></thead><tbody><tr>
                <td>{'</td><td>'.join(data[1])}</td>
            </tr><tr>
                <td>{'</td><td>'.join(data[2])}</td>
            </tr><tr>
                <td>{'</td><td>'.join(data[3])}</td>
            </tr><tr>
                <td>{'</td><td>'.join(data[4])}</td>
            </tr></tbody></table>"""
            )
            pdf.ln(16)
            pdf.cell(0, 1, txt = "DR SAURAV KUMAR", align = 'R')
            pdf.ln(20)
            pdf.image('images/q1.png', 0, 220, 230)
            self.recpt=str(self.de2)
            try:
                exp=os.path.expanduser('~')
                fdir=exp+"//hospital Management system"
                os.mkdir(fdir)
                os.mkdir(fdir+"//recept")
                outpuut=os.path.expanduser('~')+"\\hospital Management system\\recept\\"+self.recpt+'.pdf'
                pdf.output(outpuut)
                os.startfile(outpuut)
            except Exception as e:
                outpuut=os.path.expanduser('~')+"\\hospital Management system\\recept\\"+self.recpt+'.pdf'
                pdf.output(outpuut)
                os.startfile(outpuut)
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()

if __name__ == "__main__":
    if platform == "win":
        Window.maximize()
        hospitalmanagementsystem().run()
#dataBase.close()