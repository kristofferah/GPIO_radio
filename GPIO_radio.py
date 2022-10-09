#!/usr/bin/python

from gpiozero import Device, LED, Button, RotaryEncoder, MCP3008 #MCP3008 er ADCen

from gpiozero.tools import scaled_half

import vlc

import json


#GPIO Setup

button1 = Button(27) #This button is connected to GPIO17 (Not pin 17)
#button2 = Button(22) #This button is connected to GPIO27 (Not pin 27)
#button3 = Button(4)
rotor = RotaryEncoder(4,22,None,1,(-1,1),False)



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
        self.volume = 30

radio = Radio() #Make an instance of Radio


#Setting up the player
instance = vlc.Instance('--input-repeat=-1','--fullscreen')
player = instance.media_player_new()
media = instance.media_new(radio.station_urls[0])
player.set_media(media)
player.audio_set_volume(radio.volume)
player.play()



def play():
    player.play()
    

def stop():
    player.stop()
    

def play_pause():

    print("Player paused")
    player.pause()


def next_station():
    

    if(radio.current_station_no < len(radio.station_urls)-1):
         radio.current_station_no +=1

         print("Next station")
         print(radio.station_names[radio.current_station_no])

         media = instance.media_new(radio.station_urls[radio.current_station_no])
         player.set_media(media)
         player.play()
    

    

def previous_station():
    

    if(radio.current_station_no > 0):
         radio.current_station_no -=1

         print("prev station")

         print("Station " + radio.current_station_no +" " + radio.station_names[radio.current_station_no])

         media = instance.media_new(radio.station_urls[radio.current_station_no])
         player.set_media(media)
         player.play()
         
def set_volume_up():
    if(radio.volume<100):
        radio.volume += 5
        player.audio_set_volume(radio.volume)
        print("Volume is: " + str(radio.volume))
        
def set_volume_down():
    if(radio.volume>15):
        radio.volume -= 5
        player.audio_set_volume(radio.volume)
        print("Volume is: " + str(radio.volume))
        

while(1):

    button1.when_pressed = play_pause #GPIO 27 #No function call(), but assigning the "when pressed" to this function

    #button2.when_pressed = next_station #GPIO 22

    #button3.when_pressed = previous_station #GPIO 4

    rotor.when_rotated_clockwise = set_volume_up #next_Station
 
    rotor.when_rotated_counter_clockwise = set_volume_down # prev_station


#todo:
# Make all the buttons
# IncludeBluetooth support

