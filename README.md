
# Retail Order  Analysis

## **Overview**
This project aims to analyze and optimize sales performance by identifying key trends, top-performing products, and growth opportunities. Using **Python, SQL, and Streamlit**, we extract insights from a retail sales dataset obtained via the **Kaggle API**.

## **📌 Skills Takeaway**
- Kaggle API for data retrieval  
- Python (Pandas, SQLAlchemy) for data cleaning & analysis  
- SQL for querying & extracting business insights  
- Streamlit for interactive data visualization  

---

## **📂 Project Structure**
This project is organized as follows:

Retail-Order-Analysis/ │── retailanalysisproject.ipynb # Jupyter Notebook for data analysis │── streamdemo.py # Streamlit app for visualization │── README.md # Project documentation │── requirements.txt # Python dependencies


### **📜 Explanation of Each File**
| **File**                     | **Purpose** |
|------------------------------|------------|
| `retailanalysisproject.ipynb` | Jupyter Notebook for cleaning,and analyzing data. |
| `streamdemo.py`               | Streamlit app to display insights in an interactive dashboard. |
| `README.md`                   | Documentation explaining the project. |

---

## **🛠 Tools & Technologies**
- **Python** (`pandas`,  `kaggle`)
- **SQL Server** (for data storage and queries)
- **Streamlit** (for visualizing sales insights)
- **Kaggle API** (to fetch datasets)

---

## **📊 Problem Statement**
The objective of this project is to analyze sales data to:

✅ Identify the top-selling products and categories contributing the most to revenue  
✅ Analyze **Year-over-Year (YoY)** and **Month-over-Month (MoM)** sales trends  
✅ Find high-profit-margin subcategories  
✅ Perform **regional sales analysis**  
✅ Analyze the impact of **discounts** on sales  

---

## **🌐 Data Extraction (Kaggle API)**
To get the dataset from Kaggle, run:
```bash
!kaggle datasets download ankitbansal06/retail-orders -f orders.csv
```
This step: 

✔️ Fetches the dataset using Kaggle API

✔️ Saves it in the /data/ directory for further analysis

Once downloaded, load the dataset into a Jupyter Notebook or Python script for further processing.

## **🌐 Data Cleaning & Preprocessing**

After extracting the data, we clean and enhance it using Pandas:

✅ Cleaning Steps:

Handling Missing Values → Fill or drop missing values where necessary.

Renaming Columns → Standardizing column names for better readability.

Trimming Spaces → Removing unwanted spaces in text columns.

Deriving New Columns → 

- discount → To analyze discounts on products.

- sale_price → Sale price after applying discounts.

- profit → To measure profitability of each sale.

## **🔍 SQL Analysis & Queries**
Once cleaned, the dataset is moved to SQL Server for better analysis. Key SQL queries:

1.Find top 10 highest revenue-generating products

2.Top 5 cities with the highest profit margins

3.Total discount per category

4.Average sale price per category

5.Region with the highest average sale price

6.Total profit per category

7.Top 3 segments with the highest order quantity

8.Average discount percentage per region

9.Product category with the highest profit

10.Total revenue generated per year

11.All order details for the first quater of the year 2022 

12.Highest profit product for each category in each state and region

13.Profit range (min and max) per month for each year

14.Segment with the highest total quantity of orders

15.Category and sub-category with the highest total quantity and its max discount percentage

16.Rank product sub-categories based on total revenue

17.Classify product sub-categories based on total revenue performance

18.Average discount, total sales, and revenue lost by category and sub-category (for discounts > 3%)

19.Date(s) with the highest total revenue"

20.Retrieve the top 10 highest spending orders"

📌 Refer to streamdemo.py for complete queries.

## **📈Streamlit Dashboard**

A Streamlit web app is built to visualize insights interactively.

How to Run Streamlit App

Install dependencies:
```bash
pip install streamlit
```
Run the Streamlit app:
```bash
streamlit run app/streamlit_app.py
```



