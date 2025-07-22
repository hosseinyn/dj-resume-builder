# Django Resume Builder
[![My Skills](https://skillicons.dev/icons?i=html,css,scss,js,bootstrap,python,django)](https://github.com/hosseinyn)

A simple django resume builder project based on bootstrap,scss frontend and django backend

### Features:
- Login && Create account
- Change password
- Delete account
- Limitation (5 resume only)
- Create resume
- Delete resume
- Edit resume
- Share resume

## How to use?
1- Clone the repository
`git clone https://github.com/hosseinyn/dj-resume-builder.git`

2- Open project directory
`cd dj-resume-builder`

3- Create a virtual environment
   ```
	pip install virtualenv
		virtualenv venv
			Windows:
				.\venv\Scripts\activate
			Linux:
				source ./venv/bin/activate
```
4- Install requirements
`pip install -r requirements.txt`

5- Setup database
```
cd ResumeBuilder
python manage.py makemigrations
python manage.py migrate
			or
python3 manage.py makemigrations
python3 manage.py migrate
```

5- Run the website
`python manage.py runserver`
	or
	`python3 manage.py runserver`
	

**Happy :)**
