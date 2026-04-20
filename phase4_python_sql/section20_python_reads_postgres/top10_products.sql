SELECT  p.product_name,
        SUM(oi.line_total) AS total_revenue
FROM shopee_products_thailand AS p
JOIN shopee_order_items_thailand AS oi 
ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY total_revenue DESC LIMIT 10;