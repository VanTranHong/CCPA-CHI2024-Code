# CCPA-CHI2024-Code
This repository is used to measure the presence of the CCPA opt-out link

Here are steps required to set up this repository

1. Have Google Chrome installed: if not, please download one
2. Check which Google Chrome version you are using: by open Google Chrome -> About Chrome -> check the version
3. Download the Chromedriver compatible to the Google Chrome version you are using
Go to https://developer.chrome.com/docs/chromedriver/downloads and select the compatible version
4. After download the google chrome version, please drop the chromedriver to the folder "./Automate_crawl_web/"
5. Install all required libraries by running "pip install -r requirement.txt"


Here are steps required to run the experiment
1. Use VPN and change to the location you want
2. Change line 24 in file run_experiments.txt to change name of the folder you want to save to (according to the location you measure)
3. If you are using a Mac, change line 25 in run_experiment.txt to "command", if not, change to "ctrl"
4. Change line 26 to be the filename contain the list of websites you want to test
5. run "python3 run_experiments.txt"