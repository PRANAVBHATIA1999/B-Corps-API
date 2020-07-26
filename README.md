# B Corps - API
## AN API TO GET B CORPS BASIC DATA USING FLASK
[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](https://github.com/PRANAVBHATIA1999/B-Corps-API)

## What is B Corps API?
B corps API is for any application which needs  data like company name, industry and the location of a B corp certified company across the globe.


## URL 

```
GET: http://127.0.0.1:5000/bcorps?country=<Country Name>
```

## Usage
Just do a GET request on the API URL.
```
GET: http://127.0.0.1:5000/bcorps?country=<Country Name>
```

## Routes
## Arguments
```
<country name>

Name or their codes in ISO 3166-1 alpha-2
```
## Return Format
```
JSON
```
## Example
```
GET: http://127.0.0.1:5000/bcorps?country=India
#RE
```

```
GET: http://127.0.0.1:5000/bcorps
#
```

```
GET: http://127.0.0.1:5000/bcorps?country=In
#
```

## Enhancements
Please feel free to message me or open an issue if you have an idea for an enhancement. Seems like people are starting to use this and I would like to improve it further.

## License
MIT

## Contact 

<p align='center'>
<a href="https://twitter.com/pranavvbhatia">
  <img src="https://img.shields.io/badge/twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" />
</a>&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/bhatiapranav/">
  <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />
</a>&nbsp;&nbsp;
<a href="mailto:pranavbhtaia431999@gmail.com">
  <img src="https://img.shields.io/badge/email me-%23D14836.svg?&style=for-the-badge&logo=gmail&logoColor=white" />
</a>
</p>

## Author 
Pranav Bhatia