#!/usr/bin/python

from json import detect_encoding
from turtle import update
from typing import Container
from warnings import catch_warnings

 
#from gpiozero import Device, LED, Button, RotaryEncoder
import vlc
import time
import tkinter as tk
from tkinter import *
from tkinter import ttk




#GPIO Setup
"""
play_btn = Button(4) #This button is connected to GPIO17 (Not pin 17)
pause_btn = Button(5) #This button is connected to GPIO17 (Not pin 17)
stop_btn = Button(6) #This button is connected to GPIO17 (Not pin 17)
toggle_local_or_radio = Button(7) #This button is connected to GPIO17 (Not pin 17)
volume_control = RotaryEncoder(22,27,None,1,(-1,1),False)
station_control = RotaryEncoder(xx,yy,None,1,(1,1),False)
bass_equalizer = RotaryEncoder(xx,yy,None,1,(1,1),False)
treble_equalizer =RotaryEncoder(xx,yy,None,1,(1,1),False)
light_control = RotaryEncoder(xx,yy,None,1,(1,1),False)
light_btn = Button(8)
"""

# Make a class for the Radio
class Radio:

    def __init__(self):
        self.current_station_no = 0
        self.station_urls = [
          "https://lyd.nrk.no/nrk_radio_p1_hordaland_mp3_h",
          "http://lyd.nrk.no/nrk_radio_p1pluss_mp3_h",
           "http://lyd.nrk.no/nrk_radio_p2_mp3_h",
           "http://lyd.nrk.no/nrk_radio_p3_mp3_h",
           "http://lyd.nrk.no/nrk_radio_p13_mp3_h",
          "http://lyd.nrk.no/nrk_radio_alltid_nyheter_mp3_h",
          "http://lyd.nrk.no/nrk_radio_klassisk_mp3_h",
          "http://stream.resonance.fm:8000/resonance"
    ]


        self.station_names = ["NRK P1","NRK P1+","NRK P2","NRK P3","NRK P13","NRK Nyheter","NRK Klassisk","Resonance"]
        self.volume = 60
        self.low_gain = 10
        self.high_gain = 10


radio = Radio() #Make an instance of Radio



#Setting up the player
instance = vlc.Instance('--input-repeat=-1','--fullscreen')
player = instance.media_player_new()
media = instance.media_new("home/kristoffer/repo/GPIO_radio/file_example_MP3_2MG.mp3")
#media = instance.media_new(radio.station_urls[0])
player.set_media(media)
player.audio_set_volume(radio.volume)
player.play()



u_bands = vlc.libvlc_audio_equalizer_get_band_count()

i=0
while i<u_bands:
    print(vlc.libvlc_audio_equalizer_get_band_frequency(i))
    i+=1

#player.set_equalizer(vlc.libvlc_audio_equalizer_new_from_preset(1))
eq_active = True

if(eq_active==True):

    eqlz = vlc.libvlc_audio_equalizer_new() 
    vlc.libvlc_audio_equalizer_set_amp_at_index(eqlz,10,0)
    vlc.libvlc_audio_equalizer_set_amp_at_index(eqlz,10,1)
    vlc.libvlc_audio_equalizer_set_amp_at_index(eqlz,10,2)
    vlc.libvlc_audio_equalizer_set_amp_at_index(eqlz,10,3)
    vlc.libvlc_audio_equalizer_set_amp_at_index(eqlz,10,4)
    vlc.libvlc_audio_equalizer_set_amp_at_index(eqlz,10,5)
    vlc.libvlc_audio_equalizer_set_amp_at_index(eqlz,10,6)
    vlc.libvlc_audio_equalizer_set_amp_at_index(eqlz,10,7)
    vlc.libvlc_audio_equalizer_set_amp_at_index(eqlz,10,8)
    vlc.libvlc_audio_equalizer_set_amp_at_index(eqlz,10,9) 
    player.set_equalizer(eqlz)

def play():
    player.play()
    print("Player play")
def stop():
    player.stop()
    
def play_pause():
    print("Player paused")
    player.pause()

def next_station():
    if(radio.current_station_no < len(radio.station_urls)-1):
         radio.current_station_no +=1
         print("Next station")
         print("Station " + str(radio.current_station_no)+" : "+ radio.station_names[radio.current_station_no])
         media = instance.media_new(radio.station_urls[radio.current_station_no])
         player.set_media(media)
         player.play()
         v.set(radio.station_names[radio.current_station_no])
       

