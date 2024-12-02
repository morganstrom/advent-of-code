WITH tmp AS (
  SELECT
    a,
    b
  FROM read_csv(
    '{{ path }}',
    delim = ' ',
    header = false, names = ['a', 'empty0', 'empty1', 'b']
  )
),

b_counts AS (
  SELECT
    b,
    count(*) AS n
  FROM tmp
  GROUP BY b
)

SELECT sum(tmp.a * b_counts.n) AS similarity
FROM tmp
INNER JOIN b_counts
  ON tmp.a = b_counts.b;
