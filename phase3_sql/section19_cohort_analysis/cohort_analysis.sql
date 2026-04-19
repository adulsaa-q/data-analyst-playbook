WITH first_purchase AS (
    SELECT  
        customer_id,
        MIN(order_date::date) AS first_order_date
    FROM shopee_orders_thailand
    GROUP BY 1
),
cohort_data AS (
    SELECT
        o.customer_id,
        DATE_TRUNC('month', fp.first_order_date) AS cohort_month,
        DATE_TRUNC('month', o.order_date::date) AS order_month,

        -- months since first purchase
        (
            (EXTRACT(YEAR FROM o.order_date::date) - EXTRACT(YEAR FROM fp.first_order_date)) * 12 +
            (EXTRACT(MONTH FROM o.order_date::date) - EXTRACT(MONTH FROM fp.first_order_date))
        ) AS period_number

    FROM shopee_orders_thailand o
    JOIN first_purchase fp
        ON o.customer_id = fp.customer_id
),
cohort_size AS (
    -- size of each cohort (month 0)
    SELECT  
        cohort_month,
        COUNT(DISTINCT customer_id) AS cohort_size
    FROM cohort_data
    WHERE period_number = 0
    GROUP BY 1
),

cohort_agg AS (
    -- customers per cohort per period
    SELECT
        cohort_month,
        period_number,
        COUNT(DISTINCT customer_id) AS customers
    FROM cohort_data
    GROUP BY 1,2
)

SELECT
    TO_CHAR(c.cohort_month,'YYYY-MM') AS cohort_month,
    c.period_number,
    c.customers,
    cs.cohort_size,

    -- retention %
    ROUND(c.customers * 100.0 / cs.cohort_size, 2) AS retention_rate

FROM cohort_agg c
JOIN cohort_size cs
    ON c.cohort_month = cs.cohort_month

ORDER BY 1,2;