# Irises Analysis
Web application for database managing and prediction class of provided data. The prediction part of an application uses machine learning (K nearest neighbors algorithm) to predict the class of provided data based on continuous features.
You can learn more about KNN [HERE](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm).

## Preview and deletion of data records
To preview records in the database open **Main page**. If you want to delete the record, click **Action** button and select proper option.

<img src="https://github.com/BartlomiejCzerwinski/irises-analysis/assets/84719721/caa4d451-1478-4327-87af-aeee8cbb20ae"></img>

## Add new data record
To add new data record to database, open **Add** page and submit given form. In case of invalid data given, server will return 400 error (bad request) and propper error page will be loaded.

<img src="https://github.com/BartlomiejCzerwinski/irises-analysis/assets/84719721/1bfdf49d-ee95-4a42-a64d-d409771d9d4b"></src>

## Predict iris class
Open **Predict** page to predict class of given data. Firstly, fill and submit point with continous values (in case of invalid data propper error will be returned). After submit, the server will calculate class of data using
K Nearest Neighbours algorithm.
**NOTE:** If you want use predict function of app, you have to have at least 3 objects in database (actual version of an application uses 3 neighbours for class prediction). In other case, propper error will be given.

<img src="https://github.com/BartlomiejCzerwinski/irises-analysis/assets/84719721/4ee34ba9-21f7-4c87-8771-d3c06f2cefe8"></img>
<img src="https://github.com/BartlomiejCzerwinski/irises-analysis/assets/84719721/1faaa882-9e9c-4c1e-a9fa-81a6bba39a50"></img>


