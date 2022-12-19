import telebot
from telebot import types
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import requests
from reques import main, main2, litecoin, litecoin2, scrypt_s_2, scrypt_s
from datetime import datetime, date







Session = sessionmaker()
engine = create_engine('sqlite:///data.db?check_same_thread=False')
Session.configure(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    language = Column(String())
    money = Column(String())
    power = Column(String())

Base.metadata.create_all(engine)


bot = telebot.TeleBot('5717146118:AAFdQGASQmiCShD7Ur487oGERpancDxZAOU')

language = 'ru'

#asics = ['Antminer KA3', 'Antminer K7', 'Antminer L7', 'Antminer S19 XP Hyd', 'Antminer D7', 'Antminer S19 XP', 'Antminer Z15', 'Canaan AvalonMiner 1366', 'MicroBT Whatsminer M50S', 'Antminer E9', 'iBeLink BM-K1 Max Blake2S Miner', 'MicroBT Whatsminer M50', 'Goldshell LT6', 'Goldshell KD6', 'Antminer S19a Pro', 'Antminer S19 Pro', 'Canaan AvalonMiner 1346', 'MicroBT Whatsminer M30S++', 'Antminer S19j Pro', 'Innosilicon A6+ LTC Master', 'Linzhi Phoenix', 'StrongU STU-U1++', 'Goldshell CK6', 'StrongU STU-U6', 'Goldshell LT5', 'MicroBT Whatsminer M30S+', 'Antminer S19', 'Antminer S19a', 'Antminer S19j', 'MicroBT Whatsminer D1', 'Canaan AvalonMiner 1266', 'Antminer DR5', 'Goldshell KD5', 'Antminer B3', 'Antminer A3', 'Innosilicon A4+', 'Fusionsilicon X7', 'Innosilicon A6 LTC Master', 'iBeLink BM-K1 Blake2S Miner', 'Antminer L3', 'Goldshell CK5', 'Innosilicon A10', 'Antminer T19', 'Goldshell X5', 'Antminer S17 Pro 50 TH/s', 'MicroBT Whatsminer M30S', 'Canaan AvalonMiner 1246', 'Antminer S17 Pro', 'iBeLink BM-K1+ Blake2S Miner', 'Antminer L3+', 'Antminer Z9 Mini', 'Goldshell X5S', 'Antminer L3++', 'Innosilicon A9 ZMaster', 'Innosilicon A10 Pro', 'Antminer S17+', 'HyperBit BW L21', 'Innosilicon A11', 'Hummer Miner H9 Pro', 'StrongU Hornbill H8 Pro', 'Innosilicon A10 Pro 6GB', 'Antminer S1', 'Antminer S3', 'Obelisk SC1', 'Obelisk SC1 Slim', 'Ebang Ebit E11++', 'Obelisk DCR1', 'Obelisk DCR1 Slim', 'StrongU STU-U8', 'Antminer Z11', 'Cheetah Miner F5+', 'MicroBT Whatsminer M31S', 'Antminer S17 53 TH/s', 'Canaan AvalonMiner 1166 Pro', 'MicroBT Whatsminer M31S+', 'Antminer S17', 'Antminer E3', 'Antminer R4', 'Innosilicon A9++ ZMaster', 'Antminer S5', 'Innosilicon T3 43T', 'Antminer S17e', 'Innosilicon A5 Dash Master', 'Antminer S15', 'Obelisk SC1 Dual', 'Canaan AvalonMiner 1041', 'Dayun Zig M1', 'Antminer Z11j', 'Antminer S9k', 'StrongU Hornbill H8', 'Antminer Z9', 'Antminer T15', 'Innosilicon A9+ ZMaster', 'Ebang Ebit E11+', 'Antminer S9 SE', 'Innosilicon A4', 'MicroBT Whatsminer M21', 'Innosilicon T3 39T', 'Canaan AvalonMiner 1166', 'Antminer T17', 'Innosilicon T3 40T', 'Canaan AvalonMiner 821', 'Canaan AvalonMiner 841', 'Antminer S9i', 'Bitfury RD4', 'Aladdin T1 16T ', 'Canaan AvalonMiner 1166 Pro S 72T', 'Antminer S9', 'MicroBT Whatsminer M20S', 'Antminer S11', 'Antminer S9j', 'Ebang Ebit E11', 'Innosilicon D9 - DecredMaster', 'Antminer Z11e', 'Antminer V9', 'Innosilicon T3+Pro 67T', 'Canaan AvalonMiner 741', 'Ebang Ebit E9.2', 'Toddminer C1', 'Antminer T17+', 'Canaan AvalonMiner 1041F', 'Ebang Ebit E12', 'Canaan AvalonMiner 851', 'Antminer D5', 'MicroBT Whatsminer M10', 'Antminer S2', 'Canaan AvalonMiner 1126 Pro S 68T', 'Canaan AvalonMiner 921', 'Canaan AvalonMiner 1026', 'Ebang Ebit E10', 'Ebang Ebit E9i', 'Antminer T17e', 'Canaan AvalonMiner 1146 Pro', 'Fusionsilicon X1', 'Obelisk SC1 Immersion', 'Antminer DR3', 'Antminer T9', 'Canaan AvalonMiner 1047', 'Canaan AvalonMiner 911', 'Antminer T9+', 'StrongU STU-U1', 'Antminer S9 Hydro', 'Innosilicon D9+ DecredMaster', 'Canaan AvalonMiner 1126 Pro S 64T', 'MicroBT Whatsminer M32S', 'Innosilicon T2T-30T', 'Cheetah Miner F3', 'Antminer D3', 'Antminer S7', 'Dayun Zig Z1+', 'Dayun Zig Z1', 'Innosilicon A5+ Dash Master', 'Cheetah Miner F5', 'Innosilicon T2T-26T', 'Canaan AvalonMiner 1146', 'Ebang Ebit E9.3', 'StrongU STU-U1+', 'Innosilicon T3+ 57T', 'Cheetah Miner F5M', 'Canaan AvalonMiner 1126 Pro S 60T', 'Innosilicon T3 50T', 'Cheetah Miner F5I', 'Canaan AvalonMiner 1066Pro', 'Antminer S4', 'Aisen A1 24T', 'MicroBT Whatsminer M21S', 'Antminer K5', 'Hummer Miner H7 Pro 48 TH', 'Dayun Zig Z1 Pro', 'Canaan AvalonMiner 1066', 'Spondoolies SPx36', 'MicroBT Whatsminer M10S', 'Hummer Miner H7 Pro 53 TH', 'MicroBT Whatsminer M3', 'MicroBT Whatsminer M3X', 'Aladdin T1 32T ', 'Ebang Ebit E10.3', 'iBeLink DM56G X11/Dash Miner', 'iBeLink DSM6T Blake256 Miner', 'iBeLink DSM7T Miner', 'Dayun Zig D1', 'Hummer Miner H1', 'Bitfury Tardis', 'Bitfury B8']

#asics = ['Aisen A1 24T', 'Aladdin T1 16T ', 'Aladdin T1 32T ', 'Antminer D7', 'Antminer DR3', 'Antminer DR5', 'Antminer E9', 'Antminer K7', 'Antminer KA3', 'Antminer L3+', 'Antminer L3++', 'Antminer L7', 'Antminer R4', 'Antminer S11', 'Antminer S15', 'Antminer S17', 'Antminer S17 53 TH/s', 'Antminer S17 Pro', 'Antminer S17 Pro 50 TH/s', 'Antminer S17+', 'Antminer S17e', 'Antminer S19', 'Antminer S19 Pro', 'Antminer S19 XP', 'Antminer S19 XP Hyd', 'Antminer S19a', 'Antminer S19a Pro', 'Antminer S19j', 'Antminer S19j Pro', 'Antminer S9', 'Antminer S9 Hydro', 'Antminer S9 SE', 'Antminer S9i', 'Antminer S9j', 'Antminer S9k', 'Antminer T15', 'Antminer T17', 'Antminer T17+', 'Antminer T17e', 'Antminer T19', 'Antminer T9', 'Antminer T9+', 'Antminer Z11', 'Antminer Z11e', 'Antminer Z11j', 'Antminer Z15', 'Antminer Z9', 'Antminer Z9 Mini', 'Canaan AvalonMiner 1026', 'Canaan AvalonMiner 1041', 'Canaan AvalonMiner 1041F', 'Canaan AvalonMiner 1047', 'Canaan AvalonMiner 1066', 'Canaan AvalonMiner 1066Pro', 'Canaan AvalonMiner 1126 Pro S 60T', 'Canaan AvalonMiner 1126 Pro S 64T', 'Canaan AvalonMiner 1126 Pro S 68T', 'Canaan AvalonMiner 1146', 'Canaan AvalonMiner 1146 Pro', 'Canaan AvalonMiner 1166', 'Canaan AvalonMiner 1166 Pro', 'Canaan AvalonMiner 1166 Pro S 72T', 'Canaan AvalonMiner 1246', 'Canaan AvalonMiner 1266', 'Canaan AvalonMiner 1346', 'Canaan AvalonMiner 1366', 'Canaan AvalonMiner 741', 'Canaan AvalonMiner 821', 'Canaan AvalonMiner 841', 'Canaan AvalonMiner 851', 'Canaan AvalonMiner 911', 'Canaan AvalonMiner 921', 'Cheetah Miner F3', 'Cheetah Miner F5', 'Cheetah Miner F5+', 'Cheetah Miner F5I', 'Cheetah Miner F5M', 'Dayun Zig D1', 'Dayun Zig M1', 'Dayun Zig Z1', 'Dayun Zig Z1 Pro', 'Dayun Zig Z1+', 'Ebang Ebit E10', 'Ebang Ebit E10.3', 'Ebang Ebit E11', 'Ebang Ebit E11+', 'Ebang Ebit E11++', 'Ebang Ebit E12', 'Ebang Ebit E9.2', 'Ebang Ebit E9.3', 'Ebang Ebit E9i', 'Fusionsilicon X1', 'Fusionsilicon X7', 'Goldshell CK5', 'Goldshell CK6', 'Goldshell KD5', 'Goldshell KD6', 'Goldshell LT5', 'Goldshell LT6', 'Goldshell X5', 'Goldshell X5S', 'Hummer Miner H1', 'Hummer Miner H7 Pro 48 TH', 'Hummer Miner H7 Pro 53 TH', 'Hummer Miner H9 Pro', 'HyperBit BW L21', 'Innosilicon A10', 'Innosilicon A10 Pro', 'Innosilicon A10 Pro 6GB', 'Innosilicon A11', 'Innosilicon A4', 'Innosilicon A4+', 'Innosilicon A5 Dash Master', 'Innosilicon A5+ Dash Master', 'Innosilicon A6 LTC Master', 'Innosilicon A6+ LTC Master', 'Innosilicon A9 ZMaster', 'Innosilicon A9+ ZMaster', 'Innosilicon A9++ ZMaster', 'Innosilicon D9 - DecredMaster', 'Innosilicon D9+ DecredMaster', 'Innosilicon T2T-26T', 'Innosilicon T2T-30T', 'Innosilicon T3 39T', 'Innosilicon T3 40T', 'Innosilicon T3 43T', 'Innosilicon T3 50T', 'Innosilicon T3+ 57T', 'Innosilicon T3+Pro 67T', 'Linzhi Phoenix', 'MicroBT Whatsminer D1', 'MicroBT Whatsminer M10', 'MicroBT Whatsminer M10S', 'MicroBT Whatsminer M20S', 'MicroBT Whatsminer M21', 'MicroBT Whatsminer M21S', 'MicroBT Whatsminer M3', 'MicroBT Whatsminer M30S', 'MicroBT Whatsminer M30S+', 'MicroBT Whatsminer M30S++', 'MicroBT Whatsminer M31S', 'MicroBT Whatsminer M31S+', 'MicroBT Whatsminer M32S', 'MicroBT Whatsminer M3X', 'MicroBT Whatsminer M50', 'MicroBT Whatsminer M50S', 'Spondoolies SPx36', 'StrongU Hornbill H8', 'StrongU Hornbill H8 Pro', 'StrongU STU-U1', 'StrongU STU-U1+', 'StrongU STU-U1++', 'StrongU STU-U6', 'StrongU STU-U8', 'iBeLink BM-K1 Blake2S Miner', 'iBeLink BM-K1 Max Blake2S Miner', 'iBeLink BM-K1+ Blake2S Miner', 'iBeLink DM56G X11/Dash Miner', 'iBeLink DSM6T Blake256 Miner', 'iBeLink DSM7T Miner']
asics = ['Aisen A1 24T 24 TH/s\xa0', 'Aladdin T1 16T  16 TH/s\xa0', 'Aladdin T1 32T  32 TH/s\xa0', 'Antminer D7 1.286 TH/s\xa0', 'Antminer E9 2400 MH/s\xa0', 'Antminer K7 63.5 TH/s\xa0', 'Antminer KA3 166 TH/s\xa0', 'Antminer L3+ 504 MH/s\xa0', 'Antminer L3++ 580 MH/s\xa0', 'Antminer L7 9500 MH/s\xa0', 'Antminer R4 8.7 TH/s\xa0', 'Antminer S11 19 TH/s\xa0', 'Antminer S15 28 TH/s\xa0', 'Antminer S17 56 TH/s\xa0', 'Antminer S17 53 TH/s 53 TH/s\xa0', 'Antminer S17 Pro 53 TH/s\xa0', 'Antminer S17 Pro 50 TH/s 50 TH/s\xa0', 'Antminer S17+ 73 TH/s\xa0', 'Antminer S17e 64 TH/s\xa0', 'Antminer S19 95 TH/s\xa0', 'Antminer S19 Pro 110 TH/s\xa0', 'Antminer S19 XP 140 TH/s\xa0', 'Antminer S19 XP Hyd 255 TH/s\xa0', 'Antminer S19a 100 TH/s\xa0', 'Antminer S19a Pro 110 TH/s\xa0', 'Antminer S19j 90 TH/s\xa0', 'Antminer S19j Pro 100 TH/s\xa0', 'Antminer S9 13 TH/s\xa0', 'Antminer S9 Hydro 18 TH/s\xa0', 'Antminer S9 SE 16 TH/s\xa0', 'Antminer S9i 13 TH/s\xa0', 'Antminer S9j 14 TH/s\xa0', 'Antminer S9k 13.5 TH/s\xa0', 'Antminer T15 24 TH/s\xa0', 'Antminer T17 40 TH/s\xa0', 'Antminer T17+ 64 TH/s\xa0', 'Antminer T17e 53 TH/s\xa0', 'Antminer T19 84 TH/s\xa0', 'Antminer T9 11.5 TH/s\xa0', 'Antminer T9+ 10.5 TH/s\xa0', 'Antminer Z11 135 KH/s\xa0', 'Antminer Z11e 70 KH/s\xa0', 'Antminer Z11j 105 KH/s\xa0', 'Antminer Z15 420 KH/s\xa0', 'Antminer Z9 42 kH/s\xa0', 'Antminer Z9 Mini 10 kH/s\xa0', 'Bluestar L1 4900 MH/s\xa0', 'Canaan AvalonMiner 1026 30 TH/s\xa0', 'Canaan AvalonMiner 1041 31 TH/s\xa0', 'Canaan AvalonMiner 1041F 33.5 TH/s\xa0', 'Canaan AvalonMiner 1047 37 TH/s\xa0', 'Canaan AvalonMiner 1066 50 TH/s\xa0', 'Canaan AvalonMiner 1066Pro 55 TH/s\xa0', 'Canaan AvalonMiner 1126 Pro S 60T 60 TH/s\xa0', 'Canaan AvalonMiner 1126 Pro S 64T 64 TH/s\xa0', 'Canaan AvalonMiner 1126 Pro S 68T 68 TH/s\xa0', 'Canaan AvalonMiner 1146 56 TH/s\xa0', 'Canaan AvalonMiner 1146 Pro 63 TH/s\xa0', 'Canaan AvalonMiner 1166 68 TH/s\xa0', 'Canaan AvalonMiner 1166 Pro 81 TH/s\xa0', 'Canaan AvalonMiner 1166 Pro S 72T 72 TH/s\xa0', 'Canaan AvalonMiner 1246 90 TH/s\xa0', 'Canaan AvalonMiner 1266 100 TH/s\xa0', 'Canaan AvalonMiner 1346 110 TH/s\xa0', 'Canaan AvalonMiner 1366 130 TH/s\xa0', 'Canaan AvalonMiner 741 7.3 TH/s\xa0', 'Canaan AvalonMiner 821 11.5 TH/s\xa0', 'Canaan AvalonMiner 841 13.6 TH/s\xa0', 'Canaan AvalonMiner 851 14.6 TH/s\xa0', 'Canaan AvalonMiner 911 19.5 TH/s\xa0', 'Canaan AvalonMiner 921 20 TH/s\xa0', 'Cheetah Miner F3 30 TH/s\xa0', 'Cheetah Miner F5 55 TH/s\xa0', 'Cheetah Miner F5+ 66 TH/s\xa0', 'Cheetah Miner F5I 60 TH/s\xa0', 'Cheetah Miner F5M 52 TH/s\xa0', 'Ebang Ebit E10 18 TH/s\xa0', 'Ebang Ebit E10.3 24 TH/s\xa0', 'Ebang Ebit E11 30 TH/s\xa0', 'Ebang Ebit E11+ 37 TH/s\xa0', 'Ebang Ebit E11++ 44 TH/s\xa0', 'Ebang Ebit E12 44 TH/s\xa0', 'Ebang Ebit E9.2 12 TH/s\xa0', 'Ebang Ebit E9.3 16 TH/s\xa0', 'Ebang Ebit E9i 18 TH/s\xa0', 'Fusionsilicon X1 12.96 GH/s\xa0', 'Fusionsilicon X7 262 GH/s\xa0', 'Goldshell CK5 12 TH/s\xa0', 'Goldshell CK6 19.3 TH/s\xa0', 'Goldshell KD5 18 TH/s\xa0', 'Goldshell KD6 26.3 TH/s\xa0', 'Goldshell LT5 2.05 GH/s\xa0', 'Goldshell LT6 3.35 GH/s\xa0', 'Hammer D10+ 5000 MH/s\xa0', 'Hummer Miner H1 80 GH/s\xa0', 'Hummer Miner H7 Pro 48 TH 48 TH/s\xa0', 'Hummer Miner H7 Pro 53 TH 53 TH/s\xa0', 'Hummer Miner H9 Pro 84 TH/s\xa0', 'HyperBit BW L21 550 MH/s\xa0', 'Innosilicon A10 480 MH/s\xa0', 'Innosilicon A10 Pro 440 MH/s\xa0', 'Innosilicon A10 Pro 6GB 578 MH/s\xa0', 'Innosilicon A11 1500 MH/s\xa0', 'Innosilicon A4 280 MH/s\xa0', 'Innosilicon A4+ 620 MH/s\xa0', 'Innosilicon A5 Dash Master 32.5 GH/s\xa0', 'Innosilicon A5+ Dash Master 65 GH/s\xa0', 'Innosilicon A6 LTC Master 1.23 GH/s\xa0', 'Innosilicon A6+ LTC Master 2.2 GH/s\xa0', 'Innosilicon A9 ZMaster 50 kH/s\xa0', 'Innosilicon A9+ ZMaster 120 KH/s\xa0', 'Innosilicon A9++ ZMaster 140 KH/s\xa0', 'Innosilicon T2T-26T 26 TH/s\xa0', 'Innosilicon T2T-30T 30 TH/s\xa0', 'Innosilicon T3 39T 39 TH/s\xa0', 'Innosilicon T3 40T 40 TH/s\xa0', 'Innosilicon T3 43T 43 TH/s\xa0', 'Innosilicon T3 50T 50 TH/s\xa0', 'Innosilicon T3+ 57T 57 TH/s\xa0', 'Innosilicon T3+Pro 67T 67 TH/s\xa0', 'Linzhi Phoenix 2600 MH/s\xa0', 'MicroBT Whatsminer D1 48 TH/s\xa0', 'MicroBT Whatsminer M10 33 TH/s\xa0', 'MicroBT Whatsminer M10S 55 TH/s\xa0', 'MicroBT Whatsminer M20S 70 TH/s\xa0', 'MicroBT Whatsminer M21 31 TH/s\xa0', 'MicroBT Whatsminer M21S 56 TH/s\xa0', 'MicroBT Whatsminer M3 12 TH/s\xa0', 'MicroBT Whatsminer M30S 88 TH/s\xa0', 'MicroBT Whatsminer M30S+ 100 TH/s\xa0', 'MicroBT Whatsminer M30S++ 112 TH/s\xa0', 'MicroBT Whatsminer M31S 78 TH/s\xa0', 'MicroBT Whatsminer M31S+ 82 TH/s\xa0', 'MicroBT Whatsminer M32S 62 TH/s\xa0', 'MicroBT Whatsminer M3X 12.5 TH/s\xa0', 'MicroBT Whatsminer M50 114 TH/s\xa0', 'MicroBT Whatsminer M50S 126 TH/s\xa0', 'Spondoolies SPx36 540 GH/s\xa0', 'StrongU Hornbill H8 74 TH/s\xa0', 'StrongU Hornbill H8 Pro 84 TH/s\xa0', 'StrongU STU-U1 11 TH/s\xa0', 'StrongU STU-U1+ 12.8 TH/s\xa0', 'StrongU STU-U1++ 52 TH/s\xa0', 'StrongU STU-U6 440 GH/s\xa0', 'StrongU STU-U8 46 TH/s\xa0', 'iBeLink BM-K1 Blake2S Miner 5.3 TH/s\xa0', 'iBeLink BM-K1 Max Blake2S Miner 32 TH/s\xa0', 'iBeLink BM-K1+ Blake2S Miner 15.5 TH/s\xa0', 'iBeLink DM56G X11/Dash Miner 56 GH/s\xa0', 'iBeLink DSM6T Blake256 Miner 6 TH/s\xa0', 'iBeLink DSM7T Miner 3.5 TH/s\xa0']


#asics_s = {'Antminer KA3': ['166 TH/s\xa0', '3154', 'kadena'], 'Antminer K7': ['63.5 TH/s\xa0', '3080', 'nervos'], 'Antminer L7': ['9500 MH/s\xa0', '3425', 'litecoin'], 'Antminer S19 XP Hyd': ['255 TH/s\xa0', '5304', 'bitcoin'], 'Antminer D7': ['1.286 TH/s\xa0', '3148', 'dash'], 'Antminer S19 XP': ['140 TH/s\xa0', '3010', 'bitcoin'], 'Antminer Z15': ['420 KH/s\xa0', '1510', 'zcash'], 'Canaan AvalonMiner 1366': ['130 TH/s\xa0', '3250', 'bitcoin'], 'MicroBT Whatsminer M50S': ['126 TH/s\xa0', '3276', 'bitcoin'], 'Antminer E9': ['2400 MH/s\xa0', '1920', 'ethereumclassic'], 'iBeLink BM-K1 Max Blake2S Miner': ['32 TH/s\xa0', '3200', 'bitcoin'], 'MicroBT Whatsminer M50': ['114 TH/s\xa0', '3306', 'bitcoin'], 'Goldshell LT6': ['3.35 GH/s\xa0', '3200', 'bitcoin'], 'Goldshell KD6': ['26.3 TH/s\xa0', '2630', 'kadena'], 'Antminer S19a Pro': ['110 TH/s\xa0', '3245', 'bitcoin'], 'Antminer S19 Pro': ['110 TH/s\xa0', '3250', 'bitcoin'], 'Canaan AvalonMiner 1346': ['110 TH/s\xa0', '3300', 'bitcoin'], 'MicroBT Whatsminer M30S++': ['112 TH/s\xa0', '3472', 'bitcoin'], 'Antminer S19j Pro': ['100 TH/s\xa0', '3050', 'bitcoin'], 'Innosilicon A6+ LTC Master': ['2.2 GH/s\xa0', '2100', 'litecoin'], 'Linzhi Phoenix': ['2600 MH/s\xa0', '3000', 'bitcoin'], 'StrongU STU-U1++': ['52 TH/s\xa0', '2100', 'bitcoin'], 'Goldshell CK6': ['19.3 TH/s\xa0', '3300', 'bitcoin'], 'StrongU STU-U6': ['440 GH/s\xa0', '2000', 'bitcoin'], 'Goldshell LT5': ['2.05 GH/s\xa0', '2080', 'bitcoin'], 'MicroBT Whatsminer M30S+': ['100 TH/s\xa0', '3400', 'bitcoin'], 'Antminer S19': ['95 TH/s\xa0', '3250', 'bitcoin'], 'Antminer S19a': ['100 TH/s\xa0', '3450', 'bitcoin'], 'Antminer S19j': ['90 TH/s\xa0', '3100', 'bitcoin'], 'MicroBT Whatsminer D1': ['48 TH/s\xa0', '2200', 'bitcoin'], 'Canaan AvalonMiner 1266': ['100 TH/s\xa0', '3500', 'bitcoin'], 'Antminer DR5': ['35 TH/s\xa0', '1610', 'dash'], 'Goldshell KD5': ['18 TH/s\xa0', '2250', 'kadena'], 'Antminer B3': ['750 H/s\xa0', '360', 'bitcoin'], 'Antminer A3': ['820 GH/s\xa0', '1280', 'bitcoin'], 'Innosilicon A4+': ['620 MH/s\xa0', '750', 'litecoin'], 'Fusionsilicon X7': ['262 GH/s\xa0', '1420', 'dash'], 'Innosilicon A6 LTC Master': ['1.23 GH/s\xa0', '1500', 'litecoin'], 'iBeLink BM-K1 Blake2S Miner': ['5.3 TH/s\xa0', '800', 'bitcoin'], 'Antminer L3': ['250 MH/s\xa0', '400', 'bitcoin'], 'Goldshell CK5': ['12 TH/s\xa0', '2400', 'bitcoin'], 'Innosilicon A10': ['480 MH/s\xa0', '750', 'ethereumclassic'], 'Antminer T19': ['84 TH/s\xa0', '3150', 'bitcoin'], 'Goldshell X5': ['0.72 GH/s\xa0', '990', 'bitcoin'], 'Antminer S17 Pro 50 TH/s': ['50 TH/s\xa0', '1975', 'bitcoin'], 'MicroBT Whatsminer M30S': ['88 TH/s\xa0', '3344', 'bitcoin'], 'Canaan AvalonMiner 1246': ['90 TH/s\xa0', '3420', 'bitcoin'], 'Antminer S17 Pro': ['53 TH/s\xa0', '2094', 'bitcoin'], 'iBeLink BM-K1+ Blake2S Miner': ['15.5 TH/s\xa0', '2250', 'bitcoin'], 'Antminer L3+': ['504 MH/s\xa0', '800', 'litecoin'], 'Antminer Z9 Mini': ['10 kH/s\xa0', '300', 'zcash'], 'Goldshell X5S': ['1.36 GH/s\xa0', '1850', 'bitcoin'], 'Antminer L3++': ['580 MH/s\xa0', '940', 'litecoin'], 'Innosilicon A9 ZMaster': ['50 kH/s\xa0', '620', 'zcash'], 'Innosilicon A10 Pro': ['440 MH/s\xa0', '950', 'ethereumclassic'], 'Antminer S17+': ['73 TH/s\xa0', '2920', 'bitcoin'], 'HyperBit BW L21': ['550 MH/s\xa0', '950', 'litecoin'], 'Innosilicon A11': ['1500 MH/s\xa0', '2300', 'ethereumclassic'], 'Hummer Miner H9 Pro': ['84 TH/s\xa0', '3360', 'bitcoin'], 'StrongU Hornbill H8 Pro': ['84 TH/s\xa0', '3360', 'bitcoin'], 'Innosilicon A10 Pro 6GB': ['578 MH/s\xa0', '1300', 'bitcoin'], 'Antminer S1': ['180 GH/s\xa0', '360', 'bitcoin'], 'Antminer S3': ['440 GH/s\xa0', '370', 'bitcoin'], 'Obelisk SC1': ['550 GH/s\xa0', '500', 'bitcoin'], 'Obelisk SC1 Slim': ['550 GH/s\xa0', '500', 'bitcoin'], 'Ebang Ebit E11++': ['44 TH/s\xa0', '1980', 'bitcoin'], 'Obelisk DCR1': ['1.2 TH/s\xa0', '500', 'bitcoin'], 'Obelisk DCR1 Slim': ['1.2 TH/s\xa0', '500', 'bitcoin'], 'StrongU STU-U8': ['46 TH/s\xa0', '2100', 'bitcoin'], 'Antminer Z11': ['135 KH/s\xa0', '1418', 'zcash'], 'Cheetah Miner F5+': ['66 TH/s\xa0', '2838', 'bitcoin'], 'MicroBT Whatsminer M31S': ['78 TH/s\xa0', '3276', 'bitcoin'], 'Antminer S17 53 TH/s': ['53 TH/s\xa0', '2385', 'bitcoin'], 'Canaan AvalonMiner 1166 Pro': ['81 TH/s\xa0', '3400', 'bitcoin'], 'MicroBT Whatsminer M31S+': ['82 TH/s\xa0', '3444', 'bitcoin'], 'Antminer S17': ['56 TH/s\xa0', '2520', 'bitcoin'], 'Antminer E3': ['190 MH/s\xa0', '760', 'bitcoin'], 'Antminer R4': ['8.7 TH/s\xa0', '845', 'bitcoin'], 'Innosilicon A9++ ZMaster': ['140 KH/s\xa0', '1550', 'zcash'], 'Antminer S5': ['1.155 TH/s\xa0', '590', 'bitcoin'], 'Innosilicon T3 43T': ['43 TH/s\xa0', '2100', 'bitcoin'], 'Antminer S17e': ['64 TH/s\xa0', '2880', 'bitcoin'], 'Innosilicon A5 Dash Master': ['32.5 GH/s\xa0', '750', 'dash'], 'Antminer S15': ['28 TH/s\xa0', '1600', 'bitcoin'], 'Obelisk SC1 Dual': ['1.1 TH/s\xa0', '900', 'bitcoin'], 'Canaan AvalonMiner 1041': ['31 TH/s\xa0', '1736', 'bitcoin'], 'Dayun Zig M1': ['4.3 GH/s\xa0', '790', 'bitcoin'], 'Antminer Z11j': ['105 KH/s\xa0', '1418', 'zcash'], 'Antminer S9k': ['13.5 TH/s\xa0', '1148', 'bitcoin'], 'StrongU Hornbill H8': ['74 TH/s\xa0', '3330', 'bitcoin'], 'Antminer Z9': ['42 kH/s\xa0', '970', 'zcash'], 'Antminer T15': ['24 TH/s\xa0', '1540', 'bitcoin'], 'Innosilicon A9+ ZMaster': ['120 KH/s\xa0', '1550', 'zcash'], 'Ebang Ebit E11+': ['37 TH/s\xa0', '2035', 'bitcoin'], 'Antminer S9 SE': ['16 TH/s\xa0', '1280', 'bitcoin'], 'Innosilicon A4': ['280 MH/s\xa0', '1050', 'litecoin'], 'MicroBT Whatsminer M21': ['31 TH/s\xa0', '1860', 'bitcoin'], 'Innosilicon T3 39T': ['39 TH/s\xa0', '2150', 'bitcoin'], 'Canaan AvalonMiner 1166': ['68 TH/s\xa0', '3196', 'bitcoin'], 'Antminer T17': ['40 TH/s\xa0', '2200', 'bitcoin'], 'Innosilicon T3 40T': ['40 TH/s\xa0', '2200', 'bitcoin'], 'Canaan AvalonMiner 821': ['11.5 TH/s\xa0', '1200', 'bitcoin'], 'Canaan AvalonMiner 841': ['13.6 TH/s\xa0', '1290', 'bitcoin'], 'Antminer S9i': ['13 TH/s\xa0', '1280', 'bitcoin'], 'Bitfury RD4': ['25 TH/s\xa0', '1720', 'bitcoin'], 'Aladdin T1 16T ': ['16 TH/s\xa0', '1400', 'bitcoin'], 'Canaan AvalonMiner 1166 Pro S 72T': ['72 TH/s\xa0', '3420', 'bitcoin'], 'Antminer S9': ['13 TH/s\xa0', '1300', 'bitcoin'], 'MicroBT Whatsminer M20S': ['70 TH/s\xa0', '3360', 'bitcoin'], 'Antminer S11': ['19 TH/s\xa0', '1530', 'bitcoin'], 'Antminer S9j': ['14 TH/s\xa0', '1350', 'bitcoin'], 'Ebang Ebit E11': ['30 TH/s\xa0', '1950', 'bitcoin'], 'Innosilicon D9 - DecredMaster': ['2.4 TH/s\xa0', '1000', 'bitcoin'], 'Antminer Z11e': ['70 KH/s\xa0', '1390', 'zcash'], 'Antminer V9': ['4 TH/s\xa0', '1030', 'bitcoin'], 'Innosilicon T3+Pro 67T': ['67 TH/s\xa0', '3300', 'bitcoin'], 'Canaan AvalonMiner 741': ['7.3 TH/s\xa0', '1150', 'bitcoin'], 'Ebang Ebit E9.2': ['12 TH/s\xa0', '1320', 'bitcoin'], 'Toddminer C1': ['1600 GH/s\xa0', '1200', 'bitcoin'], 'Antminer T17+': ['64 TH/s\xa0', '3200', 'bitcoin'], 'Canaan AvalonMiner 1041F': ['33.5 TH/s\xa0', '2110', 'bitcoin'], 'Ebang Ebit E12': ['44 TH/s\xa0', '2508', 'bitcoin'], 'Canaan AvalonMiner 851': ['14.6 TH/s\xa0', '1450', 'bitcoin'], 'Antminer D5': ['119 GH/s\xa0', '1566', 'bitcoin'], 'MicroBT Whatsminer M10': ['33 TH/s\xa0', '2145', 'bitcoin'], 'Antminer S2': ['1 TH/s\xa0', '1000', 'bitcoin'], 'Canaan AvalonMiner 1126 Pro S 68T': ['68 TH/s\xa0', '3420', 'bitcoin'], 'Canaan AvalonMiner 921': ['20 TH/s\xa0', '1700', 'bitcoin'], 'Canaan AvalonMiner 1026': ['30 TH/s\xa0', '2070', 'bitcoin'], 'Ebang Ebit E10': ['18 TH/s\xa0', '1650', 'bitcoin'], 'Ebang Ebit E9i': ['18 TH/s\xa0', '1650', 'bitcoin'], 'Antminer T17e': ['53 TH/s\xa0', '2915', 'bitcoin'], 'Canaan AvalonMiner 1146 Pro': ['63 TH/s\xa0', '3276', 'bitcoin'], 'Fusionsilicon X1': ['12.96 GH/s\xa0', '1110', 'bitcoin'], 'Obelisk SC1 Immersion': ['2.2 TH/s\xa0', '1600', 'bitcoin'], 'Antminer DR3': ['7.8 TH/s\xa0', '1410', 'dash'], 'Antminer T9': ['11.5 TH/s\xa0', '1450', 'bitcoin'], 'Canaan AvalonMiner 1047': ['37 TH/s\xa0', '2380', 'bitcoin'], 'Canaan AvalonMiner 911': ['19.5 TH/s\xa0', '1750', 'bitcoin'], 'Antminer T9+': ['10.5 TH/s\xa0', '1430', 'bitcoin'], 'StrongU STU-U1': ['11 TH/s\xa0', '1600', 'bitcoin'], 'Antminer S9 Hydro': ['18 TH/s\xa0', '1728', 'bitcoin'], 'Innosilicon D9+ DecredMaster': ['2.8 TH/s\xa0', '1230', 'bitcoin'], 'Canaan AvalonMiner 1126 Pro S 64T': ['64 TH/s\xa0', '3420', 'bitcoin'], 'MicroBT Whatsminer M32S': ['62 TH/s\xa0', '3348', 'bitcoin'], 'Innosilicon T2T-30T': ['30 TH/s\xa0', '2200', 'bitcoin'], 'Cheetah Miner F3': ['30 TH/s\xa0', '2200', 'bitcoin'], 'Antminer D3': ['15 GH/s\xa0', '1200', 'bitcoin'], 'Antminer S7': ['4.7 TH/s\xa0', '1300', 'bitcoin'], 'Dayun Zig Z1+': ['7.25 GH/s\xa0', '1200', 'bitcoin'], 'Dayun Zig Z1': ['6.8 GH/s\xa0', '1200', 'bitcoin'], 'Innosilicon A5+ Dash Master': ['65 GH/s\xa0', '1500', 'dash'], 'Cheetah Miner F5': ['55 TH/s\xa0', '3135', 'bitcoin'], 'Innosilicon T2T-26T': ['26 TH/s\xa0', '2100', 'bitcoin'], 'Canaan AvalonMiner 1146': ['56 TH/s\xa0', '3192', 'bitcoin'], 'Ebang Ebit E9.3': ['16 TH/s\xa0', '1760', 'bitcoin'], 'StrongU STU-U1+': ['12.8 TH/s\xa0', '1850', 'bitcoin'], 'Innosilicon T3+ 57T': ['57 TH/s\xa0', '3300', 'bitcoin'], 'Cheetah Miner F5M': ['52 TH/s\xa0', '3120', 'bitcoin'], 'Canaan AvalonMiner 1126 Pro S 60T': ['60 TH/s\xa0', '3420', 'bitcoin'], 'Innosilicon T3 50T': ['50 TH/s\xa0', '3100', 'bitcoin'], 'Cheetah Miner F5I': ['60 TH/s\xa0', '3480', 'bitcoin'], 'Canaan AvalonMiner 1066Pro': ['55 TH/s\xa0', '3300', 'bitcoin'], 'Antminer S4': ['2 TH/s\xa0', '1400', 'bitcoin'], 'Aisen A1 24T': ['24 TH/s\xa0', '2200', 'bitcoin'], 'MicroBT Whatsminer M21S': ['56 TH/s\xa0', '3360', 'bitcoin'], 'Antminer K5': ['1130 GH/s\xa0', '1580', 'bitcoin'], 'Hummer Miner H7 Pro 48 TH': ['48 TH/s\xa0', '3120', 'bitcoin'], 'Dayun Zig Z1 Pro': ['13 GH/s\xa0', '1500', 'bitcoin'], 'Canaan AvalonMiner 1066': ['50 TH/s\xa0', '3256', 'bitcoin'], 'Spondoolies SPx36': ['540 GH/s\xa0', '4400', 'bitcoin'], 'MicroBT Whatsminer M10S': ['55 TH/s\xa0', '3500', 'bitcoin'], 'Hummer Miner H7 Pro 53 TH': ['53 TH/s\xa0', '3445', 'bitcoin'], 'MicroBT Whatsminer M3': ['12 TH/s\xa0', '2000', 'bitcoin'], 'MicroBT Whatsminer M3X': ['12.5 TH/s\xa0', '2050', 'bitcoin'], 'Aladdin T1 32T ': ['32 TH/s\xa0', '2800', 'bitcoin'], 'Ebang Ebit E10.3': ['24 TH/s\xa0', '2640', 'bitcoin'], 'iBeLink DM56G X11/Dash Miner': ['56 GH/s\xa0', '2100', 'bitcoin'], 'iBeLink DSM6T Blake256 Miner': ['6 TH/s\xa0', '2100', 'bitcoin'], 'iBeLink DSM7T Miner': ['3.5 TH/s\xa0', '2100', 'bitcoin'], 'Dayun Zig D1': ['48 GH/s\xa0', '2200', 'bitcoin'], 'Hummer Miner H1': ['80 GH/s\xa0', '2000', 'bitcoin'], 'Bitfury Tardis': ['80 TH/s\xa0', '6300', 'bitcoin'], 'Bitfury B8': ['72 TH/s\xa0', '6300', 'bitcoin']}
asics_s = {'Antminer B3': ['750 H/s\xa0', '360', 'bitcoin'], 'Hammer D10+ 5000 MH/s\xa0': ['5000 MH/s\xa0', '3800', 'litecoin'], 'Antminer A3': ['820 GH/s\xa0', '1280', 'bitcoin'], 'Antminer L3': ['250 MH/s\xa0', '400', 'bitcoin'], 'Antminer S1': ['180 GH/s\xa0', '360', 'bitcoin'], 'Antminer S3': ['440 GH/s\xa0', '370', 'bitcoin'], 'Obelisk SC1': ['550 GH/s\xa0', '500', 'bitcoin'], 'Obelisk SC1 Slim': ['550 GH/s\xa0', '500', 'bitcoin'], 'Obelisk DCR1': ['1.2 TH/s\xa0', '500', 'bitcoin'], 'Obelisk DCR1 Slim': ['1.2 TH/s\xa0', '500', 'bitcoin'], 'Antminer E3': ['190 MH/s\xa0', '760', 'bitcoin'], 'Antminer S5': ['1.155 TH/s\xa0', '590', 'bitcoin'], 'Obelisk SC1 Dual': ['1.1 TH/s\xa0', '900', 'bitcoin'], 'Bitfury RD4': ['25 TH/s\xa0', '1720', 'bitcoin'], 'Antminer V9': ['4 TH/s\xa0', '1030', 'bitcoin'], 'Toddminer C1': ['1600 GH/s\xa0', '1200', 'bitcoin'], 'Antminer D5': ['119 GH/s\xa0', '1566', 'bitcoin'], 'Antminer S2': ['1 TH/s\xa0', '1000', 'bitcoin'], 'Obelisk SC1 Immersion': ['2.2 TH/s\xa0', '1600', 'bitcoin'], 'Antminer D3': ['15 GH/s\xa0', '1200', 'bitcoin'], 'Antminer S7': ['4.7 TH/s\xa0', '1300', 'bitcoin'], 'Antminer S4': ['2 TH/s\xa0', '1400', 'bitcoin'], 'Antminer K5': ['1130 GH/s\xa0', '1580', 'bitcoin'], 'Bitfury Tardis': ['80 TH/s\xa0', '6300', 'bitcoin'], 'Bitfury B8': ['72 TH/s\xa0', '6300', 'bitcoin'], 'Aisen A1 24T 24 TH/s\xa0': ['24 TH/s\xa0', '2200', 'bitcoin'], 'Aladdin T1 16T  16 TH/s\xa0': ['16 TH/s\xa0', '1400', 'bitcoin'], 'Aladdin T1 32T  32 TH/s\xa0': ['32 TH/s\xa0', '2800', 'bitcoin'], 'Antminer D7 1.286 TH/s\xa0': ['1.286 TH/s\xa0', '3148', 'dash'], 'Antminer DR3 7.8 TH/s\xa0': ['7.8 TH/s\xa0', '1410', 'dash'], 'Antminer DR5 35 TH/s\xa0': ['35 TH/s\xa0', '1610', 'dash'], 'Antminer E9 2400 MH/s\xa0': ['2400 MH/s\xa0', '1920', 'ethereumclassic'], 'Antminer K7 63.5 TH/s\xa0': ['63.5 TH/s\xa0', '3080', 'nervos'], 'Antminer KA3 166 TH/s\xa0': ['166 TH/s\xa0', '3154', 'kadena'], 'Antminer L3+ 504 MH/s\xa0': ['504 MH/s\xa0', '800', 'litecoin'], 'Antminer L3++ 580 MH/s\xa0': ['580 MH/s\xa0', '940', 'litecoin'], 'Antminer L7 9500 MH/s\xa0': ['9500 MH/s\xa0', '3425', 'litecoin'], 'Antminer R4 8.7 TH/s\xa0': ['8.7 TH/s\xa0', '845', 'bitcoin'], 'Antminer S11 19 TH/s\xa0': ['19 TH/s\xa0', '1530', 'bitcoin'], 'Antminer S15 28 TH/s\xa0': ['28 TH/s\xa0', '1600', 'bitcoin'], 'Antminer S17 56 TH/s\xa0': ['56 TH/s\xa0', '2520', 'bitcoin'], 'Antminer S17 53 TH/s 53 TH/s\xa0': ['53 TH/s\xa0', '2385', 'bitcoin'], 'Antminer S17 Pro 53 TH/s\xa0': ['53 TH/s\xa0', '2094', 'bitcoin'], 'Antminer S17 Pro 50 TH/s 50 TH/s\xa0': ['50 TH/s\xa0', '1975', 'bitcoin'], 'Antminer S17+ 73 TH/s\xa0': ['73 TH/s\xa0', '2920', 'bitcoin'], 'Antminer S17e 64 TH/s\xa0': ['64 TH/s\xa0', '2880', 'bitcoin'], 'Antminer S19 95 TH/s\xa0': ['95 TH/s\xa0', '3250', 'bitcoin'], 'Antminer S19 Pro 110 TH/s\xa0': ['110 TH/s\xa0', '3250', 'bitcoin'], 'Antminer S19 XP 140 TH/s\xa0': ['140 TH/s\xa0', '3010', 'bitcoin'], 'Antminer S19 XP Hyd 255 TH/s\xa0': ['255 TH/s\xa0', '5304', 'bitcoin'], 'Antminer S19a 100 TH/s\xa0': ['100 TH/s\xa0', '3450', 'bitcoin'], 'Antminer S19a Pro 110 TH/s\xa0': ['110 TH/s\xa0', '3245', 'bitcoin'], 'Antminer S19j 90 TH/s\xa0': ['90 TH/s\xa0', '3100', 'bitcoin'], 'Antminer S19j Pro 100 TH/s\xa0': ['100 TH/s\xa0', '3050', 'bitcoin'], 'Antminer S9 13 TH/s\xa0': ['13 TH/s\xa0', '1300', 'bitcoin'], 'Antminer S9 Hydro 18 TH/s\xa0': ['18 TH/s\xa0', '1728', 'bitcoin'], 'Antminer S9 SE 16 TH/s\xa0': ['16 TH/s\xa0', '1280', 'bitcoin'], 'Antminer S9i 13 TH/s\xa0': ['13 TH/s\xa0', '1280', 'bitcoin'], 'Antminer S9j 14 TH/s\xa0': ['14 TH/s\xa0', '1350', 'bitcoin'], 'Antminer S9k 13.5 TH/s\xa0': ['13.5 TH/s\xa0', '1148', 'bitcoin'], 'Antminer T15 24 TH/s\xa0': ['24 TH/s\xa0', '1540', 'bitcoin'], 'Antminer T17 40 TH/s\xa0': ['40 TH/s\xa0', '2200', 'bitcoin'], 'Antminer T17+ 64 TH/s\xa0': ['64 TH/s\xa0', '3200', 'bitcoin'], 'Antminer T17e 53 TH/s\xa0': ['53 TH/s\xa0', '2915', 'bitcoin'], 'Antminer T19 84 TH/s\xa0': ['84 TH/s\xa0', '3150', 'bitcoin'], 'Antminer T9 11.5 TH/s\xa0': ['11.5 TH/s\xa0', '1450', 'bitcoin'], 'Antminer T9+ 10.5 TH/s\xa0': ['10.5 TH/s\xa0', '1430', 'bitcoin'], 'Antminer Z11 135 KH/s\xa0': ['135 KH/s\xa0', '1418', 'zcash'], 'Antminer Z11e 70 KH/s\xa0': ['70 KH/s\xa0', '1390', 'zcash'], 'Antminer Z11j 105 KH/s\xa0': ['105 KH/s\xa0', '1418', 'zcash'], 'Antminer Z15 420 KH/s\xa0': ['420 KH/s\xa0', '1510', 'zcash'], 'Antminer Z9 42 kH/s\xa0': ['42 kH/s\xa0', '970', 'zcash'], 'Antminer Z9 Mini 10 kH/s\xa0': ['10 kH/s\xa0', '300', 'zcash'], 'Bluestar L1 4900 MH/s\xa0': ['4900 MH/s\xa0', '3800', 'litecoin'], 'Canaan AvalonMiner 1026 30 TH/s\xa0': ['30 TH/s\xa0', '2070', 'bitcoin'], 'Canaan AvalonMiner 1041 31 TH/s\xa0': ['31 TH/s\xa0', '1736', 'bitcoin'], 'Canaan AvalonMiner 1041F 33.5 TH/s\xa0': ['33.5 TH/s\xa0', '2110', 'bitcoin'], 'Canaan AvalonMiner 1047 37 TH/s\xa0': ['37 TH/s\xa0', '2380', 'bitcoin'], 'Canaan AvalonMiner 1066 50 TH/s\xa0': ['50 TH/s\xa0', '3256', 'bitcoin'], 'Canaan AvalonMiner 1066Pro 55 TH/s\xa0': ['55 TH/s\xa0', '3300', 'bitcoin'], 'Canaan AvalonMiner 1126 Pro S 60T 60 TH/s\xa0': ['60 TH/s\xa0', '3420', 'bitcoin'], 'Canaan AvalonMiner 1126 Pro S 64T 64 TH/s\xa0': ['64 TH/s\xa0', '3420', 'bitcoin'], 'Canaan AvalonMiner 1126 Pro S 68T 68 TH/s\xa0': ['68 TH/s\xa0', '3420', 'bitcoin'], 'Canaan AvalonMiner 1146 56 TH/s\xa0': ['56 TH/s\xa0', '3192', 'bitcoin'], 'Canaan AvalonMiner 1146 Pro 63 TH/s\xa0': ['63 TH/s\xa0', '3276', 'bitcoin'], 'Canaan AvalonMiner 1166 68 TH/s\xa0': ['68 TH/s\xa0', '3196', 'bitcoin'], 'Canaan AvalonMiner 1166 Pro 81 TH/s\xa0': ['81 TH/s\xa0', '3400', 'bitcoin'], 'Canaan AvalonMiner 1166 Pro S 72T 72 TH/s\xa0': ['72 TH/s\xa0', '3420', 'bitcoin'], 'Canaan AvalonMiner 1246 90 TH/s\xa0': ['90 TH/s\xa0', '3420', 'bitcoin'], 'Canaan AvalonMiner 1266 100 TH/s\xa0': ['100 TH/s\xa0', '3500', 'bitcoin'], 'Canaan AvalonMiner 1346 110 TH/s\xa0': ['110 TH/s\xa0', '3300', 'bitcoin'], 'Canaan AvalonMiner 1366 130 TH/s\xa0': ['130 TH/s\xa0', '3250', 'bitcoin'], 'Canaan AvalonMiner 741 7.3 TH/s\xa0': ['7.3 TH/s\xa0', '1150', 'bitcoin'], 'Canaan AvalonMiner 821 11.5 TH/s\xa0': ['11.5 TH/s\xa0', '1200', 'bitcoin'], 'Canaan AvalonMiner 841 13.6 TH/s\xa0': ['13.6 TH/s\xa0', '1290', 'bitcoin'], 'Canaan AvalonMiner 851 14.6 TH/s\xa0': ['14.6 TH/s\xa0', '1450', 'bitcoin'], 'Canaan AvalonMiner 911 19.5 TH/s\xa0': ['19.5 TH/s\xa0', '1750', 'bitcoin'], 'Canaan AvalonMiner 921 20 TH/s\xa0': ['20 TH/s\xa0', '1700', 'bitcoin'], 'Cheetah Miner F3 30 TH/s\xa0': ['30 TH/s\xa0', '2200', 'bitcoin'], 'Cheetah Miner F5 55 TH/s\xa0': ['55 TH/s\xa0', '3135', 'bitcoin'], 'Cheetah Miner F5+ 66 TH/s\xa0': ['66 TH/s\xa0', '2838', 'bitcoin'], 'Cheetah Miner F5I 60 TH/s\xa0': ['60 TH/s\xa0', '3480', 'bitcoin'], 'Cheetah Miner F5M 52 TH/s\xa0': ['52 TH/s\xa0', '3120', 'bitcoin'], 'Dayun Zig D1 48 GH/s\xa0': ['48 GH/s\xa0', '2200', 'bitcoin'], 'Dayun Zig M1 4.3 GH/s\xa0': ['4.3 GH/s\xa0', '790', 'bitcoin'], 'Dayun Zig Z1 6.8 GH/s\xa0': ['6.8 GH/s\xa0', '1200', 'bitcoin'], 'Dayun Zig Z1 Pro 13 GH/s\xa0': ['13 GH/s\xa0', '1500', 'bitcoin'], 'Dayun Zig Z1+ 7.25 GH/s\xa0': ['7.25 GH/s\xa0', '1200', 'bitcoin'], 'Ebang Ebit E10 18 TH/s\xa0': ['18 TH/s\xa0', '1650', 'bitcoin'], 'Ebang Ebit E10.3 24 TH/s\xa0': ['24 TH/s\xa0', '2640', 'bitcoin'], 'Ebang Ebit E11 30 TH/s\xa0': ['30 TH/s\xa0', '1950', 'bitcoin'], 'Ebang Ebit E11+ 37 TH/s\xa0': ['37 TH/s\xa0', '2035', 'bitcoin'], 'Ebang Ebit E11++ 44 TH/s\xa0': ['44 TH/s\xa0', '1980', 'bitcoin'], 'Ebang Ebit E12 44 TH/s\xa0': ['44 TH/s\xa0', '2508', 'bitcoin'], 'Ebang Ebit E9.2 12 TH/s\xa0': ['12 TH/s\xa0', '1320', 'bitcoin'], 'Ebang Ebit E9.3 16 TH/s\xa0': ['16 TH/s\xa0', '1760', 'bitcoin'], 'Ebang Ebit E9i 18 TH/s\xa0': ['18 TH/s\xa0', '1650', 'bitcoin'], 'Fusionsilicon X1 12.96 GH/s\xa0': ['12.96 GH/s\xa0', '1110', 'bitcoin'], 'Fusionsilicon X7 262 GH/s\xa0': ['262 GH/s\xa0', '1420', 'dash'], 'Goldshell CK5 12 TH/s\xa0': ['12 TH/s\xa0', '2400', 'bitcoin'], 'Goldshell CK6 19.3 TH/s\xa0': ['19.3 TH/s\xa0', '3300', 'bitcoin'], 'Goldshell KD5 18 TH/s\xa0': ['18 TH/s\xa0', '2250', 'kadena'], 'Goldshell KD6 26.3 TH/s\xa0': ['26.3 TH/s\xa0', '2630', 'kadena'], 'Goldshell LT5 2.05 GH/s\xa0': ['2.05 GH/s\xa0', '2080', 'bitcoin'], 'Goldshell LT6 3.35 GH/s\xa0': ['3.35 GH/s\xa0', '3200', 'bitcoin'], 'Goldshell X5 0.72 GH/s\xa0': ['0.72 GH/s\xa0', '990', 'bitcoin'], 'Goldshell X5S 1.36 GH/s\xa0': ['1.36 GH/s\xa0', '1850', 'bitcoin'], 'Hummer Miner H1 80 GH/s\xa0': ['80 GH/s\xa0', '2000', 'bitcoin'], 'Hummer Miner H7 Pro 48 TH 48 TH/s\xa0': ['48 TH/s\xa0', '3120', 'bitcoin'], 'Hummer Miner H7 Pro 53 TH 53 TH/s\xa0': ['53 TH/s\xa0', '3445', 'bitcoin'], 'Hummer Miner H9 Pro 84 TH/s\xa0': ['84 TH/s\xa0', '3360', 'bitcoin'], 'HyperBit BW L21 550 MH/s\xa0': ['550 MH/s\xa0', '950', 'litecoin'], 'Innosilicon A10 480 MH/s\xa0': ['480 MH/s\xa0', '750', 'ethereumclassic'], 'Innosilicon A10 Pro 440 MH/s\xa0': ['440 MH/s\xa0', '950', 'ethereumclassic'], 'Innosilicon A10 Pro 6GB 578 MH/s\xa0': ['578 MH/s\xa0', '1300', 'bitcoin'], 'Innosilicon A11 1500 MH/s\xa0': ['1500 MH/s\xa0', '2300', 'ethereumclassic'], 'Innosilicon A4 280 MH/s\xa0': ['280 MH/s\xa0', '1050', 'litecoin'], 'Innosilicon A4+ 620 MH/s\xa0': ['620 MH/s\xa0', '750', 'litecoin'], 'Innosilicon A5 Dash Master 32.5 GH/s\xa0': ['32.5 GH/s\xa0', '750', 'dash'], 'Innosilicon A5+ Dash Master 65 GH/s\xa0': ['65 GH/s\xa0', '1500', 'dash'], 'Innosilicon A6 LTC Master 1.23 GH/s\xa0': ['1.23 GH/s\xa0', '1500', 'litecoin'], 'Innosilicon A6+ LTC Master 2.2 GH/s\xa0': ['2.2 GH/s\xa0', '2100', 'litecoin'], 'Innosilicon A9 ZMaster 50 kH/s\xa0': ['50 kH/s\xa0', '620', 'zcash'], 'Innosilicon A9+ ZMaster 120 KH/s\xa0': ['120 KH/s\xa0', '1550', 'zcash'], 'Innosilicon A9++ ZMaster 140 KH/s\xa0': ['140 KH/s\xa0', '1550', 'zcash'], 'Innosilicon D9 - DecredMaster 2.4 TH/s\xa0': ['2.4 TH/s\xa0', '1000', 'bitcoin'], 'Innosilicon D9+ DecredMaster 2.8 TH/s\xa0': ['2.8 TH/s\xa0', '1230', 'bitcoin'], 'Innosilicon T2T-26T 26 TH/s\xa0': ['26 TH/s\xa0', '2100', 'bitcoin'], 'Innosilicon T2T-30T 30 TH/s\xa0': ['30 TH/s\xa0', '2200', 'bitcoin'], 'Innosilicon T3 39T 39 TH/s\xa0': ['39 TH/s\xa0', '2150', 'bitcoin'], 'Innosilicon T3 40T 40 TH/s\xa0': ['40 TH/s\xa0', '2200', 'bitcoin'], 'Innosilicon T3 43T 43 TH/s\xa0': ['43 TH/s\xa0', '2100', 'bitcoin'], 'Innosilicon T3 50T 50 TH/s\xa0': ['50 TH/s\xa0', '3100', 'bitcoin'], 'Innosilicon T3+ 57T 57 TH/s\xa0': ['57 TH/s\xa0', '3300', 'bitcoin'], 'Innosilicon T3+Pro 67T 67 TH/s\xa0': ['67 TH/s\xa0', '3300', 'bitcoin'], 'Linzhi Phoenix 2600 MH/s\xa0': ['2600 MH/s\xa0', '3000', 'bitcoin'], 'MicroBT Whatsminer D1 48 TH/s\xa0': ['48 TH/s\xa0', '2200', 'bitcoin'], 'MicroBT Whatsminer M10 33 TH/s\xa0': ['33 TH/s\xa0', '2145', 'bitcoin'], 'MicroBT Whatsminer M10S 55 TH/s\xa0': ['55 TH/s\xa0', '3500', 'bitcoin'], 'MicroBT Whatsminer M20S 70 TH/s\xa0': ['70 TH/s\xa0', '3360', 'bitcoin'], 'MicroBT Whatsminer M21 31 TH/s\xa0': ['31 TH/s\xa0', '1860', 'bitcoin'], 'MicroBT Whatsminer M21S 56 TH/s\xa0': ['56 TH/s\xa0', '3360', 'bitcoin'], 'MicroBT Whatsminer M3 12 TH/s\xa0': ['12 TH/s\xa0', '2000', 'bitcoin'], 'MicroBT Whatsminer M30S 88 TH/s\xa0': ['88 TH/s\xa0', '3344', 'bitcoin'], 'MicroBT Whatsminer M30S+ 100 TH/s\xa0': ['100 TH/s\xa0', '3400', 'bitcoin'], 'MicroBT Whatsminer M30S++ 112 TH/s\xa0': ['112 TH/s\xa0', '3472', 'bitcoin'], 'MicroBT Whatsminer M31S 78 TH/s\xa0': ['78 TH/s\xa0', '3276', 'bitcoin'], 'MicroBT Whatsminer M31S+ 82 TH/s\xa0': ['82 TH/s\xa0', '3444', 'bitcoin'], 'MicroBT Whatsminer M32S 62 TH/s\xa0': ['62 TH/s\xa0', '3348', 'bitcoin'], 'MicroBT Whatsminer M3X 12.5 TH/s\xa0': ['12.5 TH/s\xa0', '2050', 'bitcoin'], 'MicroBT Whatsminer M50 114 TH/s\xa0': ['114 TH/s\xa0', '3306', 'bitcoin'], 'MicroBT Whatsminer M50S 126 TH/s\xa0': ['126 TH/s\xa0', '3276', 'bitcoin'], 'Spondoolies SPx36 540 GH/s\xa0': ['540 GH/s\xa0', '4400', 'bitcoin'], 'StrongU Hornbill H8 74 TH/s\xa0': ['74 TH/s\xa0', '3330', 'bitcoin'], 'StrongU Hornbill H8 Pro 84 TH/s\xa0': ['84 TH/s\xa0', '3360', 'bitcoin'], 'StrongU STU-U1 11 TH/s\xa0': ['11 TH/s\xa0', '1600', 'bitcoin'], 'StrongU STU-U1+ 12.8 TH/s\xa0': ['12.8 TH/s\xa0', '1850', 'bitcoin'], 'StrongU STU-U1++ 52 TH/s\xa0': ['52 TH/s\xa0', '2100', 'bitcoin'], 'StrongU STU-U6 440 GH/s\xa0': ['440 GH/s\xa0', '2000', 'bitcoin'], 'StrongU STU-U8 46 TH/s\xa0': ['46 TH/s\xa0', '2100', 'bitcoin'], 'iBeLink BM-K1 Blake2S Miner 5.3 TH/s\xa0': ['5.3 TH/s\xa0', '800', 'bitcoin'], 'iBeLink BM-K1 Max Blake2S Miner 32 TH/s\xa0': ['32 TH/s\xa0', '3200', 'bitcoin'], 'iBeLink BM-K1+ Blake2S Miner 15.5 TH/s\xa0': ['15.5 TH/s\xa0', '2250', 'bitcoin'], 'iBeLink DM56G X11/Dash Miner 56 GH/s\xa0': ['56 GH/s\xa0', '2100', 'bitcoin'], 'iBeLink DSM6T Blake256 Miner 6 TH/s\xa0': ['6 TH/s\xa0', '2100', 'bitcoin'], 'iBeLink DSM7T Miner 3.5 TH/s\xa0': ['3.5 TH/s\xa0', '2100', 'bitcoin']}


keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)  # наша клавиатура
key_yes = types.KeyboardButton(text='🇷🇺')  # кнопка «Да»
key_no = types.KeyboardButton(text='🇱🇷')
keyboard.add(key_yes, key_no)

