#  Copyright 2010 - 2012 Mark Finch
#
#  Licensed under the Apache License, Version 2.0 (the "License"); you may not
#  use this file except in compliance with the License. You may obtain a copy
#  of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.
import webapp2
import os

# Models
from models.Shout import Shout

# Controllers
from controllers.HomeHandler import HomeHandler
from controllers.LoginHandler import LoginHandler
from controllers.ProfileHandler import ProfileHandler

# Env idea from dave-w-smith on StackOverflow question 1916579
if os.environ['SERVER_SOFTWARE'].startswith('Development'):
    app_scheme = 'http'
else:
    app_scheme = 'https'

app = webapp2.WSGIApplication([
    webapp2.Route(r'/login', LoginHandler, name='login', schemes=[app_scheme]),
    webapp2.Route(r'/profile', ProfileHandler, name='profile', schemes=[app_scheme]),
    webapp2.Route(r'/', HomeHandler)
], debug=True)
