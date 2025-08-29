-- This query identifies which product sub-categories are profitable, low-margin, or losing money.
SELECT
    category,
    sub_category,
    SUM(quantity) as total_quantity_sold,
    ROUND(SUM(sales)::numeric, 2) as total_sales,
    ROUND(SUM(profit)::numeric, 2) as total_profit,
    CASE
        WHEN SUM(profit) < 0 THEN 'Losing Money'
        WHEN SUM(sales) > 0 AND SUM(profit)/SUM(sales) < 0.05 THEN 'Low Margin'
        ELSE 'Profitable'
    END as performance_category
FROM superstore
GROUP BY category, sub_category
ORDER BY total_profit ASC;