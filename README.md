# Scraping-UPI-statistics

Plotting web scraped data of the UPI apps available in India. Enter the details in the described manner i.e First three letters of the month with the first word capitalized (Jan, Oct, Dec), Last two digits of the year and top 'n' apps with highest transaction value. The script works for data available from Apr 2021, prior to which div tag naming structure was different and hence existing script needs to be modified. The generated Matplotlib plot is embedded in Tkinter GUI and BeautifulSoup library is used for web scraping.

<hr>

![Screenshot](img.png)

Based on the 'n' value, final stored data in python dictionary looks like this :
`{'PhonePe': 524742.49, 'Google Pay': 366669.09, 'Paytm Payments Bank App': 111149.66, 'Cred': 19716.43, 'Yes Bank Apps': 15236.04, 'ICICI Bank Apps': 11509.29}`

# Running

Install necessary python libraries as per _requirements.txt_ file and then run it

```
pip install -r requirements.txt
python3 final.py
```

Source of the data : https://www.npci.org.in/what-we-do/upi/upi-ecosystem-statistics [© NPCI]

Disclaimer: The data used in this project comes from [NPCI](https://www.npci.org.in/). The use of this data is for educational/research purposes only and is not intended for commercial or personal gain. I acknowledges and respects the intellectual property rights of NPCI and their respective owners. I do not claim ownership of the data and assumes no responsibility or liability for any errors, inaccuracies, or misinterpretations that may arise from the use of this data.

Copyright Disclaimer under the Copyright Act of 1957 : The content in this project is governed by the Copyright Act of 1957. It is used for educational and informational purposes. If you are a copyright holder and believe your rights are infringed, please contact us for resolution. I respect the rights of copyright owners and comply with the Copyright Act of 1957. I acknowledge applicable exceptions and limitations under the Copyright Act of 1957, including fair dealing and educational use. Users are urged to respect intellectual property rights, and any unauthorized use may require permission from the copyright owner.
