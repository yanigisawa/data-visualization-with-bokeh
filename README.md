# data-visualization-with-bokeh

This repository holds a jupyter notebook and django project I used to present at the PyData Indianapolis one-day conference on 10/12/2018. See below for how to install dependencies and run the django project.

The notebook contained in this repo is also available as a Google Colaboratory notebook [here](http://bit.ly/pydata-bokeh).

## Installation

Requires [pipenv](https://pipenv.readthedocs.io/en/latest/) (wraps around virtualenv and `pip install` automatically)

Run `pipenv install` to install dependencies

Run `jupyter notebook` and open `notebooks/Presentation.ipynb` to view the presentation as I presented it.

Open the `django_proj` folder and run `python manage.py runserver` to run the django project. Download the Sqlite database via the link at the index route on `/`. Copy the database into the `django_proj` folder to view the same data that was presented for Fantasy Football statistics. 
