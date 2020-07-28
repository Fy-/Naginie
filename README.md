# Naginie


| ^_^ | Naginie                               |
| ------------- | ------------------------------------ |
| ![Naginie](https://raw.githubusercontent.com/Fy-/Naginie/master/naginie_admin/public/img/icons/android-chrome-192x192.png) | Naginie is a mini-CMS based on python / flask / sqlalchemy, aimed to easily deploy content-managed websites through organized directories and files and assigning properties to the said directories and files. For example, a directory can be a blog while the other one can be just the footer navigation. |


## Status ##
It's still early stage and **Naginie is not usable at the moment**.
	// init & .env 
	python manager.py db init
	python manager.py db migrate
	python manager.py db upgrade
	python manager.py init_naginie 
	// run naginie
	flask run --host 0.0.0.0 --port 8888
	// run admin
	cd naginie_admin
	npm run serve // or you can go to localhost:5000/admin after using npm run build



## History ##
I made a flask based CMS a long time ago and this is the 2020 version of my old CMS: [FyPress](https://github.com/Fy-/FyPress). I was tired of WordPress and I plan on developing tools to migrate from WP to Naginie in the future.

## License
All program code is licensed under GPL v3.0 unless otherwise specified.  Please see the "LICENSE" file for more information.  
