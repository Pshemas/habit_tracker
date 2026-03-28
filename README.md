# Habit Tracker - with Raspberry Pico 2W

Track and update your habits stored in Pixela graph using Raspberry Pico.

This project has been created as a part of "introduction to working with Pico" workshop. Device built with Pico 2W and Waveshare 0.96" screen. Uses Pixela (https://pixe.la/) as online data storage.

Power on your device, wait till it connects to wifi. After completing some task you wish to track via Pixela service click the bottom right button - device will send the data to Pixela and the colored square will appear to mark your progress. Use the joystick to check details of your progress in the past 5 days.

Requires filling `.pixela` file with Pixela account / graph settings and `.wifi` with wifi details (SSID and password).

Requires downloading sample project for Waveshare screen (<https://files.waveshare.com/wiki/common/Pico_code.7z>) . The code for managing the screen from the extracted archive should be saved as `LCD_0inch96.py`.

The code is not meant to be pretty - and definitely needs improvement. It was created with having a clean `main.py` file in mind - workshop participants during one of the stages try to come up with steps needed to fulfill the task and we compare it with provided code, not getting into details how some of the functions / classes implement needed functionality.

The code is meant as an inspiration and a starting point. At the end of the educator shares some of the ideas how the code can be improved / extended.

Currently ui messages are hardcoded in Polish - but they are easy to find and change (it is extremely simple device). At one point I may introduce some multilingual capabilities.

# Device case - step files

`case_step` directory contains archive with models for the case. Full assembly requires short M3 inserts (external diameter 4.2mm) and 12mm M3 screws.

# Assembly

- mount heated inserts into the holes in the top part of the case
- glue the smaller buttons to the top part of the case
- put screen and pico together and place it in the bottom part of the case
- place joystick button cap on the joystick
- place top part of the case and use M3 screws to screw assembly together

If the pico with screen is a bit too loose you could add some tape on the feet that push screen into pico (on the top part of the case).

![Mounting inserts](img/habit_tracker_inserts.png)
![Putting pieces toghether](img/habit_tracker_assembly.png)
