import pandas as pd

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driverpath = r'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

def get_casename():

    info = pd.read_excel("LACountyDeathData_Clean.xlsm",sheet_name = "Coroner Case List")
    cleancase = info["CaseNumber"].str.lstrip()
    casenum_list = cleancase.tolist()

    return casenum_list

def go_towebpage(caselist):
    
    #Things to webscrape
    Name = []
    date = []
    years = []

    CaseNumber = []
    CaseStatus = []
    BodyStatus = []
    Gender = []
    Ethnicity = []
    PlaceofDeath = []
    Manner = []
    Investigator = []
    DeputyMedicalExaminer = []
    CauseA = []
    CauseB = []
    CauseC = []
    CauseD = []
    OtherSignificantConditions = []

    basic_url="https://mec.lacounty.gov/case-detail/?caseNumber="

    driver = webdriver.Edge(driverpath)
    e_wait = 5
    print("now going to webpages")
    for i in range(0, len(caselist)):
        try:
            #results to append to list 
            driver.get(basic_url + caselist[i])

            Name.append(WebDriverWait(driver, e_wait).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/h1'))).get_attribute('innerText'))
            date.append(WebDriverWait(driver, e_wait).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div[1]'))).get_attribute('innerText'))
            years.append(WebDriverWait(driver, e_wait).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div[2]'))).get_attribute('innerText'))

            CaseNumber.append(WebDriverWait(driver, e_wait).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[3]/div[1]'))).get_attribute('innerText'))
            CaseStatus.append(WebDriverWait(driver, e_wait).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[3]/div[2]'))).get_attribute('innerText'))
            BodyStatus.append(WebDriverWait(driver, e_wait).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[3]/div[3]'))).get_attribute('innerText'))
            Gender.append(WebDriverWait(driver, e_wait).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[3]/div[4]'))).get_attribute('innerText'))
            Ethnicity.append(WebDriverWait(driver, e_wait).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[3]/div[5]'))).get_attribute('innerText'))

            PlaceofDeath.append(WebDriverWait(driver, e_wait).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[4]/div[1]'))).get_attribute('innerText'))
            Manner.append(WebDriverWait(driver, e_wait).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[4]/div[2]'))).get_attribute('innerText'))
            Investigator.append(WebDriverWait(driver, e_wait).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[4]/div[3]'))).get_attribute('innerText'))
            DeputyMedicalExaminer.append(WebDriverWait(driver, e_wait).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[4]/div[4]'))).get_attribute('innerText'))

            CauseA.append(WebDriverWait(driver, e_wait).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[5]/div[1]'))).get_attribute('innerText'))
            CauseB.append(WebDriverWait(driver, e_wait).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[5]/div[2]'))).get_attribute('innerText'))
            CauseC.append(WebDriverWait(driver, e_wait).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[5]/div[3]'))).get_attribute('innerText'))
            CauseD.append(WebDriverWait(driver, e_wait).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[5]/div[4]'))).get_attribute('innerText'))
            OtherSignificantConditions.append(WebDriverWait(driver, e_wait).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[5]/div[5]'))).get_attribute('innerText'))
        
        except:

            Name.append("FAIL")
            date.append("FAIL")
            years.append("FAIL")

            CaseNumber.append(caselist[i])
            CaseStatus.append("FAIL")
            BodyStatus.append("FAIL")
            Gender.append("FAIL")
            Ethnicity.append("FAIL")
            
            PlaceofDeath.append("FAIL")
            Manner.append("FAIL")
            Investigator.append("FAIL")
            DeputyMedicalExaminer.append("FAIL")
            
            CauseA.append("FAIL")
            CauseB.append("FAIL")
            CauseC.append("FAIL")
            CauseD.append("FAIL")
            OtherSignificantConditions.append("FAIL")
            
    
    cols = ["Name", "Date", "Years" ,"CaseNumber", "CaseStatus", "BodyStatus", "Gender", "Ethnicity", "PlaceofDeath","Manner","Investigator","DeputyMedicalExaminer","CauseA","CauseB","CauseC","CauseD","OtherSignificantConditions"]    
    case_dataframe = pd.DataFrame(zip(Name, date, years,CaseNumber, CaseStatus, BodyStatus, Gender, Ethnicity, PlaceofDeath,Manner,Investigator,DeputyMedicalExaminer,CauseA,CauseB,CauseC,CauseD,OtherSignificantConditions),columns = cols)
    with pd.ExcelWriter("LACountyDeathData_Casesv3.xlsx") as writer:
        case_dataframe.to_excel(writer,sheet_name="Case List", index = False)   

    
    return case_dataframe


def cleanup(df):
    for i in range (0, len(df)):
        if df["CaseStatus"] == 'FAIL':
            basic_url="https://mec.lacounty.gov/case-detail/?caseNumber="
            driver = webdriver.Edge(driverpath)
            print("now going to webpages")
            driver.get(basic_url + caselist[i])
            #Things to webscrape
            df['Name']=WebDriverWait(driver, e_wait).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/h1'))).get_attribute('innerText')
        
            df['Date']
            df['Years']
            df['CaseStatus']
            df['BodyStatus']
            df['Gender']
            df['Ethnicity']
            df['Name']
            df['Name']
            df['Name']
            df['Name']
            

        

a = get_casename()
b = go_towebpage(a)




