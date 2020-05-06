from tkinter import Tk, StringVar, Text, Pack, ttk, Frame, Entry, Label, Button, END, IntVar, Grid, Radiobutton

calcWindow = Tk()
calcWindow.title("Calc")
calcWindow.geometry("500x500")

calcWork = ttk.Notebook(calcWindow)
calcWork.pack()

poster = Frame(calcWork, width = 500, height = 400)
banner = Frame(calcWork, width = 500, height = 400)
foil = Frame(calcWork, width = 500, height = 400)
rollUp = Frame(calcWork, width = 500, height = 400)
ulotki = Frame(calcWork, width = 500, height = 400)

calcWork.add(poster, text = "Plakaty")
calcWork.add(banner, text = "Banery")
calcWork.add(foil, text = "Folie")
calcWork.add(rollUp, text = "Roll-upy")
calcWork.add(ulotki, text = "Ulotki")

#posters
def posterCost():
    cost = float(entryPosterQuantityValue.get()) * (float(variablePosterSize.get()) / 10) * (float(variablePosterPaperWeight.get()) / 10)
    finalCost = round(cost + (cost * (float(entryPosterProfit.get()) / 100)), 2)
    textPosterCost.delete("1.0", END)
    textPosterCost.insert(END, finalCost)

labelNamePosterQuantity = Label(poster, text = "Ilość:")
labelNamePosterQuantity.pack()

entryPosterQuantityValue = StringVar()
entryPosterQuantityValue = Entry(poster, textvariable = entryPosterQuantityValue)
entryPosterQuantityValue.pack()

labelNamePosterSize = Label(poster, text = "Wielkość:")
labelNamePosterSize.pack()

variablePosterSize = IntVar()

valuesPosterSize = {"A0":11, "A1":12, "A2":13}

for (text, value) in valuesPosterSize.items():
    Radiobutton(poster, text = text, variable = variablePosterSize, value = value).pack()

labelNamePosterPaperWeight = Label(poster, text = "Gramatura:")
labelNamePosterPaperWeight.pack()

variablePosterPaperWeight = IntVar()

valuesPosterPaperWeight = {"125":11, "150":12, "200":15}

for (text, value) in valuesPosterPaperWeight.items(): 
    Radiobutton(poster, text = text, variable = variablePosterPaperWeight, value = value).pack()

labelNamePosterProfit = Label(poster, text = "Marża:")
labelNamePosterProfit.pack()

entryPosterProfit = StringVar()
entryPosterProfit = Entry(poster, textvariable = entryPosterProfit)
entryPosterProfit.pack()

buttonPosterCost = Button(poster, text = "Oblicz koszt", command = posterCost)
buttonPosterCost.pack()

textPosterCost = Text(poster, height = 1, width = 20)
textPosterCost.pack()

#banners
def bannerCost():
    cost = float(entryBannerQuantityValue.get()) * (float(variableBannerSize.get()) / 10)
    finalCost = round(cost + (cost * (float(entryBannerProfit.get()) / 100)), 2)
    textBannerCost.delete("1.0", END)
    textBannerCost.insert(END, finalCost)

labelNameBannerQuantity = Label(banner, text = "Ilość:")
labelNameBannerQuantity.pack()

entryBannerQuantityValue = Entry(banner)
entryBannerQuantityValue.pack()

labelNameBannerSize = Label(banner, text = "Wielkość:")
labelNameBannerSize.pack()

variableBannerSize = IntVar()

valuesBannerSize = {"A0":11, "A1":12, "A2":13}

for (text, value) in valuesBannerSize.items():
    Radiobutton(banner, text = text, variable = variableBannerSize, value = value).pack()

labelNameBannerProfit = Label(banner, text = "Marża:")
labelNameBannerProfit.pack()

entryBannerProfit = StringVar()
entryBannerProfit = Entry(banner, textvariable = entryBannerProfit)
entryBannerProfit.pack()

buttonBannerCost = Button(banner, text = "Oblicz koszt", command = bannerCost)
buttonBannerCost.pack()

textBannerCost = Text(banner, height = 1, width = 20)
textBannerCost.pack()


#foils
def foilCost():
    cost = float(entryFoilQuantityValue.get()) * (float(variableFoilSize.get()) / 10) * (float(variableFoilContourCut.get()) / 10)
    finalCost = round(cost + (cost * (float(entryFoilProfit.get()) / 100)), 2)
    textFoilCost.delete("1.0", END)
    textFoilCost.insert(END, finalCost)

labelNameFoilQuantity = Label(foil, text = "Ilość:")
labelNameFoilQuantity.pack()

entryFoilQuantityValue = StringVar()
entryFoilQuantityValue = Entry(foil, textvariable = entryFoilQuantityValue)
entryFoilQuantityValue.pack()

labelNameFoilSize = Label(foil, text = "Wielkość:")
labelNameFoilSize.pack()

variableFoilSize = IntVar()

valuesFoilSize = {"A0":11, "A1":12, "A2":13}

for (text, value) in valuesFoilSize.items():
    Radiobutton(foil, text = text, variable = variableFoilSize, value = value).pack()

labelNameFoilCounterCut = Label(foil, text = "Cięcie po obrysie:")
labelNameFoilCounterCut.pack()

variableFoilContourCut = IntVar()

valuesFoilContourCut = {"Tak":15, "Nie":10}

for (text, value) in valuesFoilContourCut.items():
    Radiobutton(foil, text = text, variable = variableFoilContourCut, value = value).pack()

labelNameFoilProfit = Label(foil, text = "Marża:")
labelNameFoilProfit.pack()

entryFoilProfit = StringVar()
entryFoilProfit = Entry(foil, textvariable = entryFoilProfit)
entryFoilProfit.pack()

buttonFoilCost = Button(foil, text = "Oblicz koszt", command = foilCost)
buttonFoilCost.pack()

textFoilCost = Text(foil, height = 1, width = 20)
textFoilCost.pack()

#roll-ups
labelNameRollUpQuantity = Label(rollUp, text = "Ilość:")
labelNameRollUpQuantity.pack()

entryRollUpQuantityValue = StringVar()
entryRollUpQuantityValue = Entry(rollUp, textvariable = entryRollUpQuantityValue)
entryRollUpQuantityValue.pack()

labelNameRollUpSize = Label(rollUp, text = "Wielkość kasety:")
labelNameRollUpSize.pack()

variableRollUpSize = IntVar()

valuesRollUpSize = {"1":12, "2":13}

for (text, value) in valuesRollUpSize.items():
    Radiobutton(rollUp, text = text, variable = variableRollUpSize, value = value).pack()

calcWindow.mainloop()