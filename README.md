# Irises Analysis
Web application for database managing and prediction class of provided data. The prediction part of an application uses machine learning (K nearest neighbors algorithm) to predict the class of provided data based on continuous features.
You can learn more about KNN HERE(https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm).

## Preview and deletion of data records
To preview records in the database open **Main page**. If you want to delete the record, click **Action** button and select proper option.

<img src="https://private-user-images.githubusercontent.com/84719721/298312036-caa4d451-1478-4327-87af-aeee8cbb20ae.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDU4MjU2NjUsIm5iZiI6MTcwNTgyNTM2NSwicGF0aCI6Ii84NDcxOTcyMS8yOTgzMTIwMzYtY2FhNGQ0NTEtMTQ3OC00MzI3LTg3YWYtYWVlZThjYmIyMGFlLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAxMjElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMTIxVDA4MjI0NVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTIwMDg5NzU1NmVlNTFiOTQ1NzU5MWM5MWM4MDA4MTViZjViM2JmZGE1ZWQ0ODBjNDdjN2Y0ZjY4YzAyZWViODcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.FlUbuHUXgItuX89z3rxWmW_qURVqWPN-qQ4vzqjGHmY"></img>

## Add new data record
To add new data record to database, open **Add** page and submit given form. In case of invalid data given, server will return 400 error (bad request) and propper error page will be loaded.

<img src="https://private-user-images.githubusercontent.com/84719721/298312033-1bfdf49d-ee95-4a42-a64d-d409771d9d4b.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDU4MjU2NjUsIm5iZiI6MTcwNTgyNTM2NSwicGF0aCI6Ii84NDcxOTcyMS8yOTgzMTIwMzMtMWJmZGY0OWQtZWU5NS00YTQyLWE2NGQtZDQwOTc3MWQ5ZDRiLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAxMjElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMTIxVDA4MjI0NVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTIwOTk1OTU4N2JkN2Y3OGZmNDk5MjlkNDRlZGNlZTJjYzY2NWRlYzY3M2UzYzcxOTA3Zjk4NTNkMzA2NTE1YWYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.WBqCxamSZvvKA7ptvb_haapN47vtOzjB3UmkySV6FGQ"></src>

## Predict iris class
Open **Predict** page to predict class of given data. Firstly, fill and submit point with continous values (in case of invalid data propper error will be returned). After submit, the server will calculate class of data using
K Nearest Neighbours algorithm.
**NOTE: ** If you want use predict function of app, you have to have at least 3 objects in database (actual version of an application uses 3 neighbours for class prediction). In other case, propper error will be given.

<img src="https://private-user-images.githubusercontent.com/84719721/298312031-4ee34ba9-21f7-4c87-8771-d3c06f2cefe8.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDU4MjU2NjUsIm5iZiI6MTcwNTgyNTM2NSwicGF0aCI6Ii84NDcxOTcyMS8yOTgzMTIwMzEtNGVlMzRiYTktMjFmNy00Yzg3LTg3NzEtZDNjMDZmMmNlZmU4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAxMjElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMTIxVDA4MjI0NVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWMwMDkwNTAxZWJhMGM5NGEyNWRhZTlhYjNhNjlkMjY4MjhiZGExNjJlYjA0MTJjMThjNjIxOTAyZGJkMzExMmMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.8Rhr51ImiFeilnmsFmoANsZOdlDgCHi15nWJJGBGjTc"></img>
<img src="https://private-user-images.githubusercontent.com/84719721/298312020-1faaa882-9e9c-4c1e-a9fa-81a6bba39a50.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDU4MjU2NjUsIm5iZiI6MTcwNTgyNTM2NSwicGF0aCI6Ii84NDcxOTcyMS8yOTgzMTIwMjAtMWZhYWE4ODItOWU5Yy00YzFlLWE5ZmEtODFhNmJiYTM5YTUwLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAxMjElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMTIxVDA4MjI0NVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTMyNzY2MmQwZThlNDRjZjZjOTM3NTEyNGU5MGQ0ZGU4MDlmNTNkYjA0Y2E2NTUxODllYzJiNmE3ZGRmNGM4ODMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.57V9avux_9FOnrqvlyj4-162Vwe4FoUThevnFgSFw3Y"></img>