eu = types.ReplyKeyboardMarkup(row_width=1)
calculating_profitability = types.KeyboardButton(text='📊Сalculating profitability')
сhange_settings = types.KeyboardButton(text='⚙Change Settings')
training = types.KeyboardButton(text='💰Training')
help = types.KeyboardButton(text='📩Help')
eu.add(calculating_profitability)
eu.add(сhange_settings)
eu.add(training)
eu.add(help)


tutor = types.InlineKeyboardMarkup(row_width=1)
t = types.InlineKeyboardButton(text='Урок 2', callback_data='Урок 2')
tutor.add(t)


tutor2 = types.InlineKeyboardMarkup(row_width=1)
t = types.InlineKeyboardButton(text='Урок 3', callback_data='Урок 3')
tutor2.add(t)

ru = types.ReplyKeyboardMarkup(row_width=1)
calculating_profitability = types.KeyboardButton(text='📊Расчет прибыльности')
сhange_settings = types.KeyboardButton(text='⚙Изменить настройки')
training = types.KeyboardButton(text='💰Обучение')
help = types.KeyboardButton(text='📩Помощь')
ru.add(calculating_profitability)
ru.add(сhange_settings)
ru.add(training)
ru.add(help)


help1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
calculating_profitability = types.KeyboardButton(text='Инструкция')
сhange_settings = types.KeyboardButton(text='Обратная связь')
help = types.KeyboardButton(text='В главное меню')
help1.add(calculating_profitability)
help1.add(сhange_settings)
help1.add(help)

