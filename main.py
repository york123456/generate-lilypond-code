# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 19:53:05 2022

@author: b4100
"""

import 左手
import 右手

chrd_arr = [ "c","g","am","em","f","c","dm","g"]
length =len(chrd_arr)

print('''
\\header {
  title = "Untitled"
  composer = "Composer"
}

\\score {
  <<
  \\new Staff { \\clef "treble" \\key d \\major \\time 4/4 
               \\tempo 4 = 160
      ''')

右手.display(chrd_arr, length,5)

print("""
      }
\\new Staff { \\clef "bass" 
      """)

左手.display(chrd_arr, length,5)

print("""
      }
>>


  \\layout {}
  \\midi {}
}
      """)