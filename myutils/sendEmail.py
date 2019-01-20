import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from myutils import readKeyfile
from myutils import log

def notifyViaEmail(whom, subject, body):
	credentials = readKeyfile.readOutValues("mailconfigs.txt")
	try:
		fromaddr = credentials['fromaddr']
		toaddr = whom
		msg = MIMEMultipart()
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = subject
		msg.attach(MIMEText(body, 'plain'))
		server = smtplib.SMTP(credentials['smtphost'], credentials['smtpport'])
		server.starttls()
		server.login(fromaddr, credentials['emailpass'])
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		server.quit()
		log.infoLog("Sent out notification to " + toaddr)
	except smtplib.SMTPException as error:
		log.errorLog(error)
