import streamlit as st
import sys
import pandas as pd
import pymysql
st.title("retail analysis")
myconnection = pymysql.connect(host='127.0.0.1',user='root',passwd='Suveeswar@06',database="retailorders")
cursor=myconnection.cursor()
Question = st.selectbox("Queries:",("1. Top 10 highest revenue generating products","2. Top 5 cities with the highest profit margins","3. Total discount given for each category","4. Average sale price per product category","5. Region with the highest average sale price", "6. Total profit per category", "7. Top 3 segments with the highest quantity of orders", "8. Average discount percentage given per region", "9. Product category with the highest total profit", "10. Calculate the total revenue generated per year" ,"11. All order details for the first quater of the year 2022" , "12. Highest profit product for each category in each state and region","13. Profit range (min and max) per month for each year","14. Segment with the highest total quantity of orders", "15. Category and sub-category with the highest total quantity and its max discount percentage","16. Rank product sub-categories based on total revenue", "17. Classify product sub-categories based on total revenue performance" ,"18. Average discount, total sales, and revenue lost by category and sub-category (for discounts > 3%)" ,"19. Date(s) with the highest total revenue","20. Retrieve the top 10 highest spending orders"),index=None,placeholder="Select your query ......")
st.write(Question)

if Question == "1. Top 10 highest revenue generating products":
    cursor.execute("""SELECT sub_category, round(SUM(sale_price * quantity)) AS total_revenue
            FROM retailorders.orders
            GROUP BY sub_category
            ORDER BY total_revenue DESC
            LIMIT 10;""")
    result1=cursor.fetchall()
    df1=pd.DataFrame(result1,columns=["sub_category","total_revenue"])
    st.dataframe(df1)
elif Question == "2. Top 5 cities with the highest profit margins":
    cursor.execute("""
            SELECT city, round(sum(profit*quantity) / SUM(sale_price * quantity) * 100,2) as profit_margin
            FROM retailorders.orders 
            GROUP BY city
            ORDER BY profit_margin DESC 
            LIMIT 5;""")
    result2=cursor.fetchall()
    df2=pd.DataFrame(result2,columns=["city","profit_margin"])
    st.dataframe(df2)
elif Question == "3. Total discount given for each category":
    cursor.execute("""SELECT category,sub_category, round(sum(discount_price*quantity),2) as total_discount 
            FROM retailorders.orders 
            GROUP BY category,sub_category
            ORDER BY total_discount DESC;""")
    result3=cursor.fetchall()
    df3=pd.DataFrame(result3,columns=["category","sub_category","total_discount"])
    st.dataframe(df3)
elif Question == "4. Average sale price per product category":
    cursor.execute("""SELECT sub_category, round(avg(sale_price),2) as avg_sale_price 
            FROM retailorders.orders 
            GROUP BY sub_category
            ORDER BY avg_sale_price DESC;""")
    result4=cursor.fetchall()
    df4=pd.DataFrame(result4,columns=["sub_category","avg_sale_price"])
    st.dataframe(df4)
elif Question == "5. Region with the highest average sale price":
    cursor.execute("""SELECT region, round(avg(sale_price),2) as avg_sale_price_per_region
            FROM retailorders.orders 
            GROUP BY region
            ORDER BY avg_sale_price_per_region  DESC
            lIMIT 1;""")
    result5=cursor.fetchall()
    df5=pd.DataFrame(result5,columns=["region","avg_sale_price_per_region"])
    st.dataframe(df5)
elif Question == "6. Total profit per category":
    cursor.execute("""SELECT category, round(sum(profit*quantity),2) as tot_profit_per_category
            FROM retailorders.orders 
            GROUP BY category
            ORDER BY tot_profit_per_category DESC;""")
    result6=cursor.fetchall()
    df6=pd.DataFrame(result6,columns=["category","tot_profit_per_category"])
    st.dataframe(df6)
elif Question == "7. Top 3 segments with the highest quantity of orders":
    cursor.execute("""SELECT segment,cast(sum(quantity) as signed) as total_quantity
            FROM retailorders.orders 
            GROUP BY segment
            ORDER BY total_quantity DESC
            LIMIT 3;""")
    result7=cursor.fetchall()
    df7=pd.DataFrame(result7,columns=["segment","total_quantity"])
    st.dataframe(df7)
