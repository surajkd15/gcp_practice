SELECT
  name,
  SUM(number) AS total
FROM
  suraj_dt.prac_1
GROUP BY
  name
ORDER BY
  total DESC
LIMIT
  30;
