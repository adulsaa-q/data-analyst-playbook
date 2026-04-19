WITH monthly_revenue AS (
    SELECT  
        DATE_TRUNC('month', order_date::date) AS month,  -- group by month
        SUM(total_amount) AS revenue
    FROM shopee_orders_thailand
    GROUP BY 1
),

calc AS (
    SELECT
        month,
        revenue,
        LAG(revenue) OVER (ORDER BY month) AS prev_revenue
        -- previous month revenue
    FROM monthly_revenue
)

SELECT 
    TO_CHAR(month, 'YYYY-MM') AS month,
    revenue,
    prev_revenue,

    ROUND(
        ((revenue - prev_revenue) * 100.0 / prev_revenue)::numeric,
        2
    ) AS pct_change,
    -- % growth vs previous month

    CASE 
        WHEN prev_revenue IS NULL THEN 'N/A'   -- first row
        WHEN revenue > prev_revenue THEN 'UP'
        WHEN revenue < prev_revenue THEN 'DOWN'
        ELSE 'FLAT'
    END AS trend
    -- simple trend label

FROM calc
ORDER BY month;