# LACounty-Coroner (Incomplete)
Data visualization project using LACounty-Coroner data from thier public websites
<br />
### Still filling out the Readme and Respository.
# Why make this project
This project was inspired by LA Times Homicide Report. https://homicide.latimes.com/ <br />
It made me realize that many people die in an area and it is not mentioned in the news and I wanted to bring awareness to myself of all the lives lost. 

The end goal of this project is to show people how I used Selenium to traverse the website and get information.
# Things to Note
This project is only data from people processed by the LA County Medical Examiner Office so it is simply a portion of all the deaths that happend in LA County. 

### LACounty-Coroner Website:
There are three websites to get data from. <br />
https://mec.lacounty.gov/case-search/<br />
https://mec.lacounty.gov/unidentified-persons-search/<br />
https://mec.lacounty.gov/unclaimed-persons-search/<br />

# Step 1: Go and Inspect the Website
Learn more about the website and see patterns and hows its formatted. First thing to note is that you can manipulate the 


Second thing to note is that if you know all of the case numbers you can go trhough the deatils of each case from the url. (Base url + casenumber) -> case details
![image](https://user-images.githubusercontent.com/51274827/184560486-06df2d87-4a71-44f8-9ca0-c13dd9f7a21d.png)
![image](https://user-images.githubusercontent.com/51274827/184560506-4d3a9860-5d1c-4bc9-b544-ae2bf140d9c7.png)


# Step 2: Get the Case Numbers (Not fully automated yet - to be added at a later date)
Looking at the selenium 
![image](https://user-images.githubusercontent.com/51274827/184560847-ec12809e-4ed2-49a1-9bec-29b3935ad044.png)


# Step 3: Get all the Case deatils
This is a very structed websites and every case has the same number of objects to read. Using selenium we can go through all the cases and extract case information:
* CaseNumber
* CaseStatus
* BodyStatus
* Gender
* Ethnicity
* PlaceofDeath 
* Manner
* Investigator
* DeputyMedicalExaminer
* CauseA 
* CauseB
* CauseC 
* CauseD 
* OtherSignificantConditions

The overall goal is to grab all this informaiton and export it to an excel sheet. 

# Step 4: Clean up data
After extracting all the data its important to transform the data to optimize its useage. For isntance cleaning up can include getting rid of trailing and leading spaces or just normalizing results. 



# Step 5: Visulize Trends  
Once we have an excel sheet with all the information, we can start using visulization tools like tableu, PowerBI, python libraries to start visualizing trends and seeing patterns.  
