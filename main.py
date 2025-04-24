import queue
import sounddevice as sd
import vosk
import json
import win32api
import win32con
import time

q = queue.Queue()
model = vosk.Model("vosk-model-small-ru-0.22")
grammar = '["включить", "спирит", "колд", "сан страйк", "метеор", "метиор", "ем по", "я им по", "торнадо", "комбо один", "комбо два", "комбо три", "пиздец", "зашибись", "[unk]"]'
commands = ["включить","спирит", "колд", "сан страйк", "метеор", "метиор", "ем по", "я им по", "торнадо", "комбо один", "комбо два", "комбо три", "пиздец", "зашибись"]

class Spells:
    def __init__(self):
        self.q = 0x51
        self.w = 0x57
        self.e = 0x45
        self.t = 0x54
        self.y = 0x59
        self.r = 0x52
        self.one = 0x31
        self.two = 0x32
        self.three = 0x33
        self.six = 0x36

    def press_t_double(self):
        time.sleep(0.1)

        win32api.keybd_event(self.t, 0, 0, 0)
        win32api.keybd_event(self.t, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.1)

        win32api.keybd_event(self.t, 0, 0, 0)
        win32api.keybd_event(self.t, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.1)

    def press_y_and_click(self):
        time.sleep(0.1)

        win32api.keybd_event(self.y, 0, 0, 0)
        win32api.keybd_event(self.y, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.1)

        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        time.sleep(0.1)

    def press_t_and_click(self):
        time.sleep(0.1)

        win32api.keybd_event(self.t, 0, 0, 0)
        win32api.keybd_event(self.t, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.1)

        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        time.sleep(0.1)

    def spirit(self):
        keys = [self.e,self.e,self.q,self.r]
        for key_code in keys:
            win32api.keybd_event(key_code, 0, 0, 0)
            win32api.keybd_event(key_code, 0, win32con.KEYEVENTF_KEYUP, 0)


    def snap(self):
        keys = [self.q,self.q,self.q,self.r]
        for key_code in keys:
            win32api.keybd_event(key_code, 0, 0, 0)
            win32api.keybd_event(key_code, 0, win32con.KEYEVENTF_KEYUP, 0)

    def sunstrike(self):
        keys = [self.e,self.e,self.e,self.r]
        for key_code in keys:
            win32api.keybd_event(key_code, 0, 0, 0)
            win32api.keybd_event(key_code, 0, win32con.KEYEVENTF_KEYUP, 0)

    def meteor(self):
        keys = [self.e,self.e,self.w,self.r]
        for key_code in keys:
            win32api.keybd_event(key_code, 0, 0, 0)
            win32api.keybd_event(key_code, 0, win32con.KEYEVENTF_KEYUP, 0)

    def blast(self):
        keys = [self.q,self.w,self.e,self.r]
        for key_code in keys:
            win32api.keybd_event(key_code, 0, 0, 0)
            win32api.keybd_event(key_code, 0, win32con.KEYEVENTF_KEYUP, 0)

    def tornado(self):
        keys = [self.w,self.w,self.q,self.r]
        for key_code in keys:
            win32api.keybd_event(key_code, 0, 0, 0)
            win32api.keybd_event(key_code, 0, win32con.KEYEVENTF_KEYUP, 0)

    def emp(self):
        keys = [self.w,self.w,self.w,self.r]
        for key_code in keys:
            win32api.keybd_event(key_code, 0, 0, 0)
            win32api.keybd_event(key_code, 0, win32con.KEYEVENTF_KEYUP, 0)

    def ghost_walk(self):
        keys = [self.q, self.q, self.w, self.r]
        for key_code in keys:
            win32api.keybd_event(key_code, 0, 0, 0)
            win32api.keybd_event(key_code, 0, win32con.KEYEVENTF_KEYUP, 0)

    def zashibisj(self):
        self.ghost_walk()
        self.press_t_and_click()

    def combo_one(self):
        self.snap()
        self.press_t_and_click()
        time.sleep(0.2)
        self.tornado()
        self.press_t_and_click()
        time.sleep(0.2)
        self.emp()
        self.press_t_and_click()
        time.sleep(1)
        self.sunstrike()
        self.press_t_and_click()
        time.sleep(0.2)
        self.meteor()
        self.press_t_and_click()
        time.sleep(0.2)
        self.blast()
        self.press_t_and_click()

    def combo_two(self):
        win32api.keybd_event(self.one, 0, 0, 0)
        win32api.keybd_event(self.one, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        time.sleep(0.1)
        self.press_t_and_click()
        self.press_y_and_click()
        self.blast()
        time.sleep(0.4)
        self.press_t_and_click()

    def combo_three(self):
        self.tornado()
        self.press_t_and_click()
        time.sleep(0.2)
        self.emp()
        self.press_t_and_click()
        time.sleep(1)
        self.sunstrike()
        self.press_t_double()
        time.sleep(0.2)
        self.meteor()
        self.press_t_and_click()
        win32api.keybd_event(self.one, 0, 0, 0)
        win32api.keybd_event(self.one, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.4)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        time.sleep(0.1)
        win32api.keybd_event(self.two, 0, 0, 0)
        win32api.keybd_event(self.two, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        win32api.keybd_event(self.three, 0, 0, 0)
        win32api.keybd_event(self.three, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.1)
        self.blast()
        self.press_t_and_click()
        time.sleep(0.2)
        win32api.keybd_event(self.six, 0, 0, 0)
        win32api.keybd_event(self.six, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.2)
        win32api.keybd_event(self.one, 0, 0, 0)
        win32api.keybd_event(self.one, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        time.sleep(0.1)
        win32api.keybd_event(self.two, 0, 0, 0)
        win32api.keybd_event(self.two, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        win32api.keybd_event(self.three, 0, 0, 0)
        win32api.keybd_event(self.three, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.1)
        self.emp()
        self.press_t_and_click()
        time.sleep(0.2)
        self.sunstrike()
        self.press_t_double()
        time.sleep(0.2)
        self.meteor()
        self.press_t_and_click()
        time.sleep(0.4)
        self.blast()
        self.press_t_and_click()

    def pizdec(self):
        self.tornado()
        self.press_t_and_click()
        time.sleep(0.2)
        self.emp()
        self.press_t_and_click()
        time.sleep(1)
        self.sunstrike()
        self.press_t_double()
        time.sleep(0.2)
        self.meteor()
        self.press_t_and_click()
        time.sleep(0.4)
        self.blast()
        self.press_t_and_click()
        time.sleep(0.2)
        win32api.keybd_event(self.six, 0, 0, 0)
        win32api.keybd_event(self.six, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.2)
        self.emp()
        self.press_t_and_click()
        time.sleep(0.2)
        self.sunstrike()
        self.press_t_double()
        time.sleep(0.2)
        self.meteor()
        self.press_t_and_click()
        time.sleep(0.4)
        self.blast()
        self.press_t_and_click()


def _callback(indata, frames, time_, status):
    if status:
        print(status)
    q.put(bytes(indata))

def _recognize_loop():
    spells = Spells()
    startVoice = False
    with sd.RawInputStream(
        samplerate=16000,
        blocksize=548,
        dtype='int16',
        channels=1,
        callback=_callback
    ):
        print("🎙 Готов к приёму команд...")
        rec = vosk.KaldiRecognizer(model, 16000, grammar)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "").lower()
                if text:
                    print(f"🗣 Распознано: {text}")
                    for word in commands:
                        if word in text:
                            if word == "включить":
                                if startVoice == False:
                                    startVoice = True
                                else:
                                    startVoice = False
                                print(f"{startVoice} голосовое управление")
                            if startVoice:
                                if word == "зашибись":
                                    spells.zashibisj()
                                if word == "комбо один":
                                    spells.combo_one()
                                if word == "комбо два":
                                    spells.combo_two()
                                if word == "комбо три":
                                    spells.combo_three()
                                if word == "пиздец":
                                    spells.pizdec()
                                if word == "спирит":
                                    spells.spirit()
                                if word == "колд":
                                    spells.snap()
                                if word == "сан страйк":
                                    spells.sunstrike()
                                if word == "метеор":
                                    spells.meteor()
                                if word == "я им по" or word == "ем по":
                                    spells.emp()
                                if word == "торнадо":
                                    spells.tornado()
                            break

_recognize_loop()