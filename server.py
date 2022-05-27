from yahoo_fin import stock_info as si
import serial
from time import sleep

def chooseTicker(c):
    count = c
    if (ser.in_waiting):    
        input = ser.read(1)
        if (input == b'\x00'):
            count+=1
            if (count >= 9):
                count = 0
        elif (input == b'\x01'):
            count-=1
            if (count <= -1):
                count = 8
            
    return count
def getClose():
    for i in range(9):
        closePrice[i] = si.get_quote_table(tickers[i])['Previous Close']

ser = serial.Serial('com5', 9600)
count = 0
tickers = ["sava", "ikt", "coin"]
closePrice = [0, 0, 0]
getClose()

while True:
    count = chooseTicker(count)
    price = round(si.get_live_price(tickers[count]),2)
    ser.write(int(price).to_bytes(2, 'big'))
    ser.write(int((price%1)*100).to_bytes(1, 'big'))
    ser.write(int(closePrice[count]).to_bytes(2, 'big'))
    ser.write(int((closePrice[count]%1)*100).to_bytes(1, 'big'))

