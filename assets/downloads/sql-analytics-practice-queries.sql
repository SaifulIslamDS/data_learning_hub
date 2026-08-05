-- SQL Analytics practice queries. Run after sql-analytics-practice-database.sql

-- 01. Welcome to SQL for Data Analytics
SELECT order_id, order_date, status FROM orders ORDER BY order_date DESC LIMIT 5;

-- 02. Relational Databases and Tables
SELECT name AS table_name FROM sqlite_master WHERE type='table' ORDER BY name;

-- 03. SQL Dialects: PostgreSQL and SQLite
SELECT strftime('%Y-%m-01', order_date) AS month, COUNT(*) AS orders FROM orders GROUP BY 1 ORDER BY 1;

-- 04. Explore the Practice Database Schema
PRAGMA table_info('orders');

-- 05. SELECT Fundamentals
SELECT customer_id, customer_name, segment FROM customers ORDER BY customer_id LIMIT 10;

-- 06. Aliases, Comments, and Readable Formatting
SELECT o.order_id, o.order_date AS purchased_on, o.status FROM orders AS o WHERE o.status IN ('Completed','Shipped') ORDER BY o.order_id LIMIT 8;

-- 07. Logical Query Processing Order
SELECT region, COUNT(*) AS order_count FROM orders WHERE status <> 'Cancelled' GROUP BY region HAVING COUNT(*) >= 2 ORDER BY order_count DESC;

-- 08. DISTINCT Values
SELECT DISTINCT region, channel FROM orders ORDER BY region, channel;

-- 09. Filter Rows with WHERE
SELECT order_id, order_date, region, status FROM orders WHERE region='Dhaka' ORDER BY order_date;

-- 10. Comparison Operators
SELECT product_id, product_name, list_price FROM products WHERE list_price >= 50 ORDER BY list_price DESC;

-- 11. Combine Conditions with AND, OR, and NOT
SELECT order_id, region, channel, status FROM orders WHERE region='Dhaka' AND (channel='Online' OR channel='Retail') AND NOT status='Cancelled' ORDER BY order_id;

-- 12. IN and BETWEEN
SELECT order_id, order_date, region FROM orders WHERE region IN ('Dhaka','Chattogram') AND order_date BETWEEN '2026-01-01' AND '2026-03-31' ORDER BY order_date;

-- 13. LIKE and Pattern Matching
SELECT customer_id, customer_name, city FROM customers WHERE customer_name LIKE 'A%' ORDER BY customer_name;

-- 14. NULL and Three-Valued Logic
SELECT customer_id, customer_name, city FROM customers WHERE city IS NULL ORDER BY customer_id;

-- 15. ORDER BY, LIMIT, and OFFSET
SELECT order_id, order_date, region, status FROM orders ORDER BY order_date DESC, order_id DESC LIMIT 10 OFFSET 0;

-- 16. Arithmetic Expressions
SELECT order_item_id, quantity, unit_price, discount_pct, ROUND(quantity*unit_price*(1-discount_pct),2) AS net_revenue FROM order_items ORDER BY order_item_id LIMIT 12;

-- 17. CASE Expressions
SELECT order_id, status, channel, CASE WHEN status='Cancelled' THEN 'Excluded' WHEN channel='Online' THEN 'Digital' ELSE 'Store-assisted' END AS order_group FROM orders ORDER BY order_id LIMIT 15;

-- 18. COALESCE and NULLIF
SELECT customer_id, customer_name, COALESCE(city,'Unknown') AS city_label FROM customers ORDER BY customer_id;

-- 19. String Functions
SELECT customer_id, customer_name, UPPER(TRIM(customer_name)) AS standardized_name, LENGTH(customer_name) AS name_length FROM customers ORDER BY customer_id LIMIT 12;

-- 20. Date and Time Functions
SELECT strftime('%Y-%m', order_date) AS order_month, COUNT(*) AS orders FROM orders GROUP BY order_month ORDER BY order_month;