settingsru = types.ReplyKeyboardMarkup(row_width=1)
calculating_profitability = types.KeyboardButton(text='Изменить язык')
сhange_settings = types.KeyboardButton(text='Изменить валюту')
training = types.KeyboardButton(text='Изменить цену за электроэнергию')
help = types.KeyboardButton(text='В главное меню')
settingsru.add(calculating_profitability)
settingsru.add(сhange_settings)
settingsru.add(training)
settingsru.add(help)


settings = types.ReplyKeyboardMarkup(row_width=1)
calculating_profitability = types.KeyboardButton(text='Change the language')
сhange_settings = types.KeyboardButton(text='Change Currency')
training = types.KeyboardButton(text='Change the price for electricity')
help = types.KeyboardButton(text='To the main menu')
settings.add(calculating_profitability)
settings.add(сhange_settings)
settings.add(training)
settings.add(help)


sposob = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
calculating_profitability = types.KeyboardButton(text='Выбрать устройство')
сhange_settings = types.KeyboardButton(text='Задать характеристики')
mainer1 = types.KeyboardButton(text='В главное меню')
sposob.add(calculating_profitability)
sposob.add(сhange_settings)
sposob.add(mainer1)

sposob2 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
calculating_profitability = types.KeyboardButton(text='Select a device')
сhange_settings = types.KeyboardButton(text='Set characteristics')
sposob2.add(calculating_profitability)
sposob2.add(сhange_settings)

