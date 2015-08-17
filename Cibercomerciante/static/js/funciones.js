$(document).ready(function() {

//----------------------------------------------------------
//     Funcion  filtro Subcategorias
//----------------------------------------------------------

/*
Autor           Jhonatan Acelas Arevalo
Fecha           30 Julio 2015
Descripcion     filtro generico input para tablas de contenido
Modificado      2 Agosto 2015 Generico, elimino codigo repetido
*/ 

$('.categoria').change(function(e){
           
         var url1='/filtrar_categorias/'+this.value+'/' ;

       e.preventDefault();
       $.ajax({
        type: 'GET',
        url: url1,
        beforeSend: function(){

           },
           complete: function(data){

           },
           success: function (data) {
                var subcategoria = '';  
                subcategoria += '<option selected value="0">Seleccionar</option>';
                for (i in data) {

                 subcategoria += '<option value="'+data[i].pk+'">';
                 subcategoria +=  data[i].fields.nombre_cat_interna;
                 subcategoria += '</option>';

             };

             $('.subcategoria').html(subcategoria);
            },
            error: function(errors){
                alert('no se ha creado');
            }
        })
});


//----------------------------------------------------------
//     Funcion  Filtro Input Tabla  Ajax
//----------------------------------------------------------


/*
Autor           Jhonatan Acelas Arevalo
Fecha           30 Julio 2015
Descripcion     filtro generico INPUT para tablas de contenido
Modificado      2 Agosto 2015 Generico, elimino codigo repetido
*/ 

$('.buscarInputTablas').keyup(function(){
     var formulariolistar = $('.formularioTablasAjax');
       $.ajax({
                type:'post',
                url: formulariolistar.attr('action'),
                data: formulariolistar.serialize(),
                beforeSend: function(){

                },
                complete: function(data){
                    
                },
                success: function (data) {
                    $('.eliminar').remove();

                    $(".tabla").append(data);
  
                },
                error: function(errors){
                    alert('no se ha creado');
                }
            });

});

//----------------------------------------------------------
//     Funcion  Filtro Select  Tabla  Ajax
//----------------------------------------------------------


/*
Autor           Jhonatan Acelas Arevalo
Fecha           30 Julio 2015
Descripcion     filtro generico SELECT para tablas de contenido
Modificado      2 Agosto 2015 Generico, elimino codigo repetido
*/ 

$('.buscarSelectTablas').change(function(){
     var formulariolistar = $('.formularioTablasAjax');
       $.ajax({
                type:'post',
                url: formulariolistar.attr('action'),
                data: formulariolistar.serialize(),
                beforeSend: function(){

                },
                complete: function(data){
                    
                },
                success: function (data) {
                    $('.eliminar').remove();

                    $(".tabla").append(data);
  
                },
                error: function(errors){
                    alert('no se ha creado');
                }
            });

});



    var formulariolistar = $('.listar_ajax');
        formulariolistar.bind('submit',function () {
            $.ajax({
                type: formulariolistar.attr('method'),
                url: formulariolistar.attr('action'),
                data: formulariolistar.serialize(),
                beforeSend: function(){

                },
                complete: function(data){
                    
                },
                success: function (data) {
                    $('.eliminar').remove();

                    $("#tablacontenido").append(data);
  
                },
                error: function(errors){
                    alert('no se ha creado');
                }
            });
       return false;
    });

//----------------------------------------------------------
//     Funcion  filtro Ciudades
//----------------------------------------------------------

/*
Autor           Jhonatan Acelas Arevalo
Fecha           4 Julio 2015
Descripcion     filtro generico input para tablas de contenido
Modificado      
*/ 
    $('#departamento').change(function(e){
         // alert(this.value);
         var url1='/filtrar_ciudades/'+this.value+'/' ;

       // alert(id_grupo);
       e.preventDefault();
       $.ajax({
        type: 'GET',
        url: url1,
        beforeSend: function(){
           },
           complete: function(data){

           },
           success: function (data) {
                var ciudades = '';  
                ciudades += '<option value="seleccionar">Seleccionar</option>';
                for (i in data) {

                   ciudades += '<option value="'+data[i].pk+'">';
                   ciudades +=  data[i].fields.nombre_lugar;
                   ciudades += '</option>';

               };
               $('#seleccionar_ciudades').html(ciudades);
            },
            error: function(errors){
                alert('no se ha creado');
            }
        })
    });


//----------------------------------------------------------
//     JS INTERFAZ GRAFICA USUARIOS VENDEDOR
//----------------------------------------------------------


    // Funcion al seleccionar permisos check box
    $("#administrador").change(function() { 
        if($("#administrador").is(':checked')) { 

            $('#catalogo').attr('disabled','disabled');
            $("#catalogo").prop('checked', true);

            $('#pedidos').attr('disabled','disabled');
            $("#pedidos").prop('checked', true);

            $('#reportes').attr('disabled','disabled');
            $("#reportes").prop('checked', true);

        }else{

            $('#catalogo').removeAttr('disabled');
            $("#catalogo").prop('checked', false);

            $('#pedidos').removeAttr('disabled');
            $("#pedidos").prop('checked', false);

            $('#reportes').removeAttr('disabled');
            $("#reportes").prop('checked', false);
        }
    }); 


    $('.eliminar_usuarios').click(function(){

         $('#nombre_eliminar').html($(this).attr('nombre'));
         $('#apellido_eliminar').html($(this).attr('apellido'));
         $('#email_eliminar').html($(this).attr('email'));
         $('#username_eliminar').html($(this).attr('usuario'));
         $('#pk_eliminar').val($(this).attr('usuario'));
    });

    $('.eliminar_productos').click(function(){

         $('#nombre_eliminar').html($(this).attr('nombre'));
         $('#subcategoria_eliminar').html($(this).attr('subcategoria'));
         $('#precioCompra_eliminar').html($(this).attr('precioCompra'));
         $('#precioVenta_eliminar').html($(this).attr('PrecioVenta'));
         $('#descuento_eliminar').html($(this).attr('descuento'));
         $('#iva_eliminar').html($(this).attr('iva'));
         $('#descripcion_eliminar').html($(this).attr('descripcion'));
         $('#imagen_eliminar').html($(this).attr('imagen'));
         $('#presentacion_eliminar').html($(this).attr('presentacion'));
         $('#empresa_eliminar').html($(this).attr('empresa'));
         $('#pk_eliminar').val($(this).attr('producto'));
    });


// ----------------------------------------------------------------------------------------
// ----------------------------------------------------------------------------------------
//                             Pantalla productos en compradores 
// ----------------------------------------------------------------------------------------
// ----------------------------------------------------------------------------------------

/*
Autor           Jhonatan Acelas Arevalo
Fecha           30 Julio 2015
Descripcion     filtro de productos con Categoria
Modificado
*/ 

$('#categoriaFiltroProductos').change(function(){
     var formulariolistar = $('.productosCompradorAjax');
       $.ajax({
                type:'post',
                url: '/filtroCompradorProductos/',
                data: formulariolistar.serialize(),
                beforeSend: function(){

                },
                complete: function(data){
                    
                },
                success: function (data) {
                    $('.eliminar').remove();

                    $("#tablaCatalogo").append(data);
  
                },
                error: function(errors){
                    alert('no se ha creado');
                }
            });

});

// '''
// Autor           Jhonatan Acelas Arevalo 
// Fecha           23 Julio 2015
// Descripcion     validar que se seleccione al menos un permiso en modificar y agregar usuarios
// Funcion         Vendedores.compradres.1
// '''

    var checkboxes = $('.require-one');
    var checkbox_names = $.map(checkboxes, function(e, i) {
        return $(e).attr("name")
    }).join(" ");
    
    $("#itemForm").validate({
        groups: {
            checks: checkbox_names
        },
        rules: {
            
        },
        messages: {
            
        },
        errorPlacement: function(error, element) {
            $('#form_error').append(error);
            $('#form_error').html('<div class="alert alert-danger" role="alert"><span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span><span class="sr-only">Error: </span>Seleccione al menos un Permiso</div>');

        }
           
    });

});

// '''
// Autor           Jhonatan Acelas Arevalo 
// Fecha           23 Julio 2015
// Descripcion     validar que se seleccione al menos un permiso en modificar y agregar usuarios
// Funcion         Vendedores.compradres.1
// '''

$.validator.addMethod('require-one', function(value) {
    if (true) {
        return $('.require-one:checked').size() > 0;
    } else {
        return true;
    }
}, 'Seleccione un permiso.');

function validarCategoria(form) 
    { 
        
        if (form.categoria.options[form.categoria.selectedIndex].value == 0){
            alert("Debe seleccionar una categoria");
            return false;
        }
        if (form.subcategoria.options[form.subcategoria.selectedIndex].value == 0){
            alert("Debe seleccionar una subcategoria");
            return false;
        }
        return true;
    }  
 