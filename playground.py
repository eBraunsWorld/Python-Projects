import re
import pandas as pd

while True:
    try:
        fname = input("Enter file name:")
        filehand = open(fname) 
        
        #Empty dictionary to store urls found from Zotero .txt Report
        urls = dict()
        #Count to track number of URLs in report.
        count = 1
        url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

        #Iterate through links and separate out URL portion.
        #Counter will assign value to the link to select for opening webpage.
        for line in filehand:
            urls_found = re.findall(url_pattern, line)
            for url in urls_found:
                urls[url] = urls.get(url, count)

        export_request = int(input("Enter 1 for .csv of URLs from file.\nEnter 2 for display on screen.\n"))
        if export_request == 1:
            excel_urls = pd.DataFrame(data=urls, index=[0])
            excel_urls.to_excel(excel_writer=any, sheet_name="url_report")
        elif export_request == 2:
            for link in urls:
                print(count, link)
                count = count + 1
        else:
            break
        break
    except FileNotFoundError:
        print("Unable to find file.")







    


