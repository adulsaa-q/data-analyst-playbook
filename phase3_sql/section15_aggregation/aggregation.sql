
-- Q1: Total revenue and order count by product
SELECT pd.product_name,
    sum(od.line_total) AS total_revenue,
    count(DISTINCT(od.order_id)) AS total_orders
FROM shopee_products_thailand AS pd
JOIN shopee_order_items_thailand AS od on pd.product_id = od.product_id
GROUP BY pd.product_name 
ORDER BY total_orders DESC;

-- Q2: Products with total revenue > 50,000
SELECT pd.product_name,
    sum(od.line_total) AS total_revenue,
    count(DISTINCT(od.order_id)) AS total_orders
FROM shopee_products_thailand AS pd
JOIN shopee_order_items_thailand AS od on pd.product_id = od.product_id
GROUP BY pd.product_name
HAVING sum(od.line_total) > 50000 
ORDER BY total_orders DESC;

-- Q3: Average quantity per product - filter product avg quantity > 1.5
SELECT  product_id,
        ROUND(avg(quantity), 2) AS avg_qty
FROM shopee_order_items_thailand
GROUP BY product_id 
HAVING avg(quantity) >= 1.5;

-- Q4: Order count by month
SELECT DATE_TRUNC('month', order_date::date) AS month,
    COUNT(order_id) AS order_count
FROM shopee_orders_thailand
GROUP BY month
ORDER BY month;