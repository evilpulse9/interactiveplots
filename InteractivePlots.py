# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 20:58:20 2020

@author: thoma
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import math
import sys

plt.close('all')

initFrequency = 1.0

def sinc(x, frequency):
    omega = 2*math.pi*frequency
    return np.sin(omega*x)/x

x = np.linspace(-2*math.pi, 2*math.pi, 100)
fig, axl = plt.subplots(1) #Create new figure with one axis
plt.subplots_adjust(left = 0.25, bottom = 0.25) #move position of axes
axesHandle = plt.plot(x, sinc(x, 1.0), lw=2, color='green')

#add a slider
'''
def sliderCallback(val):
    localfrequency = sliderHandle.val #get the data from the slider
    axesHandle.set_ydata(sinc(x, localfrequency)) #reset y axis data
    fig.canvas.draw_idle() #redraw axes
    return fig, sliderHandle
ax2 = plt.axes([0.25,0.1,0.65,0.03]) #add new axes to the figure

sliderHandle = widgets.Slider(ax2, 'Freq', 0.1, 10.0, valinit=initFrequency)
sliderHandle.on_changed(sliderCallback)
'''
#add a button
plt.plot(x, sinc(x, 1.0), lw=2, color='green')
def clickCallback(event):
    
    color = axesHandle.get_color()
    
    if(color == 'green'):
        
    else:
        axesHandle.set_color('green')
    fig.canvas.draw_idle() #redraw axes
    return(buttonHandle)
#Find out what event is??

ax3 = plt.axes([0.1,0.75,0.1,0.1])

buttonHandle = widgets.Button(ax3, 'Foo')
buttonHandle.on_clicked(clickCallback)
'''
def clickCallback(event):
    
    color = axesHandle.get_color()
    
    if(color == 'green'):
        axesHandle.set_color('red')
    else:
        axesHandle.set_color('green')
    fig.canvas.draw_idle() #redraw axes
    return(buttonHandle)
#Find out what event is??

ax3 = plt.axes([0.1,0.75,0.1,0.1])

buttonHandle = widgets.Button(ax3, 'Foo')
buttonHandle.on_clicked(clickCallback)
'''
#add some keypress input
'''
def keyPressCallback(event):
    print(event.key)
    if(event.key == 'right'):
        axesHandle.set_ydata(sinc(x, 10.0)) #reset y axis data
    elif(event.key == 'left'):
        axesHandle.set_ydata(sinc(x, 0.1)) #reset the y axis data
    elif(event.key == 'escape'):
        plt.close('all')
    
    fig.canvas.draw_idle() #redraw the axes

fig.canvas.mpl_connect('key_press_event', keyPressCallback)
'''
plt.show(block=False)