alg = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
calculating_profitability = types.KeyboardButton(text='SHA-256')
calculating_profitability2 = types.KeyboardButton(text='Scrypt')
mainer1 = types.KeyboardButton(text='В главное меню')
alg.add(calculating_profitability)
alg.add(calculating_profitability2)
alg.add(mainer1)

moneyru = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
calculating_profitability = types.KeyboardButton(text='RUB')
сhange_settings = types.KeyboardButton(text='USD')
moneyru.add(calculating_profitability, сhange_settings)

mainer = types.ReplyKeyboardMarkup(row_width=1)
mainer1 = types.KeyboardButton(text='В главное меню')
mainer.add(mainer1)
for i in asics:
    mainer1 = types.KeyboardButton(text=i)
    mainer.add(mainer1)

mainereu = types.ReplyKeyboardMarkup(row_width=1)
mainer1 = types.KeyboardButton(text='To the main menu')
mainereu.add(mainer1)
for i in asics:
    mainer1 = types.KeyboardButton(text=i)
    mainereu.add(mainer1)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Hello, I am profit bot. Please select language.", reply_markup=keyboard)
    if message.text == "🇷🇺":
        bot.send_message(message.from_user.id, "Язык изменен - текущий язык 🇷🇺", reply_markup=ru)
        db_sess = Session()
        if db_sess.query(User).filter(User.id == message.from_user.id).first():
            us = db_sess.query(User).filter(User.id == message.from_user.id).first()
            us.language = 'Ru'
            db_sess.commit()
        else:
            user = User(
                id=message.from_user.id,
                language='Ru',
                money='Rub',
                power='0'
            )
            db_sess.add(user)
            db_sess.commit()
    if message.text == "🇱🇷":
        bot.send_message(message.from_user.id, "Language changed - current language 🇱🇷", reply_markup=eu)
        db_sess = Session()
        if db_sess.query(User).filter(User.id == message.from_user.id).first():
            us = db_sess.query(User).filter(User.id == message.from_user.id).first()
            us.language = 'Eu'
            db_sess.commit()
        else:
            user = User(
                id=message.from_user.id,
                language='Eu',
                money='Usd',
                power='0'
            )
            db_sess.add(user)
            db_sess.commit()
    if message.text == "📊Расчет прибыльности":
        bot.send_message(message.from_user.id, "Выберите способ", reply_markup=sposob)

    if message.text == "Выбрать устройство":
        bot.send_message(message.from_user.id, "Выберите майнер", reply_markup=mainer)
        bot.register_next_step_handler(message, asic)

    if message.text == "Задать характеристики":
        bot.send_message(message.from_user.id, "Выберите алгоритм", reply_markup=alg)



    if message.text == "Set characteristics":
        bot.send_message(message.from_user.id, "Choose an algorithm", reply_markup=alg)

    if message.text == "SHA-256":
        db_sess = Session()
        us = db_sess.query(User).filter(User.id == message.from_user.id).first()
        text = '''Введите Hash-мощность TH\s и потребление энергии одним сообщением.
Пример: 
14
1370'''
        text2 = '''Enter the Hash power of TH\s and the power consumption in one message.
Example:
14
1370'''
        try:
            if us.language == 'Ru':
                bot.send_message(message.from_user.id, f"{text}")
                bot.register_next_step_handler(message, hash2)
            else:
                bot.send_message(message.from_user.id, f"{text2}")
                bot.register_next_step_handler(message, hash)
        except Exception:
            bot.send_message(message.from_user.id, f"{text}")
            bot.register_next_step_handler(message, hash2)

    if message.text == "Scrypt":
        db_sess = Session()
        us = db_sess.query(User).filter(User.id == message.from_user.id).first()
        text = '''Введите Hash-мощность MH\s и потребление энергии одним сообщением.
Пример: 
9500
1370'''
        text2 = '''Enter the Hash power of MH\s and the power consumption in one message.
Example:
9500
1370'''
        try:
            if us.language == 'Ru':
                bot.send_message(message.from_user.id, f"{text}")
                bot.register_next_step_handler(message, scrypt2)
            else:
                bot.send_message(message.from_user.id, f"{text2}")
                bot.register_next_step_handler(message, scrypt)
        except Exception:
            bot.send_message(message.from_user.id, f"{text}")
            bot.register_next_step_handler(message, scrypt2)

    if message.text == "⚙Изменить настройки":
        bot.send_message(message.from_user.id, "Выберите настройки", reply_markup=settingsru)

    if message.text == "Изменить язык":
        bot.send_message(message.from_user.id, "Выберите язык", reply_markup=keyboard)

    if message.text == "Изменить валюту":
        bot.send_message(message.from_user.id, "Выберите валюту", reply_markup=moneyru)

    if message.text == "📩Помощь":
        bot.send_message(message.from_user.id, "С чем вам помочь?", reply_markup=help1)

    if message.text == "📊Сalculating profitability":
        bot.send_message(message.from_user.id, "Choose a method", reply_markup=sposob2)

    if message.text == "Select a device":
        bot.send_message(message.from_user.id, "Choose a miner", reply_markup=mainereu)
        bot.register_next_step_handler(message, asic2)

    if message.text == "Инструкция":
        text = '''Калькулятор для моментального расчета прибыльности майнеров. 
Разовые настройки бота: 
1) Выберите в настройках язык ввода.
2) Выберите валюту расчета.
3) Установите цену за ЭЭ, указываем только цифру.

После переходим в главное меню.
Там вызываем "Расчет прибыльности" (выбрав модель нажатием соответствующей кнопки). И получаем искомый результат!

При следующем выборе достаточно сразу нажать кнопку "Расчет прибыльности" и выбрать искомую модель майнера.
Выставленные вами настройки по ЭЭ и валюте запомнились и будут применены автоматически.

Для изменения в настройках цены за ЭЭ, валюты или языка ввода.
Нажмите кнопку "Изменить настройки" и далее все по инструкции на экране.

Если не видны команды бота значит панель с ними просто скрылась. 
Откройте её нажатием на кнопку, похожую формой на электроплиту, 
рядом с полем для ввода сообщения.'''

        bot.send_message(message.from_user.id, f"{text}", reply_markup=ru)



    if message.text == "⚙Change Settings":
        bot.send_message(message.from_user.id, "Select Settings", reply_markup=settings)

    if message.text == "Change the language":
        bot.send_message(message.from_user.id, "Select a language", reply_markup=keyboard)

    if message.text == "Change Currency":
        bot.send_message(message.from_user.id, "Choose a currency", reply_markup=moneyru)

    if message.text == "Change the price for electricity":
        bot.send_message(message.from_user.id, "Write the price for electricity in the selected currency (kWh). Example: 0.003")
        bot.register_next_step_handler(message, electricity)

    if message.text == "Изменить цену за электроэнергию":
        bot.send_message(message.from_user.id, "Напишите цену на электроэнергию в выбранной валюте (kWh). Пример: 3")
        bot.register_next_step_handler(message, electricity_ru)

    if message.text == "Обратная связь":
        tt = """Бот для обратной связи: @CalcCryptoSupport_bot

Наш канал в TG: @cryptocalcru"""
        bot.send_message(message.from_user.id, f"{tt}")


    if message.text == "💰Обучение":
        text4 = '''Вы получили бесплатное обучение❗️

Это бесплатное обучение азам в мире криптовалют. 
Тут вы можете научиться пльзоваться криптой, современными технологиями.
Первый урок - https://telegra.ph/Poshagovaya-instrukciya-kak-ustanovit-koshelek-Trust-Wallet-12-15'''
        bot.send_message(message.from_user.id, f'{text4}', reply_markup=tutor)



    if message.text == "RUB":
        db_sess = Session()
        us = db_sess.query(User).filter(User.id == message.from_user.id).first()
        try:
            us.money = 'Rub'
        except:
            pass
        db_sess.commit()
        try:
            if us.language == 'Ru':
                bot.send_message(message.from_user.id, "Валюта изменена.", reply_markup=ru)
            else:
                bot.send_message(message.from_user.id, "Currency changed.", reply_markup=eu)
        except Exception:
            bot.send_message(message.from_user.id, "Валюта изменена.", reply_markup=ru)

    if message.text == "USD":
        db_sess = Session()
        us = db_sess.query(User).filter(User.id == message.from_user.id).first()
        try:
            us.money = 'Usd'
        except:
            pass
        db_sess.commit()
        try:
            if us.language == 'Ru':
                bot.send_message(message.from_user.id, "Валюта изменена.", reply_markup=ru)
            else:
                bot.send_message(message.from_user.id, "Currency changed.", reply_markup=eu)
        except Exception:
            bot.send_message(message.from_user.id, "Валюта изменена.", reply_markup=ru)


    if message.text == "To the main menu":
        bot.send_message(message.from_user.id, "You are in the main menu", reply_markup=eu)
    if message.text == "В главное меню":
        bot.send_message(message.from_user.id, "Вы в главном меню", reply_markup=ru)

