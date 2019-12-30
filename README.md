# GEOG5990 Assessment 1 
Programming for Geographical Information Analysts: Core Skills

Student ID: 201376715

Website: [gy19cp.github.io](https://gy19cp.github.io/index.html)

This animated agent-based model uses Sheep and Foxes within an raster grid environment. Sheep move, eat, share food with neighbouring Sheep and are unfortunately killed by Foxes. Foxes move and eat Sheep up to a specific food capacity. For a more detailed Model Summary click [here](https://gy19cp.github.io/model1summary.html) to be taken to the Webpage Model 1 in depth Summary.

### Model Files List
-	[Developer Model*](https://gy19cp.github.io/developermodel.py) - Recommended Model to download and run as it contains detailed explanatory comments, testing and debugging. 
-	[User Model](https://gy19cp.github.io/usermodel.py) - Basic comments.
-	[Agent Framework*](https://gy19cp.github.io/agentframework.py) - Code for Agents in the Model.
-	[in.txt*](https://gy19cp.github.io/in.txt) - Text file that contains the values for the Environment. 
- [License](https://github.com/gy19cp/GEOG5990Assessment1/blob/master/LICENSE) - GNU General Public License v3.0 agreement for the Repository code.
- [Pycache](https://github.com/gy19cp/GEOG5990Assessment1/tree/master/__pycache__) - Folder directory automatically generated by Python containing bytecode cache files. 

The __*__ indicates files are essential to download to run the model. 
These files download once selected. The in.txt file opens in the same tab so it is advised to open in a new tab or save the in.txt file, before selecting the back command to return to this page.

## Model Instructions 

**Step 1 -** Open Spyder (Anaconda 3). If you have not got this downloaded, it can be installed through the Anaconda Distribution [here](https://www.anaconda.com/distribution/). All code works with Python 3.7. Ensure when going through the installation process that you download ‘Spyder’. 

![Spyder Screenshot](SpyderScreenshot.jpg "Initiating Spyder")

**Step 2 -** Download the necessary files by clicking on the following hyperlinks - [User Model](http://gy19cp.github.io/usermodel.py), [Developer Model](http://gy19cp.github.io/developermodel.py), [Agent Framework](http://gy19cp.github.io/agentframework.py) and [in.txt](https://gy19cp.github.io/in.txt). All these files should be downloaded to the computers ‘Downloads’ folder. The User Model contains basic comments for ease for the user. The Developer Model version contains explanatory comments, testing, and debugging. 

**Alternative Step 2 -** Complete Step 2 above or this step, not both. Alternatively you can select this [Repository](https://github.com/gy19cp/GEOG5990Assessment1) hyperlink, which will take you directly to the Assessment 1 Repository within the GitHub website. Once in the Repository, select the green ‘Clone or download’ button (on the right side) and ‘Download Zip’. The files downloaded to the ‘Downloads’ folder this way will need to be ‘extracted’ before they appear as individual files as shown below. Both Step 2 methods are effective and up to personal preference.  

![DownloadsScreenshot](DownloadsScreenshot.jpg "Downloads")

**Step 3 -** Once downloaded, open Spyder and open the Agent Framework file and the selected Model (either the User/Developer version). 

**Step 4 -** Have the ‘agentframework’ file selected within Spyder and click the green right-pointed arrow to ‘Run’ it.

![AgentFrameworkScreenshot](AgentFrameworkScreenshot.jpg "Agent Framework")
  
**Step 5 -** Now select the ‘model’ file within Spyder and click ‘Run’ again. This time a box entitled ‘Model’ should pop out. Click the subheading ‘Menu’ and ‘Run Model’. 
 
![RunModelScreenshot](RunModelScreenshot.jpg "Run Model")
 
## Model Expectations 
When the model is run, the orange dots represent ‘Foxes’ and the white dots represent ‘Sheep’. When a Sheep is killed by a Fox, the coordinates of where it took place is printed in the IPython Console. Where grass has been eaten, dark squares/pixels are shown. The darker the square/pixels, the more the grass has been grazed by multiple Sheep. This model will run until the Agents (Sheep) Food Store Capacity is met or until a specific number of steps (‘num_of_iterations’) has been completed. 

## Potential Issues
- A strong internet connection is required as the web scraped html file for the Foxes movement will not work without an internet connection. The HTTPConnectionPool error will show if the internet is not connected.
- It is recommended to open the Model on a Windows Operating System. However, when doing so a pop up box entitled 'Figure' will appear alongside the 'Model' box. This is a preknown issue that occurs with Windows. This Figure box is not used. To close the Model fully before potentially rerunning the Model again, both the Model and the Figure box need to be closed and the red square in the IPython console selected (if it is not already greyed out).

## Future Developments
- Other predators could be added (e.g. Wolves).
- A survival of the fittest/best adapted Sheep could take place using a range of possible functions including 'wolf_hunt', 'chase' and 'sheep_fitness' (after a number of iterations the Sheep would be exhausted and possibly be eaten).

## Final Points
I do not condon any form of animal cruelty. This model was only to represent skills developed following the [Programming for Geographical Information Analysts: Core Skills module](https://www.geog.leeds.ac.uk/courses/computing/study/core-python/) as part of an MSc GIS from the University of Leeds. 
