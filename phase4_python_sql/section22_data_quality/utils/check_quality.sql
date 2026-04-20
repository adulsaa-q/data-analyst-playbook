--shopee_order_items_thailand
SELECT * FROM shopee_order_items_thailand LIMIT 10;
--shopee_orders_thailand
SELECT * FROM shopee_orders_thailand LIMIT 10;


SELECT column_name 
FROM information_schema.columns 
WHERE table_name = 'shopee_order_items_thailand';