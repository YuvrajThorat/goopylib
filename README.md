# Goopy

## Introduction
Goopy is a simple-yet-powerful 2D graphics framework built on top of Tkinter capable of creating good-looking, modern GUIs, games, and simple animations.

This graphics library is built upon John Zelle's graphics.py package which he made for use with his textbook "Python Programming: An Introduction to Computer Science". Over the past 2 years, I have worked on editing this library to add more featurs to use with making my GUIs and games. My entire aim while editing was to create a powerful medium to enable me to create good-looking graphics within Python and I have spent a lot of time making sure this is the case. Thus, this is a very intuitive, simple to use package with the potential of growing into one of the best Python Graphics Libraries. 

If you would want to contribute to this library by suggesting features, reporting bugs, or adding changes yourself, please do so. I would love it if you would use this library in your projects and do make sure to tell me about them! Right now, this is very much an alpha stage - there are many bugs, many features that aren't compatible with each other, and a ton of things to do differently, but hopefully this can all be fixed with future releases. 

If you want to contact me, you can drop me an email at: bhavyemathur@gmail.com or post an issue on the issues tab.

### Installation

This library is very simple to use, all you need is the folder called 'goopy.py' and the requirements mentioned in the requirement.txt file. These include the Pillow (PIL) and the keyboard modules which you can download individually or clone this repository and in that directory execute:

```sh
python3 -m pip install -r requirements.txt
```

Now, wherever you need access to the library, simply import as so:

```python

from goopy.imports import *
# or
import goopy as gp

```

The first allows you to import everything that is part of the library, but if you want only specific classes & functions, read on. 

### Organization

Goopy is organized into a few different files and depending on what you want to do, you can import these files. There are 2 subfolders in goopy: math & objects. The objects folder contains all of the graphics objects you might want to use like Images, Rectangles, Buttons, etc. To import these, type:

```python
from goopy.math.BezierCurve import BezierCurve # The other sub-packages are 'Interpolation', & 'BSpline'
# or
from goopy.objects.Rectangle import Rectangle  # For a list of graphics objects, look at the documentation
```

To access elements of Goopy like the Point & GraphWin classes, Colours, etc. use this:

```python
from goopy.colours import *

from goopy.GraphWin import GraphWin
from goopy.Point import Point
```

### Documentation

There are plans to create a detailed documentation for this library both in the form of YouTube videos and a written document, however, there is not such documentation right now.

### Projects made using Goopy

As these are entire projects, I have not supplied the code for these. If you want to look at example projects with code, skip to the next section 'Examples'. 

**1. A Pac-Man Recreation**

I worked on this as a school project and used the goopy library to fully functional Pac-Man Game! (and an arcade too) Pac-Man runs around while the ghosts (all animated of course) chase after him! He must collect all the pellets and fruits to go on to the next level.