def asic(message):
    try:
        asic = message.text
        if asic == 'В главное меню':
            bot.send_message(message.from_user.id, "Вы в главном меню", reply_markup=ru)
        else:
            db_sess = Session()
            us = db_sess.query(User).filter(User.id == message.from_user.id).first()
            side = ''
            try:
                print(asics_s[asic + '\xa0'][0])
                print('ОНО')
                if 'TH/s' in asics_s[asic + '\xa0'][0]:
                    side = 'TH'
                elif 'MH/s' in asics_s[asic + '\xa0'][0]:
                    print('ДА')
                    side = 'MH'
                elif 'KH/s' in asics_s[asic + '\xa0'][0]:
                    side = 'KH'
                elif 'GH/s' in asics_s[asic + '\xa0'][0]:
                    side = 'GH'
                elif 'H/s' in asics_s[asic + '\xa0'][0]:
                    side = 'H'
            except Exception:
                print(asics_s[asic][0])
                print('ОНО')
                if 'TH/s' in asics_s[asic][0]:
                    side = 'TH'
                elif 'MH/s' in asics_s[asic][0]:
                    print('ДА')
                    side = 'MH'
                elif 'KH/s' in asics_s[asic][0]:
                    side = 'KH'
                elif 'GH/s' in asics_s[asic][0]:
                    side = 'GH'
                elif 'H/s' in asics_s[asic][0]:
                    side = 'H'

            count = ''
            rub = False
            try:
                if us.money == 'Rub':
                    count = '₽'
                    rub = True
                else:
                    count = '$'
            except Exception:
                count = '$'
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            current_date = date.today()
            data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
            usd = data['Valute']['USD']['Value']
            text = f''' {asic}
Время: {current_time}
Дата:  {current_date}

'''
            try:
                if asics_s[asic + '\xa0'][2] == 'litecoin':
                    text2 = litecoin2(asics_s[asic + '\xa0'][2], asics_s[asic + '\xa0'][0].split(' ')[0], asics_s[asic + '\xa0'][1], us.power, side, rub=rub)
                else:
                    text2 = main(asics_s[asic + '\xa0'][2], asics_s[asic + '\xa0'][0].split(' ')[0], asics_s[asic + '\xa0'][1], us.power, side, rub=rub)

            except Exception:
                if asics_s[asic][2] == 'litecoin':
                    text2 = litecoin2(asics_s[asic][2], asics_s[asic][0].split(' ')[0], asics_s[asic][1], us.power, side, rub=rub)
                else:
                    text2 = main(asics_s[asic][2], asics_s[asic][0].split(' ')[0], asics_s[asic][1], us.power, side, rub=rub)



            text4 = f'''-------------------------------------
        
При указанной цене за kWh {us.power}{count}.

Цена доллара к рублю 1$\{usd}₽

'''
            text3 = text + '\n' + text2 + '\n' + text4
            bot.send_message(message.from_user.id, text3, reply_markup=ru)
    except Exception:
        pass


