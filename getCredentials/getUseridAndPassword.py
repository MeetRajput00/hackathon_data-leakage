import requests
import pandas as pd
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

query = {"free netflix account", "free hotstar account", "free amazon prime accounts"}
usernames=[]
passwords=[]
for s in query:
    for links in search(s, tld="co.in", num=10, stop=10, pause=2):
        r = requests.get(links)
        try:
            df_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
            df = df_list[0]
            for col_names in df.columns:
                if 'username' in col_names or 'Username' in col_names:
                    for validusrs in df[col_names].values.tolist():
                        if "@" in validusrs or "protected" in validusrs:
                            usernames.append(validusrs) 
                if "password" in col_names or "Password" in col_names:
                    for pswd in df[col_names].values.tolist():
                        passwords.append(pswd)
        except:
            pass
usernameFile = open("dataFiles\\userNames.txt", "a")
for element in usernames:
    usernameFile.write(element + "\n")
usernameFile.close()
passwordFile = open("dataFiles\\passwords.txt","a")
for element in passwords:
    passwordFile.write(element+"\n")
passwordFile.close()