# DiscordPackager
Package and locally store everything in a discord server

# HOW TO (authorization data)

Step 1: Open discord in a browser and log in

Step 2: Go to any server that you are a part of

Step 3: Open developer tools (F12 in Google Chrome and Firefox)

Step 4: Go to "Network"

Step 5: type something into the chat box (Usually no need to send a message, just type something)

Step 6: Find the "typing" HTTP POST method (as seen in the picture below)
![Authorization header](https://i.imgur.com/DKaTfCt.png)

Step 7: Find and copy the value of "Authorization" (also seen in the picture above)

# HOW TO (Channel id(s))

Step 1: Same as step 1-4 of HOW TO (authorization data) (You need to have opened developer tools before opening discord in your browser)
Step 2: Find and copy the highlighted value of a HTTP GET method with the name/file name "messages?limit=50" (doesn't have to be limit=50, but it usually is)
![Channel ID](https://i.imgur.com/ZROOm68.png)
