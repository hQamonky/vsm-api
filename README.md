# vsm-api

## Project Description

QMK Virtual Sound Mixer API is a REST API coded in Python that exposes commands to control a linux pulseaudio sound server.

## Get going with PyCharm

### Checkout project from GitHub

Open PyCharm and go to **VCS -> Get from Version Control...**  
Then, in GitHub tab, connect with your username and password and all your repos will appear.  
Select vsm-api, enter the desired directory path and click **Clone**.  

### Install Plugins

Go to **File -> Settings...**, and then **Plugins**   
Search for the following plugins and install them :  
- Markdown  
- Git Flow Integration  

### Configure Project Interpreter

Go to **File -> Settings...**  
Then to **Project: vsm-api -> Project Interpreter**  
Click on the drop-down list and click **Show All...**  
A window will appear with an empty space. Click on the **+**. Choose **Virtualenv Environment** and click **OK**. The environment will be added, click **OK**.  
Then click on the **+** from the base settings window. From there, install :  
- Markdown  
- Flask  
- Flask-RESTful  

### Add Configuration

Click on **Add Configuration...**  
Click on **+** on the top left. Select **Python**.  
If it doesn't detect it automatically, enter the path **run.py**.  
Click **OK**.
