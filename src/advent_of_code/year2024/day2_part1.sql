WITH tmp AS (
  SELECT *
  FROM read_csv(
    '{{ path }}',
    header = false,
    delim = ' ',
    columns
    = {
      'column0': 'int64',
      'column1': 'int64',
      'column2': 'int64',
      'column3': 'int64',
      'column4': 'int64',
      'column5': 'int64',
      'column6': 'int64',
      'column7': 'int64'
    },
    null_padding = true,
    ignore_errors = true
  )
),

diff AS (
  SELECT
    column1 - column0 AS diff1,
    column2 - column1 AS diff2,
    column3 - column2 AS diff3,
    column4 - column3 AS diff4,
    column5 - column4 AS diff5,
    column6 - column5 AS diff6,
    column7 - column6 AS diff7
  FROM tmp
),

validation AS (
  SELECT
    coalesce(
      coalesce(diff1 > 0, true)
      AND coalesce(diff2 > 0, true)
      AND coalesce(diff3 > 0, true)
      AND coalesce(diff4 > 0, true)
      AND coalesce(diff5 > 0, true)
      AND coalesce(diff6 > 0, true)
      AND coalesce(diff7 > 0, true), false
    ) AS all_positive,
    coalesce(
      coalesce(diff1 < 0, true)
      AND coalesce(diff2 < 0, true)
      AND coalesce(diff3 < 0, true)
      AND coalesce(diff4 < 0, true)
      AND coalesce(diff5 < 0, true)
      AND coalesce(diff6 < 0, true)
      AND coalesce(diff7 < 0, true), false
    ) AS all_negative,
    coalesce(
      coalesce(abs(diff1) < 4, true)
      AND coalesce(abs(diff2) < 4, true)
      AND coalesce(abs(diff3) < 4, true)
      AND coalesce(abs(diff4) < 4, true)
      AND coalesce(abs(diff5) < 4, true)
      AND coalesce(abs(diff6) < 4, true)
      AND coalesce(abs(diff7) < 4, true), false
    ) AS correct_range
  FROM diff
)

SELECT count(*) AS result
FROM validation
WHERE (all_positive OR all_negative) AND correct_range;
