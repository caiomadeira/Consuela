from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser



class Reports_pdf():
    def printLogins(self):
        webbrowser.open("my_logins.pdf")

    def generateReport(self):
        self.l = canvas.Canvas("my_logins.pdf")

        self.account_report = self.entry_account.get()
        self.user_or_email_report = self.entry_user.get()
        self.pass_report = self.entry_pass.get()

        self.l.setFont("Helvetica", 8)
        self.l.drawString(210, 750, 'Gerado por Consuela (por Caio Madeira)')

        self.l.setFont("Helvetica-Bold", 24)
        self.l.drawString(150, 790, f'Dados da conta: {self.account_report}')

        self.l.setFont("Helvetica-Bold", 10)
        self.l.drawString(50, 700, 'Conta:')
        self.l.drawString(50, 680, 'Usuário/E-mail:')
        self.l.drawString(50, 660, 'Senha:')

        # =======================================
        self.l.setFont("Helvetica", 10)
        self.l.drawString(150, 700, self.account_report)
        self.l.drawString(150, 680, self.user_or_email_report)
        self.l.drawString(150, 660, self.pass_report)

        self.l.rect(20, 730, 550, 100, fill=False, stroke=True)
        self.l.rect(20, 520, 550, 200, fill=False, stroke=True)

        self.l.showPage()
        self.l.save()
        self.printLogins()