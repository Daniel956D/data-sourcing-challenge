# data-sourcing-challenge
Sources for the README Page:

NASA API DocumentationURL: https://api.nasa.gov/The NASA API documentation provides detailed information on how to use the DONKI (Space Weather Database Of Notifications, Knowledge, Information) API. It includes guidance on endpoints, parameters, and authentication required for accessing CME and GST data.

Pandas DocumentationURL: https://pandas.pydata.org/pandas-docs/stable/The Pandas documentation is helpful for understanding various methods used for data transformation, such as .dropna(), .explode(), and .merge(). This project relies heavily on Pandas for data wrangling and analysis.

Python Requests Library DocumentationURL: https://docs.python-requests.org/en/master/This project uses the Requests library to make HTTP requests to the NASA API. The documentation explains how to use different request types and handle API responses.

Python DotenvURL: https://pypi.org/project/python-dotenv/The dotenv library is used to load environment variables from the .env file. This helps manage the API key securely.

PrettyTable DocumentationURL: https://pypi.org/project/PrettyTable/PrettyTable was used to display intermediate data in a tabular format for better visualization during the development process.

Additional Information for the Professor:

This project is aimed at analyzing the time it takes for Coronal Mass Ejections (CMEs) to trigger Geomagnetic Storms (GSTs) using NASA's DONKI API. Below are some key aspects of the project that might be of interest:

Data Transformation and Processing:

The project utilizes two types of solar activity data, namely CMEs and GSTs, retrieved using two separate API requests.

These datasets are expanded to handle nested lists within the API response using .explode() and for-loop operations, ensuring that each row is properly represented for further analysis.

Key Analysis Conducted:

The main analysis performed in the project involves calculating the time difference between CME and GST occurrences. This helps to understand the lag between these two types of solar events.

Summary statistics such as mean and median are computed for this time difference, giving insights into the average and typical delay from the cause (CME) to the effect (GST).

Error Handling and Data Cleaning:

Data from the NASA API is handled carefully, with try-except blocks used to manage potential errors during data extraction.

Rows with missing values are dropped strategically to ensure data quality, while specific columns are converted to appropriate formats for accurate calculations (e.g., datetime conversion).

Output and Use Case:

The final dataset is exported to a CSV file, which can be used for further analysis or visualization.

This analysis can be helpful in predicting space weather effects and understanding the impact of solar activity on Earth's geomagnetic environment.

Challenges and Solutions:

One challenge faced was managing nested dictionary lists within the linkedEvents column. This was solved by expanding these nested lists and creating a structured DataFrame from them.

Another challenge involved data type mismatches during arithmetic operations between timestamps, which was resolved by explicitly converting all relevant columns to datetime format.

Potential Improvements:

Future iterations of this project could involve visualizing the data using tools like Matplotlib or Seaborn to provide a more intuitive understanding of trends.

More features could be extracted, such as correlating the severity of GSTs to specific CMEs, potentially using machine learning techniques.

This project is an excellent demonstration of applying data science techniques to real-world datasets, showcasing data acquisition, cleaning, transformation, merging, and finally analyzing patterns that impact the Earth's environment.
