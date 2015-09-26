$(document).ready(function() {

var contadorFactura =0;

//----------------------------------------------------------
//     Funcion  agregar item a factura 
//----------------------------------------------------------
/*
Autor           Sebastian Rincon 
Fecha           2 agosto 2015
Descripcion     agregar un producto a factura en el modulo de ventas de compradores
Modificado      
*/
$('.addProducto').click(function(){
    var contador = 0;
    var nombre = $(this).attr('nombre');
    $('#tablaFactura tr').each(function () {      
        if ($(this).children('.nombre:first-child').text()===nombre) {
            contador++;
        }
    });
    if (contador==0) {
        $('#tablaFactura').append('<tr><td class="nombre">'+$(this).attr('nombre')+'</td><td><input name= "producto'+contadorFactura+'" value="' +$(this).attr('pk')+ '" /><input class="cantidad" name="cantidad'+contadorFactura+'" type="number" value="1" style="width:80px"/></td><td class="precio">'+$(this).attr('precio')+'</td><td class="total" >'+$(this).attr('precio')+'</td><td class="texto-centrado"><button class="eliminarProductoFactura btn btn-danger"><i class="fa fa-trash-o"></i></button></td></tr>');
        sumarTotal();
        contadorFactura++;
    }else {
        alert('el producto ya existe en la factura');
    };
    contador=0;
    $('.cantidad').keyup(function(){
        this.value = (this.value + '').replace(/[^1-9]/g, '1');
        $(this).parent().siblings('td.total').text(parseInt($(this).attr('value'))*parseInt($(this).parent().siblings('.precio').text()));
        sumarTotal();
    });

    $('.cantidad').change(function(){
        if (this.value=='') {
        this.value = (this.value + '').replace('', '1');
};
        $(this).parent().siblings('td.total').text(parseInt($(this).attr('value'))*parseInt($(this).parent().siblings('.precio').text()));
        sumarTotal();
    });

    function sumarTotal(){
        var suma = 0;
        $('#tablaFactura tr').each(function(){ //filas con clase 'dato', especifica una clase, asi no tomas el nombre de las columnas
            suma += parseInt($(this).find('td').eq(3).text()||0,10) //numero de la celda 3
        });
        //alert(suma) 
        $('.totalFactura').text(suma);
    };
    $('.eliminarProductoFactura').click(function(){
        $(this).parent().parent().remove();
        sumarTotal();
    });
});

//----------------------------------------------------------
//     Funcion  sumar valores  Pedido
//----------------------------------------------------------
/*
Autor           Jhonatan Acelas Arevalo 
Fecha           11 agosto 2015
Descripcion     asigna valores al formulario para eliminar el ittem
Modificado      
*/

$('.cantidad').keyup(function(){
    $(this).parent().siblings('.total').text(($(this).parent().siblings('.valorUnitario').text()*$(this).val()));
sumarTotalPedido();
});

$('.cantidad').change(function(){
    if (this.value=='') {
        this.value = (this.value + '').replace('', '1');
        $(this).parent().siblings('.total').text(($(this).parent().siblings('.valorUnitario').text()*$(this).val()));
sumarTotalPedido();
        
    }
}); 
function sumarTotalPedido(){
        var suma = 0;
        $('.tablaPedido tr').each(function(){ //filas con clase 'dato', especifica una clase, asi no tomas el nombre de las columnas
            suma += parseInt($(this).find('.total').text()||0,10) //numero de la celda 3
            //alert();
        });
        //alert(suma) 
        $('.totalPedido').text(suma);
    };


//----------------------------------------------------------
//     Funcion  asignar valores a modal Elimianr item Pedido
//----------------------------------------------------------
/*
Autor           Jhonatan Acelas Arevalo 
Fecha           10 agosto 2015
Descripcion     asigna valores al formulario para eliminar el ittem
Modificado      
*/
    $('.eliminar_item').click(function(){

         $('#nombre_eliminar').html($(this).attr('nombreItem'));
         $('#pk_eliminar').val($(this).attr('pkItem'));
    });


//----------------------------------------------------------
//     Funcion  Guardar pedido al change de el input cantidad en detalle pedido
//----------------------------------------------------------
/*
Autor           Jhonatan Acelas Arevalo 
Fecha           30 agosto 2015
Descripcion     metodo generico ajax para enviar formulario por post de modiicar la cantidad
Modificado      
*/

$('.modificarCantidadPedido').change(function(){
     var formulariolistar = $('.formularioActualizarCantidad');
       $.ajax({
                type:'post',
                url: formulariolistar.attr('action'),
                data: formulariolistar.serialize(),
                beforeSend: function(){

                },
                complete: function(data){
                    
                },
                success: function (data) {
                    alert('Se modifico la cantidad');
  
                },
                error: function(errors){
                    alert('no se ha actualizado');
                }
            });

});





//----------------------------------------------------------
//     Funcion  Guardar pedido al change de el input cantidad en detalle pedido
//----------------------------------------------------------
/*
Autor           Jhonatan Acelas Arevalo 
Fecha           18 septiembre 2015
Descripcion     metodo generico ajax para enviar formulario por post de modiicar la cantidad
Modificado      
*/

$('#generarFactura').click(function(){
     var formulariolistar = $('.facturaForm');
       $.ajax({
                type:'post',
                url: formulariolistar.attr('action'),
                data: formulariolistar.serialize(),
                beforeSend: function(){

                },
                complete: function(data){
                    
                },
                success: function (data) {
                    $('#factura').remove();
                    // alert('Se creo la factura' + data);
                    $('.span8').append('<a  href="/inicioCompradorVentas" class="btn ">Facturar + </a>  <iframe width=100% height=75%  src="http://localhost:14342/ReportesCibercomerciante/reporte?reporte=factura&factura='+data+'&TELEFONO_CLIENTE=342342&NIT_CLIENTE=345345&DIRECCION_CLIENTE=3232&NOMBRE_CLIENTE=323" frameborder="0"></iframe>')
  
                },
                error: function(errors){
                    alert('no se ha actualizado');
                }
            });

});




// cierra paquete 
});