-- 21. Type Conversion and CAST
SELECT product_id, product_name, list_price, CAST(list_price AS REAL) AS numeric_price FROM products ORDER BY product_id;

-- 22. Conditional Aggregation
SELECT region, COUNT(*) AS all_orders, SUM(CASE WHEN status='Cancelled' THEN 1 ELSE 0 END) AS cancelled_orders FROM orders GROUP BY region ORDER BY region;

-- 23. Profile Data Quality with SQL
SELECT COUNT(*) AS rows, SUM(CASE WHEN city IS NULL THEN 1 ELSE 0 END) AS missing_city, COUNT(DISTINCT customer_id) AS unique_customers FROM customers;

-- 24. Aggregate Functions
SELECT COUNT(*) AS orders, MIN(order_date) AS first_order, MAX(order_date) AS last_order FROM orders;

-- 25. GROUP BY
SELECT region, COUNT(*) AS order_count FROM orders GROUP BY region ORDER BY order_count DESC;

-- 26. Filter Groups with HAVING
SELECT customer_id, COUNT(*) AS orders FROM orders GROUP BY customer_id HAVING COUNT(*) >= 3 ORDER BY orders DESC, customer_id;

-- 27. Group by Multiple Dimensions
SELECT region, channel, status, COUNT(*) AS orders FROM orders GROUP BY region, channel, status ORDER BY region, channel, status;

-- 28. Ratios, Percentages, and Average Order Value
SELECT COUNT(*) AS orders, SUM(CASE WHEN status='Cancelled' THEN 1 ELSE 0 END) AS cancelled, ROUND(100.0*SUM(CASE WHEN status='Cancelled' THEN 1 ELSE 0 END)/NULLIF(COUNT(*),0),2) AS cancellation_rate FROM orders;

-- 29. Detect Duplicates with GROUP BY
SELECT customer_name, signup_date, COUNT(*) AS copies FROM customers GROUP BY customer_name, signup_date HAVING COUNT(*) > 1 ORDER BY copies DESC;

-- 30. Aggregation Pitfalls
SELECT o.order_id, COUNT(*) AS item_rows, ROUND(SUM(oi.quantity*oi.unit_price),2) AS gross_value FROM orders o JOIN order_items oi ON oi.order_id=o.order_id GROUP BY o.order_id ORDER BY o.order_id LIMIT 12;

-- 31. Keys and Table Relationships
SELECT COUNT(*) AS rows, COUNT(DISTINCT order_id) AS unique_orders FROM orders;

-- 32. INNER JOIN
SELECT o.order_id, c.customer_name, o.order_date, o.region FROM orders o INNER JOIN customers c ON c.customer_id=o.customer_id ORDER BY o.order_id LIMIT 15;

-- 33. LEFT JOIN
SELECT c.customer_id, c.customer_name, COUNT(o.order_id) AS orders FROM customers c LEFT JOIN orders o ON o.customer_id=c.customer_id GROUP BY c.customer_id,c.customer_name ORDER BY orders, c.customer_id;

-- 34. Join Multiple Tables
SELECT o.order_id, c.segment, p.category, oi.quantity, oi.unit_price FROM orders o JOIN customers c ON c.customer_id=o.customer_id JOIN order_items oi ON oi.order_id=o.order_id JOIN products p ON p.product_id=oi.product_id ORDER BY o.order_id LIMIT 18;

-- 35. Self Joins
SELECT e.employee_id, e.employee_name, m.employee_name AS manager_name, e.team FROM employees e LEFT JOIN employees m ON m.employee_id=e.manager_id ORDER BY e.employee_id;

-- 36. CROSS JOIN
SELECT r.region, c.channel FROM (SELECT DISTINCT region FROM orders) r CROSS JOIN (SELECT DISTINCT channel FROM orders) c ORDER BY r.region,c.channel;

-- 37. UNION and UNION ALL
SELECT 'Customer' AS entity, customer_name AS name FROM customers UNION ALL SELECT 'Employee', employee_name FROM employees ORDER BY entity,name LIMIT 25;

