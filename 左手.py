# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 15:26:29 2022

@author: b4100
"""


import numpy as np
import random


chord_c = [ "c", "e", "g","a"]
chord_f = [ "d", "f", "a" ,"b'"]
chord_g = [ "d","g","b" ,"c'"]
chord_e = [ "e","gis", "b" ,"d'"]

chord_am = [ "c",  "e","a","c'" ]
chord_dm = [ "d", "f", "a" ,"d'"]
chord_em = [ "e", "g", "b" ,"e'"]


def mutiNote(chord,num):
    if num==0:
        return chord[0]
    elif num==1:
        return chord[1]
    elif num==2:
        return chord[2]
    elif num==3:
        return "<"+chord[0]+" "+ chord[1]+">"
    elif num==4:
        return "<" + chord[0] + " " + chord[2] +">"
    elif num==5:
        return "<" + chord[1] + " " + chord[2] +">"
    elif num==6:
        return "<" + chord[0] + " " + chord[1] +" " + chord[2] +">"

def randomBeats( totalbeat, QuarterNote, TheAmountOfOutputBeats):
    nrandom=0
    num=0
    i=0
    beatssec=0.0
    nsum=0.0
    OutputBeats = [""] * 100
    
    
    beatarr=np.zeros(100)
    
    arr=[totalbeat / 1.0 , totalbeat / 2.0 , totalbeat / 2.0 + totalbeat / 4.0 , totalbeat / 4.0 , totalbeat / 8.0 , totalbeat / 16.0 ,totalbeat / 32.0]
    count=0
    while 1:
        for j in range(TheAmountOfOutputBeats):
            beatarr[j]=0
        nsum=0
        num=0
        
        while 1:
            if num > TheAmountOfOutputBeats:
                break
            nrandom = random.randint(0,QuarterNote) 
            beatssec = arr[nrandom]
            
            if nsum + beatssec <= totalbeat:
                nsum += beatssec
                beatarr[num] = nrandom
                num+=1
            
            if nsum == totalbeat:
                break
        
        if num == TheAmountOfOutputBeats:
            break
        if count>10000:
            return -77777777,OutputBeats
        count=count+1
    
    for i in range(num):
        n=beatarr[i]
        if   n==0:
            OutputBeats[i] = "1"
        elif n==1:
            OutputBeats[i] = "2"
        elif n==2:
            OutputBeats[i] = "2."
        elif n==3:
            OutputBeats[i] = "4"
        elif n==4:
            OutputBeats[i] = "8"
        elif n==5:
            OutputBeats[i] = "16"
        elif n==6:
            OutputBeats[i] = "32"
    
    return num,OutputBeats



def Chord(str,number):
    if   str=="c":
        return mutiNote(chord_c,number)
    elif str=="f":
        return mutiNote(chord_f,number)
    elif str=="g":
        return mutiNote(chord_g,number)
    elif str=="am":
        return mutiNote(chord_am,number)
    elif str=="dm":
        return mutiNote(chord_dm,number)
    elif str=="em":
        return mutiNote(chord_em,number)
    elif str=="e":
        return mutiNote(chord_e,number)
    return "exit"



def sort(N):   #0-N隨機排列
    arr=[0]*N
    for i in range(N):
        nout=True
        while nout:
            n=random.randint(0,N)
            nout=False
            for j in range(i):
                if arr[j]==n:
                    nout=True
                    break
        arr[i]=n
    return arr


def melody(chrd_arr,arraylength,Sent):
    bar=0
    note=0
    note_n=0
    sent=0
    
    for sent in range(Sent):
        r=0
        r=random.randint(2,3)
        '''
        if sent==0:
            r=random.randint(2,3)
        elif sent==1:
            r=random.randint(2,3)
        elif sent==2:
            r=random.randint(2,3)
        elif sent==3:
            r=random.randint(2,3)
        elif sent==4:
            r=random.randint(2,3)
'''
        #outputbeats=[""]*100
        num= -77777777
        
        while num == -77777777:
            num,outputbeats = randomBeats(4, 3, r)  #總拍子數    幾分音符    輸出幾個beats    OutputBeats[]
        
        
        chordarr=[0]*100
        for I in range(100):
            chordarr[I] =random.randint(0,5)
        
        
        for bar in range(arraylength):
            note_n = num
            for note in range(note_n):
                
                print(Chord(chrd_arr[bar], chordarr[note]),end="")
                #Chordstr= Chord(chrd_arr[bar], random.randint(0,5) )
                
                #if Chordstr=="rand":
                    #arr=sort(4)
                    #print("<",end="")
                    
                    #for note in range(note_n):
                        #print(Chord(chrd_arr[bar], chordarr[note])," ",end="")
                    #print(">",end="")
                #else:
                    #print(Chordstr,end="")
                
                print(outputbeats[note]," ",end="")
            print("\n",end="")
        print("\n\n",end="")
    
    print("c1",end="")
    return 0





    

def display(chrd_arr,arraylength, Sent):

    melody(chrd_arr, arraylength, Sent)
    


if __name__ == '__main__':
    chrd_arr = [ "c","g","am","em","f","c","dm","g"]
    length =len(chrd_arr)
    
    display(chrd_arr, length,5)
    
#a,b=randomBeats(4,6,8)  # 總拍子數    幾分音符    輸出幾個beats 