elif Question == "8. Average discount percentage given per region":
    cursor.execute("""SELECT region,CAST(avg(discount_percent) AS FLOAT) as avg_dis_percent
            FROM retailorders.orders 
            GROUP BY region
            ORDER BY avg_dis_percent;""")
    result8=cursor.fetchall()
    df8=pd.DataFrame(result8,columns=["region","avg_dis_percent"])
    st.dataframe(df8)
elif Question == "9. Product category with the highest total profit":
    cursor.execute("""SELECT category,sub_category,round(sum(profit*quantity),2) as high_profit
            FROM retailorders.orders 
            GROUP BY category, sub_category
            ORDER BY high_profit DESC
            LIMIT 1;""")
    result9=cursor.fetchall()
    df9=pd.DataFrame(result9,columns=["category","sub_category","high_profit"])
    st.dataframe(df9)
elif Question == "10. Calculate the total revenue generated per year":
    cursor.execute("""SELECT year(order_date) as years,round(sum(sale_price*quantity),2) as rev_per_year
            FROM retailorders.orders 
            GROUP BY  years 
            ORDER BY years DESC;""")
    result10=cursor.fetchall()
    df10=pd.DataFrame(result10,columns=["years","rev_per_year"])
    st.dataframe(df10)
elif Question == "11. All order details for the first quater of the year 2022":
    cursor.execute("""SELECT distinctrow a.order_id, a.order_date,a.ship_mode,a.segment,a.country, a.city,a.state,a.postal_code,a.region,a.sub_category,a.category, round(b.profit*b.quantity) as tot_profit 
            FROM retailorders.rodetails a  
            JOIN retailorders.roprice b ON a.order_id = b.order_id
            WHERE a.order_date BETWEEN '2022-01-01' AND '2022-04-31' ;""")
    result11=cursor.fetchall()
    df11=pd.DataFrame(result11,columns=["order_id","order_date","ship_mode","segment","country","city","state","postal_code","region","sub_category","category", "tot_profit"])
    st.dataframe(df11)
elif Question ==   "12. Highest profit product for each category in each state and region":
    cursor.execute("""SELECT a.state,a.region,a.category,ROUND(SUM(b.profit * b.quantity),2) as profit_amt 
            from retailorders.rodetails a  
            LEFT JOIN retailorders.roprice b 
            ON a.order_id = b.order_id 
            GROUP BY a.state,a.region,a.category 
            ORDER BY profit_amt DESC ;""")
    result12=cursor.fetchall()
    df12=pd.DataFrame(result12,columns=["state","region","category","profit_amt"])
    st.dataframe(df12)
elif Question == "13. Profit range (min and max) per month for each year":
    cursor.execute("""SELECT year(a.order_date) as year,month(a.order_date) as month,round(sum(b.profit*b.quantity)) as monthly_profit,
            ROUND(MIN(b.profit * b.quantity), 2) AS min_profit,
            ROUND(MAX(b.profit * b.quantity), 2) AS max_profit
            from retailorders.rodetails a  
            inner JOIN retailorders.roprice b 
            ON a.order_id = b.order_id 
            GROUP BY month,year
            ORDER BY year asc,month asc;""")
    result13=cursor.fetchall()
    df13=pd.DataFrame(result13,columns=["year","month","monthly_profit","min_profit","max_profit"])
    st.dataframe(df13)
elif Question == "14. Segment with the highest total quantity of orders":
    cursor.execute("""select a.segment, cast(sum(b.quantity) as float) as tot_quantity 
            from retailorders.rodetails a  
            inner JOIN retailorders.roprice b 
            ON a.order_id = b.order_id 
            GROUP BY a.segment 
            ORDER BY tot_quantity desc;""")
    result14=cursor.fetchall()
    df14=pd.DataFrame(result14,columns=["segment","tot_quantity"])
    st.dataframe(df14)
elif Question == "15. Category and sub-category with the highest total quantity and its max discount percentage":
    cursor.execute("""WITH TopCategory AS (SELECT a.CATEGORY, a.SUB_CATEGORY
            FROM retailorders.rodetails a join retailorders.roprice b on a.order_id=b.order_id 
            GROUP BY a.CATEGORY, a.SUB_CATEGORY
            ORDER BY SUM(b.QUANTITY) DESC
            LIMIT 1)
            SELECT A.CATEGORY, A.SUB_CATEGORY, MAX(B.DISCOUNT_PERCENT) AS MAX_DISCOUNT
            FROM retailorders.rodetails A
            JOIN retailorders.roprice B 
            ON A.ORDER_ID = B.ORDER_ID
            JOIN TopCategory T
            ON A.CATEGORY = T.CATEGORY AND A.SUB_CATEGORY = T.SUB_CATEGORY
            GROUP BY A.CATEGORY, A.SUB_CATEGORY;""")
    result15=cursor.fetchall()
    df15=pd.DataFrame(result15,columns=["sub_category","category","max_discount"])
    st.dataframe(df15)
