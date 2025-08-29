-- This query segments customers and calculates the average lifetime value for each segment.
WITH customer_metrics AS (
  SELECT
    customer_id,
    customer_name,
    segment,
    COUNT(DISTINCT order_id) as total_orders,
    SUM(sales) as lifetime_value
  FROM superstore
  GROUP BY customer_id, customer_name, segment
)
SELECT
  segment,
  COUNT(*) as customer_count,
  ROUND(AVG(lifetime_value)::numeric, 2) as avg_clv
FROM customer_metrics
GROUP BY segment
ORDER BY avg_clv DESC;