-- This query aggregates sales and profit by month and year to identify seasonal patterns.
SELECT
  EXTRACT(YEAR FROM order_date) as year,
  EXTRACT(MONTH FROM order_date) as month,
  COUNT(DISTINCT order_id) as total_orders,
  ROUND(SUM(sales)::numeric, 2) as monthly_sales,
  ROUND(SUM(profit)::numeric, 2) as monthly_profit
FROM superstore
GROUP BY EXTRACT(YEAR FROM order_date), EXTRACT(MONTH FROM order_date)
ORDER BY year, month;