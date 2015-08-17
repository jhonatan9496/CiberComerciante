$(document).ready(function() {
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
        $('#tablaFactura').append('<tr><td class="nombre">'+$(this).attr('nombre')+'</td><td><input class="cantidad" type="number" value="1" style="width:80px"/></td><td class="precio">'+$(this).attr('precio')+'</td><td class="total" >'+$(this).attr('precio')+'</td><td><button class="eliminarProductoFactura"><i class="fa fa-trash-o"></i></button></td></tr>');
        sumarTotal();
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



// cierra paquete 
});