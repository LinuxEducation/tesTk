from tkmodule import App, AppFrame
from widgets import tesNotification

i = 0
def update_notification(event):
	global i
	if i == 0:
		tesNotification().type('simple', frame, icon='./icons/info.png', title='Recall', subtitle='Drink the water',)
	if i == 1:
		tesNotification().type('simple', frame, icon='./icons/email.png', title='E-mail', subtitle='You have three messages from Emily')
	i += 1

report = {'call':	 ['Today:  11:20', 'Yesterday:  7:30', 'A week ago:  19:10'],
		  'weather': ['Temperature:  16C', 'Humidity:  84%', 'Wind:  18km/h']}

app = App('System Notification', '#313338')
frame = AppFrame(app)

a = tesNotification().type('missed', frame, icon='./icons/missed.png', title='Missed Call', subtitle='784604058', report=report['call']) ; a.pack()
b = tesNotification().type('simple', frame, icon='./icons/info.png', title='Recall', subtitle='Remember the coffee?') ; b.pack()
c = tesNotification().type('weather', frame, icon='./icons/weather.png' ,title='Weather', subtitle='Rain and strong wind', report=report['weather']) ; c.pack()
d = tesNotification().type('player', frame, icon='./icons/music.png', title='Paused', subtitle='Kings Of Leon - Sex on Fire') ; d.pack()

for obj in a,b,c,d:
	obj.bind('<Destroy>', update_notification)

app.mainloop()

