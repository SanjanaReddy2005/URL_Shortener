import requests

try:
#initializing the urlslist ehich is going to be shortened
     URLlist=[]
     infile =open("theURLlist.txt","r")
     line = infile.readline()
     print("theUrLlist.txt exist")
     while line:
          URLlist.append(line.rstrip("\n").strip(","))
          line = infile.readline()
     infile.close()
except FileNotFoundError :
     print("the <theURLlist.txt> file is not found")
     print("starting new list ffir storing the short urls")
     URLlist=[]#reinitializing the arrays


def shorten_link(full_link,link_name):

     API_KEY = 'f7492a478804c48ba22906235b07a56c'
     BASE_URL = 'https://cutt.ly/api/api.php'

     payload = {'key': API_KEY, 'short': full_link, 'name':link_name}
     request = requests.get(BASE_URL, params=payload)
     data = request.json()
     return data
     # print(data)
# instructions for the format in which cutlly shortens the urls
print(""" status:1 -the shortened link comes from the domain that shortens the link, i.e. the link has already been shortened
status:2 - the entered link is not a link
status:3 - the entered link is not a link
status:4 - Invalid API key
status:5 - the link has not passed the validation. Includes invalid characters
status:6 - The link provided is from a blocked domain
status:7 - OK - the link has been shortened
status:8 - You have reached your monthly link limit. You can upgrade your subscription plan to add more links. """)


a=1
while a:
    long_url=input('Enter the url which you want to shorten it :')
    name_url=input('Enter the name which you want to give it :')
    short_url=shorten_link(long_url,name_url)
    print(short_url)
    URLlist.append(short_url)
    a=input("do you still want to shorten any other url the press 1 otherwise 0 : ")
print(URLlist)

outfile = open("theURLlist.txt","w")
for urls in URLlist :
     outfile.write(",".join(urls) + "\n")
outfile.close()

if __name__=="__shorten_link__":
     shorten_link()
     