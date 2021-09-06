# BlocksFromTwitter

Twitter-Python app using Tweepy for making a sum list of profiles who blocked yours

## Versions
- Python 3.7.3
- Tweepy  3.8.0

## Functions and details 
* You will use Python and some libraries like Tweepy, Time and Json. You might have to install them.

* You will also need a Twitter Developer account for getting the keys and hashes.

* The app doesn't create the txt file it writes in (u gotta do it yourself, in the same directory of the file).
  * The file name is set as "sum_of_blocks.txt" on the code, if u create a file with another name, you should change it on the code too.

* The list may contain double profiles for it doesnt check if they exist before appending.

* The code dumps the array result on the txt file everytime it finds a block, so if the code crashes u wont lose data.
