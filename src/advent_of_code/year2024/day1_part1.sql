WITH tmp AS (
  SELECT
    a,
    b,
    row_number() OVER (ORDER BY a) AS a_order,
    row_number() OVER (ORDER BY b) AS b_order
  FROM read_csv(
    '{{ path }}',
    delim = ' ',
    header = false, names = ['a', 'empty0', 'empty1', 'b']
  )
)

SELECT sum(abs(a.a - b.b)) AS diff
FROM tmp AS a
INNER JOIN tmp AS b
  ON a.a_order = b.b_order;
