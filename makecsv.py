from nis import cat
from common_imports import *
import parsedesc
import re

import pandas as pd


def returnurl(driver):
    while True:
        try:
            return driver.current_url
        except:
            pass

def getjobs(driver):
    page = 0
    df = pd.DataFrame(columns=['name','id','company_name','location','workplace','posted_date','applicantcount','schedule','seniority','number_of_employees','field','apply','details','url','stack','possible_salary'])
    df.to_csv('jobs.csv')
    while True:
        try:
            if(driver.find_element(by=By.CLASS_NAME, value='jobs-search-no-results-banner')):
                break
        except:
            pass
        #if(page==25):
        #    break
        try:
            driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3129197532&f_CR=103644278%2C102713980%2C102890883%2C101165590%2C101282230%2C101174742%2C105015875%2C102890719%2C101355337&f_EA=true&f_F=it&f_JT=F&f_T=9&f_WT=2&geoId=92000000&location=Mundial&refresh=true&sortBy=R&start="+str(page))
        except:
            pass
        for x in range(0,20):
            jobs = driver.find_elements(by=By.XPATH, value='//div[@data-job-id]')
            while True:
                try:
                    jobs[-1].location_once_scrolled_into_view
                    break
                except:
                    pass
        for x in jobs:
            while True:
                try:
                    name = x.find_element(by=By.CLASS_NAME, value='job-card-list__title').text
                    url = x.find_element(by=By.CLASS_NAME, value='job-card-list__title').get_attribute('href')
                    result = re.search("view/(.*?)/", url)
                    job_id = result.group(1)
                    break
                except:
                    pass
            company_name = x.find_element(by=By.CLASS_NAME, value='job-card-container__company-name').text
            location = x.find_element(by=By.CLASS_NAME, value='job-card-container__metadata-item').text
            try:
                workplace = x.find_element(by=By.CLASS_NAME, value='job-card-container__metadata-item--workplace-type').text
            except:
                workplace = "Unknown"
            x.location_once_scrolled_into_view
            while True:
                try:
                    x.click()
                    break
                except:
                    pass
            time.sleep(2)
            frame = driver.find_element(by=By.CLASS_NAME, value='jobs-details')
            posteddate = frame.find_element(by=By.CLASS_NAME, value='jobs-unified-top-card__posted-date').text
            try:
                applicantcount = frame.find_element(by=By.CLASS_NAME, value='jobs-unified-top-card__applicant-count').text
            except:
                applicantcount = "Unknown"
            jobinsight1 = ""
            jobinsight2 = ""
            schedule = ""
            seniority = ""
            number_of_employees = ""
            field = ""
            try:
                jobinsights = frame.find_elements(by=By.CLASS_NAME, value='jobs-unified-top-card__job-insight')
                jobinsight1 = jobinsights[0].text
                if(" · " in jobinsight1):
                    schedule = jobinsight1.split(" · ")[0]
                    seniority = jobinsight1.split(" · ")[1]
                else:
                    schedule = jobinsight1
                jobinsight2 = jobinsights[1].text
                if(" · " in jobinsight2):
                    number_of_employees = jobinsight2.split(" · ")[0]
                    field = jobinsight2.split(" · ")[1]
                else:
                    number_of_employees = jobinsight2
            except:
                pass
            try:
                apply = frame.find_element(by=By.CLASS_NAME, value='jobs-s-apply').text
            except:
                apply = ""
            details = frame.find_element(by=By.ID, value='job-details').text
            try:
                frame.find_element(by=By.CLASS_NAME, value='jobs-s-apply').click()
                window_after = driver.window_handles[1]
                driver.switch_to.window(window_after)
                url = returnurl(driver)
                while("linkedin.com/" in url):
                    driver.find_element(by=By.CLASS_NAME, value='in-page__destination-link').click()
                    url = returnurl(driver)
                driver.close()
                window_before = driver.window_handles[0]
                driver.switch_to.window(window_before)
            except Exception as e:
                print(e)
                try:
                    driver.find_element(by=By.CLASS_NAME, value='artdeco-modal__dismiss').click()
                    driver.find_element(by=By.CLASS_NAME, value='artdeco-modal__confirm-dialog-btn').click()
                except:
                    pass
            stack = parsedesc.parseTechInDesc(name+" "+details)
            possible_salary = parsedesc.parseSalary(name+" "+details)
            df2 = pd.DataFrame({'name': name,'id':job_id,'company_name': company_name,'location': location,'workplace':workplace,'posted_date':posteddate,'applicantcount':next(iter(re.findall("\d+", applicantcount)), 0),'schedule':schedule,'seniority':seniority,'number_of_employees':number_of_employees,'field':field,'apply':apply,'details':details.replace('\n', '|'),'url':url,'stack':stack,'possible_salary':possible_salary},index=[0])
            df = pd.concat([df,df2],ignore_index=True)
            df.to_csv('jobs.csv')
        page = page + 25
