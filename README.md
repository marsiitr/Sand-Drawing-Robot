# Sand-Drawing-Robot
**Srishti 2020**
## Abstract

The aim of this project is to draw a clear and neat structure of any image in sand given with maximum accuracy level.


 ![image](/Images/sdr.jpg)

## Motivation:
<p align="justify">
Even in this fast and busy world  we see huge crowd in beaches.And most of the people often write their names in the sand on the sea shore with a stick or so.We also see most of the social account profiles with a photo of them which is drawn on a paper or sand or something else.This shows that people are more interested in these drawings on paper or sand than the original photo of theirs.We also see many abstract painters and also their customers who are interested to get their painted photo.But they draw on a paper which is quite comfortable.We rarely see those who paints on sand which is a bit difficult compared to that of paper.So,we planned  to prepare a machine (a bot) which can draw a given image on sand and also which can be carried easily.It can be kept in a suitcase and we can take it wherever we want.</p>

## Components:
1. 2 stepper motors
2. 1 servo motor
3. 1 Arduino mega
4. Jumper wires 
5. 4 linear motion bearings
6. 1 6mm timing belt
7. 2 20teeth pulley 5mm bore
8. 2mm and 3mm nuts and bolts

## Workflow:

![worflow](/Images/WORKFLOW.png)

## Mechanical Aspects:
* The bot itself doesn’t move but the shaft of the bot moves vertically.
For this we are using a stepper motor which inturn is connected Arduino which is powered by a 12v dc motor or an adapter.
* We use 2 steppers in this bot ,one to move the shaft and the another to move the servo motor on the shaft.
This servo motor is connected to a stick in such a way that if servo motor rotates by certain angle then the stick turns upside down.
* For the stability of the bot we use cardboard pieces on the bottom.
Actually stepper motor moves along the shaft, shaft is still
* We use a big cardboard for the sand and there are 3d prints to hold the shaft tightly
* We use timing belts and timing pulley for the movement of motors. To maintain the accuracy of the movement of timing belt ,it is held tightly between two 3d printed rectangular box.

## Electronic aspects of the design:

### Micro controller :
<p align="justify">
Arduino mega is used.It is one of the most important compnents used to make sand drawing robot.Arduino code in this micro controller helps the servo motor rotate according to the pixels of the pixelated image.It also helps the stepper motor to move the shaft vertically and to slide the servo motor horizontally on the shaft. Basically this gives main connection to the pixelated image and the mechanical motors. The power supply for this board is given by 12v battery or an adapter.
</p>

### Actuators :

<p align="justify">
1 stepper motor moves on the shaft horizontally.
Another stepper motor is is used to move the servo motor horizontally on the shaft'
1 servo motor is used to turn the stick up and down to draw lines on the sand.
1 L2983D motor driver is also used.</p>

### Power :
12v battery or an adapter is used to power the arduino, the main component of the project.

## Cost structure:
Components | Cost(INR)  
-----------| ---------  
2 Timing belt and pulleys | 910   
4 Linear bearings | 948     
Wooden cardboard | 200     
8mm brass rods | 640     
Nuts, bolts,jumper wires | 250     
Miscellaneous | 200     
Total | 3148       
## Applications:
<p align="justify">
**Beaches** - on sand we can draw one’s picture.

**In any malls or tourism places** - we can draw pictures on sand instead of paper
</p>

## Limitations:
Time taken to draw a picture is very high
## Future Improvements:
We can use more servo motors to draw a given picture so that the time taken will be less.
We can also increase the roatation of servo motor and decrease the delay to speeden the drawing.

## Team members:
                        

 
 1. [Sejal Agarwal](https://github.com/sejal-ag)    
 2. Kavya Reddy   
 3. Vishal Gusaiwal  
 4. Zoaya Zahoor   
 5. [Ravina Bishnoi](https://github.com/ravinab29)  

## Mentors:

1. [Shubham goyal](https://github.com/shubham491981)    
2. Naveen chandra rai
