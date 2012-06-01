[HTTP-to-HTTPS](http://http-to-https.appspot.com) - Python / webapp2 / Base App
===============================================================================

[AE-BaseApp](http://AE-BaseApp.appspot.com) is a multi-platform app-engine base-app created by 
[Mark Finch](http://markfinch.info) to assist developers looking to build their first applications 
leveraging [Google's Cloud Infrastructure](http://developers.google.com/appengine/). HTTP-to-HTTPS is loosely based 
on the video from [Brett Slatkin](http://www.google.com/profiles/bslatkin) introducing Google App Engine at 
[Google IO 2008](http://sites.google.com/site/io/).

This simple application is for demonstrating HTTP to HTTPS routes using WSGI, in 
reference to my [Stack Overflow](http://stackoverflow.com/questions/10804873/how-to-use-wsgi-to-reroute-a-user-from-http-to-https)
question on this subject.  Please check out the other AE-BaseApp applications
for more feature complete Base Applications.  Please note this application 
uses AdSense and the source includes my AdSense code, if you object to AdSense
it shouldn't be trouble to Remove the few lines that import them, also you 
can easily change the code to your own.

Accomplished:
-------------
  * Version 1
    * Ad-Sense Integration
    * Basic Template Usage
    * Access the Datastore to Create and Read
    * Route HTTP to HTTPS using WSGI

Application Stack:
------------------
  * Google App Engine Python
  * Google webapp2 Framework
  * Django Templates

Issues:
-------
  * THIS APP IS NOT PRODUCTION READY!!!
  * Read the file ISSUES to see a list of known issues and resolutions.

No Warranties:
--------------
There are no warranties expressed or implied.  Use at your own RISK!

Setup:
------
  * Edit the app.yaml file to change the application name.
  * Run the dev server.
  * Go back to the home page and double check everything is working.
  * Hack away, but remember you break it you bought it!  *wink* 1

License:
--------
HTTP-to-HTTPS BaseApp source code is licensed under the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0).  

Please check the file LICENSE to see other licenses that impact this project.

Notes:
------
*  1 The corollary is you got what you paid for!
