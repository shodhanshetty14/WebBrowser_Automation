import pyautogui as py
import webbrowser

websites = { "youtube": "http://www.youtube.com", "spotify": "https://open.spotify.com/", "github": "https://github.com/"}
names = 'Youtube, Spotify & Github'
# sleep(3)
def Run():
    py.alert("The websites avalilabe are: Youtube, Spotify & Github" ,title="Web_Opener")
    url = py.prompt("Enter the website name you want to connect:\n",title="Web Opener")
    # print(url)
    
    if url is None or not url:
        quit() 
    elif url.lower() in websites:
        url = websites[url.lower()]
        webbrowser.open(url)
        # print(url)
    else:
        # add_To_websites(url)
        py.alert("Sorry, These are the only websites currently present in the memory\nPlease add the details of this mentioned site so that we can use it for future reference", title= 'ALERT!!')
        webbrowser.open(add_To_websites(url))
        # print(websites)


def add_To_websites(link):
    # web_name = input("Enter the name of the website")
    web_link = py.prompt('Enter the link of the above mentioned website:\n')
    if not web_link:
        quit()
    websites[link] = web_link
    
    py.alert("ThankYou for Helping us update our memory")
    return websites[link]


Run()