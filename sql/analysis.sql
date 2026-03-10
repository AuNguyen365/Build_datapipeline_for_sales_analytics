SELECT SUM(revenue)
From sales;

SELECT product, SUM(quantity)
FROM sales
GROUP BY product
ORDER BY SUM(quantity) DESC;