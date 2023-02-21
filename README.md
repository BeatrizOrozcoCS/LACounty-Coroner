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




# Step 3: Get all the Case deatils
This is a very structed websites that uses an api. Every case has the same number of objects to read. Using selenium we can go through all the cases and extract case information using the api seen from inspecting the webpage.
Data:
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

For instance Place of death can include many ways of saying hte same thing. WE can normalize indoors vs outdoors, make the following: *Freeway, * FreeWay - Off Ramp, * FreeWat - On Ramp 
into -> Freeway

# Step 5: Visulize Trends  
Once we have an excel sheet with all the information, we can start using visulization tools like tableu, PowerBI, python libraries to start visualizing trends and seeing patterns.  