-- 38. EXISTS, Semi Joins, and Anti Joins
SELECT c.customer_id, c.customer_name FROM customers c WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.customer_id=c.customer_id) ORDER BY c.customer_id;

-- 39. Debug and Reconcile Joins
SELECT (SELECT COUNT(*) FROM orders) AS order_rows, (SELECT COUNT(DISTINCT order_id) FROM order_items) AS orders_with_items, (SELECT COUNT(*) FROM orders o WHERE NOT EXISTS (SELECT 1 FROM order_items i WHERE i.order_id=o.order_id)) AS orders_without_items;

-- 40. Scalar Subqueries
SELECT product_id, product_name, list_price FROM products WHERE list_price>(SELECT AVG(list_price) FROM products) ORDER BY list_price DESC;

-- 41. Subqueries in FROM
SELECT region, ROUND(AVG(order_value),2) AS average_order_value FROM (SELECT o.order_id,o.region,SUM(oi.quantity*oi.unit_price*(1-oi.discount_pct)) AS order_value FROM orders o JOIN order_items oi ON oi.order_id=o.order_id GROUP BY o.order_id,o.region) q GROUP BY region ORDER BY region;

-- 42. Correlated Subqueries
SELECT p.product_id,p.product_name,p.category,p.list_price FROM products p WHERE p.list_price>(SELECT AVG(p2.list_price) FROM products p2 WHERE p2.category=p.category) ORDER BY p.category,p.list_price DESC;

-- 43. EXISTS Subqueries
SELECT p.product_id,p.product_name FROM products p WHERE EXISTS (SELECT 1 FROM order_items oi WHERE oi.product_id=p.product_id) ORDER BY p.product_id;

-- 44. Common Table Expressions
WITH order_totals AS (SELECT order_id,SUM(quantity*unit_price*(1-discount_pct)) AS revenue FROM order_items GROUP BY order_id) SELECT ROUND(AVG(revenue),2) AS average_order_value FROM order_totals;

-- 45. Recursive CTEs
WITH RECURSIVE hierarchy(employee_id,employee_name,manager_id,level) AS (SELECT employee_id,employee_name,manager_id,0 FROM employees WHERE manager_id IS NULL UNION ALL SELECT e.employee_id,e.employee_name,e.manager_id,h.level+1 FROM employees e JOIN hierarchy h ON e.manager_id=h.employee_id) SELECT * FROM hierarchy ORDER BY level,employee_id;

-- 46. Modular Query Design
WITH valid_orders AS (SELECT * FROM orders WHERE status<>'Cancelled'), order_totals AS (SELECT o.customer_id,o.order_id,SUM(oi.quantity*oi.unit_price*(1-oi.discount_pct)) AS revenue FROM valid_orders o JOIN order_items oi ON oi.order_id=o.order_id GROUP BY o.customer_id,o.order_id), customer_metrics AS (SELECT customer_id,COUNT(*) AS orders,SUM(revenue) AS revenue FROM order_totals GROUP BY customer_id) SELECT * FROM customer_metrics ORDER BY revenue DESC;

-- 47. Window Function Foundations
SELECT order_id,region,order_date,COUNT(*) OVER (PARTITION BY region) AS region_orders FROM orders ORDER BY region,order_date,order_id LIMIT 25;

-- 48. ROW_NUMBER, RANK, and DENSE_RANK
SELECT product_id,product_name,category,list_price,DENSE_RANK() OVER (PARTITION BY category ORDER BY list_price DESC) AS price_rank FROM products ORDER BY category,price_rank,product_id;

