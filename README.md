# Motivational-Meme-Generator

Meme Generator is a multimedia application to dynamically generate memes, which includes an image with an overlaid quote. It is a dynamic data - rich application. It is primarily focused on **data engineer** and **full - stack** roles in Python development. 

## This application does the following:

* Interacts with a variety of complex filetypes. 
* Load quotes from a variety of filetypes (CSV, Docx, PDF, Text files)
* Load, manipulate and save images
* Accept dynamic user input through a command-line tool and a web serive. 

## Libraries 

* requests
* python - docx
* pandas
* pillow
* flask

## PDF file handling
The app uses the `subprocess` module for the purpose of converting data from PDF to Txt format. Firstly, `pdftotext` needs to be installed on Mac or Windows. For this `xpdf` should be downloaded using [here](https://www.xpdfreader.com/pdftotext-man.html). For Mac, run `brew install pkg-config poppler python` and then `pip install pdftotext`

## Project Interface
There are two ways of running this project:

   1. Running on the command line - `python2 meme.py`. For getting more information you 
      could run `python meme.py --help` which will provide further explanation. 

      Explanation here

      sample for what to pass in the command line here

    Through this way, the meme will be generated in `tmp` directory. The parameters are optional. If no parameter is passed then a random meme will be generated. 


    2. Running the project in the app - `python3 app.py` and go to `the link`

       Sample passing command 

       The app will use `QuoteEngine` module and `Meme Generator` module which will generate the meme with a random quote. It will use `requests` package to fetch an image which the user submits. 

## Modules description 
The structure of the project:

The `QuoteEngine` module is responsible for ingesting various file types which contain the quotes. It contains many classes and showcases inheritance, abstract classes, classmethods, strategy objects. 

The `MemeEngine` module is responsible for the resizing, cropping and drawing text on the images for the memes. 
      