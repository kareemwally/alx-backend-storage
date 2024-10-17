-- selectin the longest and most consistent
-- Glam rock band
SELECT
    band_name,
    IFNULL(CAST(split AS UNSIGNED) - formed, 2022 - formed) AS lifespan
FROM
    metal_bands
WHERE
    style LIKE '%Glam rock%'
ORDER BY
    lifespan DESC;
