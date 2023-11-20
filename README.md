# capstone
In this project, we scrape historical flight prices for 60 days from Google Flights Website and use this data to predict best time to purchase flight 
tickets for future flights.

Data Scraping: We use Selenium to automate the data scraping process. We scrape prices for flights from RDU Airport to 25 different destinations. 
For each flight we scrape historical prices for 60 days until the flight date.

We pool flight price data based on the destination and week of the day. We collected six weeks of data. Here is an example of pooled data for a 
Tuesday Denver flight:

<img width="727" alt="image" src="https://github.com/osmanarslan61/capstone/assets/133136319/ead6d0b6-a10d-4d77-aa5e-2eb732bbdb55">

Predicting Best Time Window and Calculate Accuracy by Cross Validation: In this part of the project, we estimate the best time window to purchase tickets based on the minimum average pooled price. We first start a window size of 7 days, if the accuracy is lower than 80%, we increase our window size to 14 days and then 21 days if needed.

We calculate the accuracy with cross validation. We pooled data for 6 weeks. So we estimate the best time window using 5 weeks of data and then compare this with the one that is not included and we repeat this 6 times.

Our overall accuracy is on average, average price of the predicted time-window is 10% off from the average minimum price of the best time-window.

Here is an example plot of how we estimate the best time window to purchase a ticket: 
<img width="726" alt="image" src="https://github.com/osmanarslan61/capstone/assets/133136319/98ce39de-06e7-477b-95ad-dbbcde758a50">