def asic2(message):
    try:
        asic = message.text
        if asic == 'To the main menu':
            bot.send_message(message.from_user.id, "You are in the main menu", reply_markup=eu)
        else:
            db_sess = Session()
            us = db_sess.query(User).filter(User.id == message.from_user.id).first()
            side = ''
            try:
                print(asics_s[asic + '\xa0'][0])
                if 'TH/s' in asics_s[asic + '\xa0'][0]:
                    side = 'TH'
                elif 'MH/s' in asics_s[asic + '\xa0'][0]:
                    print('ДА')
                    side = 'MH'
                elif 'KH/s' in asics_s[asic + '\xa0'][0]:
                    side = 'KH'
                elif 'GH/s' in asics_s[asic + '\xa0'][0]:
                    side = 'GH'
                elif 'H/s' in asics_s[asic + '\xa0'][0]:
                    side = 'H'
            except Exception:
                print(asics_s[asic][0])
                if 'TH/s' in asics_s[asic][0]:
                    side = 'TH'
                elif 'MH/s' in asics_s[asic][0]:
                    print('ДА')
                    side = 'MH'
                elif 'KH/s' in asics_s[asic][0]:
                    side = 'KH'
                elif 'GH/s' in asics_s[asic][0]:
                    side = 'GH'
                elif 'H/s' in asics_s[asic][0]:
                    side = 'H'

            count = ''
            rub = False
            try:
                if us.money == 'Rub':
                    count = '₽'
                    rub = True
                else:
                    count = '$'
            except Exception:
                count = '$'
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            current_date = date.today()
            data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
            usd = data['Valute']['USD']['Value']
            text = f''' {asic}
Time: {current_time}
Date:  {current_date}

'''
        try:
            if asics_s[asic + '\xa0'][2] == 'litecoin':
                text2 = litecoin(asics_s[asic + '\xa0'][2], asics_s[asic + '\xa0'][0].split(' ')[0],
                                  asics_s[asic + '\xa0'][1], us.power, side, rub=rub)
            else:
                text2 = main2(asics_s[asic + '\xa0'][2], asics_s[asic + '\xa0'][0].split(' ')[0], asics_s[asic + '\xa0'][1],
                                 us.power, side, rub=rub)
        except Exception:
            if asics_s[asic][2] == 'litecoin':
                text2 = litecoin(asics_s[asic][2], asics_s[asic][0].split(' ')[0],
                                  asics_s[asic][1], us.power, side, rub=rub)
            else:
                text2 = main2(asics_s[asic][2], asics_s[asic][0].split(' ')[0], asics_s[asic][1],
                                 us.power, side, rub=rub)
        text4 = f'''-------------------------------------

At the specified price per kWh {us.power}{count}.

The price of the dollar to the ruble 1$\{usd}₽

'''
        text3 = text + '\n' + text2 + '\n' + text4
        bot.send_message(message.from_user.id, text3, reply_markup=eu)
    except Exception:
        pass


