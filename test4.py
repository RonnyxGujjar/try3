
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

Window.clearcolor = (0,0,1,1)
Window.size = (330,520)

class RonnyApp(App):
    def build(self):
        self.icon = "appiconmain.jpg"
        layout = BoxLayout(orientation = "vertical",spacing = 10,padding = 30)
        label = Label(text = "Welcome to Ronny Gujjar PCR data")
        btn1 = Button(text = "BANK PCR",on_press = self.pcrbank)
        btn2 = Button(text = "NIFTY PCR",on_press = self.pcrnifty)
        btn3 = Button(text = "FIN NIFTY PCR",on_press = self.pcrfin)
        btn4 = Button(text = "MID CP PCR",on_press= self.pcrmcd)

        layout.add_widget(label)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        return layout

    ###########################################################
    ###########################################################
    ###########################################################
    ##BANK NIFTY###BANK NIFTY ##############################
    ####################################################
    ########################################

    def pcrbank(self, obj):

        import requests
        import pandas as pd
        import datetime

        url = "https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en;q=0.9,hi-IN;q=0.8,hi;q=0.7,en-US;q=0.6'
        }

        session = requests.session()
        requests = session.get(url, headers=headers)

        cookise = dict(requests.cookies)

        response = session.get(url, headers=headers, cookies=cookise).json()
        rawdata = pd.DataFrame(response)
        rawop = pd.DataFrame(rawdata['filtered']['data']).fillna(0)

        def dataframe(rawop):
            data = []
            for i in range(0, len(rawop)):
                calloi = callcoi = cltp = putoi = putcoi = pltp = 0
                stp = rawop['strikePrice'][i]
                if (rawop['CE'][i] == 0):
                    calloi = callcoi = 0

                else:
                    calloi = rawop['CE'][i]['openInterest']
                    callcoi = rawop['CE'][i]['changeinOpenInterest']
                    cltp = rawop['CE'][i]['lastPrice']

                if (rawop['PE'][i] == 0):
                    putoi = putcoi = 0

                else:
                    putoi = rawop['PE'][i]['openInterest']
                    putcoi = rawop['PE'][i]['changeinOpenInterest']
                    pltp = rawop['PE'][i]['lastPrice']

                opdata = {
                    'CALL OI ': calloi, 'CALL CHNG OI': callcoi, 'CALL LTP': cltp, 'STRIKE PRICE': stp,
                    'PUT OI ': putoi, 'PUT CHNG OI': putcoi, 'PUT LTP': pltp,
                }
                data.append(opdata)
            optionchain = pd.DataFrame(data)
            return optionchain

        optionchain = dataframe(rawop)

        TotalCallOI = optionchain['CALL OI '].sum()
        TotalPutOI = optionchain['PUT OI '].sum()

        TotalCallCOI = optionchain['CALL CHNG OI'].sum()
        TotalPutCOI = optionchain['PUT CHNG OI'].sum()
        print(f'Total Call OI: {TotalCallOI} , Total Put OI: {TotalPutOI}')
        print(f"OI PCR RATIO IS : ", (TotalPutOI / TotalCallOI))

        print("")
        print(f'Total Call COI: {TotalCallCOI} , Total Put COI: {TotalPutCOI}')
        print("COI PCR RATIO IS : ", (TotalPutCOI / TotalCallCOI))
        print(datetime.datetime.now())
        print("")

    ########################################
    ########################################
    ########################################
    ###NIFTY # NIFTY#################
    ##############################
    def pcrnifty(self, obj):

        import requests
        import pandas as pd
        import datetime

        url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en;q=0.9,hi-IN;q=0.8,hi;q=0.7,en-US;q=0.6'
        }

        session = requests.session()
        requests = session.get(url, headers=headers)

        cookise = dict(requests.cookies)

        response = session.get(url, headers=headers, cookies=cookise).json()
        rawdata = pd.DataFrame(response)
        rawop = pd.DataFrame(rawdata['filtered']['data']).fillna(0)

        def dataframe(rawop):
            data = []
            for i in range(0, len(rawop)):
                calloi = callcoi = cltp = putoi = putcoi = pltp = 0
                stp = rawop['strikePrice'][i]
                if (rawop['CE'][i] == 0):
                    calloi = callcoi = 0

                else:
                    calloi = rawop['CE'][i]['openInterest']
                    callcoi = rawop['CE'][i]['changeinOpenInterest']
                    cltp = rawop['CE'][i]['lastPrice']

                if (rawop['PE'][i] == 0):
                    putoi = putcoi = 0

                else:
                    putoi = rawop['PE'][i]['openInterest']
                    putcoi = rawop['PE'][i]['changeinOpenInterest']
                    pltp = rawop['PE'][i]['lastPrice']

                opdata = {
                    'CALL OI ': calloi, 'CALL CHNG OI': callcoi, 'CALL LTP': cltp, 'STRIKE PRICE': stp,
                    'PUT OI ': putoi, 'PUT CHNG OI': putcoi, 'PUT LTP': pltp,
                }
                data.append(opdata)
            optionchain = pd.DataFrame(data)
            return optionchain

        optionchain = dataframe(rawop)

        TotalCallOI = optionchain['CALL OI '].sum()
        TotalPutOI = optionchain['PUT OI '].sum()

        TotalCallCOI = optionchain['CALL CHNG OI'].sum()
        TotalPutCOI = optionchain['PUT CHNG OI'].sum()
        print(f'Total Call OI: {TotalCallOI} , Total Put OI: {TotalPutOI}')
        print(f"OI PCR RATIO IS : ", (TotalPutOI / TotalCallOI))

        print("")
        print(f'Total Call COI: {TotalCallCOI} , Total Put COI: {TotalPutCOI}')
        print("COI PCR RATIO IS : ", (TotalPutCOI / TotalCallCOI))
        print(datetime.datetime.now())
        print("")

    ###########################################################
    ###########################################################
    ###########################################################
    ##FIN NIFTY###FIN NIFTY ##############################
    ####################################################
    ########################################

    def pcrfin(self, obj):

        import requests
        import pandas as pd
        import datetime

        url = "https://www.nseindia.com/api/option-chain-indices?symbol=FINNIFTY"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en;q=0.9,hi-IN;q=0.8,hi;q=0.7,en-US;q=0.6'
        }

        session = requests.session()
        requests = session.get(url, headers=headers)

        cookise = dict(requests.cookies)

        response = session.get(url, headers=headers, cookies=cookise).json()
        rawdata = pd.DataFrame(response)
        rawop = pd.DataFrame(rawdata['filtered']['data']).fillna(0)

        def dataframe(rawop):
            data = []
            for i in range(0, len(rawop)):
                calloi = callcoi = cltp = putoi = putcoi = pltp = 0
                stp = rawop['strikePrice'][i]
                if (rawop['CE'][i] == 0):
                    calloi = callcoi = 0

                else:
                    calloi = rawop['CE'][i]['openInterest']
                    callcoi = rawop['CE'][i]['changeinOpenInterest']
                    cltp = rawop['CE'][i]['lastPrice']

                if (rawop['PE'][i] == 0):
                    putoi = putcoi = 0

                else:
                    putoi = rawop['PE'][i]['openInterest']
                    putcoi = rawop['PE'][i]['changeinOpenInterest']
                    pltp = rawop['PE'][i]['lastPrice']

                opdata = {
                    'CALL OI ': calloi, 'CALL CHNG OI': callcoi, 'CALL LTP': cltp, 'STRIKE PRICE': stp,
                    'PUT OI ': putoi, 'PUT CHNG OI': putcoi, 'PUT LTP': pltp,
                }
                data.append(opdata)
            optionchain = pd.DataFrame(data)
            return optionchain

        optionchain = dataframe(rawop)

        TotalCallOI = optionchain['CALL OI '].sum()
        TotalPutOI = optionchain['PUT OI '].sum()

        TotalCallCOI = optionchain['CALL CHNG OI'].sum()
        TotalPutCOI = optionchain['PUT CHNG OI'].sum()
        print(f'Total Call OI: {TotalCallOI} , Total Put OI: {TotalPutOI}')
        print(f"OI PCR RATIO IS : ", (TotalPutOI / TotalCallOI))

        print("")
        print(f'Total Call COI: {TotalCallCOI} , Total Put COI: {TotalPutCOI}')
        print("COI PCR RATIO IS : ", (TotalPutCOI / TotalCallCOI))
        print(datetime.datetime.now())
        print("")

    ########################################
    ########################################
    ########################################
    ###MCD # MCD#################
    ##############################
    def pcrmcd(self, obj):

        import requests
        import pandas as pd
        import datetime

        url = "https://www.nseindia.com/api/option-chain-indices?symbol=MIDCPNIFTY"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en;q=0.9,hi-IN;q=0.8,hi;q=0.7,en-US;q=0.6'
        }

        session = requests.session()
        requests = session.get(url, headers=headers)

        cookise = dict(requests.cookies)

        response = session.get(url, headers=headers, cookies=cookise).json()
        rawdata = pd.DataFrame(response)
        rawop = pd.DataFrame(rawdata['filtered']['data']).fillna(0)

        def dataframe(rawop):
            data = []
            for i in range(0, len(rawop)):
                calloi = callcoi = cltp = putoi = putcoi = pltp = 0
                stp = rawop['strikePrice'][i]
                if (rawop['CE'][i] == 0):
                    calloi = callcoi = 0

                else:
                    calloi = rawop['CE'][i]['openInterest']
                    callcoi = rawop['CE'][i]['changeinOpenInterest']
                    cltp = rawop['CE'][i]['lastPrice']

                if (rawop['PE'][i] == 0):
                    putoi = putcoi = 0

                else:
                    putoi = rawop['PE'][i]['openInterest']
                    putcoi = rawop['PE'][i]['changeinOpenInterest']
                    pltp = rawop['PE'][i]['lastPrice']

                opdata = {
                    'CALL OI ': calloi, 'CALL CHNG OI': callcoi, 'CALL LTP': cltp, 'STRIKE PRICE': stp,
                    'PUT OI ': putoi, 'PUT CHNG OI': putcoi, 'PUT LTP': pltp,
                }
                data.append(opdata)
            optionchain = pd.DataFrame(data)
            return optionchain

        optionchain = dataframe(rawop)

        TotalCallOI = optionchain['CALL OI '].sum()
        TotalPutOI = optionchain['PUT OI '].sum()

        TotalCallCOI = optionchain['CALL CHNG OI'].sum()
        TotalPutCOI = optionchain['PUT CHNG OI'].sum()
        print(f'Total Call OI: {TotalCallOI} , Total Put OI: {TotalPutOI}')
        print(f"OI PCR RATIO IS : ", (TotalPutOI / TotalCallOI))

        print("")
        print(f'Total Call COI: {TotalCallCOI} , Total Put COI: {TotalPutCOI}')
        print("COI PCR RATIO IS : ", (TotalPutCOI / TotalCallCOI))
        print(datetime.datetime.now())
        print("")


RonnyApp().run()



