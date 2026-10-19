from tkinter import *

def kalkulator(event):
    if (float(koffein_var.get()) >= 30.0 and float(koffein_var.get()) <= 130.0) and (float(dl_var.get()) >= 0.3 and float(dl_var.get()) <= 5.0):
        time0_var.set(format(float(koffein_var.get()) * float(dl_var.get()), ".1f"))
        inntak = float(koffein_var.get()) * float(dl_var.get())
        
        for k in range(1,6,1):
            inntak = inntak * 0.87

            if k == 1:
                time1_var.set(format(inntak, ".1f"))
            
            if k == 5:
                time5_var.set(format(inntak, ".1f"))
        
        inntak = float(koffein_var.get()) * float(dl_var.get())
        inntak2 = float(koffein_var.get()) * float(dl_var.get())

        for t in range(1,13,1):
            inntak2 = inntak2 * 0.87 + inntak
            
            if t == 12:
                time12_var.set(format(inntak2, ".1f"))
    else:
        time0_var.set("Ugyldig")


vindu = Tk()
vindu.title("Koffein kalkulator")

lbl_koffein = Label(vindu, text = "Oppgi mengden koffein per dl:")
lbl_koffein.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = SE)
lbl_koffein_mg = Label(vindu, text = "mg")
lbl_koffein_mg.grid(row = 0, column = 2, sticky = W)

lbl_dl = Label(vindu, text = "Oppgi mengden dl i drikken:")
lbl_dl.grid(row = 0, column = 3, padx = 5, pady = 5, sticky = SE)
lbl_dl_enhet = Label(vindu, text = "dl")
lbl_dl_enhet.grid(row = 0, column = 5, sticky = W)

lbl_resultat = Label(vindu, text = "Koffeininnhold i kroppen:")
lbl_resultat.grid(row = 2, column = 0, columnspan = 5, padx = 5, pady = 5)

lbl_0timer = Label(vindu, text = "Rett etter 1 enhet:")
lbl_0timer.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = E)
lbl_0timer_mg = Label(vindu, text = "mg")
lbl_0timer_mg.grid(row = 3, column = 2, sticky = W)

lbl_1time = Label(vindu, text = "1 time etter inntak:")
lbl_1time.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = E)
lbl_1time_mg = Label(vindu, text = "mg")
lbl_1time_mg.grid(row = 4, column = 2, sticky = W)

lbl_5timer = Label(vindu, text = "5 timer etter inntak:")
lbl_5timer.grid(row = 5, column = 0, padx = 5, pady = 5, sticky = E)
lbl_5timer_mg = Label(vindu, text = "mg")
lbl_5timer_mg.grid(row = 5, column = 2, sticky = W)

lbl_12timer = Label(vindu, text = "12 timer med 1 enhet hver time:")
lbl_12timer.grid(row = 6, column = 0, padx = 5, pady = 5, sticky = E)
lbl_12timer_mg = Label(vindu, text = "mg")
lbl_12timer_mg.grid(row = 6, column = 2, sticky = W)


koffein_var = StringVar()
ent_koffein = Entry(vindu, width = 6, textvariable = koffein_var)
ent_koffein.grid(row = 0, column = 1, padx = 5, pady = 20, sticky = W)

dl_var = StringVar()
ent_dl = Entry(vindu, width = 6, textvariable = dl_var)
ent_dl.grid(row = 0, column = 4, padx = 5, pady = 20, sticky = W)

time0_var = StringVar()
ent_time0 = Entry(vindu, width = 6, textvariable = time0_var, state = "readonly")
ent_time0.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = W)

time1_var = StringVar()
ent_time1 = Entry(vindu, width = 6, textvariable = time1_var, state = "readonly")
ent_time1.grid(row = 4, column = 1, padx = 5, pady = 5, sticky = W)

time5_var = StringVar()
ent_time5 = Entry(vindu, width = 6, textvariable = time5_var, state = "readonly")
ent_time5.grid(row = 5, column = 1, padx = 5, pady = 5, sticky = W)

time12_var = StringVar()
ent_time12 = Entry(vindu, width = 6, textvariable = time12_var, state = "readonly")
ent_time12.grid(row = 6, column = 1, padx = 5, pady = 5, sticky = W)

scale_koffein = Scale(vindu, orient = HORIZONTAL, length = 30, from_ = 30.0, to = 130.0, variable = koffein_var, command = kalkulator, resolution = 0.1)
scale_koffein.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = EW)

scale_dl = Scale(vindu, orient = HORIZONTAL, length = 50, from_ = 0.3, to = 5.0, variable = dl_var, command = kalkulator, resolution = 0.1)
scale_dl.grid(row = 1, column = 3, columnspan = 5, padx = 5, pady = 5, sticky = EW)

btn_avslutt = Button(vindu, text = "Avslutt", command = vindu.destroy)
btn_avslutt.grid(row = 7, column = 6, padx = 5, pady = 5, sticky = SE)

vindu.mainloop()