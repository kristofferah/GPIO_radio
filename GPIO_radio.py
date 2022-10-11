#!/usr/bin/python

from gpiozero import Device, LED, Button, RotaryEncoder
import vlc
import json



#GPIO Setup

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

eqlz = vlc.AudioEqualizer 
player.set_equalizer(eqlz)
libvlc_audio_equalizer_release()

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
     radio.current_station_no -=1
     print("prev station")

     print("Station " + radio.cur
     media = instance.media_new(radio.station_urls[radio.current_station_no])
     player.set_media(medi
     player.play()
         
def set_volume_up():
    if(radio.volume<100):
         player.set_media(media)
         player.play()
         
print("Volume is: " + str(radio.volume))
        

def set_volume_down():
     if(radio.volume>15):
        radio.volume -= 5
        player.audio_set_volume(radio.volume)
            
print("Volume is: " + str(radio.volume))
        
def bass_eq():
    print("This is the bass")
    
def treble_eq():
    print("This is the treble")

def chose_input():
    print("Input changed to  local/radio")

def light_control_func():
    print("The light is this")
    
    
while(1):
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
    
# ToDo:
# #Bluetooth support
