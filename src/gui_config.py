# Use Tkinter for python 2, tkinter for python 3
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Tweetefly Configurator")
window.geometry('300x400')

lbl = Label(window, text="API SECRET")
lbl.grid(column=0, row=0)

txt = Entry(window, width=10)
txt.grid(column=1, row=0)
api_secret = txt.get()
print(api_secret)

lbl2 = Label(window, text="API KEY")
lbl2.grid(column=0, row=1)

txt2 = Entry(window, width=10)
txt2.grid(column=1, row=1)
api_key = txt2.get()

lbl3 = Label(window, text="BEARER")
lbl3.grid(column=0, row=3)

txt3 = Entry(window, width=10)
txt3.grid(column=1, row=3)
bearer = txt3.get()

lbl4 = Label(window, text="APP ID")
lbl4.grid(column=0, row=5)

txt4 = Entry(window, width=10)
txt4.grid(column=1, row=5)
app_id = txt4.get()

lbl5 = Label(window, text="CLIENT ID")
lbl5.grid(column=0, row=7)

txt5 = Entry(window, width=10)
txt5.grid(column=1, row=7)
client_id = txt5.get()

lbl6 = Label(window, text="ACCESS TOKEN")
lbl6.grid(column=0, row=9)

txt6 = Entry(window, width=10)
txt6.grid(column=1, row=9)
access_token = txt6.get()

lbl7 = Label(window, text="ACCESS SECRET")
lbl7.grid(column=0, row=10)

txt7 = Entry(window, width=10)
txt7.grid(column=1, row=10)
access_secret = txt7.get()

lbl8 = Label(window, text="USER ID")
lbl8.grid(column=0, row=12)

txt8 = Entry(window, width=10)
txt8.grid(column=1, row=12)
user_id = txt8.get()


def clicked():
    messagebox.showinfo('Tweetifly', 'Configuration Modified!!')


def write_config():
    env_conf = f"""
## API TOKEN ##
API_SECRET={api_secret}
API_KEY={api_key}

## BEARER ##
BEARER={bearer}

## CLIENT AND APP ID ##
APP_ID={app_id}
CLIENT_ID={client_id}

## ACCESS TOKEN ##
ACCESS_TOKEN={access_token}
ACCESS_SECRET={access_secret}

## USER ID AND INFO ##
MY_USER_ID={user_id}
    """

    with open('src/.env', 'w') as cf:
        cf.seek(0)
        cf.write(env_conf)
        cf.close()
    print("Config Modified!!")
    clicked()


btn = Button(window, text='Write Configuration', command=write_config)
btn.grid(column=1, row=13)
window.mainloop()
