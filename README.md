# Clickbait Detector

An extension to detect if the articles content match its title.

This was developed in a period of 24-hours in a hackathon called 'Hallothon'

## Working
On click of the extension, the extension will call teh API (a basic flask app) which will scrape the contents of the website and use NLP to determine the similarity between the title and the content in the article and return the similarity as a percentage value back to the extension which will be displayed to the user

Example:
* The first image is an article whose title was exaggarated heavily and is caught too be having a high chance of being a clickbait
* The second image is a normal article
<p align="center">
   <img src="images\clickbait_example.jpg" alt="clickbait" width = "150"/>
   <img src="images\not_clickbait_example.jpg" alt="clickbait" width = "155"/>
</p>


## Usage instruction

1. Download or clone the repo using the command 
```bash
git clone https://github.com/ArvindAROO/Clickbait-detector.git
```

2. Go to any chromium based browser (Chrome, edge, brave) => extensions => 'load unpacked' and select the folder `/plugin`

3. Start the flask app by using the command inside `/API`
```bash
flask run
```

The extension must be ready to use and will return the values when clicked


## Team Members:
* [Anurag Khanra](https://github.com/anuragisfree)
* [Arvind Krishna](https://github.com/ArvindAROO)
* [Dhruva A Prasad](https://github.com/dhruva17)
* [Jeevan Samrudh L H](https://github.com/JeevanSamrudh)
* Tejas B
* Vansidhar A

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
