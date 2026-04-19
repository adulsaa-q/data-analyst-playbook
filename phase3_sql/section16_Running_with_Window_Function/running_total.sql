WITH daily AS (
    SELECT  
        order_date::date AS order_date,  -- cast to date for proper sorting + date math
        SUM(total_amount) AS daily_revenue  -- revenue per day
    FROM shopee_orders_thailand
    GROUP BY order_date::date
)

SELECT  
    order_date,

    ROUND(daily_revenue::numeric, 2) AS daily_revenue,  
    -- keep 2 decimals (cast needed for postgres round)

    ROUND(
        (SUM(daily_revenue) OVER (ORDER BY order_date))::numeric,
        2
    ) AS running_total,  
    -- cumulative revenue over time

    ROUND(
        (
            (SUM(daily_revenue) OVER (ORDER BY order_date) * 100.0)
            / SUM(daily_revenue) OVER ()
        )::numeric,
        2
    ) AS pct_of_total,  
    -- % of total revenue reached so far

    (order_date - MIN(order_date) OVER ()) AS days_elapsed  
    -- days since first date (day 0, day 1, ...)

FROM daily
ORDER BY order_date;