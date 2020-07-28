from tkinter import Tk, StringVar, Text, Pack, ttk, Frame, Entry, Label, Button, END, IntVar, Grid, Radiobutton, OptionMenu
import math

calcWindow = Tk()
calcWindow.title("Calc")
calcWindow.geometry("500x650")

calcWork = ttk.Notebook(calcWindow)
calcWork.pack()

businessCard = Frame(calcWork)
poster = Frame(calcWork)
flyer = Frame(calcWork)
rollUp = Frame(calcWork)
foldedFlyer = Frame(calcWork)
customFlyer = Frame(calcWork)
banner = Frame(calcWork)

calcWork.add(banner, text = "Banery")
calcWork.add(customFlyer, text = "Ulotki niestandardowe")
calcWork.add(businessCard, text = "Wizytówki")
calcWork.add(poster, text = "Plakaty")
calcWork.add(flyer, text = "Ulotki")
calcWork.add(rollUp, text = "Roll-upy")
calcWork.add(foldedFlyer, text = "Ulotki składane")

# odstępy
# zmiana kosztów papieru etc
# ff6600

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
cenaPapieruSra3Ozdobny = sra3RyzaOzdobny / iloscRyzaOzdobny
ciecieA3PracownikLokal = 4 * (0.5 + 0.5)
ciecieA4PracownikLokal = 5 * (0.5 + 0.5)
ciecieA5PracownikLokal = 6 * (0.5 + 0.5)
ciecieA6PracownikLokal = 7 * (0.5 + 0.5)
ciecieDlPracownikLokal = 7 * (0.5 + 0.5)
przelotSerwisowy = 0.1
leasingMaszyny = 985.0
kosztWliczonyDoPrzelotu = leasingMaszyny / 10000.0
drukKosztPracownika1MinutaLokalZa1Pracownika = 0.5 + 0.5
drukKosztPracownikaLokal36Sra3NaMin = drukKosztPracownika1MinutaLokalZa1Pracownika / 30.0
drukKosztPracownikaLokal36Sra3NaMinWiz = drukKosztPracownika1MinutaLokalZa1Pracownika / 36.0
przygotowanieDoDrukuRozgrzanieMaszyny10Min = 30.0 / 60.0 * 10.0
cenaFoliiZaPrzelotSra310 = 390.0 / 3000.0 / 2.0
ryczaltZakupFoliarkiDoliczonydoPrzelotu10Sra3 = 0.2
foliaKosztPracownikaLokal = 0.5 + 0.5
foliaKosztPracownikaLokal2PrzelotyNaMin = foliaKosztPracownikaLokal / 2.0
ciecieKosztPracownika8MinutLokal = 8.0 * (0.5 + 0.5)
ryczaltZaGilotyneNozMin = 5.0
stalyProcent = 7.0 / 100.0
pakowanie = 5.0
iloscNaArkuszu = 20.0

#businessCard
def cardsCost():
    ciecieWizytowek = float((ciecieKosztPracownika8MinutLokal + ryczaltZaGilotyneNozMin) * float(entryCardsPatterns.get()))
    cost1 = float(entryCardsPatterns.get()) * float(entryCardsQuantity.get()) / float(iloscNaArkuszu)
    margin = round((float(entryCardsMargin.get()) / 100), 3)
    cenaPrzelotuPracownik = 0
    if varCardsOverprint.get() == "4+0":
        cenaPrzelotuPracownik = float(2 * (przelotSerwisowy + kosztWliczonyDoPrzelotu + drukKosztPracownikaLokal36Sra3NaMinWiz))
    else:
        cenaPrzelotuPracownik = float(4 * (przelotSerwisowy + kosztWliczonyDoPrzelotu + drukKosztPracownikaLokal36Sra3NaMinWiz))
    foliowanie = float(cenaFoliiZaPrzelotSra310) + float(ryczaltZakupFoliarkiDoliczonydoPrzelotu10Sra3) + float(foliaKosztPracownikaLokal2PrzelotyNaMin)
    if (varCardsOverprint.get() == "4+0" or varCardsOverprint.get() == "4+4") and varCardsFoil.get() == "Brak":
        foliowanie = 0
    elif varCardsOverprint.get() == "4+0" and varCardsFoil.get() == "1+0":
        foliowanie = float(foliowanie)
    elif (varCardsOverprint.get() == "4+0" and varCardsFoil.get() == "1+1") or (varCardsOverprint.get() == "4+4" and varCardsFoil.get() == "1+0"):
        foliowanie = float(foliowanie * 2)
    else:
        foliowanie = float(foliowanie * 4)
    cost2 = float(cenaPapieruSra3350g) + float(cenaPrzelotuPracownik) + float(foliowanie)
    finalCost = round(((cost1 * cost2) + ciecieWizytowek + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min), 2)
    finalCostProfit = round((finalCost + (finalCost * stalyProcent)), 3)
    finalCostMargin = round((finalCostProfit + (finalCostProfit * margin)), 3)
    finalCostMarginVAT = round(finalCostMargin * 1.23, 3)
    textCardsCostProfit.delete("1.0", END)
    textCardsCostProfit.insert(END, finalCostProfit)
    textCardsMarginFinal.delete("1.0", END)
    textCardsMarginFinal.insert(END, finalCostMargin)
    textCardsMarginFinalVAT.delete("1.0", END)
    textCardsMarginFinalVAT.insert(END, finalCostMarginVAT)

labelCardsPatterns = Label(businessCard, text = "Ilość wzorów:")
labelCardsPatterns.pack()

entryCardsPatterns = StringVar()
entryCardsPatterns = Entry(businessCard, textvariable = entryCardsPatterns)
entryCardsPatterns.pack()

labelCardsQuantity = Label(businessCard, text = "Ilość:")
labelCardsQuantity.pack()

entryCardsQuantity = StringVar()
entryCardsQuantity = Entry(businessCard, textvariable = entryCardsQuantity)
entryCardsQuantity.pack()

labelCardsPaperWeight = Label(businessCard, text = "Gramatura:")
labelCardsPaperWeight.pack()

optionsCardsPaperWeight = ["350", "Ozdobny"]
varCardsPaperWeight = StringVar()
varCardsPaperWeight.set(optionsCardsPaperWeight[0])
optCardsPaperWeightMenu = OptionMenu(businessCard, varCardsPaperWeight, *optionsCardsPaperWeight)
optCardsPaperWeightMenu.pack()

labelCardsOverprint = Label(businessCard, text = "Zadruk:")
labelCardsOverprint.pack()

optCardsOverprint = ["4+0", "4+4"]
varCardsOverprint = StringVar()
varCardsOverprint.set(optCardsOverprint[0])
optCardsOverprintMenu = OptionMenu(businessCard, varCardsOverprint, *optCardsOverprint)
optCardsOverprintMenu.pack()

labelCardsFoil = Label(businessCard, text = "Foliowanie:")
labelCardsFoil.pack()

optCardsFoil = ["Brak", "1+0", "1+1"]
varCardsFoil = StringVar()
varCardsFoil.set(optCardsFoil[0])
optCardsFoil = OptionMenu(businessCard, varCardsFoil, *optCardsFoil)
optCardsFoil.pack()

labelCardsMargin = Label(businessCard, text = "Marża:")
labelCardsMargin.pack()

