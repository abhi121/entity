# entity

python version: 3.6.9
django version: 3.0.7
elasticsearch : 7.0.5

database: postgresql 


1. Go to EntityManagement/settings.py
 	
	Change the db name, password according to your db configs.
	create db

2. Run migrations
	
	$python manage.py makemigrations
	$python manage.py migrate

3. Run server

	$python manage.py runserver


4. Api Endpoints:

	/api/entities -> {CRUD}

	/api/tags/{tag-name}/entites  -> Get - return all entites to a particular tag
		
	/api/discover/?name=?    -> Get - return all tags based on search params

	