def previous_station():
    if(radio.current_station_no >0):
     radio.current_station_no -=1
     print("prev station")

     print("Station " + str(radio.current_station_no)+" : "+ radio.station_names[radio.current_station_no])
     media = instance.media_new(radio.station_urls[radio.current_station_no])
     player.set_media(media)
     player.play()
     v.set(radio.station_names[radio.current_station_no])

     
def set_volume_up():
    if(radio.volume<100):
         radio.volume+=5
         player.play()
         player.audio_set_volume(radio.volume)
         print("Volume is: " + str(radio.volume))
        

def set_volume_down():
     if(radio.volume>15):
        radio.volume -= 5
        player.audio_set_volume(radio.volume)
        print("Volume is: " + str(radio.volume))
        
def bass_eq_up():
    if(radio.low_gain<20):
        radio.low_gain +=1
        set_equalizer()
        low_gain_level.set("Low Gain :"+str(radio.low_gain))
        

def bass_eq_down():
    if(radio.low_gain>-20):
        radio.low_gain -=1
        set_equalizer()
        low_gain_level.set("Low Gain :"+str(radio.low_gain))
       

def treble_eq_up():
    if(radio.high_gain<20):
        radio.high_gain +=1
        set_equalizer()
        high_gain_level.set("High Gain :"+str(radio.high_gain))
       

def treble_eq_down():
    if(radio.high_gain>-20):
        radio.high_gain -=1
        set_equalizer()
        high_gain_level.set("High Gain :"+str(radio.high_gain))
       

def set_equalizer():
    vlc.libvlc_audio_equalizer_set_amp_at_index(eqlz,radio.low_gain,0)  #31.25Hz
    vlc.libvlc_audio_equalizer_set_amp_at_index(eqlz,radio.low_gain,1)  #62.5Hz
    vlc.libvlc_audio_equalizer_set_amp_at_index(eqlz,radio.low_gain,2)  #125Hz
    vlc.libvlc_audio_equalizer_set_amp_at_index(eqlz,10,3)              #250Hz
    vlc.libvlc_audio_equalizer_set_amp_at_index(eqlz,10,4)              #500Hz
    vlc.libvlc_audio_equalizer_set_amp_at_index(eqlz,10,5)              #1kHz
    vlc.libvlc_audio_equalizer_set_amp_at_index(eqlz,radio.high_gain,6) #2kHz
    vlc.libvlc_audio_equalizer_set_amp_at_index(eqlz,radio.high_gain,7) #4kHz
    vlc.libvlc_audio_equalizer_set_amp_at_index(eqlz,radio.high_gain,8) #8kHz
    vlc.libvlc_audio_equalizer_set_amp_at_index(eqlz,radio.high_gain,9) #16kHz
    player.set_equalizer(eqlz)
    print("Freq: "+str(vlc.libvlc_audio_equalizer_get_band_frequency(0))+"hz Gain "+str(vlc.libvlc_audio_equalizer_get_amp_at_index(eqlz,0)))
    print("Freq: "+str(vlc.libvlc_audio_equalizer_get_band_frequency(1))+"hz Gain "+str(vlc.libvlc_audio_equalizer_get_amp_at_index(eqlz,1)))
    print("Freq: "+str(vlc.libvlc_audio_equalizer_get_band_frequency(2))+"hz Gain "+str(vlc.libvlc_audio_equalizer_get_amp_at_index(eqlz,2)))
    print("Freq: "+str(vlc.libvlc_audio_equalizer_get_band_frequency(3))+"hz Gain "+str(vlc.libvlc_audio_equalizer_get_amp_at_index(eqlz,3)))
    print("Freq: "+str(vlc.libvlc_audio_equalizer_get_band_frequency(4))+"hz Gain "+str(vlc.libvlc_audio_equalizer_get_amp_at_index(eqlz,4)))
    print("Freq: "+str(vlc.libvlc_audio_equalizer_get_band_frequency(5))+"hz Gain "+str(vlc.libvlc_audio_equalizer_get_amp_at_index(eqlz,5)))
    print("Freq: "+str(vlc.libvlc_audio_equalizer_get_band_frequency(6))+"hz Gain "+str(vlc.libvlc_audio_equalizer_get_amp_at_index(eqlz,6)))
    print("Freq: "+str(vlc.libvlc_audio_equalizer_get_band_frequency(7))+"hz Gain "+str(vlc.libvlc_audio_equalizer_get_amp_at_index(eqlz,7)))
    print("Freq: "+str(vlc.libvlc_audio_equalizer_get_band_frequency(8))+"hz Gain "+str(vlc.libvlc_audio_equalizer_get_amp_at_index(eqlz,8)))
    print("Freq: "+str(vlc.libvlc_audio_equalizer_get_band_frequency(9))+"hz Gain "+str(vlc.libvlc_audio_equalizer_get_amp_at_index(eqlz,9)))
