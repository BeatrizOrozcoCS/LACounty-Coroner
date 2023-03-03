import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def get_general_caseinfo():
    # #found API Call
    pgnum = 1

    api = "http://api.lacounty.gov/mecsearch/CaseInformationServlet?pageNumber=" + str(pgnum) + "&pageSize=10000&NameFirst=&NameLast=&BirthDate=&Age=&DeathDate=&CaseNum=&sortColumn=CaseNum&sortOrder=desc"
    # 
    driverpath = r"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    driver = webdriver.Edge(driverpath)
    driver.get(api)

    content = driver.find_elements(By.TAG_NAME, "pre")
    import json 
    data = json.loads(content[0].text)
    CaseNum = []
    fName = []
    lName =[]
    Age = []
    bdate = []
    gender = []
    dDate = []
    deathPlace = []
    bodyStatus = []
    mode = []
    causeA = []
    Investigator = []
    DME = []
    CaseStatus = []


    for i in range(1, int(data["totalPages"])+1):
        
        print("Page: ", str(i) +"/ " + str(data["totalPages"]))
        for j in range(0, len(data["cases"])):
            CaseNum.append(data["cases"][j]["CaseNum"])
            fName.append(data["cases"][j]["NameFirst"])
            lName.append(data["cases"][j]["NameLast"])
            Age.append(data["cases"][j]["Age"])
            bdate.append(data["cases"][j]["BirthDate"])
            gender.append(data["cases"][j]["Gender"])
            dDate.append(data["cases"][j]["DeathDate"])
            deathPlace.append(data["cases"][j]["DeathPlace"])
            bodyStatus.append(data["cases"][j]["BodyStatus"])
            mode.append(data["cases"][j]["Mode"])
            causeA.append(data["cases"][j]["CauseA"])
            Investigator.append(data["cases"][j]["Investigator"])
            DME.append(data["cases"][j]["DME"])
            CaseStatus.append(data["cases"][j]["CaseStatus"])
        pgnum+=1
        if (i > int(data["totalPages"])):
            print("done")
        else:
            api = "http://api.lacounty.gov/mecsearch/CaseInformationServlet?pageNumber=" + str(pgnum) + "&pageSize=10000&NameFirst=&NameLast=&BirthDate=&Age=&DeathDate=&CaseNum=&sortColumn=CaseNum&sortOrder=desc"
            try:
                driver.get(api)
                content = driver.find_elements(By.TAG_NAME, "pre")
                data = json.loads(content[0].text)
            except:
                driver.get(api)
                content = driver.find_elements(By.TAG_NAME, "pre")
                data = json.loads(content[0].text)

    driver.quit()
    cols = ["Case Number", "First Name", "Last Name", "Age", "Birthdate", "DeathDate", "Gender", "Place of Death",
            "Body Status", "Mode", "Cause A", "Investigator", "DME", "Case Status"]    
    case_dataframe = pd.DataFrame(zip(CaseNum,fName,lName,Age,bdate,dDate,gender,deathPlace,
        bodyStatus ,mode,causeA, Investigator,DME,CaseStatus),columns = cols)
    with pd.ExcelWriter("LACountyDeathData_Casesv3.xlsx") as writer:
        case_dataframe.to_excel(writer,sheet_name="Case List", index = False)
    return CaseNum

