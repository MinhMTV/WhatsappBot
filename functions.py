import os

import WhatsAppBot as w
import time as t
import keyfunc as k
import Settings as s
from datetime import datetime, date


# e.g d1 today, d2 birthyear
def years_between(d1, d2):
    return d1.year - d2.year - ((d1.month, d1.day) < (d2.month, d2.day))


# e.g d1 today, d2 birthyear replaced by actual date
def days_age(d1, d2):
    actualYear = date(getActualDate().year, d2.month, d2.day)
    if (d1 - actualYear).days > -1:
        return (d1 - actualYear).days
    else:
        actualYear = date(subtract_years(getActualDate(), 1).year, d2.month, d2.day)
        print(actualYear)
    return (d1 - actualYear).days


def subtract_years(dt, years):
    try:
        dt = dt.replace(year=dt.year-years)
    except ValueError:
        dt = dt.replace(year=dt.year-years, day=dt.day-1)
    return dt


def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)


def getActualDate():
    today = date.today()
    return today


def getCreationDay(file_path):
    return str(datetime.fromtimestamp(os.path.getctime(file_path)).strftime("%Y-%m-%d"))


class Func:
    def __init__(self, browser):
        self.chrome_browser = browser
        self.k = k.Keyfunc(browser)

    def noticeAllUser(self):
        for u in s.user_answer_list:
            t.sleep(2)
            self.k.writeMessageToUser(u, f"Hallo {self.k.getUserName(u)}")
            self.k.writeMessageToUser(u,
                                      f"Mein Name ist Hachiko und ich bin ein WhatsApp-Bot programmiert von meinem Erfinder, dem sensationellen *Minh*")
            self.k.writeMessageToUser(u, f"Erfahre mehr über mich mit dem Befehl *!Bot*")
            self.k.writeMessageToUser(u, f"Lerne alle meine Funktionen kennen mit dem Befehl *!Help*")
            self.k.writeMessageToUser(u, f"Erfahre mehr über Minh, dem Erfinder mit dem Befehl *!Minh*")
            self.k.writeMessageToUser(u, f"Lerne Fakten über Minh kennen mit dem Befehl *!Facts*")

    def repeatFunc(self, user):

        x = ""
        LAST_BOT_MSG = self.k.writeMessageToUser(user, "Repeat Funktion wurde gestarted")
        while 1:
            msg = self.k.getMessage()
            try:
                if msg != x and msg.lower().replace(" ", "") != "!startrepeat":
                    if msg.lower().replace(" ", "") in s.valid_end:
                        self.k.writeMessageToUser(user, "Repeat Funktion wurde beendet")
                        return 1
                    else:
                        self.k.writeMessageToUser(user, msg)
                        x = self.k.getMessage()
            except AttributeError:
                pass

    def getHelp(self, u):
        self.k.writeMessageToUser(u, f"Hallo {self.k.getUserName(u)}")
        self.k.writeMessageToUser(u,
                                  f"Mein Bot hat einige Funktionen, die du durch eine TextNachricht aktivieren kannst")
        self.k.writeMessageToUser(u, f"1.")
        self.k.writeMessageToUser(u, f"*!Start Repeat*")
        self.k.writeMessageToUser(u,
                                  f"Wiederholt jedes Wort, welches du mir schreibst. Beenden kannst du die Funktion mit dem Befehl: *!End*")
        self.k.writeMessageToUser(u, f"Erfahre mehr mich mit dem Befehl *!Bot*")
        self.k.writeMessageToUser(u, f"Erfahre mehr über Minh, dem Erfinder mit dem Befehl *!Minh*")
        self.k.writeMessageToUser(u, f"Lerne Fakten über Minh kennen mit dem Befehl *!Facts*")

        return

    def explainBot(self, u):
        self.k.writeMessageToUser(u, f"Mein Name ist Hachiko")
        self.k.writeMessageToUser(u,
                                  f"Ich bin am {getCreationDay(w.FILE_CREATION)} zur Welt gekommen, bin jetzt schon {days_between(getCreationDay(w.FILE_CREATION), str(getActualDate()))} Tage alt und werde seitdem stetig verbessert")
        self.k.writeMessageToUser(u,
                                  "Ich laufe nicht 24 Stunden lang (vorerst), sondern nur, solange Minh mich startet")
        self.k.writeMessageToUser(u,
                                  "Falls ich aber laufe, bin ich laufend für dich verfügbar und du kannst jederzeit mit mir interagieren")
        self.k.writeMessageToUser(u,
                                  "Falls du Ideen oder Anregungen hast ,um mich zu verbessern, kannst du gerne meinen Erfindern anschreiben")
        self.k.writeMessageToUser(u, "Ansonsten wünsche ich dir jetzt jetzt einen schönen Tag :)")

    def explainMinh(self, u):
        self.k.writeMessageToUser(u,
                                  f"Minh, auch bekannt als 'Der Coolste' ist {years_between(getActualDate(), s.birth_Inventor)} Jahre und {days_age(getActualDate(), s.birth_Inventor)} Tage alt")
        self.k.writeMessageToUser(u,
                                  f"Momentan studiert er Medizintechnik an der Universität Duisburg-Essen")
        self.k.writeMessageToUser(u,
                                  "Schon früh hat er erkannt, dass menschliche Interaktion ein Pain in the Ass ist")
        self.k.writeMessageToUser(u,
                                  "Daher hat er mich erfunden, um mit euch neben seine wirklich busyen Lifestyle zu kommunizieren")
        self.k.writeMessageToUser(u,
                                  "Nichtsdestotrotz gibt er sich Mühe, ab und zu mal sozialen Aktivitäten zu unternehmen")
        self.k.writeMessageToUser(u, "Möchtest du mehr Fakten über Minh lernen, schicke eine Message mit *!Facts*")

    def explainFacts(self, u):
        self.k.writeMessageToUser(u,
                                  f"Minh spricht *8* Sprachen fließend. Er gibt aber nicht gerne an und spricht damit auch nicht mit Bekannten, weil es ihm peinlich ist")
        self.k.writeMessageToUser(u,
                                  f"Im Alter von 10 Jahre hat er sein eigenes Business gegründet namens *M&M* (Minh&Man)")
        self.k.writeMessageToUser(u,
                                  "Sein Lebensmotto? *Minhimaler Effort*, Maximaler Output")
        self.k.writeMessageToUser(u,
                                  "Neben seinem 'normalen Leben' geht er auch Nachts auf Verbrecherjagd. Seine Deckname ist vielleicht bekannt unter den Namen *Batman*" )
        self.k.writeMessageToUser(u,
                                  "Obwohl Minh immer schon ein normaler Junge sein wollte, war es ihm es nie möglich, ein normales Leben zu führen, da sein *hoher* Intelligenzquotient dazu"
                                  " führte, dumme Menschen zu verachten und Hass in ihm aufzubauen")
        self.k.writeMessageToUser(u, "In seiner Freizeit hilft Minh bei verschiedenen Projekten. Sein letztes Projekt ist streng geheim gewesen, aber ein Tipp: Es hat was mit *Raketen* und der *ISS* zu tun")

    def getFunction(self, u, message):
        x = message.lower().replace(" ", "")
        if x.startswith('!'):
            if x == "!startrepeat":
                self.repeatFunc(u)
                return "!startrepeat"
            elif x == "!help":
                self.getHelp(u)
                return "!help"
            elif x == "!bot":
                self.explainBot(u)
                return "!bot"
            elif x == "!minh":
                self.explainMinh(u)
                return "!minh"
            elif x == "!facts":
                self.explainFacts(u)
                return "!facts"
        else:
            return
