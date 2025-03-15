# Weather web app
#### Video Demo:  <https://youtu.be/XIOgNvHzENM>
#### Description:
This is a web application for weather forecasting. When it is launched, only a text field and a 'Search' button appear on the screen. The user can enter the name of the city and click on the 'Search' button to get information about the weather in the city of interest, which is obtained from the third-party API Visual Crossing. At the first query for a certain city the result is cached using Redis, which speeds up further display of information on this city. But the timer for storing data in the cache for a certain city is set to half an hour, which is close to the optimal time for storing weather information, the state of which can change rapidly, after which the data is reset. And if you enter the wrong city name or a set of random characters, instead of the result a picture is displayed, which informs the user of the error. The same is provided in case of a temporary malfunction in the API.
The header part of the main file 'app.py' with python code contains a list of imported modules, a link to .env file, which contains api key from Visual Crossing service, code for connecting Redis service, implementation of 'apology' function, which is used in case of API failure or entering incorrect city name. The main part of 'app.py' implies flask-methods Get and Post, which are responsible for loading the page without information about the weather in the desired city and with information, the receipt of which is realized with the help of the request module and a special link with api key in it, respectively.
The information received from the API is passed to the index.html file, which is rendered as a result of the successful execution of the code in app.py.
The information received from the API is passed to the index.html file, which is located in the templates folder and which is rendered as a result of the successful execution of the code in app.py. With the help of Jinja, each part of the passed information is substituted in the right place and correctly displayed on the rendered page. One of the elements of the passed information is the name of the image, which is substituted in the html file into the link that points to a pre-loaded set of images in the Static folder, and thanks to this, this image is displayed on the page.
The last of the main files is the CSS file, which is located in the static folder and is responsible for the style of the page.
Among the auxiliary files are:
1) .env file which contains the api key to the Visual Crossing service.
2) WeatherIcons folder in the Static folder, which contains several sets of various images of weather conditions.
3) requirements.txt which contains a list of all modules and packages required for the correct operation of the program.
4) README.md which you are reading now.

#### Roadmap.sh project URL:  <https://roadmap.sh/projects/weather-api-wrapper-service>