![Pac-Man Screenshot](https://github.com/BhavyeMathur/goopy/blob/master/Examples/Pac-Man.png)

**2. Multiplayer UNO**

During the COVID-19 Pandemic, my friends and I often hopped on a call and played a few games together: one such, was UNO. But the app we used was very laggy and didn't really function well. So I took it upon myself to create a Multiplayer UNO game in 5 days or less - and I succeeded on day 6... *"but day indices start at 0 so it was really the fifth day..."*. 

The game allows 2-7 players to play together and the graphics animate the cards, rotate them randomly, make them travel to the centre (as opposed to just instantly moving there) and more.

Here is a screenshot of the game:

![UNO Screenshot](https://github.com/BhavyeMathur/goopy/blob/master/Examples/MultiplayerUNO.png)

Avatar graphics are from freepik.com

**3. Activity Club Selection App**

My school has these weekly activity clubs where we all go to well, do activities. And every year, we sign up for activities using a pen & paper. Writing down our choices, handing them over to our teachers and waiting for them to sort through hundreds of entries and assign everybody a club - but not this year. This year I made an activity club selection app using the goopy library that would automatically do all this work for you! 

Goopy is compatible with auto-py-to-exe which means you can easily convert any program into a .exe file and mail it to anyone to use. Now mind you, this was made with an older version of Goopy so it did not contain lots of animations and visual feedback, but here is a screenshot:

![Activity Selection App Screenshot](https://github.com/BhavyeMathur/goopy/blob/master/Examples/ActivtySelectionApp.png)

### Examples

These examples with the code and required textures are included in folders for you to download and try out for yourselves!

1. This is a simply, modern, light Login Page that can be used for your application. It demonstrates the usage of Checkbox, Entries, and Buttons to take input from the user and was made entirely with just 60 lines of code! (excluding comments). 

This includes giving the user visual feedback if they hover over a button, making sure the user has entered a valid input, a functional tab to change from registering to signing up, and more.

![GUI Screenshot](https://github.com/BhavyeMathur/goopy/blob/master/Examples//ModernUI-LoginPage%20Example/ExampleScreenshot.png)

2. Also provided is a very simple animation of Pac-Man being chased by some ghosts and it was created with just 40 lines of code! This really is an example of how simple animations such as these can help make a really good game or project. 

Goopy also has functionality for other animations such as moving to locations, rotating animations, and a lot to come soon. I am planning to include animations for almost every attribute of a Graphics Object like size, colour, outline thickness, transformation (skewing, fliping, etc.) and more. It also contains easy-to-use easing functions like those you would find in a professional animator.

![Pac-Man Animation Example](https://github.com/BhavyeMathur/goopy/blob/master/Examples/Pac-Man-Animation%20Example/Pac-ManAnimation.png)


## Contributions

1. Reblochon Masque, https://stackoverflow.com/questions/62715279/creating-rounded-edges-for-a-polygon-in-python - 3rd July 2020 - Help with creating rounded polygon corners
2. Spectral Doy - 3rd July 2020 - Helping me choose a name! we went through a lot of options... pyraphics, oreopy, pyllustrate, guipy... barnacle...
3. John Zelle - Creating the graphics.py package which formed the basis for my library.
4. Nico Schertler, https://stackoverflow.com/questions/62738195/python-zerodivisionerror-in-open-uniform-b-spline-curve - 4th July 2020 - Helped fix a ZeroDivisionError with Open Unifrom B-Splines
5. Bryan Oakle, https://stackoverflow.com/questions/62740726/tkinter-polygons-width-not-being-set-to-zero-even-though-specified/62741739#62741739 - 4th July 2020 - Helped fix bug with Polygons drawing their outlines even though the width is 0 
6. 

## Version History

### v1.0

#### 1.0.0-alpha to 1.0.1-alpha - 6th July 2020

* Added move_to(), move_to_x(), move_to_y(), move(), move_x(), and move_y() functions to the GraphWin class to move a window on the screen
* Added seperate Cursor Lists for All, Windows, & Mac OSx 
* Expanded the Cursor List to include all available cursors
* Added a Cursor Dictionary to reference the Cursors with more intuitive names like 'up-down arrow' rather than 'sb_h_double_arrow'

* Added Closure functions for all the interpolations so that the user can 1. Get a value of the interpolation, or 2. Get the function with predifined parameters other than time for use in animations internally

### v6.11-dev

#### 6.11.11 to 6.11.29 to 1.0.0-alpha - 4th-5th July 2020

* Added a callback function to the Entry object which will allow for features like controlling what text the user can type in there, prompt text, etc.
* Added a promptText attribute to the Entry which displays text before the user has typed and disappears when he/she starts typing
* Added a new style key 'entry width' which deafults to 0 to make Entries look better with less manual configuration
* Entry now raises and error if you try to getText() when it is not drawn, or the GraphWin is closed

* Added a set_enabled() and toggle_enabled() function for Buttons

* Point adding & setting functions don't mutate the point itself now, instead they return a clone of the point with the operations performed
* Added a getState() function to the checkbox which returns its current state

* Added functions for finding Bezier Curves, Bernstein Polynomials, & 'nCk' (combinations) to create better curves
* Added Open & Closed Uniform B-Spline curve functions
* Added a Rational Bezier Curve Function for weighted Curves

* Fixed Bug with Polygon drawing outline even though the width is specified to be 0
* Fixed Bug with an error being caused if you rotated more than 180 deg. (Any angle (deg) whose sin < 0)
* Fixed os.isfile() reference to os.path.isfile()
* Fixed GraphWin self.Closed() references to self.isClosed()
* Fixed Misc Bugs & Naming Issues
* Fixed Line set arrow functions

* Split Goopy into multiple files! 
* Renamed everything to follow Python Convention! (These 2 things took a lot of time...)

* Renamed the GraphicsObject update functions to be non-protected 
* Made everything in Goopy abide by the PEP 8 standard

#### 6.11.0 to 6.11.10 - 3rd July 2020

* Removed the Image_depr class which was used as a backup until the new class using the Pillow library was created
* Removed the ToDos, Version History, and Introduction from Goop.py and moved it to the README file

* Closed issue regarding adding new colour formats after adding Hex & CMYK support in v6.10
* Fixed the GraphWin's setBackground() function to work with colours referencing a style
* Fixed bug with the GraphWin not referencing the global style properly

* Warning added to warn the user if they are both calling the updateWin() function manually and the autoflush of the GraphWin is set to True
* While resizing a rectangle, you can set the min. width & height beyond which, the rectangle cannot be resized 
* A GraphicsError is now raised if the minWidth & minHeight arguments of the setResizable() function are < 1

* The Rectangle class now draws a rectangle using a polygon rather than directly to allow for rounded edges
* Removed the RoundedRectangle class and built its functionality into the Rectangle class

* Added Errors to the setStyle() function & GraphWin class to make sure the user has entered the correct arguments


### v6.10-dev

* Points are no longer graphic objects
* Custom Support for Cursors on the GraphWin & _BBox classes
* Added support for colour palettes and added 3 style: default, pycharm darcula, and intellij
* Added Assertions to the graphics objects to give better error statements
* Added Config functions for all configurations for the Graphics Window class
* Added circular and ovular bounding boxes
* Added setObjectWidth & Height functions as well as _BBox object resizing functions
* Bounding boxes are now represented by graphics objects (_BBox objects)
* Fixed bugs with using the mouseEvent functions returning None value and added the refresh argument
* Fixed Bug with Graphics Objects resizing when resizing the window
* Fixed bug with background not filling colour of the entire region of window (not only the seen region)
* Tested the graphics window class
* Organized code in the GraphWin
* More colour definitions!
* ColourHex, ColourCMYK, and ColourRGB classes added

* Changed Version History dates from mm/dd/yyyy to dd/mm/yyyy

### v6.9-dev 31/5/2020
* Added argument assert statements to the Graphics Window class
* Added a colour class
* Changed all references of 'Color' to 'Colour'

### v6.8 17/5/2020
* Added a window parameter to every Graphics Class that allows the user to draw the window in the class declaration
* Added more functions to set the Arrow of a line
* You can now set the arrow of a line inside the __init__ function
* Removed all the sound functions
* Added TODOs

### v6.7-dev 25/4/2020
* The Image Object now uses the Pillow (PIL) library which gives the user far more ways to manipulate the object
* Added the ImageGrp class to Group Images together
* Added RadioButtons, & CycleButtons
* New & Improved functions to the GraphWin including the ability to resize the window!
* Added Glide & GlideTo functions with easing to animate objects!

### v6.6-dev 24/11/2019
* Added a few more colour definitions
* Image scaling functions (zoom & resize) now return the image class & don't require the image to have been drawn
* Added ButtonPressed attributes to the GraphWin class to have more variety in mouse events
* Added a moveTo function for BBox classes
* Made the CheckBox class much easier to work with
* Various bug fixes

### v6.5-dev 16/9/2019
* Added Right, Left and Middle click events to the GraphWin class
* Changed GraphWin getKey() and checkKey() functions to use the keyboard library instead of tkinter
* Added checkForKeys() function to GraphWin to check for Multiple keys at once
* Added attribute setting functions for SlideBar class
* Fixed bug of SlideBar class not functioning when p1.(x or y) > p2.(x or y) - x or y depending on orientation

* Added isClicked() function for points and lines
* Added isSelected() function for all GraphicObject children Classes
* Added enabled, disabled and read only states to Entry Class and added many more functions

* GraphicsObject objects now return themselves when the draw() function is called to allow the user to create and
draw an object with 1 line of code
* Added playSound function which plays music

### v6.2-dev 12/9/2019
* Fixed Bug of Line class not drawing due to error
* Fixed Bug of the Graphics Objects' undraw() function not undrawing
* Added SlideBar class
* Added a function to get the Mouse Scroll value to graphwin
* Removed restrictions on text fonts and size allowing user to use whatever values they want
* Added a very basic rectangular Button class

### v6.1-dev 29/8/2019
* Checkboxes added as a class
* Button class added
* Fixed bug with isClicked() function that didn't work when x1 > x2 or y1 > y2
* Added more Fonts

### v6-dev 15/7/2019
* added moveTo() function for all graphics objects to specify x & y variables rather than dx & dy
* added more parameters for classes to customize them during creation rather than using multiple functions
* Defined multiple variables containing colour information to use when colouring object
* added more fonts for text objects to use
* Implemented a new error for missing values
* Added isClicked() function for Image and BBox objects
