## Jobs_scraping


### Installation & Running locally

* Install python 3.8+
* Git clone `git@github.com/kyien/jobs_scraping.git` or `https://github.com/kyien/jobs_scraping.git`
* navigate to the Cloned folder and Setup an environment with `python3 -m venv venv`
* Activate virtual environment by running:
  
                    a) on windows run 'venv/Scripts/activate'
                    b) on MAC or Linux run   'source  venv/bin/activate'
            
* Run `pip install -r requirements.txt`
* Run `python3 app.py` to start the application

### Docker Image 
* The image is hosted on docker hub:
                 a)  'docker pull kyien/job_scraping:dev'
                 b) on your host run 'docker run -it kyien/job_scraping:dev'
   
