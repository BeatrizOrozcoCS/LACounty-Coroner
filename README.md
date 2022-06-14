# LACounty-Coroner (Incomplete)
Data visualization project using LACounty-Coroner data from thier public websites
<br />
### Still filling out the Readme and Respository.
# Why make this project
This project was inspired by LA Times Homicide Report. https://homicide.latimes.com/ <br />
It made me realize that many people die in an area and it is not mentioned in the news and I wanted to bring awareness to myself of all the lives lost. 

The end goal of this project is to show people how I managed to webscrape data from a difficult webpage that uses JQuery to populate thier fields and 
to show what I was able to find and how I am progressing in my project. 

# Things to Note
This project is only data from people processed by the LA County Medical Examiner Office so it is simply a portion of all the deaths that happend in LA County. 

### LACounty-Coroner Website:
There are three websites to get data from. <br />
https://mec.lacounty.gov/case-search/<br />
https://mec.lacounty.gov/unidentified-persons-search/<br />
https://mec.lacounty.gov/unclaimed-persons-search/<br />

# Step 1: Go and Inspect the Website
For this read me example we will use the link: https://mec.lacounty.gov/case-search/<br />

![image](https://user-images.githubusercontent.com/51274827/173214058-ef33c0e7-2aa3-4a13-8c65-0cc879e40d0f.png)<br />

### Inspect the elements you want. <br />
Locate a common element name or container id, class<br />

![image](https://user-images.githubusercontent.com/51274827/173214919-2ae59c8b-e830-494a-9c52-83940a2f42a2.png)<br />
![image](https://user-images.githubusercontent.com/51274827/173214720-04283cc1-aa4a-46b4-8979-23afba726312.png)<br /> 
![image](https://user-images.githubusercontent.com/51274827/173214885-d0e50742-6c8d-4853-95b2-6063cc1e5142.png)<br />

In this case all of the relevant data is under the class container name "row caseList" and each individual data container has the same class name "col-xs-12 col-sm-12 col-md-12 col-lg-12"
<br />

### Keep inspecting

##### First bad sign is that the url does not change with going to the next page
Page 1
![image](https://user-images.githubusercontent.com/51274827/173214161-93f1f79c-ff48-4f6c-a188-34bc06a4d7fb.png)<br />

Page 5
![image](https://user-images.githubusercontent.com/51274827/173214171-dda8fbc5-36c7-4cd1-8a16-c270c667cc14.png)<br />

![image](https://user-images.githubusercontent.com/51274827/173214204-68f33c40-1f75-424c-a6d4-c25789860ca2.png)<br />

And if you look inspect the button element there is no reference to another link it just says value. 
After looking at that and also seeing how the data changes as we move to the "next page" I was able to saely deduce that there is a JQuery. 
I confirmed it with going to the Network Tab and seeing that there was a JQuery script running on this webpage. 

![image](https://user-images.githubusercontent.com/51274827/173215122-aea7b85d-02e6-4e30-9fba-1f81b97299c2.png)

# Step 2: 
 
# Step 3: 

# Step 4: Data Cleanup using Python
After manually Copying and Pasting all that information onto an excel sheet, you now have over 700,000 rows of data
### know your data
In this data, every container of persons should have 5 rows of data assciated with them. The importance of knowing your data is to see if you can identify any edge cases that may throw off your python automated data cleanup script. 

#### 1) Name 
#### 2) Case Number 
#### 3) Place of Death
#### 4) Birth and Death Dates
#### 5) Years of life
#### Example
![image](https://user-images.githubusercontent.com/51274827/173220146-d1da0da7-5eb1-4c75-a6af-7336c0a51ddd.png)<br />

In this case for people that died the same day they were born they do not have 5) Years of life row. That is an edge case that we must account for. I also want to get rid of any useless characters in my row and I also want to seperate the 4) Birth and Death Dates Dates into two seperate fields. 




# Step 4: Data Visualization

![image](https://user-images.githubusercontent.com/51274827/173510049-a122a8e8-9d4c-4df0-93a4-75fa3c94cc3d.png)

