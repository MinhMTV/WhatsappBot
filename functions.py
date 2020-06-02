import WhatsAppBot as w
import time as t
import keyfunc as k
import Settings as s



class Func:
    def __init__(self, browser):
        self.chrome_browser = browser
        self.k = k.Keyfunc(browser)

    def noticeAllUser(self):
            for u in s.user_answer_list:
                t.sleep(2)
                self.k.writeMessageToUser(u, f"Hallo {self.k.getUserName(u)}")
                self.k.writeMessageToUser(u, f"Mein Name ist Chris und ich bin ein WhatsApp-Bot programmiert von meinem Erfinder, dem sensationellen *Minh*")
                self.k.writeMessageToUser(u, f"Erfahre mehr über mich mit dem Befehl *!Bot*")
                self.k.writeMessageToUser(u, f"Lerne alle meine Funktionen kennen mit dem Befehl *!Help*")
                self.k.writeMessageToUser(u, f"Erfahre mehr über Minh, dem Erfinder mit dem Befehl *!Minh*")


        # TODO: reply automatically depending on the user input
        # TODO: Set a busy or not trigger to run this script

    def repeatFunc(self, user):
        global LAST_BOT_MSG
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


    def getHelp(self,u):
        self.k.writeMessageToUser(u, f"Hallo {self.k.getUserName(u)}")
        self.k.writeMessageToUser(u, f"Mein Bot hat einige Funktionen, die du durch eine TextNachricht aktivieren kannst")
        self.k.writeMessageToUser(u, f"1.")
        self.k.writeMessageToUser(u, f"*!Start Repeat*")
        self.k.writeMessageToUser(u, f"Wiederholt jedes Wort, welches du mir schreibst. Beenden kannst du die Funktion mit dem Befehl: *!End*")

        return


    def getfunction(self, message, u):
        x = message.lower().replace(" ", "")
        if x.startswith('!'):
            if x == "!startrepeat":
                self.repeatFunc(u)
            elif x == "!help":
                self.getHelp(u)