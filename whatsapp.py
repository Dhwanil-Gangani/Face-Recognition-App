import pywhatkit as kt

def whatsapp(phone, message):
    return kt.sendwhatmsg_instantly(phone, message)  