def hash(message):
    try:
        ans = message.text.split('\n')
        hash = ans[0]
        power = ans[1]

        db_sess = Session()
        us = db_sess.query(User).filter(User.id == message.from_user.id).first()
        side = ''
        count = ''
        rub = False
        try:
            if us.money == 'Rub':
                count = '₽'
                rub = True
            else:
                count = '$'
        except Exception:
            count = '$'
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = date.today()
        data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        usd = data['Valute']['USD']['Value']
        text = f'''
        Time: {current_time}
Date:  {current_date}

            '''
        text2 = main2(asics_s[asic + '\xa0'][2], asics_s[asic + '\xa0'][0].split(' ')[0], asics_s[asic + '\xa0'][1],
                         us.power, side, rub=rub)

        text4 = f'''-------------------------------------

At the specified price per kWh {us.power}{count}.

The price of the dollar to the ruble 1$\{usd}₽

            '''
        text3 = text + '\n' + text2 + '\n' + text4
        bot.send_message(message.from_user.id, text3, reply_markup=eu)
    except Exception as e:
        bot.send_message(message.from_user.id, 'Not the correct values!', reply_markup=eu)

def scrypt(message):
    try:
        ans = message.text.split('\n')
        hash = ans[0]
        power = ans[1]

        db_sess = Session()
        us = db_sess.query(User).filter(User.id == message.from_user.id).first()
        side = ''
        count = ''
        rub = False
        try:
            if us.money == 'Rub':
                count = '₽'
                rub = True
            else:
                count = '$'
        except Exception:
            count = '$'
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = date.today()
        data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        usd = data['Valute']['USD']['Value']
        text = f'''
        Time: {current_time}
Date:  {current_date}

            '''
        text2 = scrypt_s(alg='litecoin', hashRate=hash, power=power,
                         power_cost=us.power, hashuint='MH', rub=rub)

        text4 = f'''-------------------------------------

At the specified price per kWh {us.power}{count}.

The price of the dollar to the ruble 1$\{usd}₽

            '''
        text3 = text + '\n' + text2 + '\n' + text4
        bot.send_message(message.from_user.id, text3, reply_markup=eu)
    except Exception as e:
        bot.send_message(message.from_user.id, 'Not the correct values!', reply_markup=eu)