def chose_input():
    print("Input changed to  local/radio")

def light_control_func():
    print("The light is this")
    

#Graphical User Interface:
window = tk.Tk()
window.geometry('600x900')
window.resizable(False,True)
window.title("Kristoffers Radio")


v = StringVar()
myLabel=ttk.Label(window, textvariable=v,padding=10).pack()
v.set(radio.station_names[radio.current_station_no])

high_gain_level = StringVar()
ttk.Label(window,textvariable=high_gain_level,padding=10).pack()
high_gain_level.set("High Gain :"+str(radio.high_gain))

low_gain_level = StringVar()
ttk.Label(window,textvariable=low_gain_level,padding=10).pack()
low_gain_level.set("Low Gain :"+str(radio.low_gain))


#GuiPlayButton:
gui_play_btn = ttk.Button(window,text="PLAY",command=play)
gui_play_btn.pack(ipadx=5,ipady=5,expand=True)
#GuiPauseButton:
gui_pause_btn = ttk.Button(window,text="PAUSE",command=play_pause)
gui_pause_btn.pack(ipadx=5,ipady=5,expand=True)
#GuiNextButton:
gui_pause_btn = ttk.Button(window,text="NEXT",command=next_station)
gui_pause_btn.pack(ipadx=5,ipady=5,expand=True)
#GuiPrevButton:
gui_pause_btn = ttk.Button(window,text="PREV",command=previous_station)
gui_pause_btn.pack(ipadx=5,ipady=5,expand=True)

#GuiVolButton_up:
gui_pause_btn = ttk.Button(window,text="VOL UP",command=set_volume_up)
gui_pause_btn.pack(ipadx=5,ipady=5,expand=True)
#GuiPrevButton:
gui_pause_btn = ttk.Button(window,text="VOL DOWN",command=set_volume_down)
gui_pause_btn.pack(ipadx=5,ipady=5,expand=True)

#GuiHighGainUpButton:
gui_high_gain_up = ttk.Button(window,text="High Gain Up",command=treble_eq_up)
gui_high_gain_up.pack(ipadx=5,ipady=5,expand=True)
#GuiHighGainDownButton:
gui_high_gain_down = ttk.Button(window,text="High Gain DOWN",command=treble_eq_down)
gui_high_gain_down.pack(ipadx=5,ipady=5,expand=True)
#GuiLowGainUpButton:
gui_low_gain_up = ttk.Button(window,text="Low Gain Up",command=bass_eq_up)
gui_low_gain_up.pack(ipadx=5,ipady=5,expand=True)
#GuiLowGainDownButton:
gui_low_gain_down = ttk.Button(window,text="Low Gain DOWN",command=bass_eq_down)
gui_low_gain_down.pack(ipadx=5,ipady=5,expand=True)

window.mainloop()
    

"""
while(1):

    if(radio.volume >200):
        print(radio.volume)


    #BUTTONS
    play_btn.when_pressed = play_pause #GPIO 27 
    pause_btn.when_pressed = play_pause
    stop_btn.when_pressed = stop
    toggle_local_or_radio.when_pressed = chose_input
    
    #ROTOR ENCODERS
    #Volume adjust
    volume_control.when_rotated_clockwise = set_volume_up #callback to set volume up
    volume_control.when_rotated_counter_clockwise = set_volume_down # callback to set colume down
    #Station change
    station_control.when_rotated_clockwise = next_station #callback to next_Station
    station_control.when_rotated_counter_clockwise = previous_station #callback to prev_station
    #Bass Equalizer
    bass_equalizer.when_rotated_clockwise = bass_eq #callback to next_Station
    bass_equalizer.when_rotated_counter_clockwise = bass_eq #callback to prev_station
    #Treble Equalizer
    treble_equalizer.when_rotated_clockwise = bass_eq #callback to next_Station
    treble_equalizer.when_rotated_counter_clockwise = bass_eq #callback to prev_station
    #Light controller
    light_control.when_rotated_clockwise = light_control_func

    """


# ToDo:
# #Bluetooth support
