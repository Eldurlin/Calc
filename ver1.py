from tkinter import Tk, StringVar, Text, Pack, ttk, Frame, Entry, Label, Button, END, IntVar, Grid, Radiobutton, OptionMenu

calcWindow = Tk()
calcWindow.title("Calc")
calcWindow.geometry("450x700")

calcWork = ttk.Notebook(calcWindow)
calcWork.pack()

poster = Frame(calcWork)
banner = Frame(calcWork)
foil = Frame(calcWork)
rollUp = Frame(calcWork)
ulotki = Frame(calcWork)
businessCard = Frame(calcWork)

calcWork.add(businessCard, text = "Wizytówki")
calcWork.add(poster, text = "Plakaty")
calcWork.add(banner, text = "Banery")
calcWork.add(foil, text = "Folie")
calcWork.add(rollUp, text = "Roll-upy")
calcWork.add(ulotki, text = "Ulotki")

#podstawowe stałe
sra3Ryza130g = 48.47
sra3Ryza150g = 55.81
sra3Ryza170g = 63.12
sra3Ryza200g = 37.48
sra3Ryza250g = 47.87
sra3Ryza300g = 57.58
sra3Ryza350g = 34.5
sra3RyzaOzdobny = 185.0
iloscRyza125 = 125.0
iloscRyza250 = 250.0
iloscRyza500 = 500.0
iloscRyzaOzdobny = 100
cenaPapieruSra3130g = sra3Ryza130g / iloscRyza500
cenaPapieruSra3150g = sra3Ryza150g / iloscRyza500
cenaPapieruSra3170g = sra3Ryza170g / iloscRyza500
cenaPapieruSra3200g = sra3Ryza200g / iloscRyza250
cenaPapieruSra3250g = sra3Ryza250g / iloscRyza250
cenaPapieruSra3300g = sra3Ryza300g / iloscRyza250
cenaPapieruSra3350g = sra3Ryza350g / iloscRyza125
ciecieA3PracownikLokal = 4 * (0.5 + 0.5)
ciecieA4PracownikLokal = 5 * (0.5 + 0.5)
ciecieA5PracownikLokal = 6 * (0.5 + 0.5)
ciecieA6PracownikLokal = 7 * (0.5 + 0.5)
ciecieDlPracownikLokal = 7 * (0.5 + 0.5)
przelotSerwisowy = 0.1
leasingMaszyny = 985.0
kosztWliczonyDoPrzelotu = leasingMaszyny / 10000.0
drukKosztPracownika1MinutaLokalZa1Pracownika = 0.5 + 0.5
drukKosztPracownikaLokal36Sra3NaMin = drukKosztPracownika1MinutaLokalZa1Pracownika / 36.0
przygotowanieDoDrukuRozgrzanieMaszyny10Min = 30.0 / 60.0 * 10.0
cenaFoliiZaPrzelotSra310 = 390.0 / 3000.0 / 2.0
ryczaltZakkupFoliarkiDoliczonydoPrzelotu10Sra3 = 0.2
foliaKosztPracownikaLokal = 0.5 + 0.5
foliaKosztPracownikaLokal2PrzelotyNaMin = foliaKosztPracownikaLokal / 2.0
ciecieKosztPracownika8MinutLokal = 8.0 * (0.5 + 0.5)
ryczaltZaGilotyneNozMin = 5.0
stalyProcent = 7.0 / 100.0
pakowanie = 5.0
iloscNaArkuszu = 20.0

#businessCard
def businessCardCost():
    ciecieWizytowek = float((ciecieKosztPracownika8MinutLokal + ryczaltZaGilotyneNozMin) * float(entryCardsQuantityPatternsValue.get()))
    cost1 = float(entryCardsQuantityPatternsValue.get()) * float(entryCardsQuantityValue.get()) / float(iloscNaArkuszu)
    cenaPrzelotuPracownik = 0
    if variableCardsOverprint.get() == "0":
        cenaPrzelotuPracownik = float(2 * (przelotSerwisowy + kosztWliczonyDoPrzelotu + drukKosztPracownikaLokal36Sra3NaMin))
    else:
        cenaPrzelotuPracownik = float(4 * (przelotSerwisowy + kosztWliczonyDoPrzelotu + drukKosztPracownikaLokal36Sra3NaMin))
    foliowanie = float(cenaFoliiZaPrzelotSra310) + float(ryczaltZakkupFoliarkiDoliczonydoPrzelotu10Sra3) + float(foliaKosztPracownikaLokal2PrzelotyNaMin)
    if (variableCardsOverprint.get() == "0" or variableCardsOverprint.get() == "1") and variableCardsFoil.get() == "0":
        foliowanie = 0
    elif variableCardsOverprint.get() == "0" and variableCardsFoil.get() == "1":
        foliowanie = float(foliowanie)
    elif (variableCardsOverprint.get() == "0" and variableCardsFoil.get() == "2") or (variableCardsOverprint.get() == "1" and variableCardsFoil.get() == "1"):
        foliowanie = float(foliowanie * 2)
    else:
        foliowanie = float(foliowanie * 4)
    cost2 = float(cenaPapieruSra3350g) + float(cenaPrzelotuPracownik) + float(foliowanie)
    finalCost = round(((cost1 * cost2) + ciecieWizytowek + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min), 2)
    finalCostProfit = round((finalCost + (finalCost * stalyProcent)), 3)
    textBusinessCardsCost.delete("1.0", END)
    textBusinessCardsCost.insert(END, finalCost)
    textBusinessCardsCostProfit.delete("1.0", END)
    textBusinessCardsCostProfit.insert(END, finalCostProfit)