def hash2(message):
    try:
        ans = message.text.split('\n')
        hash = ans[0]
        power = ans[1]

        db_sess = Session()
        us = db_sess.query(User).filter(User.id == message.from_user.id).first()
        side = ''
        count = ''
        rub = False
        try:
            if us.money == 'Rub':
                count = '₽'
                rub = True
            else:
                count = '$'
        except Exception:
            count = '$'
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = date.today()
        data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        usd = data['Valute']['USD']['Value']
        text = f'''
        Время: {current_time}
Дата:  {current_date}

            '''
        text2 = main('bitcoin', hash, power, us.power, 'TH', rub=rub)
        text4 = f'''-------------------------------------

При указанной цене за kWh {us.power}{count}

Цена доллара к рублю 1$\{usd}₽

            '''
        text3 = text + '\n' + text2 + '\n' + text4
        bot.send_message(message.from_user.id, text3, reply_markup=ru)
    except Exception as e:
        bot.send_message(message.from_user.id, 'Не правильные значения!', reply_markup=ru)

def scrypt2(message):
    try:
        ans = message.text.split('\n')
        hash = ans[0]
        power = ans[1]

        db_sess = Session()
        us = db_sess.query(User).filter(User.id == message.from_user.id).first()
        side = ''
        count = ''
        rub = False
        try:
            if us.money == 'Rub':
                count = '₽'
                rub = True
            else:
                count = '$'
        except Exception:
            count = '$'
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = date.today()
        data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        usd = data['Valute']['USD']['Value']
        text = f'''
        Время: {current_time}
Дата:  {current_date}

            '''
        text2 = scrypt_s_2('litecoin', hash, power, us.power, 'MH', rub=rub)
        text4 = f'''-------------------------------------

При указанной цене за kWh {us.power}{count}

Цена доллара к рублю 1$\{usd}₽

            '''
        text3 = text + '\n' + text2 + '\n' + text4
        bot.send_message(message.from_user.id, text3, reply_markup=ru)
    except Exception as e:
        bot.send_message(message.from_user.id, 'Не правильные значения!', reply_markup=ru)


def electricity(message):
    try:
        price = message.text
        db_sess = Session()
        us = db_sess.query(User).filter(User.id == message.from_user.id).first()
        us.power = price
        db_sess.commit()
        bot.send_message(message.from_user.id, 'Successfully changed', reply_markup=eu)
    except Exception as e:
        bot.send_message(message.from_user.id, 'Check the correctness of the data entered!', reply_markup=ru)

def electricity_ru(message):
    try:
        price = message.text
        db_sess = Session()
        us = db_sess.query(User).filter(User.id == message.from_user.id).first()
        us.power = price
        db_sess.commit()
        bot.send_message(message.from_user.id, 'Успешно изменено', reply_markup=ru)
    except Exception as e:
        bot.send_message(message.from_user.id, 'Проверьте правильность вводимых данных!', reply_markup=ru)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "Урок 2":
            text5 = """Урок 2: Регистрация на крипто бирже 

Биржа это как банк в крипте. У каждого криптана должна быть хотя бы одна регистрация на бирже. 
https://telegra.ph/Kak-zaregistrirovatsya-na-Binance-12-15"""
            bot.send_message(call.from_user.id, f'{text5}', reply_markup=tutor2)

        if call.data == "Урок 3":
            text6 = '''Урок 3: Покупка криптовалюты 

Инструкция по покупке криптовалюты на P2P площадке Binance
https://telegra.ph/Kak-kupit-kriptovalyutu-na-Binance-P2P-Instrukciya-po-pokupke-kriptovalyuty-na-P2P-ploshchadke-Binance-12-16'''
            bot.send_message(call.from_user.id, f'{text6}', reply_markup=ru)
bot.polling(none_stop=True, interval=0)