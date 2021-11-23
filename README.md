This repo leverages Peter Van Dijk's [DNS Reverse Scanning technique](http://7bits.nl/blog/2012/03/26/finding-v6-hosts-by-efficiently-mapping-ip6-arpa).
I conducted a small survey on how real-world IPv6 networks were vulnerable to this type of reconnaissance attacks.

### Structure:

- `./data` consists of assigned IPv6 prefixes from 19 countries, collected from [Regional Internet Registries Statistics](https://www-public.imtbs-tsp.eu/~maigron/RIR_Stats/RIR_Delegations/AFRINIC/IPv6-ByNb.html)
- `ip6_arpa_scan.py` implements the core scanning functionality (mostly by Peter, I modified a little to clarify input arguments, customize termination and log results).
-  `./run.py` reads the datasets, applying the scanning technique on each IPv6 subnet.

### Results (as of November 2021):

| Country      | Numner of assigned IPv6 prefixes | Number of prefixes having active IPv6 |   Percentage  |
| :---         |    :----:                        |   :---:                               |   :---:       |
|  United States    |     2880    |     389    |     13.51| 
| Germany    |     625    |     170    |     27.20| 
| Sweden    |     332    |     118    |     35.54 | 
| Brazil    |     592    |     73    |     12.33 | 
| 	United Kingdom    |     216    |     69    |     31.94| 
| 	Netherland    |     230    |     64    |     27.83| 
| 	Russia    |     288    |     55    |     19.10|
| 	Poland    |     231    |     46    |     19.91| 
| 	France    |     137    |     46    |     33.58| 
| 	Canada    |     276    |     38    |     13.77| 
| 	Czech Republic    |     102    |     38    |     37.25| 
| 	Australia    |     664    |     36    |     5.42| 
| 	Austria    |     149    |     35    |     23.49| 
| 	Japan    |     105    |     29    |     27.62| 
| 	Indonesia    |     1033    |     20    |     1.94| 
| 	Argentina    |     153    |     18    |     11.76| 
| 	India    |     751    |     16    |     2.13| 
| 	Singapore    |     158    |     12    |     7.59| 
| 	Italy    |     29    |     10    |     34.48| 


### To reproduce, simply run those commands:

```
git clone https://github.com/cuongvng/ip6-arpa-scan
pip install -r requirements.txt
python run.py
```