labelNameCardsPatterns = Label(businessCard, text = "Ilość wzorców:")
labelNameCardsPatterns.pack()

entryCardsQuantityPatternsValue = StringVar()
entryCardsQuantityPatternsValue = Entry(businessCard, textvariable = entryCardsQuantityPatternsValue)
entryCardsQuantityPatternsValue.pack()

labelNameCardsQuantity = Label(businessCard, text = "Ilość:")
labelNameCardsQuantity.pack()

entryCardsQuantityValue = StringVar()
entryCardsQuantityValue = Entry(businessCard, textvariable = entryCardsQuantityValue)
entryCardsQuantityValue.pack()

labelNameCardsPaperWeight = Label(businessCard, text = "Gramatura:")
labelNameCardsPaperWeight.pack()

variableCardsPaperWeight = IntVar()

valuesCardsPaperWeightSize = {"350":0, "Ozdobny":1}

for (text, value) in valuesCardsPaperWeightSize.items():
    Radiobutton(businessCard, text = text, variable = variableCardsPaperWeight, value = value).pack()

labelNameCardsOverprint = Label(businessCard, text = "Zadruk:")
labelNameCardsOverprint.pack()

variableCardsOverprint = StringVar()

valuesCardsOverprint = {"4+0":0, "4+4":1}

for (text, value) in valuesCardsOverprint.items():
    Radiobutton(businessCard, text = text, variable = variableCardsOverprint, value = value).pack()

labelNameCardsFoil = Label(businessCard, text = "Foliowanie:")
labelNameCardsFoil.pack()

variableCardsFoil = StringVar()

valuesCardsFoil = {"Brak":0, "1+0":1, "1+1":2}

for (text, value) in valuesCardsFoil.items():
    Radiobutton(businessCard, text = text, variable = variableCardsFoil, value = value).pack()

buttonBusinessCardsCost = Button(businessCard, text = "Oblicz koszt", command = businessCardCost)
buttonBusinessCardsCost.pack()

textBusinessCardsCost = Text(businessCard, height = 1, width = 20)
textBusinessCardsCost.pack()

labelNameCardsProfit = Label(businessCard, text = "Stały koszt 7%")
labelNameCardsProfit.pack()

textBusinessCardsCostProfit = Text(businessCard, height = 1, width = 20)
textBusinessCardsCostProfit.pack()

