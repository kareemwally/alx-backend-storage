-- selectin the longest and most consistent
-- Glam rock band
SELECT
    band_name,
    IFNULL(split - formed, 2022 - formed) AS lifespan
FROM
    metal_bands
WHERE
    style = 'Glam rock'
ORDER BY
    lifespan DESC;
