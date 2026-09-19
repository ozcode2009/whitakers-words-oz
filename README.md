# Whitaker’s Words
This is the source code for the website at https://latin.ozapps.cloud

Whitaker’s Words is an open source Latin dictionary written in Ada by Colonel William A. Whitaker. Several reimplementations of the dictionary in Python exist, however none support the full functionality of the original Ada version. This project provides a web frontend for the Ada application. The original Ada code is kept up to date by GitHub user mk270. 

This implementation was built because https://latin-words.com does not support English->Latin lookups and has had spotty availability for the past few weeks. It is built using FastAPI and calls directly into the WORDS program. 

Long caching times (1 month by default) are used in conjunction with Cloudflare to reduce server load.
## Running
To run the website, first follow the steps for building Whitaker’s Words at https://github.com/mk270/whitakers-words

Then, copy bin/words and all required files to the `whitakers-words` directory in this project. You may find it easiest to recursively copy the entire directory. 

Update any settings in main.py. The HTML files point to https://latin.ozapps.cloud by default when looking up a word; you’ll likely want to change this.

Finally, run the project with Docker.
