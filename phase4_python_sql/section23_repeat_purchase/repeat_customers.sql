SELECT  customer_id,
        ROUND(SUM(total_amount::numeric),2) AS total_amount,
        COUNT(order_id) AS total_order 
FROM shopee_orders_thailand
GROUP BY customer_id
ORDER BY total_amount DESC;
