# hw-company-app
Simple Project and Website for Database Class 2018 - Hot Water Company Application
This website uses django to create models that enable the admin users to modify them.

## Getting Started

When executing the program for the first time and in a local environment you will need to:

```
cd hw-company-app/hwcompany         # access manage directory
python3 manage.py runserver         # will enable the website on localhost
python3 manage.py runserver 0.0.0.0 # will enable the website on default address
```

To make changes to the database:
```
cd hw-company-app/hwcompany       # access manage directory
python3 manage.py makemigrations  
python3 manage.py migrate       
```

### Prerequisites

#### Linux
```
sudo apt-get install python3 python3-pip
sudo pip install barnum django django-tables2
```

### Hot Water company

This entity relation database covers a Manufacturer, Brand, and Model entity that enables
users to produce spa services for sale. Attributes can be seen under models.py. There is
a word document under data/ that covers a dictionary of each attribute on the database.

### TODO

Input validation
Reports section

## Author

* **Jordan Alexis Caraballo-Vega** - University of Puerto Rico at Humacao

## Acknowledgments

  * Ollantay Medina
  * Colleagues from Class UPRH
