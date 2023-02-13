import webbrowser

# webbrowser.open("https://www.python.org/", new=1)

# help(webbrowser)

# this is setting a webbrowser to use a specific program.
firefox_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))
firefox = webbrowser.get('firefox')
firefox.open("https://www.python.org/")

# This uses the default browser from the user.
webbrowser.open("https://www.python.org/")