entryCardsMargin = StringVar()
entryCardsMargin = Entry(businessCard, textvariable = entryCardsMargin)
entryCardsMargin.pack()

buttonCardsCost = Button(businessCard, text = "Oblicz", command = cardsCost)
buttonCardsCost.pack()

labelCardsProfit = Label(businessCard, text = "Nasz koszt 7%:")
labelCardsProfit.pack()

textCardsCostProfit = Text(businessCard, height = 1, width = 20)
textCardsCostProfit.pack()

labelCardsMarginFinal = Label(businessCard, text = "Finalny koszt:")
labelCardsMarginFinal.pack()

textCardsMarginFinal = Text(businessCard, height = 1, width = 20)
textCardsMarginFinal.pack()

labelCardsMarginFinalVAT = Label(businessCard, text = "Finalny koszt + VAT:")
labelCardsMarginFinalVAT.pack()

textCardsMarginFinalVAT = Text(businessCard, height = 1, width = 20)
textCardsMarginFinalVAT.pack()

#posters
def posterCost():
    cost = 0
    margin = round((float(entryPosterMargin.get()) / 100), 3)
    if varPosterSize.get() == "A4":
        cost = float(entryPostersPatterns.get()) * float(entryPosterQuantity.get()) / 2
    else:
        cost = float(entryPostersPatterns.get()) * float(entryPosterQuantity.get()) / 1
    cenaPrzelotuPracownik = 0
    if varPosterOverprint.get() == "4+0":
        cenaPrzelotuPracownik = (2 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + drukKosztPracownikaLokal36Sra3NaMin
    else:
        cenaPrzelotuPracownik = (4 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + drukKosztPracownikaLokal36Sra3NaMin
    foliowanie = float(cenaFoliiZaPrzelotSra310) + float(ryczaltZakupFoliarkiDoliczonydoPrzelotu10Sra3) + float(foliaKosztPracownikaLokal2PrzelotyNaMin)
    if (varPosterPaperWeight.get() == "200" or varPosterPaperWeight.get() == "250" or varPosterPaperWeight.get() == "300" or varPosterPaperWeight.get() == "350") and varPosterFoil.get() == "1+0" and varPosterOverprint.get() == "4+0":
        foliowanie = foliowanie
    elif (varPosterPaperWeight.get() == "200" or varPosterPaperWeight.get() == "250" or varPosterPaperWeight.get() == "300" or varPosterPaperWeight.get() == "350") and varPosterFoil.get() == "1+1" and varPosterOverprint.get() == "4+4":
        foliowanie = foliowanie * 2 + drukKosztPracownikaLokal36Sra3NaMin
    elif varPosterPaperWeight.get() == "Ozdobny" and varPosterOverprint.get() == "4+4":
        foliowanie = drukKosztPracownikaLokal36Sra3NaMin
    else:
        foliowanie = 0
    ciecie = 0
    if varPosterSize.get() == "A4":
        ciecie = (ciecieA4PracownikLokal + ryczaltZaGilotyneNozMin) * float(entryPostersPatterns.get())
    else:
        ciecie = (ciecieA3PracownikLokal + ryczaltZaGilotyneNozMin) * float(entryPostersPatterns.get())
    finalCost = 0
    if varPosterPaperWeight.get() == "130":
        finalCost = (cost * (cenaPapieruSra3130g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varPosterPaperWeight.get() == "150":
        finalCost = (cost * (cenaPapieruSra3150g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varPosterPaperWeight.get() == "170":
        finalCost = (cost * (cenaPapieruSra3170g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varPosterPaperWeight.get() == "200":
        finalCost = (cost * (cenaPapieruSra3200g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varPosterPaperWeight.get() == "250":
        finalCost = (cost * (cenaPapieruSra3250g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varPosterPaperWeight.get() == "300":
        finalCost = (cost * (cenaPapieruSra3300g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varPosterPaperWeight.get() == "350":
        finalCost = (cost * (cenaPapieruSra3350g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    else:
        finalCost = (cost * (cenaPapieruSra3Ozdobny + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    finalCost = round(finalCost, 2)
    finalCostProfit = round((finalCost + (finalCost * stalyProcent)), 3)
    finalCostMargin = round((finalCostProfit + (finalCostProfit * margin)), 3)
    finalCostMarginVAT = round(finalCostMargin * 1.23, 3)
    textPosterCostProfit.delete("1.0", END)
    textPosterCostProfit.insert(END, finalCostProfit)
    textPosterMarginFinal.delete("1.0", END)
    textPosterMarginFinal.insert(END, finalCostMargin)
    textPosterMarginFinalVAT.delete("1.0", END)
    textPosterMarginFinalVAT.insert(END, finalCostMarginVAT)

labelPosterPatterns = Label(poster, text = "Ilość wzorów:")
labelPosterPatterns.pack()

entryPostersPatterns = StringVar()
entryPostersPatterns = Entry(poster, textvariable = entryPostersPatterns)
entryPostersPatterns.pack()

labelPosterQuantity = Label(poster, text = "Ilość:")
labelPosterQuantity.pack()

entryPosterQuantity = StringVar()
entryPosterQuantity = Entry(poster, textvariable = entryPosterQuantity)
entryPosterQuantity.pack()

labelPosterSize = Label(poster, text = "Wielkość:")
labelPosterSize.pack()

optPosterSize = ["A4", "A3"]
varPosterSize = StringVar()
varPosterSize.set(optPosterSize[0])
optPosterSize = OptionMenu(poster, varPosterSize, *optPosterSize)
optPosterSize.pack()

labelPosterPaperWeight = Label(poster, text = "Gramatura:")
labelPosterPaperWeight.pack()

optPosterPaperWeight = ["130", "150", "170", "200", "250", "300", "350", "Ozdobny"]
varPosterPaperWeight = StringVar()
varPosterPaperWeight.set(optPosterPaperWeight[0])
optPosterPaperWeight = OptionMenu(poster, varPosterPaperWeight, *optPosterPaperWeight)
optPosterPaperWeight.pack()

labelPostersOverprint = Label(poster, text = "Zadruk:")
labelPostersOverprint.pack()

optPosterOverprint = ["4+0", "4+4"]
varPosterOverprint = StringVar()
varPosterOverprint.set(optPosterOverprint[0])
optPosterOverprint = OptionMenu(poster, varPosterOverprint, *optPosterOverprint)
optPosterOverprint.pack()

labelPosterFoil = Label(poster, text = "Foliowanie:")
labelPosterFoil.pack()

optPosterFoil = ["Brak", "1+0", "1+1"]
varPosterFoil = StringVar()
varPosterFoil.set(optPosterFoil[0])
optPosterFoil = OptionMenu(poster, varPosterFoil, *optPosterFoil)
optPosterFoil.pack()

labelPosterMargin = Label(poster, text = "Marża:")
labelPosterMargin.pack()

entryPosterMargin = StringVar()
entryPosterMargin = Entry(poster, textvariable = entryPosterMargin)
entryPosterMargin.pack()

buttonPosterCost = Button(poster, text = "Oblicz", command = posterCost)
buttonPosterCost.pack()

labelPostersProfit = Label(poster, text = "Nasz koszt 7%:")
labelPostersProfit.pack()

textPosterCostProfit = Text(poster, height = 1, width = 20)
textPosterCostProfit.pack()

labelPosterMarginFinal = Label(poster, text = "Finalny koszt:")
labelPosterMarginFinal.pack()

textPosterMarginFinal = Text(poster, height = 1, width = 20)
textPosterMarginFinal.pack()

labelPosterMarginFinalVAT = Label(poster, text = "Finalny koszt + VAT:")
labelPosterMarginFinalVAT.pack()

textPosterMarginFinalVAT = Text(poster, height = 1, width = 20)
textPosterMarginFinalVAT.pack()

#flyers
def flyerCost():
    margin = round((float(entryFlyerMargin.get()) / 100), 3)
    cost = 0
    if varFlyerSize.get() == "A4":
        cost = float(entryFlyerPatterns.get()) * float(entryFlyerQuantity.get()) / 2
    elif varFlyerSize.get() == "A5" or varFlyerSize.get() == "14/14 14,5/14,5 15/15":
        cost = float(entryFlyerPatterns.get()) * float(entryFlyerQuantity.get()) / 4
    elif varFlyerSize.get() == "A6":
        cost = float(entryFlyerPatterns.get()) * float(entryFlyerQuantity.get()) / 8
    else:
        cost = float(entryFlyerPatterns.get()) * float(entryFlyerQuantity.get()) / 6
    cenaPrzelotuPracownik = 0
    if varFlyerOverprint.get() == "4+0":
        cenaPrzelotuPracownik = (2 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + drukKosztPracownikaLokal36Sra3NaMin
    else:
        cenaPrzelotuPracownik = (4 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + drukKosztPracownikaLokal36Sra3NaMin
    foliowanie = float(cenaFoliiZaPrzelotSra310) + float(ryczaltZakupFoliarkiDoliczonydoPrzelotu10Sra3) + float(foliaKosztPracownikaLokal2PrzelotyNaMin)
    if (varFlyerPaperWeight.get() == "200" or varFlyerPaperWeight.get() == "250" or varFlyerPaperWeight.get() == "300" or varFlyerPaperWeight.get() == "350") and varFlyerFoil.get() == "1+0" and varFlyerOverprint.get() == "4+0":
        foliowanie = foliowanie
    elif (varFlyerPaperWeight.get() == "200" or varFlyerPaperWeight.get() == "250" or varFlyerPaperWeight.get() == "300" or varFlyerPaperWeight.get() == "350") and varFlyerFoil.get() == "1+1" and varFlyerOverprint.get() == "4+4":
        foliowanie = foliowanie * 2 + drukKosztPracownikaLokal36Sra3NaMin
    elif varFlyerPaperWeight.get() == "Ozdobny" and varFlyerOverprint.get() == "4+4":
        foliowanie = drukKosztPracownikaLokal36Sra3NaMin
    else:
        foliowanie = 0
    ciecie = 0
    if varFlyerSize.get() == "A4":
        ciecie = (ciecieA4PracownikLokal + ryczaltZaGilotyneNozMin) * float(entryFlyerPatterns.get())
    elif varFlyerSize.get() == "A5" or varFlyerSize.get() == "14/14 14,5/14,5 15/15":
        ciecie = (ciecieA5PracownikLokal + ryczaltZaGilotyneNozMin) * float(entryFlyerPatterns.get())
    elif varFlyerSize.get() == "A6":
        ciecie = (ciecieA6PracownikLokal + ryczaltZaGilotyneNozMin) * float(entryFlyerPatterns.get())
    else:
        ciecie = (ciecieDlPracownikLokal + ryczaltZaGilotyneNozMin) * float(entryFlyerPatterns.get())
    finalCost = 0
    if varFlyerPaperWeight.get() == "130":
        finalCost = (cost * (cenaPapieruSra3130g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varFlyerPaperWeight.get() == "150":
        finalCost = (cost * (cenaPapieruSra3150g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varFlyerPaperWeight.get() == "170":
        finalCost = (cost * (cenaPapieruSra3170g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varFlyerPaperWeight.get() == "200":
        finalCost = (cost * (cenaPapieruSra3200g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varFlyerPaperWeight.get() == "250":
        finalCost = (cost * (cenaPapieruSra3250g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varFlyerPaperWeight.get() == "300":
        finalCost = (cost * (cenaPapieruSra3300g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varFlyerPaperWeight.get() == "350":
        finalCost = (cost * (cenaPapieruSra3350g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    else:
        finalCost = (cost * (cenaPapieruSra3Ozdobny + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    finalCost = round(finalCost, 2)
    finalCostProfit = round((finalCost + (finalCost * stalyProcent)), 3)
    finalCostMargin = round((finalCostProfit + (finalCostProfit * margin)), 3)
    finalCostMarginVAT = round(finalCostMargin * 1.23, 3)
    textFlyerCostProfit.delete("1.0", END)
    textFlyerCostProfit.insert(END, finalCostProfit)
    textFlyerMarginFinal.delete("1.0", END)
    textFlyerMarginFinal.insert(END, finalCostMargin)
    textFlyerMarginFinalVAT.delete("1.0", END)
    textFlyerMarginFinalVAT.insert(END, finalCostMarginVAT)

labelFlyerPatterns = Label(flyer, text = "Ilość wzorów:")
labelFlyerPatterns.pack()

entryFlyerPatterns = StringVar()
entryFlyerPatterns = Entry(flyer, textvariable = entryFlyerPatterns)
entryFlyerPatterns.pack()

labelFlyerQuantity = Label(flyer, text = "Ilość:")
labelFlyerQuantity.pack()

entryFlyerQuantity = StringVar()
entryFlyerQuantity = Entry(flyer, textvariable = entryFlyerQuantity)
entryFlyerQuantity.pack()

labelFlyerSize = Label(flyer, text = "Wielkość:")
labelFlyerSize.pack()

optFlyerSize = ["A4", "A5", "A6", "DL", "14/14 14,5/14,5 15/15"]
varFlyerSize = StringVar()
varFlyerSize.set(optFlyerSize[0])
optFlyerSize = OptionMenu(flyer, varFlyerSize, *optFlyerSize)
optFlyerSize.pack()

labelFlyerPaperWeight = Label(flyer, text = "Gramatura:")
labelFlyerPaperWeight.pack()

optFlyerPaperWeight = ["130", "150", "170", "200", "250", "300", "350", "Ozdobny"]
varFlyerPaperWeight = StringVar()
varFlyerPaperWeight.set(optFlyerPaperWeight[0])
optFlyerPaperWeight = OptionMenu(flyer, varFlyerPaperWeight, *optFlyerPaperWeight)
optFlyerPaperWeight.pack()

labelFlyersOverprint = Label(flyer, text = "Zadruk:")
labelFlyersOverprint.pack()

optFlyerOverprint = ["4+0", "4+4"]
varFlyerOverprint = StringVar()
varFlyerOverprint.set(optFlyerOverprint[0])
optFlyerOverprint = OptionMenu(flyer, varFlyerOverprint, *optFlyerOverprint)
optFlyerOverprint.pack()

labelFlyerFoil = Label(flyer, text = "Foliowanie:")
labelFlyerFoil.pack()

optFlyerFoil = ["Brak", "1+0", "1+1"]
varFlyerFoil = StringVar()
varFlyerFoil.set(optFlyerFoil[0])
optFlyerFoil = OptionMenu(flyer, varFlyerFoil, *optFlyerFoil)
optFlyerFoil.pack()

labelFlyerMargin = Label(flyer, text = "Marża:")
labelFlyerMargin.pack()

entryFlyerMargin = StringVar()
entryFlyerMargin = Entry(flyer, textvariable = entryFlyerMargin)
entryFlyerMargin.pack()

buttonFlyerCost = Button(flyer, text = "Oblicz", command = flyerCost)
buttonFlyerCost.pack()

labelFlyerProfit = Label(flyer, text = "Nasz koszt 7%:")
labelFlyerProfit.pack()

textFlyerCostProfit = Text(flyer, height = 1, width = 20)
textFlyerCostProfit.pack()

labelFlyerMarginFinal = Label(flyer, text = "Finalny koszt:")
labelFlyerMarginFinal.pack()

textFlyerMarginFinal = Text(flyer, height = 1, width = 20)
textFlyerMarginFinal.pack()

labelFlyerMarginFinalVAT = Label(flyer, text = "Finalny koszt + VAT:")
labelFlyerMarginFinalVAT.pack()

textFlyerMarginFinalVAT = Text(flyer, height = 1, width = 20)
textFlyerMarginFinalVAT.pack()

#roll-ups
blockoutSico420gm = 5.85
blockoutSico530gm = 7.60
cenaMaterial420gm = 2.5 * blockoutSico420gm
cenaMaterial420gm120 = 2.5 * blockoutSico420gm * 1.2
cenaMaterial530gm150 = 2.5 * blockoutSico530gm * 1.5
kosztAtramentM2 = 2.21
cenaWydruk85M2 = 0.85 * kosztAtramentM2 * 2.1
cenaWydruk100M2 = 1.0 * kosztAtramentM2 * 2.1
cenaWydruk120M2 = 1.2 * kosztAtramentM2 * 2.1
cenaWydruk150M2 = 1.5 * kosztAtramentM2 * 2.1
ryczaltMaszyna = 1.5
ryczaltSerwis85M2 = ryczaltMaszyna * 0.85 * 2.1
ryczaltSerwis100M2 = ryczaltMaszyna * 1.0 * 2.1
ryczaltSerwis120M2 = ryczaltMaszyna * 1.2 * 2.1
ryczaltSerwis150M2 = ryczaltMaszyna * 1.5 * 2.1
kosztKaseta85 = 35.4
kosztKaseta100 = 38.9
kosztKaseta120 = 68.0
kosztKaseta150 = 84.0
plikMediaZaladowanieTestGlowicy = 10.0
czasObsMasDrukStawkaPrac = 4.0
kosztPracownik85 = czasObsMasDrukStawkaPrac * 0.85 * 2.1
kosztPracownik100 = czasObsMasDrukStawkaPrac * 1.0 * 2.1
kosztPracownik120 = czasObsMasDrukStawkaPrac * 1.2 * 2.1
kosztPracownik150 = czasObsMasDrukStawkaPrac * 1.5 * 2.1
kosztPracCiecie = 4.0
kosztPracCiecie150 = 8.0
kosztPracMontazKaseta = 8.0

def rollUpCost():
    margin = round((float(entryRollUpMargin.get()) / 100), 3)
    finalCost = 0
    if varRollUpWidthThickness.get() == "85":
        finalCost = (plikMediaZaladowanieTestGlowicy + pakowanie + (cenaMaterial420gm + cenaWydruk85M2 + ryczaltSerwis85M2 + kosztKaseta85 + kosztPracownik85 + kosztPracCiecie + kosztPracMontazKaseta) * float(entryRollUpQuantity.get())) * float(entryRollUpPattern.get())
    elif varRollUpWidthThickness.get() == "100":
        finalCost = (plikMediaZaladowanieTestGlowicy + pakowanie + (cenaMaterial420gm + cenaWydruk100M2 + ryczaltSerwis100M2 + kosztKaseta100 + kosztPracownik100 + kosztPracCiecie + kosztPracMontazKaseta) * float(entryRollUpQuantity.get())) * float(entryRollUpPattern.get())
    elif varRollUpWidthThickness.get() == "120":
        finalCost = (plikMediaZaladowanieTestGlowicy + pakowanie + (cenaMaterial420gm120 + cenaWydruk120M2 + ryczaltSerwis120M2 + kosztKaseta120 + kosztPracownik120 + kosztPracCiecie + kosztPracMontazKaseta) * float(entryRollUpQuantity.get())) * float(entryRollUpPattern.get())
    elif varRollUpWidthThickness.get() == "150":
        finalCost = (plikMediaZaladowanieTestGlowicy + pakowanie + (cenaMaterial530gm150 + cenaWydruk150M2 + ryczaltSerwis150M2 + kosztKaseta150 + kosztPracownik150 + kosztPracCiecie150 + kosztPracMontazKaseta) * float(entryRollUpQuantity.get())) * float(entryRollUpPattern.get())
    else:
        finalCost = 666.66    
    finalCost = round(finalCost, 2)
    finalCostProfit = round((finalCost + (finalCost * stalyProcent)), 3)
    finalCostMargin = round((finalCostProfit + (finalCostProfit * margin)), 3)
    finalCostMarginVAT = round(finalCostMargin * 1.23, 3)
    textRollUpCostProfit.delete("1.0", END)
    textRollUpCostProfit.insert(END, finalCostProfit)
    textRollUpMarginFinal.delete("1.0", END)
    textRollUpMarginFinal.insert(END, finalCostMargin) 
    textRollUpMarginFinalVAT.delete("1.0", END)
    textRollUpMarginFinalVAT.insert(END, finalCostMarginVAT)

labelRollUpPattern = Label(rollUp, text = "Ilość wzorów:")
labelRollUpPattern.pack()

entryRollUpPattern = StringVar()
entryRollUpPattern = Entry(rollUp, textvariable = entryRollUpPattern)
entryRollUpPattern.pack()

labelRollUpQuantity = Label(rollUp, text = "Ilość:")
labelRollUpQuantity.pack()

entryRollUpQuantity = StringVar()
entryRollUpQuantity = Entry(rollUp, textvariable = entryRollUpQuantity)
entryRollUpQuantity.pack()

labelRollUpWidthThickness = Label(rollUp, text = "Szerokość/grubość:")

optRollUpWidthThickness = ["85", "100", "120", "150"]
varRollUpWidthThickness = StringVar()
varRollUpWidthThickness.set(optRollUpWidthThickness[0])
optRollUpWidthThickness = OptionMenu(rollUp, varRollUpWidthThickness, *optRollUpWidthThickness)
optRollUpWidthThickness.pack()

labelRollUpMargin = Label(rollUp, text = "Marża:")
labelRollUpMargin.pack()

entryRollUpMargin = StringVar()
entryRollUpMargin = Entry(rollUp, textvariable = entryRollUpMargin)
entryRollUpMargin.pack()

buttonRollUpCost = Button(rollUp, text = "Oblicz", command = rollUpCost)
buttonRollUpCost.pack()

labelRollUpProfit = Label(rollUp, text = "Nasz koszt 7%:")
labelRollUpProfit.pack()

textRollUpCostProfit = Text(rollUp, height = 1, width = 20)
textRollUpCostProfit.pack()

labelRollUpMarginFinal = Label(rollUp, text = "Finalny koszt:")
labelRollUpMarginFinal.pack()

textRollUpMarginFinal = Text(rollUp, height = 1, width = 20)
textRollUpMarginFinal.pack()

labelRollUpMarginFinalVAT = Label(rollUp, text = "Finalny koszt + VAT:")
labelRollUpMarginFinalVAT.pack()

textRollUpMarginFinalVAT = Text(rollUp, height = 1, width = 20)
textRollUpMarginFinalVAT.pack()

#folded flyers
skladanieMaszynowe = 1 / 18
przygotowanieMaszynyDoSkladania = 5.00
ryczaltFalcerkaSkladarka = 10.00
skladanieReczne = 6 / 60
bigowanie = 7.2 / 60
przygotowanieBigownicy = 5.00

def foldedFlyerCost():
    margin = round((float(entryFoldedFlyerMargin.get()) / 100), 3)

    cenaPrzelotuPracownik = 0
    if varFoldedFlyerOverprint.get() == "4+0":
        cenaPrzelotuPracownik = (2 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + drukKosztPracownikaLokal36Sra3NaMin
    elif varFoldedFlyerOverprint.get() == "4+0" and varFoldedFlyerFoil.get() == "1+0":
        cenaPrzelotuPracownik = (2 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + (2 * drukKosztPracownikaLokal36Sra3NaMin)
    elif varFoldedFlyerOverprint.get() == "4+4" and varFoldedFlyerFoil.get() == "1+1":
        cenaPrzelotuPracownik = (4 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + (2 * drukKosztPracownikaLokal36Sra3NaMin)
    else:
        cenaPrzelotuPracownik = (4 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + drukKosztPracownikaLokal36Sra3NaMin

    foliowanie = float(cenaFoliiZaPrzelotSra310) + float(ryczaltZakupFoliarkiDoliczonydoPrzelotu10Sra3) + float(foliaKosztPracownikaLokal2PrzelotyNaMin)
    if (varFoldedFlyerPaperWeight.get() == "200" or varFoldedFlyerPaperWeight.get() == "250" or varFoldedFlyerPaperWeight.get() == "300" or varFoldedFlyerPaperWeight.get() == "350") and varFoldedFlyerFoil.get() == "1+0" and varFoldedFlyerOverprint.get() == "4+0":
        foliowanie = foliowanie
    elif (varFoldedFlyerPaperWeight.get() == "200" or varFoldedFlyerPaperWeight.get() == "250" or varFoldedFlyerPaperWeight.get() == "300" or varFoldedFlyerPaperWeight.get() == "350") and varFoldedFlyerFoil.get() == "1+1" and varFoldedFlyerOverprint.get() == "4+4":
        foliowanie = foliowanie * 2
    else:
        foliowanie = 0
    
    ciecie = 0
    if varFoldedFlyerSize.get() == "A5 do A6":
        ciecie = (ciecieA5PracownikLokal + ryczaltZaGilotyneNozMin) * float(entryFoldedFlyerPatterns.get())
    elif varFoldedFlyerSize.get() == "A6 do A7":
        ciecie = (ciecieA6PracownikLokal + ryczaltZaGilotyneNozMin) * float(entryFoldedFlyerPatterns.get())
    else:
        ciecie = ((ciecieA4PracownikLokal + ryczaltZaGilotyneNozMin) * float(entryFoldedFlyerPatterns.get()))
    
    foldMachineArm = round(ryczaltFalcerkaSkladarka + przygotowanieMaszynyDoSkladania + (skladanieMaszynowe * float(entryFoldedFlyerQuantity.get())), 3)
    
    foldBig = 0
    if varFoldedFlyerFold.get() == "Tylko big" and varFoldedFlyerSize.get() == "A4 do DL":
        foldBig = round(przygotowanieBigownicy + (bigowanie * float(entryFoldedFlyerQuantity.get()) * 2) + (skladanieReczne * float(entryFoldedFlyerQuantity.get()) * 0), 3)
    elif varFoldedFlyerFold.get() == "Składanie + big" and varFoldedFlyerSize.get() == "A4 do DL":
        foldBig = round(przygotowanieBigownicy + (bigowanie * float(entryFoldedFlyerQuantity.get()) * 2) + (skladanieReczne * float(entryFoldedFlyerQuantity.get()) * 2), 3)
    elif varFoldedFlyerFold.get() == "Tylko big":
        foldBig = round(przygotowanieBigownicy + (bigowanie * float(entryFoldedFlyerQuantity.get())), 3)
    else:
        foldBig = round(przygotowanieBigownicy + (bigowanie * float(entryFoldedFlyerQuantity.get())) + skladanieReczne * float(entryFoldedFlyerQuantity.get()), 3)
       
    cost = 0
    if varFoldedFlyerSize.get() == "A3 do A4":
        cost = float(entryFoldedFlyerPatterns.get()) * float(entryFoldedFlyerQuantity.get())
    elif varFoldedFlyerSize.get() == "A5 do A6":
        cost = float(entryFoldedFlyerPatterns.get()) * float(entryFoldedFlyerQuantity.get()) / 4
    elif varFoldedFlyerSize.get() == "A6 do A7":
        cost = float(entryFoldedFlyerPatterns.get()) * float(entryFoldedFlyerQuantity.get()) / 8
    elif varFoldedFlyerSize.get() == "28 do 14":
        cost = float(entryFoldedFlyerPatterns.get()) * float(entryFoldedFlyerQuantity.get()) / 3
    else:
        cost = float(entryFoldedFlyerPatterns.get()) * float(entryFoldedFlyerQuantity.get()) / 2
    
    finalCost = 0
    if varFoldedFlyerPaperWeight.get() == "130":
        finalCost = (cost * (cenaPapieruSra3130g + cenaPrzelotuPracownik + foliowanie) + foldMachineArm + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varFoldedFlyerPaperWeight.get() == "150":
        finalCost = (cost * (cenaPapieruSra3150g + cenaPrzelotuPracownik + foliowanie) + foldMachineArm + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varFoldedFlyerPaperWeight.get() == "170":
        finalCost = (cost * (cenaPapieruSra3170g + cenaPrzelotuPracownik + foliowanie) + foldBig + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varFoldedFlyerPaperWeight.get() == "200":
        finalCost = (cost * (cenaPapieruSra3200g + cenaPrzelotuPracownik + foliowanie) + foldBig + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varFoldedFlyerPaperWeight.get() == "250":
        finalCost = (cost * (cenaPapieruSra3250g + cenaPrzelotuPracownik + foliowanie) + foldBig + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varFoldedFlyerPaperWeight.get() == "300":
        finalCost = (cost * (cenaPapieruSra3300g + cenaPrzelotuPracownik + foliowanie) + foldBig + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varFoldedFlyerPaperWeight.get() == "350":
        finalCost = (cost * (cenaPapieruSra3350g + cenaPrzelotuPracownik + foliowanie) + foldBig + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    else:
        finalCost = (cost * (cenaPapieruSra3Ozdobny + cenaPrzelotuPracownik + foliowanie) + foldBig + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    
    finalCost = round(finalCost, 2)
    finalCostProfit = round((finalCost + (finalCost * stalyProcent)), 3)
    finalCostProfitMargin = round((finalCostProfit + (finalCostProfit * margin)), 3)
    finalCostProfitMarginVAT = round(finalCostProfitMargin * 1.23, 3)
    textFoldedFlyerCostProfit.delete("1.0", END)
    textFoldedFlyerCostProfit.insert(END, finalCostProfit)
    textFoldedFlyerMarginFinal.delete("1.0", END)
    textFoldedFlyerMarginFinal.insert(END, finalCostProfitMargin)
    textFoldedFlyerMarginFinalVAT.delete("1.0", END)
    textFoldedFlyerMarginFinalVAT.insert(END, finalCostProfitMarginVAT)

labelFoldedFlyerPatterns = Label(foldedFlyer, text = "Ilość wzorów:")
labelFoldedFlyerPatterns.pack()

entryFoldedFlyerPatterns = StringVar()
entryFoldedFlyerPatterns = Entry(foldedFlyer, textvariable = entryFoldedFlyerPatterns)
entryFoldedFlyerPatterns.pack()

labelFoldedFlyerQuantity = Label(foldedFlyer, text = "Ilość:")
labelFoldedFlyerQuantity.pack()

entryFoldedFlyerQuantity = StringVar()
entryFoldedFlyerQuantity = Entry(foldedFlyer, textvariable = entryFoldedFlyerQuantity)
entryFoldedFlyerQuantity.pack()

labelFoldedFlyerFold = Label(foldedFlyer, text = "Składanie/bigowanie:")
labelFoldedFlyerFold.pack()

optFoldedFlyerFold = ["Tylko big", "Składanie + big"]
varFoldedFlyerFold = StringVar()
varFoldedFlyerFold.set(optFoldedFlyerFold[0])
optFoldedFlyerFold = OptionMenu(foldedFlyer, varFoldedFlyerFold, *optFoldedFlyerFold)
optFoldedFlyerFold.pack()

labelFoldedFlyerSize = Label(foldedFlyer, text = "Wielkość:")
labelFoldedFlyerSize.pack()

optFoldedFlyerSize = ["A3 do A4", "A4 do A5", "A5 do A6", "A6 do A7", "A4 do DL", "2xDL do DL", "28 do 14", "29 do 14,5, 30 do 15"]
varFoldedFlyerSize = StringVar()
varFoldedFlyerSize.set(optFoldedFlyerSize[0])
optFoldedFlyerSize = OptionMenu(foldedFlyer, varFoldedFlyerSize, *optFoldedFlyerSize)
optFoldedFlyerSize.pack()

labelFoldedFlyerPaperWeight = Label(foldedFlyer, text = "Gramatura:")
labelFoldedFlyerPaperWeight.pack()

optFoldedFlyerPaperWeight = ["130", "150", "170", "200", "250", "300", "350", "Ozdobny"]
varFoldedFlyerPaperWeight = StringVar()
varFoldedFlyerPaperWeight.set(optFoldedFlyerPaperWeight[0])
optFoldedFlyerPaperWeight = OptionMenu(foldedFlyer, varFoldedFlyerPaperWeight, *optFoldedFlyerPaperWeight)
optFoldedFlyerPaperWeight.pack()

labelFoldedFlyersOverprint = Label(foldedFlyer, text = "Zadruk:")
labelFoldedFlyersOverprint.pack()

optFoldedFlyerOverprint = ["4+0", "4+4"]
varFoldedFlyerOverprint = StringVar()
varFoldedFlyerOverprint.set(optFoldedFlyerOverprint[0])
optFoldedFlyerOverprint = OptionMenu(foldedFlyer, varFoldedFlyerOverprint, *optFoldedFlyerOverprint)
optFoldedFlyerOverprint.pack()

labelFoldedFlyerFoil = Label(foldedFlyer, text = "Foliowanie:")
labelFoldedFlyerFoil.pack()

optFoldedFlyerFoil = ["Brak", "1+0", "1+1"]
varFoldedFlyerFoil = StringVar()
varFoldedFlyerFoil.set(optFoldedFlyerFoil[0])
optFoldedFlyerFoil = OptionMenu(foldedFlyer, varFoldedFlyerFoil, *optFoldedFlyerFoil)
optFoldedFlyerFoil.pack()

labelFoldedFlyerMargin = Label(foldedFlyer, text = "Marża:")
labelFoldedFlyerMargin.pack()

entryFoldedFlyerMargin = StringVar()
entryFoldedFlyerMargin = Entry(foldedFlyer, textvariable = entryFoldedFlyerMargin)
entryFoldedFlyerMargin.pack()

buttonFoldedFlyerCost = Button(foldedFlyer, text = "Oblicz", command = foldedFlyerCost)
buttonFoldedFlyerCost.pack()

labelFoldedFlyerProfit = Label(foldedFlyer, text = "Nasz koszt 7%:")
labelFoldedFlyerProfit.pack()

textFoldedFlyerCostProfit = Text(foldedFlyer, height = 1, width = 20)
textFoldedFlyerCostProfit.pack()

labelFoldedFlyerMarginFinal = Label(foldedFlyer, text = "Finalny koszt:")
labelFoldedFlyerMarginFinal.pack()

textFoldedFlyerMarginFinal = Text(foldedFlyer, height = 1, width = 20)
textFoldedFlyerMarginFinal.pack()

labelFoldedFlyerMarginFinalVAT = Label(foldedFlyer, text = "Finalny koszt + VAT:")
labelFoldedFlyerMarginFinalVAT.pack()

textFoldedFlyerMarginFinalVAT = Text(foldedFlyer, height = 1, width = 20)
textFoldedFlyerMarginFinalVAT.pack()

# custom flyers
def customFlyerCost():
    margin = round((float(entryCustomFlyerMargin.get()) / 100), 3)

    cenaPrzelotuPracownik = 0
    if varCustomFlyerOverprint.get() == "4+0":
        cenaPrzelotuPracownik = (2 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + drukKosztPracownikaLokal36Sra3NaMin
    elif varCustomFlyerOverprint.get() == "4+0" and varFoldedFlyerFoil.get() == "1+0":
        cenaPrzelotuPracownik = (2 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + (2 * drukKosztPracownikaLokal36Sra3NaMin)
    elif varCustomFlyerOverprint.get() == "4+4" and varFoldedFlyerFoil.get() == "1+1":
        cenaPrzelotuPracownik = (4 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + (2 * drukKosztPracownikaLokal36Sra3NaMin)
    else:
        cenaPrzelotuPracownik = (4 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + drukKosztPracownikaLokal36Sra3NaMin

    foliowanie = float(cenaFoliiZaPrzelotSra310) + float(ryczaltZakupFoliarkiDoliczonydoPrzelotu10Sra3) + float(foliaKosztPracownikaLokal2PrzelotyNaMin)
    if (varCustomFlyerPaperWeight.get() == "200" or varCustomFlyerPaperWeight.get() == "250" or varCustomFlyerPaperWeight.get() == "300" or varCustomFlyerPaperWeight.get() == "350") and varCustomFlyerFoil.get() == "1+0" and varFoldedFlyerOverprint.get() == "4+0":
        foliowanie = foliowanie
    elif (varCustomFlyerPaperWeight.get() == "200" or varCustomFlyerPaperWeight.get() == "250" or varCustomFlyerPaperWeight.get() == "300" or varCustomFlyerPaperWeight.get() == "350") and varCustomFlyerFoil.get() == "1+1" and varFoldedFlyerOverprint.get() == "4+4":
        foliowanie = foliowanie * 2
    else:
        foliowanie = 0
    
    ciecie = 10
    
    foldMachineArm = round(ryczaltFalcerkaSkladarka + przygotowanieMaszynyDoSkladania + (skladanieMaszynowe * float(entryCustomFlyerQuantity.get())), 3)
    
    foldBig = 0
    if varCustomFlyerFold.get() == "Tylko big":
        foldBig = round(przygotowanieBigownicy + (bigowanie * float(entryCustomFlyerQuantity.get()) * 2) + (skladanieReczne * float(entryCustomFlyerQuantity.get()) * 0), 3)
    elif varCustomFlyerFold.get() == "Składanie + big":
        foldBig = round(przygotowanieBigownicy + (bigowanie * float(entryCustomFlyerQuantity.get()) * 2) + (skladanieReczne * float(entryCustomFlyerQuantity.get()) * 2), 3)
    else:
        foldBig = 0
    
    customLengthQuantityPerSheet = math.floor(30.9 / int(entryCustomFlyerLength.get()))
    customWidthQuantityPerSheet = math.floor(43.9 / int(entryCustomFlyerWidth.get()))
    customQuantityPerSheet = customLengthQuantityPerSheet * customWidthQuantityPerSheet

    cost = float(entryCustomFlyerQuantity.get()) / customQuantityPerSheet
    
    finalCost = 0
    if varCustomFlyerPaperWeight.get() == "130":
        finalCost = (cost * (cenaPapieruSra3130g + cenaPrzelotuPracownik + foliowanie) + foldMachineArm + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varCustomFlyerPaperWeight.get() == "150":
        finalCost = (cost * (cenaPapieruSra3150g + cenaPrzelotuPracownik + foliowanie) + foldMachineArm + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varCustomFlyerPaperWeight.get() == "170":
        finalCost = (cost * (cenaPapieruSra3170g + cenaPrzelotuPracownik + foliowanie) + foldBig + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varCustomFlyerPaperWeight.get() == "200":
        finalCost = (cost * (cenaPapieruSra3200g + cenaPrzelotuPracownik + foliowanie) + foldBig + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varCustomFlyerPaperWeight.get() == "250":
        finalCost = (cost * (cenaPapieruSra3250g + cenaPrzelotuPracownik + foliowanie) + foldBig + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varCustomFlyerPaperWeight.get() == "300":
        finalCost = (cost * (cenaPapieruSra3300g + cenaPrzelotuPracownik + foliowanie) + foldBig + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varCustomFlyerPaperWeight.get() == "350":
        finalCost = (cost * (cenaPapieruSra3350g + cenaPrzelotuPracownik + foliowanie) + foldBig + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    else:
        finalCost = (cost * (cenaPapieruSra3Ozdobny + cenaPrzelotuPracownik + foliowanie) + foldBig + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    
    finalCost = round(finalCost, 2)
    finalCostProfit = round((finalCost + (finalCost * stalyProcent)), 3)
    finalCostProfitMargin = round((finalCostProfit + (finalCostProfit * margin)), 3)
    finalCostProfitMarginVAT = round(finalCostProfitMargin * 1.23, 3)
    textCustomFlyerQuantityPerSheet.delete("1.0", END)
    textCustomFlyerQuantityPerSheet.insert(END, customQuantityPerSheet)
    textCustomFlyerCostProfit.delete("1.0", END)
    textCustomFlyerCostProfit.insert(END, finalCostProfit)
    textCustomFlyerMarginFinal.delete("1.0", END)
    textCustomFlyerMarginFinal.insert(END, finalCostProfitMargin)
    textCustomFlyerMarginFinalVAT.delete("1.0", END)
    textCustomFlyerMarginFinalVAT.insert(END, finalCostProfitMarginVAT)

labelCustomFlyerLength = Label(customFlyer, text = "Długość [cm]:")
labelCustomFlyerLength.pack()

entryCustomFlyerLength = StringVar()
entryCustomFlyerLength = Entry(customFlyer, textvariable = entryCustomFlyerLength)
entryCustomFlyerLength.pack()

labelCustomFlyerWidth = Label(customFlyer, text = "Szerokość [cm]:")
labelCustomFlyerWidth.pack()

entryCustomFlyerWidth = StringVar()
entryCustomFlyerWidth = Entry(customFlyer, textvariable = entryCustomFlyerWidth)
entryCustomFlyerWidth.pack()

labelCustomFlyerQuantity = Label(customFlyer, text = "Ilość:")
labelCustomFlyerQuantity.pack()

entryCustomFlyerQuantity = StringVar()
entryCustomFlyerQuantity = Entry(customFlyer, textvariable = entryCustomFlyerQuantity)
entryCustomFlyerQuantity.pack()

labelCustomFlyerFold = Label(customFlyer, text = "Składanie/bigowanie:")
labelCustomFlyerFold.pack()

optCustomFlyerFold = ["Brak", "Tylko big", "Składanie + big"]
varCustomFlyerFold = StringVar()
varCustomFlyerFold.set(optCustomFlyerFold[0])
optCustomFlyerFold = OptionMenu(customFlyer, varCustomFlyerFold, *optCustomFlyerFold)
optCustomFlyerFold.pack()

labelCustomFlyerPaperWeight = Label(customFlyer, text = "Gramatura:")
labelCustomFlyerPaperWeight.pack()

optCustomFlyerPaperWeight = ["130", "150", "170", "200", "250", "300", "350", "Ozdobny"]
varCustomFlyerPaperWeight = StringVar()
varCustomFlyerPaperWeight.set(optCustomFlyerPaperWeight[0])
optCustomFlyerPaperWeight = OptionMenu(customFlyer, varCustomFlyerPaperWeight, *optCustomFlyerPaperWeight)
optCustomFlyerPaperWeight.pack()

labelCustomFlyersOverprint = Label(customFlyer, text = "Zadruk:")
labelCustomFlyersOverprint.pack()

optCustomFlyerOverprint = ["4+0", "4+4"]
varCustomFlyerOverprint = StringVar()
varCustomFlyerOverprint.set(optCustomFlyerOverprint[0])
optCustomFlyerOverprint = OptionMenu(customFlyer, varCustomFlyerOverprint, *optCustomFlyerOverprint)
optCustomFlyerOverprint.pack()

labelCustomFlyerFoil = Label(customFlyer, text = "Foliowanie:")
labelCustomFlyerFoil.pack()

optCustomFlyerFoil = ["Brak", "1+0", "1+1"]
varCustomFlyerFoil = StringVar()
varCustomFlyerFoil.set(optCustomFlyerFoil[0])
optCustomFlyerFoil = OptionMenu(customFlyer, varCustomFlyerFoil, *optCustomFlyerFoil)
optCustomFlyerFoil.pack()

labelCustomFlyerMargin = Label(customFlyer, text = "Marża:")
labelCustomFlyerMargin.pack()

entryCustomFlyerMargin = StringVar()
entryCustomFlyerMargin = Entry(customFlyer, textvariable = entryCustomFlyerMargin)
entryCustomFlyerMargin.pack()

buttonCustomFlyerCost = Button(customFlyer, text = "Oblicz", command = customFlyerCost)
buttonCustomFlyerCost.pack()

labelCustomFlyerQuantityPerSheet = Label(customFlyer, text = "Ilość na arkuszu:")
labelCustomFlyerQuantityPerSheet.pack()

textCustomFlyerQuantityPerSheet = Text(customFlyer, height = 1, width = 20)
textCustomFlyerQuantityPerSheet.pack()

labelCustomFlyerProfit = Label(customFlyer, text = "Nasz koszt 7%:")
labelCustomFlyerProfit.pack()

textCustomFlyerCostProfit = Text(customFlyer, height = 1, width = 20)
textCustomFlyerCostProfit.pack()

labelCustomFlyerMarginFinal = Label(customFlyer, text = "Finalny koszt:")
labelCustomFlyerMarginFinal.pack()

textCustomFlyerMarginFinal = Text(customFlyer, height = 1, width = 20)
textCustomFlyerMarginFinal.pack()

labelCustomFlyerMarginFinalVAT = Label(customFlyer, text = "Finalny koszt + VAT:")
labelCustomFlyerMarginFinalVAT.pack()

textCustomFlyerMarginFinalVAT = Text(customFlyer, height = 1, width = 20)
textCustomFlyerMarginFinalVAT.pack()

# banner
def bannerCost():
    margin = round((float(entryBannerMargin.get()) / 100), 3)

    bannerCircuit = float(2 * (float(entryBannerLength.get()) + float(entryBannerWidth.get())))
    bannerArea = float(entryBannerLength.get()) * float(entryBannerWidth.get())

    bannerTapeCost = 0
    if varBannerTape.get() == "Tak":
        bannerTapeCost = float(bannerCircuit * 0.46)
    else:
        bannerTapeCost = 0

    bannerEyeletCost = 0
    bannerSingleEyeletCost = 0.09
    if varBannerEyelet.get() == "Co 25 cm":
        bannerEyeletCost = float((bannerCircuit / 0.25) * bannerSingleEyeletCost)
    elif varBannerEyelet.get() == "Co 50 cm":
        bannerEyeletCost = float((bannerCircuit / 0.50) * bannerSingleEyeletCost)
    elif varBannerEyelet.get() == "Tylko rogi":
        bannerEyeletCost = 4 * bannerSingleEyeletCost
    else:
        bannerEyeletCost = 0

    bannerLaminationCost = 0
    if varBannerLamination.get() == "Tak":
        bannerLaminationCost = float(bannerArea * 6.0)
        if bannerLaminationCost < 25.0:
            bannerLaminationCost = 25.0
        else:
            bannerLaminationCost = float(bannerArea * 6.0)
    else:
        bannerLaminationCost = 0

    bannerCut = 5.0
    cenaJednostkowaMaterialBaner = 3.2

    bannerMaterialCost = float(cenaJednostkowaMaterialBaner * bannerArea)
    bannerPrintCost = float(kosztAtramentM2 * bannerArea)
    bannerRyczaltSerwis = float(ryczaltMaszyna * bannerArea)
    kosztPracownikaBaner = 8.0

    finalCost = (plikMediaZaladowanieTestGlowicy + pakowanie + (bannerMaterialCost + bannerPrintCost + bannerEyeletCost + bannerTapeCost + bannerLaminationCost + bannerRyczaltSerwis + kosztPracownikaBaner + bannerCut) * float(entryBannerQuantity.get()))

    finalCost = round(finalCost, 2)
    finalCostProfit = round((finalCost + (finalCost * stalyProcent)), 3)
    finalCostMargin = round((finalCostProfit + (finalCostProfit * margin)), 3)
    finalCostMarginVAT = round(finalCostMargin * 1.23, 3)
    textBannerCostProfit.delete("1.0", END)
    textBannerCostProfit.insert(END, finalCostProfit)
    textBannerMarginFinal.delete("1.0", END)
    textBannerMarginFinal.insert(END, finalCostMargin) 
    textBannerMarginFinalVAT.delete("1.0", END)
    textBannerMarginFinalVAT.insert(END, finalCostMarginVAT)

labelBannerLength = Label(banner, text = "Długość [m]:")
labelBannerLength.pack()

entryBannerLength = StringVar()
entryBannerLength = Entry(banner, textvariable = entryBannerLength)
entryBannerLength.pack()

labelBannerWidth = Label(banner, text = "Szerokość [m]:")
labelBannerWidth.pack()

entryBannerWidth = StringVar()
entryBannerWidth = Entry(banner, textvariable = entryBannerWidth)
entryBannerWidth.pack()

labelBannerQuantity = Label(banner, text = "Ilość:")
labelBannerQuantity.pack()

entryBannerQuantity = StringVar()
entryBannerQuantity = Entry(banner, textvariable = entryBannerQuantity)
entryBannerQuantity.pack()

labelBannerTape = Label(banner, text = "Taśma banerowa:")
labelBannerTape.pack()

optBannerTape = ["Tak", "Nie"]
varBannerTape = StringVar()
varBannerTape.set(optBannerTape[1])
optBannerTape = OptionMenu(banner, varBannerTape, *optBannerTape)
optBannerTape.pack()

labelBannerEyelet = Label(banner, text = "Oczka:")
labelBannerEyelet.pack()

optBannerEyelet = ["Brak", "Co 25 cm", "Co 50 cm", "Tylko rogi"]
varBannerEyelet = StringVar()
varBannerEyelet.set(optBannerEyelet[0])
optBannerEyelet = OptionMenu(banner, varBannerEyelet, *optBannerEyelet)
optBannerEyelet.pack()

labelBannerLamination = Label(banner, text = "Laminowanie płynem:")
labelBannerLamination.pack()

optBannerLamination = ["Tak", "Nie"]
varBannerLamination = StringVar()
varBannerLamination.set(optBannerLamination[1])
optBannerLamination = OptionMenu(banner, varBannerLamination, *optBannerLamination)
optBannerLamination.pack()

labelBannerMargin = Label(banner, text = "Marża:")
labelBannerMargin.pack()

entryBannerMargin = StringVar()
entryBannerMargin = Entry(banner, textvariable = entryBannerMargin)
entryBannerMargin.pack()

buttonBannerCost = Button(banner, text = "Oblicz", command = bannerCost)
buttonBannerCost.pack()

labelBannerProfit = Label(banner, text = "Nasz koszt 7%:")
labelBannerProfit.pack()

textBannerCostProfit = Text(banner, height = 1, width = 20)
textBannerCostProfit.pack()

labelBannerMarginFinal = Label(banner, text = "Finalny koszt:")
labelBannerMarginFinal.pack()

textBannerMarginFinal = Text(banner, height = 1, width = 20)
textBannerMarginFinal.pack()

labelBannerMarginFinalVAT = Label(banner, text = "Finalny koszt + VAT:")
labelBannerMarginFinalVAT.pack()

textBannerMarginFinalVAT = Text(banner, height = 1, width = 20)
textBannerMarginFinalVAT.pack()

calcWindow.mainloop()