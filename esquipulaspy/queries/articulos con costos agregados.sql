﻿select c.idarticulo,ad.descripcion, sum(case ca.idtipocosto when 3 then ca.valorcosto else 0 end) as 'DAI',sum(case ca.idtipocosto when 2 then ca.valorcosto else 0 end) as 'ISC',sum(case ca.idtipocosto when 7 then ca.valorcosto else 0 end) as 'Comisión'  FROM costoagregadoarticulo c join vw_articulosdescritos ad on c.idarticulo=ad.idarticulo join costoagregado ca on c.idcostoagregado=ca.idcostoagregado where ca.activo=1 group by c.idarticulo ;
select c.idarticulo,ad.descripcion, sum(IF( ca.idtipocosto = 3,ca.valorcosto , 0)) as 'DAI',sum(IF( ca.idtipocosto = 2 ,ca.valorcosto , 0)) as 'ISC',sum(IF( ca.idtipocosto = 7 ,ca.valorcosto , 0 )) as 'Comisión'  FROM costoagregadoarticulo c join vw_articulosdescritos ad on c.idarticulo=ad.idarticulo join costoagregado ca on c.idcostoagregado=ca.idcostoagregado where ca.activo=1 group by c.idarticulo ;