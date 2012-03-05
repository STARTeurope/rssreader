Python + GAE RSSReader
=============

Simple Python RSSReader developed to display our RSS Blog Feeds as Tab App within Facebook.


Setup / Installation:
-------------------
1. Install Python2.7
2. Install Google App Engine
3. Change application data, AppId, etc.
4. Change html, css
5. Deploy
6. Use as Facebook Tab App URL


What to change:
---------------
### app.yaml
    application: your_application

### rssreader.py
    rss_reader = RSSReader('http://feeds.feedburner.com/[FeedBurner_Projekt_Name]?format=xml')
    #insert your RSSFeed URL - only tested with Feedburner RSS Feed Link

### index.html
change the layout, add css classes, ...
    * item.title #the title
    * item.link #the link to blog entry
    * item.pubDate #publish date of entry
    * item.description #the excerpt / short description
    * item.content #the whole content
    * item.img #url of first image in content

### style.css
add your css to style your index.html


Credits:
--------
I used some Python code for the RSS Reader from: http://www.learningpython.com/2006/01/30/rss-reader-part-three-generator-class/