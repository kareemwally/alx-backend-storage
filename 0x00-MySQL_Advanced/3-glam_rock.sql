-- selectin the longest and most consistent
-- Glam rock band
select band_name , formed - split as lifespan
from metal_bands 
where style='Glam rock';