def get_case_details(casenum):
    api = "https://api.lacounty.gov/mecsearch/CaseInformationServlet?caseDetails=1&CaseNum="
    driverpath = r"C:\Users\Orozc\OneDrive\My Documents\Projects\edgedriver_win64\msedgedriver.exe"
    driver = webdriver.Edge(driverpath)
    #"https://api.lacounty.gov/mecsearch/CaseInformationServlet?caseDetails=1&CaseNum=2022-08749"
    CaseNum_local = []
    fName = []
    lName =[]
    Age = []
    bdate = []
    gender = []
    dDate = []
    deathPlace = []
    bodyStatus = []
    mode = []
    causeA = []
    causeB = []
    causeC = []
    causeD = []
    causeOther =[]
    Investigator = []
    DME = []
    Toxstatus = []
    CaseStatus = []
    Race = []
    for i in range(0, len(casenum)):
        j = 0
        try:
            driver.get(api + str(casenum[i]))
            content = driver.find_elements(By.TAG_NAME, "pre")
            import json 
            data = json.loads(content[0].text)
            print(data)
            CaseNum_local.append(data["caseDetail"][j]["CaseNum"])
            fName.append(data["caseDetail"][j]["NameFirst"])
            lName.append(data["caseDetail"][j]["NameLast"])
            Age.append(data["caseDetail"][j]["Age"])
            
            bdate.append(data["caseDetail"][j]["BirthDate"])
            gender.append(data["caseDetail"][j]["Gender"])
            dDate.append(data["caseDetail"][j]["DeathDate"])
            deathPlace.append(data["caseDetail"][j]["DeathPlace"])
            bodyStatus.append(data["caseDetail"][j]["BodyStatus"])
            mode.append(data["caseDetail"][j]["Mode"])
            causeA.append(data["caseDetail"][j]["CauseA"])
            causeB.append(data["caseDetail"][j]["CauseB"])
            causeC.append(data["caseDetail"][j]["CauseC"])
            causeD.append(data["caseDetail"][j]["CauseD"])
            causeOther.append(data["caseDetail"][j]["CauseOther"])
            Investigator.append(data["caseDetail"][j]["Investigator"])
            DME.append(data["caseDetail"][j]["DME"])
            Toxstatus.append(data["caseDetail"][j]["ToxStatus"])
            CaseStatus.append(data["caseDetail"][j]["CaseStatus"])
            Race.append(data["caseDetail"][j]["Race"])
        except:
            driver.get(api + str(casenum[i]))
            content = driver.find_elements(By.TAG_NAME, "pre")
            import json 
            data = json.loads(content[0].text)
            print(data)
            CaseNum_local.append(data["caseDetail"][j]["CaseNum"])
            fName.append(data["caseDetail"][j]["NameFirst"])
            lName.append(data["caseDetail"][j]["NameLast"])
            Age.append(data["caseDetail"][j]["Age"])
            
            bdate.append(data["caseDetail"][j]["BirthDate"])
            gender.append(data["caseDetail"][j]["Gender"])
            dDate.append(data["caseDetail"][j]["DeathDate"])
            deathPlace.append(data["caseDetail"][j]["DeathPlace"])
            bodyStatus.append(data["caseDetail"][j]["BodyStatus"])
            mode.append(data["caseDetail"][j]["Mode"])
            causeA.append(data["caseDetail"][j]["CauseA"])
            causeB.append(data["caseDetail"][j]["CauseB"])
            causeC.append(data["caseDetail"][j]["CauseC"])
            causeD.append(data["caseDetail"][j]["CauseD"])
            causeOther.append(data["caseDetail"][j]["CauseOther"])
            Investigator.append(data["caseDetail"][j]["Investigator"])
            DME.append(data["caseDetail"][j]["DME"])
            Toxstatus.append(data["caseDetail"][j]["ToxStatus"])
            CaseStatus.append(data["caseDetail"][j]["CaseStatus"])
            Race.append(data["caseDetail"][j]["Race"])
    cols = ["Case Number", "First Name", "Last Name", "Age", "Race",
            "Birthdate", "DeathDate","Gender", "Place of Death",
            "Body Status", "Mode", "Cause A","Cause B","Cause C","Cause D",
            "Cause Other", "Investigator", "DME", "Tox Status", "Case Status"]    
    casedetails_dataframe = pd.DataFrame(zip(CaseNum_local,fName,lName,Age,Race,bdate,dDate,gender,deathPlace,
        bodyStatus ,mode,causeA,causeB,causeC,causeD,causeOther, Investigator,DME,Toxstatus,
        CaseStatus),columns = cols)
    with pd.ExcelWriter("LACountyDeathData_Cases_Final.xlsx") as writer:
        casedetails_dataframe.to_excel(writer,sheet_name="Case List", index = False)   
    driver.quit()
    return
a = get_general_caseinfo()
get_case_details(a)
