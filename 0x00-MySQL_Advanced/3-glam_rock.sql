-- selectin the longest and most consistent
-- Glam rock band
select band_name, IFNULL(split - formed, 2022 - formed) as lifespan
from metal_bands
where style='Glam rock';
