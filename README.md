# DailyParking - An Automated Guest Parking Registration Script

DailyParking is a Python script that automatically submits your car information for guest parking registration with a single click! After successful registration, the script will also email you the confirmation code from the registration website. 
In order to make the script run daily, I utilized cron in Linux. 

![](https://github.com/kjohnson8781/DailyParking/blob/main/DailyParkingPresentation.gif)

## Installation

1. Install [geckodriver](https://github.com/mozilla/geckodriver/releaseshttps://github.com/mozilla/geckodriver/releases)
  * Unzip File

  * Copy .exe file into python parent (ex. C:\Python34)

2. Install selenium: ```pip install selenium``` 

## Usage

1. Input User Information
  * Property Name
```python
property = " "
```
  * Apartment Number
```python
aptnum = " "
```
  * Car Make
```python
make = " "
```
  * Car Model
```python
model = " "
```
  * License Plate
```python
lp = " "
```
  * Email
```python
email = " "
```
2. Run ```$ python DailyParking.py```
3. The script will open Register2Park and begin entering information.

## To run automatically in Linux
1. Open Linux Terminal
2. Run crontab -e
3. To run code daily at 5 PM ```0 17 * * * /usr/bin/python3 /home/Documents/DailyParking.py >> cron.log 2>&1``` (Note: Change scheduler modifier and file location for your needs)
4. Cron will write errors to the cron.log output if any occur but otherwise should be empty
5. You should get an email confirmation code when the code runs at your specified time!

## Inspiration
I have guests come over to my apartment a lot and it's hard to remember to register them. If I forget, they are at risk of being towed. I wrote this bot so I don't have to worry as much about remembering. I learned a lot about HTML code and selenium, especially how to wait until an element exists. I dove into Linux in order to write the cron code and am working on writing a bash script to run the code daily as well!
Special thanks to Selenium and cron for making this script possible. 

## License
[MIT](https://choosealicense.com/licenses/mit/)