-- 49. Running Totals
WITH daily AS (SELECT order_date,COUNT(*) AS orders FROM orders GROUP BY order_date) SELECT order_date,orders,SUM(orders) OVER (ORDER BY order_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_orders FROM daily ORDER BY order_date;

-- 50. Moving Averages
WITH daily AS (SELECT order_date,COUNT(*) AS orders FROM orders GROUP BY order_date) SELECT order_date,orders,ROUND(AVG(orders) OVER (ORDER BY order_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW),2) AS moving_average FROM daily ORDER BY order_date;

-- 51. LAG and LEAD
WITH monthly AS (SELECT strftime('%Y-%m',order_date) AS month,COUNT(*) AS orders FROM orders GROUP BY 1) SELECT month,orders,LAG(orders) OVER (ORDER BY month) AS previous_orders, orders-LAG(orders) OVER (ORDER BY month) AS change FROM monthly ORDER BY month;

-- 52. FIRST_VALUE and LAST_VALUE
SELECT customer_id,order_id,order_date,FIRST_VALUE(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS first_order FROM orders ORDER BY customer_id,order_date;

-- 53. NTILE and Percentile Bands
WITH customer_revenue AS (SELECT o.customer_id,SUM(oi.quantity*oi.unit_price*(1-oi.discount_pct)) AS revenue FROM orders o JOIN order_items oi ON oi.order_id=o.order_id WHERE o.status<>'Cancelled' GROUP BY o.customer_id) SELECT customer_id,ROUND(revenue,2) AS revenue,NTILE(4) OVER (ORDER BY revenue DESC) AS value_quartile FROM customer_revenue ORDER BY revenue DESC;

-- 54. Top N per Group
WITH ranked AS (SELECT product_id,product_name,category,list_price,ROW_NUMBER() OVER (PARTITION BY category ORDER BY list_price DESC,product_id) AS rn FROM products) SELECT * FROM ranked WHERE rn<=2 ORDER BY category,rn;

-- 55. Cohort Retention with SQL
WITH first_order AS (SELECT customer_id,MIN(strftime('%Y-%m',order_date)) AS cohort_month FROM orders WHERE status<>'Cancelled' GROUP BY customer_id), activity AS (SELECT o.customer_id,f.cohort_month,(CAST(strftime('%Y',o.order_date) AS INTEGER)-CAST(substr(f.cohort_month,1,4) AS INTEGER))*12+(CAST(strftime('%m',o.order_date) AS INTEGER)-CAST(substr(f.cohort_month,6,2) AS INTEGER)) AS period_number FROM orders o JOIN first_order f ON f.customer_id=o.customer_id WHERE o.status<>'Cancelled') SELECT cohort_month,period_number,COUNT(DISTINCT customer_id) AS active_customers FROM activity GROUP BY cohort_month,period_number ORDER BY cohort_month,period_number;

-- 56. CREATE TABLE, Data Types, and Constraints
DROP TABLE IF EXISTS demo_targets; CREATE TABLE demo_targets(target_month TEXT NOT NULL,region TEXT NOT NULL,revenue_target REAL CHECK(revenue_target>=0),PRIMARY KEY(target_month,region)); INSERT INTO demo_targets VALUES('2026-07-01','Dhaka',50000); SELECT * FROM demo_targets;

-- 57. INSERT, UPDATE, and DELETE Safely
DROP TABLE IF EXISTS demo_changes; CREATE TABLE demo_changes(id INTEGER PRIMARY KEY,status TEXT); INSERT INTO demo_changes VALUES(1,'Open'),(2,'Open'); UPDATE demo_changes SET status='Closed' WHERE id=1; SELECT * FROM demo_changes ORDER BY id;

-- 58. Transactions
DROP TABLE IF EXISTS demo_tx; CREATE TABLE demo_tx(id INTEGER PRIMARY KEY,value INTEGER); BEGIN; INSERT INTO demo_tx VALUES(1,100); UPDATE demo_tx SET value=120 WHERE id=1; COMMIT; SELECT * FROM demo_tx;

-- 59. Views
DROP VIEW IF EXISTS demo_completed_orders; CREATE VIEW demo_completed_orders AS SELECT order_id,customer_id,order_date,region FROM orders WHERE status='Completed'; SELECT * FROM demo_completed_orders ORDER BY order_id LIMIT 10;

-- 60. Indexes and EXPLAIN
EXPLAIN QUERY PLAN SELECT * FROM orders WHERE customer_id=10 ORDER BY order_date;

-- 61. Star Schema for Analytics
SELECT p.category,ROUND(SUM(oi.quantity*oi.unit_price*(1-oi.discount_pct)),2) AS net_sales FROM order_items oi JOIN products p ON p.product_id=oi.product_id GROUP BY p.category ORDER BY net_sales DESC;

-- 62. Project: Sales KPI Scorecard
WITH order_totals AS (SELECT o.order_id,SUM(oi.quantity*oi.unit_price*(1-oi.discount_pct)) AS revenue FROM orders o JOIN order_items oi ON oi.order_id=o.order_id WHERE o.status<>'Cancelled' GROUP BY o.order_id) SELECT COUNT(*) AS orders,ROUND(SUM(revenue),2) AS revenue,ROUND(AVG(revenue),2) AS average_order_value FROM order_totals;

-- 63. Project: Customer Segmentation
WITH customer_metrics AS (SELECT c.customer_id,c.customer_name,COUNT(DISTINCT o.order_id) AS orders,MAX(o.order_date) AS last_order,COALESCE(SUM(oi.quantity*oi.unit_price*(1-oi.discount_pct)),0) AS revenue FROM customers c LEFT JOIN orders o ON o.customer_id=c.customer_id AND o.status<>'Cancelled' LEFT JOIN order_items oi ON oi.order_id=o.order_id GROUP BY c.customer_id,c.customer_name) SELECT customer_id,customer_name,orders,last_order,ROUND(revenue,2) AS revenue,NTILE(4) OVER (ORDER BY revenue DESC) AS value_band FROM customer_metrics ORDER BY revenue DESC;

-- 64. Project: Funnel Analysis
SELECT campaign,COUNT(DISTINCT CASE WHEN event_name='visit' THEN customer_id END) AS visitors,COUNT(DISTINCT CASE WHEN event_name='product_view' THEN customer_id END) AS viewers,COUNT(DISTINCT CASE WHEN event_name='add_to_cart' THEN customer_id END) AS carts,COUNT(DISTINCT CASE WHEN event_name='purchase' THEN customer_id END) AS purchasers FROM web_events GROUP BY campaign ORDER BY campaign;

-- 65. Project: SQL Data Quality Audit
SELECT 'missing_customer_city' AS check_name,COUNT(*) AS failures FROM customers WHERE city IS NULL UNION ALL SELECT 'orphan_orders',COUNT(*) FROM orders o LEFT JOIN customers c ON c.customer_id=o.customer_id WHERE c.customer_id IS NULL UNION ALL SELECT 'orphan_items',COUNT(*) FROM order_items i LEFT JOIN orders o ON o.order_id=i.order_id WHERE o.order_id IS NULL UNION ALL SELECT 'invalid_discount',COUNT(*) FROM order_items WHERE discount_pct<0 OR discount_pct>1;

-- 66. Final Project: Retail SQL Analytics Portfolio
WITH order_totals AS (SELECT o.order_id,o.customer_id,o.order_date,o.region,SUM(oi.quantity*oi.unit_price*(1-oi.discount_pct)) AS revenue FROM orders o JOIN order_items oi ON oi.order_id=o.order_id WHERE o.status<>'Cancelled' GROUP BY o.order_id,o.customer_id,o.order_date,o.region), monthly AS (SELECT strftime('%Y-%m',order_date) AS month,COUNT(*) AS orders,SUM(revenue) AS revenue,AVG(revenue) AS aov FROM order_totals GROUP BY 1) SELECT month,orders,ROUND(revenue,2) AS revenue,ROUND(aov,2) AS aov,LAG(ROUND(revenue,2)) OVER (ORDER BY month) AS previous_revenue FROM monthly ORDER BY month;