#posters
def posterCost():
    finalCost = 0
    cost = 0
    if variablePosterSize.get() == "0":
        cost = float(entryPostersQuantityPatterns.get()) * float(entryPosterQuantityValue.get()) / 2
    else:
        cost = float(entryPostersQuantityPatterns.get()) * float(entryPosterQuantityValue.get()) / 1
    cenaPrzelotuPracownik = 0
    if variablePostersOverprint.get() == "0":
        cenaPrzelotuPracownik = 2 * (przelotSerwisowy + kosztWliczonyDoPrzelotu) + drukKosztPracownikaLokal36Sra3NaMin
    else:
        cenaPrzelotuPracownik = 4 * (przelotSerwisowy + kosztWliczonyDoPrzelotu) + drukKosztPracownikaLokal36Sra3NaMin
    foliowanie = 0
    if (variablePosterPaperWeight.get() == "3" or variablePosterPaperWeight.get() == "4" or variablePosterPaperWeight.get() == "5" or variablePosterPaperWeight.get() == "6") and variablePostersFoil.get() == "1":
        foliowanie = cenaFoliiZaPrzelotSra310 + ryczaltZakkupFoliarkiDoliczonydoPrzelotu10Sra3 + foliaKosztPracownikaLokal2PrzelotyNaMin
    elif (variablePosterPaperWeight.get() == "3" or variablePosterPaperWeight.get() == "4" or variablePosterPaperWeight.get() == "5" or variablePosterPaperWeight.get() == "6") and variablePostersFoil.get() == "2":
        foliowanie = (cenaFoliiZaPrzelotSra310 + ryczaltZakkupFoliarkiDoliczonydoPrzelotu10Sra3 + foliaKosztPracownikaLokal2PrzelotyNaMin) * 2
    else:
        foliowanie = 0
    # odtąd pisać dalej, dodać cięcie w zależności od rozmiaru
    if variablePosterPaperWeight.get() == "0":
        finalCost = (cost * (cenaPapieruSra3130g + cenaPrzelotuPracownik + foliowanie))
    elif variablePosterPaperWeight.get() == "1":
        cenaPrzelotuPracownik = cenaPapieruSra3150g * (przelotSerwisowy + kosztWliczonyDoPrzelotu)
    elif variablePosterPaperWeight.get() == "2":
        cenaPrzelotuPracownik = cenaPapieruSra3170g * (przelotSerwisowy + kosztWliczonyDoPrzelotu)
    elif variablePosterPaperWeight.get() == "3":
        cenaPrzelotuPracownik = cenaPapieruSra3200g * (przelotSerwisowy + kosztWliczonyDoPrzelotu)
    elif variablePosterPaperWeight.get() == "4":
        cenaPrzelotuPracownik = cenaPapieruSra3250g * (przelotSerwisowy + kosztWliczonyDoPrzelotu)
    elif variablePosterPaperWeight.get() == "5":
        cenaPrzelotuPracownik = cenaPapieruSra3300g * (przelotSerwisowy + kosztWliczonyDoPrzelotu)
    else:
        cenaPrzelotuPracownik = cenaPapieruSra3350g * (przelotSerwisowy + kosztWliczonyDoPrzelotu) + drukKosztPracownikaLokal36Sra3NaMin
    textPosterCost.delete("1.0", END)
    textPosterCost.insert(END, cenaPrzelotuPracownik)

labelNamePosterPatterns = Label(poster, text = "Ilość wzorców:")
labelNamePosterPatterns.pack()

entryPostersQuantityPatterns = StringVar()
entryPostersQuantityPatterns = Entry(poster, textvariable = entryPostersQuantityPatterns)
entryPostersQuantityPatterns.pack()

labelNamePosterQuantity = Label(poster, text = "Ilość:")
labelNamePosterQuantity.pack()

entryPosterQuantityValue = StringVar()
entryPosterQuantityValue = Entry(poster, textvariable = entryPosterQuantityValue)
entryPosterQuantityValue.pack()

labelNamePosterSize = Label(poster, text = "Wielkość:")
labelNamePosterSize.pack()

variablePosterSize = IntVar()

valuesPosterSize = {"A4":0, "A3":1}

for (text, value) in valuesPosterSize.items():
    Radiobutton(poster, text = text, variable = variablePosterSize, value = value).pack()

labelNamePosterPaperWeight = Label(poster, text = "Gramatura:")
labelNamePosterPaperWeight.pack()

variablePosterPaperWeight = IntVar()

valuesPosterPaperWeight = {"130":0, "150":1, "170":2, "200":3, "250":4, "300":5, "350":6, "Ozdobny":7}

for (text, value) in valuesPosterPaperWeight.items(): 
    Radiobutton(poster, text = text, variable = variablePosterPaperWeight, value = value).pack()

labelNamePostersOverprint = Label(poster, text = "Zadruk:")
labelNamePostersOverprint.pack()

variablePostersOverprint = StringVar()

valuesPostersOverprint = {"4+0":0, "4+4":1}

for (text, value) in valuesPostersOverprint.items():
    Radiobutton(poster, text = text, variable = variablePostersOverprint, value = value).pack()

labelNamePostersFoil = Label(poster, text = "Foliowanie:")
labelNamePostersFoil.pack()

variablePostersFoil = StringVar()

valuesPostersFoil = {"Brak":0, "1+0":1, "1+1":2}

for (text, value) in valuesPostersFoil.items():
    Radiobutton(poster, text = text, variable = valuesPostersFoil, value = value).pack()

buttonPosterCost = Button(poster, text = "Oblicz koszt", command = posterCost)
buttonPosterCost.pack()

textPosterCost = Text(poster, height = 1, width = 20)
textPosterCost.pack()

labelNamePostersProfit = Label(poster, text = "Stały koszt 7%")
labelNamePostersProfit.pack()

textPostersCostProfit = Text(poster, height = 1, width = 20)
textPostersCostProfit.pack()

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

#flyers


calcWindow.mainloop()