elif Question == "16. Rank product sub-categories based on total revenue":
    cursor.execute("""WITH ProductRevenue AS (SELECT  SUB_CATEGORY, SUM(sale_price * quantity) AS total_revenue
    FROM retailorders.ORDERS
    GROUP BY SUB_CATEGORY)
    SELECT SUB_CATEGORY, total_revenue,
    ROW_NUMBER() OVER (ORDER BY total_revenue DESC) AS revenue_rank
    FROM ProductRevenue;""")
    result16=cursor.fetchall()
    df16=pd.DataFrame(result16,columns=["sub_category","total_revenue","revenue_rank"])
    st.dataframe(df16)
elif Question == "17. Classify product sub-categories based on total revenue performance":
    cursor.execute("""WITH ProductRevenue AS (SELECT SUB_CATEGORY, SUM(sale_price * quantity) AS total_revenue
            FROM RETAILORDERS.ORDERS
            GROUP BY SUB_CATEGORY)
            SELECT SUB_CATEGORY, total_revenue,
            CASE 
            WHEN total_revenue > 5000000 THEN 'High Performer'
            WHEN total_revenue BETWEEN 1000000 AND 5000000 THEN 'Medium Performer'
            ELSE 'Low Performer'
            END AS performance_category FROM ProductRevenue;""")
    result17=cursor.fetchall()
    df17=pd.DataFrame(result17,columns=["sub_category","total_revenue","product_revenue"])
    st.dataframe(df17)
elif Question =="18. Average discount, total sales, and revenue lost by category and sub-category (for discounts > 3%)" :
    cursor.execute("""SELECT a.CATEGORY,a.SUB_CATEGORY, CAST(AVG(b.discount_percent)AS FLOAT) AS avg_discount,
    CAST(ROUND(SUM(b.sale_price * b.quantity),2) AS FLOAT) AS total_sales,
    CAST(ROUND(SUM((b.sale_price * b.quantity) * (b.discount_percent / 100)),2) AS FLOAT) AS revenue_lost_due_to_discount
            FROM retailorders.rodetails as a
            LEFT JOIN retailorders.roprice as b on a.order_id = b.order_id
            WHERE discount_percent > 3
            GROUP BY CATEGORY,SUB_CATEGORY 
            ORDER BY revenue_lost_due_to_discount DESC;""")
    result18=cursor.fetchall()
    df18=pd.DataFrame(result18,columns=["category","sub_category","avg_discount","total_sales","revenue_lost_due_to_discount"])
    st.dataframe(df18)
elif Question == "19. Date(s) with the highest total revenue":
    cursor.execute("""SELECT a.order_date, round(SUM(b.quantity * b.sale_price),2) AS total_revenue
            FROM retailorders.rodetails a
            JOIN retailorders.roprice b ON a.order_id = b.order_id  
            GROUP BY a.order_date
            ORDER BY total_revenue DESC
            LIMIT 1; """)
    result19=cursor.fetchall()
    df19=pd.DataFrame(result19,columns=["order_date","total_revenue"])
    st.dataframe(df19)
elif Question == "20. Retrieve the top 10 highest spending orders":
    cursor.execute("""SELECT distinct a.order_id,a.order_date,a.ship_mode,a.country,a.city,a.state,a.region,a.category,a.sub_category,round(SUM(b.quantity * b.sale_price),2) AS total_spent
            FROM retailorders.rodetails as a
            JOIN retailorders.roprice as b ON a.order_id = b.order_id 
            GROUP BY a.order_id,a.order_date,a.ship_mode,a.country,a.city,a.state,a.region,a.category,a.sub_category
            ORDER BY total_spent DESC
            LIMIT 10;""")
    result20=cursor.fetchall()
    df20=pd.DataFrame(result20,columns=["order_id","order_date","ship_mode","country","city","state","region","category","sub_category","total_spent"])
    st.dataframe(df20)















    























    





    
                                    
