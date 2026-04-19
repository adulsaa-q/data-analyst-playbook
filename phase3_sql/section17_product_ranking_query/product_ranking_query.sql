WITH product_revenue AS (
    SELECT  
        pd.product_name,
        SUM(line_total) AS total_revenue
    FROM shopee_products_thailand AS pd
    JOIN shopee_order_items_thailand AS oi
        ON pd.product_id = oi.product_id
    GROUP BY pd.product_name
)

SELECT  
    product_name,
    total_revenue,

    RANK() OVER (
        ORDER BY total_revenue DESC
    ) AS rank,
    -- rank with gaps (ties will skip numbers)

    ROW_NUMBER() OVER (
        ORDER BY total_revenue DESC
    ) AS row_num,
    -- unique ordering (no ties)

    DENSE_RANK() OVER (
        ORDER BY total_revenue DESC
    ) AS dense_rank,
    -- rank without gaps

    NTILE(4) OVER (
        ORDER BY total_revenue DESC
    ) AS quartile
    -- split into 4 buckets (top 25%, etc.)

FROM product_revenue
ORDER BY total_revenue DESC;