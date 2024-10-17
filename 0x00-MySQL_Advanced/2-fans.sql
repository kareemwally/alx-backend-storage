-- selecting the most famous bands all over the globe
-- based on their popularity
SELECT origin , fans as nb_fans from metal_bands
ORDER BY nb_fans DESC;
