SELECT  
	GESTION_ITEMFACTURA.CANTIDAD,
	GESTION_ITEMFACTURA.PRODUCTO_ID,
	GESTION_ITEMFACTURA.FACTURA_ID ,
	GESTION_PRODUCTO.NOMBRE_PRODUCTO,
	GESTION_PRODUCTO.COSTO,
	GESTION_PRODUCTO.COSTO_VENTA,
	GESTION_PRODUCTO.IVA_ID,
	SUM(GESTION_PRODUCTO.COSTO) NETO ,
	SUM(GESTION_PRODUCTO.COSTO_VENTA) TOTAL,
	SUM(GESTION_PRODUCTO.IVA_ID) IVA
FROM 
	GESTION_ITEMFACTURA INNER JOIN GESTION_PRODUCTO 
	ON GESTION_ITEMFACTURA.PRODUCTO_ID = GESTION_PRODUCTO.ID
	